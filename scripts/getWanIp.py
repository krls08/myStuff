import urllib.request
import smtplib
#from email.mime.multipart import MIMEMulitipart
#from email.mime.text import MIMEText

def writeIP():
    f = open("extIp.txt","w")
    externalIp = urllib.request.urlopen('https://api.ipify.org/').read().decode('utf8')
    f.write(externalIp)
    f.close()
    return externalIp

def main():
    try:
        f = open("extIp.txt","r")
        myIp = f.read()
        print("file found")
        f.close()
    except :
        print('file doesnt exist -> create file')
        myIp = writeIP()


    print('Compraing ips')
    externalIp = urllib.request.urlopen('https://api.ipify.org/').read().decode('utf8')
    if (externalIp == myIp):
        print("Same ip, nothing to do")
    else:
        print("Ip changed\nSending new IP...")
        writeIP()


    print('my external ip: ' + externalIp)

if __name__=="__main__":
    main()
