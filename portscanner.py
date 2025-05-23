import socket
import threading

target = input("Enter the target IP address to scan: ") #import the target IP address
print("Enter the range of ports to scan(format: start-end):")
start_port, end_port = map (map(int, input().split('-'))




def port_scanner(port):
    try:
        #Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Set a timeout, 5 secounds is fine
        s.setting(5)
        con =s.connect((target,port))
        print(f'The port{port} is open')
        con.close()
    except:
        pass

          
 # Scan the first 1024 ports
 for port in range(start_port, end_port+1):
     thread = threading.Thread(target =portscanner, args=(port,))
     thread.start()
     

