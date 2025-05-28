import sys
import binascii
from socket import socket, AF_INET, SOCK_DGRAM

if len(sys.argv) >3:
    print("Specify destination host and port")
    exit(1)
    
#Create the udp socket with 1sec receive timeout
 sock = socket(AF_INET, SOCK_DGRAM)
sock.settingtimeout(1)
addr = (sys.arg[1], int(sys.argv[2]))

for lin sys.stdin:
    msg = binascii.a2b_hex(line.strip())
    sock.sendto(msg, addr)
    
    try:
        data, server = sock.recvfrom(1024)
        print(binascii.b2a(data))
        except:
            pass


#run this command python udp.client.py HOSTNAME 12345 < udp_outbound.txt
