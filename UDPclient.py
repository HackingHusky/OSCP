import socket

target_host = "127.0.0.1" #change this
target_port = 9997 #change this

#create the object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send data
client.sendto(b"AAABBBCCC", (target_host,target_port))
#remember udp is connectionless, it doesn't matter how its sent

# receive data 
data, addr  = client.recvfrom(4096)

print(dtat.decode())
client.close()
