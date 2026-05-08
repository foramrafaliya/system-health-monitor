import psutil
import time
import datetime
import logging

logging.basicConfig(
    filename='health.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)
def get_stats():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
   
    logging.info(f"---Stats [{datetime.datetime.now().strftime('%H:%M:%S')}]---")
    print(f"---Stats [{datetime.datetime.now().strftime('%H:%M:%S')}]---")
    logging.info(f"CPU Usage    : {cpu}%")
    print(f"CPU Usage    : {cpu}%")
    logging.info(f"RAM Usage    : {ram.percent}%  ({ram.used // 1024**2} MB used)")
    print(f"RAM Usage    : {ram.percent}%  ({ram.used // 1024**2} MB used)")
    logging.info(f"Disk Usage   : {disk.percent}% ({disk.used // 1024**3} GB used)")
    print(f"Disk Usage   : {disk.percent}% ({disk.used // 1024**3} GB used)")
    
    if (cpu >= 80):
        logging.info("alert : cpu high!!!")
        print("alert : cpu high!!!")

    if (ram.percent > 80):
        logging.info("alert : ram high!!!")
        print("alert : ram high!!!")

    if (disk.percent > 90):
        logging.info("alert : disk full!!!")  
        print("alert : disk full!!!")    

while True:
     get_stats()
     time.sleep(5)    
   
get_stats()   
