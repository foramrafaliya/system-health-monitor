import psutil
import time
import datetime
import logging
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(
    filename='health.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def send_alert(subject, message):
    sender = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    receiver = os.getenv("EMAIL")
    
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        print("Alert email sent!")
    except Exception as e:
        print(f"Email failed: {e}")
        logging.error(f"Email failed: {e}")    
  
    
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
    
    if (cpu >= 90):
        logging.info("alert : cpu high!!!")
        print("alert : cpu high!!!")
        send_alert("PR PVT.LTD!", f"CPU usage is {cpu}% - exceeded 80% threshold!")

    if (ram.percent > 80):
        logging.info("alert : ram high!!!")
        print("alert : ram high!!!")
        send_alert("RAM Alert!", f"RAM usage is {ram.percent}% - exceeded 80% threshold!")

    if (disk.percent > 90):
        logging.info("alert : disk full!!!")  
        print("alert : disk full!!!")  
        send_alert("DISK Alert!", f"DISK usage is {disk.percent}% - exceeded 90% threshold!")  

while True:
     get_stats()
     time.sleep(5)    
