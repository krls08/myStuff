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

def getCredentials(pathToCredentials):
    try:
        f = open(pathToCredentials,"r")
        sender = f.readline()[:-1]
        pss = f.readline()[:-1]
        receiver = f.readline()[:-1]
        return sender, pss, receiver
    except:
        print("Error reading Credentials")
        exit()
        return 1

def sendEmail(ip):
    bodyMss = ip
    sender,pss,receiver = getCredentials("../../credentials.txt")
    print("Sending the message")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender, pss)
    server.sendmail(
        sender,
        receiver,
        bodyMss
        )
    server.quit()
    print("message is send")

# main program
def main():
    try:
        f = open("extIp.txt","r")
        myIp = f.read()
        print("file found")
        f.close()
        fileFound = True
    except :
        print('file doesnt exist -> create file')
        myIp = writeIP()
        fileFound = False

    print('Compraing ips')
    externalIp = urllib.request.urlopen('https://api.ipify.org/').read().decode('utf8')
    if (externalIp == myIp and fileFound):
        print("Same ip, nothing to do")
    else:
        print("Ip changed\nSending new IP...")
        writeIP()
        sendEmail(externalIp)


    print('my external ip: ' + externalIp)

if __name__=="__main__":
    main()
