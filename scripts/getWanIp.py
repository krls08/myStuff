import urllib.request

try:
    f = open("extIp.txt","r")
    myIp = f.read()
    print("file found")
except :
    print('file doesnt exist -> create file')
    f = open("extIp.txt","w")
    externalIp = urllib.request.urlopen('https://api.ipify.org/').read().decode('utf8')
    f.write(externalIp)

f.close()
externalIp = urllib.request.urlopen('https://api.ipify.org/').read().decode('utf8')

print('my external ip: ' + externalIp)

