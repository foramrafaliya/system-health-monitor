import psutil
import datetime

def get_stats():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
   
    print(f"---Stats [{datetime.datetime.now().strftime('%H:%M:%S')}]---")
    print(f"CPU Usage    : {cpu}%")
    print(f"RAM Usage    : {ram.percent}%  ({ram.used // 1024**2} MB used)")
    print(f"Disk Usage   : {disk.percent}% ({disk.used // 1024**3} GB used)")
    
    if (cpu >= 80):
        print("alert : cpu high!!!")

    if (ram.percent > 80):
        print("alert : ram high!!!")

    if (disk.percent > 90):
        print("alert : disk full!!!")    
   
get_stats()