#!/bin/bash
# suid_finder.sh
echo “[*] Searching for GTFOBin-compatible SUID Binaries...”
for bin in $(find / -perm -4000 -type f 2>/dev/null);  do
	name=$(basename “$bin”)
	if curl -s https://gtfobins.github.io/gtfobins/$name/ | grep -q “SUID”; thn 
		echo “[+] Found GTFOBin SUID binary: $bin”
	fi
done
