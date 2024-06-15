from flask import Flask, jsonify, render_template
import psutil
import time
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/resource')
def resource():
    try:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        network = psutil.net_io_counters()
        swap = psutil.swap_memory().percent
        cpu_freq = psutil.cpu_freq().current
        cpu_cores = psutil.cpu_count(logical=False)
        cpu_threads = psutil.cpu_count(logical=True)
        load_avg = psutil.getloadavg()
        boot_time = psutil.boot_time()
        uptime = int(time.time() - boot_time)

        return jsonify(
            cpu=cpu,
            memory=memory,
            disk=disk,
            network=network._asdict(),
            swap=swap,
            cpu_freq=cpu_freq,
            cpu_cores=cpu_cores,
            cpu_threads=cpu_threads,
            load_avg=load_avg,
            uptime=uptime
        )
    except Exception as e:
        app.logger.error(f"Error fetching system resource data: {e}")
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
