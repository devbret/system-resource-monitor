import logging
import os
import threading
import time

import psutil
from flask import Flask, jsonify, render_template, request

HOST = os.environ.get("HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", "5000"))
SAMPLE_INTERVAL_S = float(os.environ.get("SAMPLE_INTERVAL", "1"))
STALE_AFTER_S = SAMPLE_INTERVAL_S * 5

if SAMPLE_INTERVAL_S <= 0:
    raise SystemExit("SAMPLE_INTERVAL must be a positive number of seconds")

app = Flask(__name__)

LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG" if app.debug else "INFO").upper()
logging.basicConfig(level=LOG_LEVEL)
logging.getLogger("werkzeug").setLevel(LOG_LEVEL)


def collect_metrics():
    cpu = psutil.cpu_percent(interval=SAMPLE_INTERVAL_S)
    freq = psutil.cpu_freq()
    return {
        "cpu": cpu,
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
        "network": psutil.net_io_counters()._asdict(),
        "swap": psutil.swap_memory().percent,
        "cpu_freq": freq.current if freq else 0,
        "cpu_cores": psutil.cpu_count(logical=False) or 0,
        "cpu_threads": psutil.cpu_count(logical=True) or 0,
        "load_avg": psutil.getloadavg(),
        "uptime": int(time.time() - psutil.boot_time()),
        "sampled_at": time.time(),
    }


class ResourceSampler:
    def __init__(self):
        self._lock = threading.Lock()
        self._ready = threading.Event()
        self._snapshot = None
        self._updated_at = None
        self._thread = None

    def start(self):
        with self._lock:
            if self._thread is not None:
                return
            self._thread = threading.Thread(
                target=self._run, name="resource-sampler", daemon=True
            )
            self._thread.start()

    def _run(self):
        while True:
            try:
                snapshot = collect_metrics()
            except Exception:
                app.logger.exception("Failed to sample system resources")
                time.sleep(SAMPLE_INTERVAL_S)
                continue
            with self._lock:
                self._snapshot = snapshot
                self._updated_at = time.monotonic()
            self._ready.set()

    def latest(self, timeout=None):
        self._ready.wait(timeout)
        with self._lock:
            if self._snapshot is None:
                return None, None
            return self._snapshot, time.monotonic() - self._updated_at


sampler = ResourceSampler()


@app.before_request
def start_sampler():
    sampler.start()


@app.after_request
def no_cache_for_api(response):
    if request.path.startswith("/api/"):
        response.headers["Cache-Control"] = "no-store"
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/resource")
def resource():
    snapshot, age = sampler.latest(timeout=SAMPLE_INTERVAL_S + 1)
    if snapshot is None:
        return jsonify(error="System metrics are not available yet"), 503
    if age > STALE_AFTER_S:
        return jsonify(error="System metrics are stale"), 503
    return jsonify(snapshot)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
