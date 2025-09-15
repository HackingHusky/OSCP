#! /bin/bash
for ip in $(seq 1 254); do
  ping -c 1 -w 1 10.x.x.$ip | grep "64 bytes" &> /dev/null
&& echo "Host 10.x.x.$ip is up"
done
