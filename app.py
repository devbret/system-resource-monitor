from flask import Flask, jsonify, render_template
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/resource')
def resource():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    network = psutil.net_io_counters()
    return jsonify(cpu=cpu, memory=memory, disk=disk, network=network._asdict())

if __name__ == '__main__':
    app.run(debug=True)
