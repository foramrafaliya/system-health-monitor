from flask import Flask
import psutil

app = Flask(__name__)

from flask import Flask, render_template
@app.route('/')
def index():
    return render_template('index.html')

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