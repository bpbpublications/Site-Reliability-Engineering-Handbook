import os
import time

def check_service():
    status = os.system("systemctl is-active --quiet myservie")
    return status == 0

while True:
    if not chek_servie():
        print("Service is down! Restarting...")
        os.system("systemctl restart myservice")
    time.sleep(60)	
