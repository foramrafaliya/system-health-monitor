from flask import Flask
import psutil

app = Flask(__name__)

@app.route('/metrics')
def metrics():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    return {
        "cpu": cpu,
        "ram": ram.percent,
        "disk": disk.percent
    }

if __name__ == '__main__':
    app.run(debug=True)