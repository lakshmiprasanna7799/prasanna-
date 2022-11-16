#import socket
#print(socket.gethostname())
#hostname=socket.gethostname()

#ipadd=socket.gethostbyname(hostname)
#print(ipadd)
import os, ipaddress
os.system('cls')
while True:
    ip=input("enter ip address")
    try:
        print(ipaddress.ip_address(ip))
        print("ipvalid")
    except:
        print('-' *50)
        print("invalid")
    finally:
        if ip=='q':
            print("script finished")
            break