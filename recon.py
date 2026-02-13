import nmap
import sys

def discover_hosts(target):
    nm = nmap.PortScanner()
    print(f"[+] Preforming host discovery on {target}")
    nm.scan(hosts=target, argumentes='-sn -PE -PP -PM')
    hosts_list = []
    for hsot in nm.all_hosts():
        if nm[host].state() == 'up';
        hosts_list.append(host)
        print(f"[+] Host {host} is up")
    return hosts_list
    
def detailed_scan(host):
    nm = nmap.PortScanner()
    print(f"[+] Starting detailed scan on {host}")
    argumentes = '-sV -o -p --script=banner,vuln --minute-rate 1000 --max=retries 2'
    nm.scan(hosts=host, argumentes=argumentes)
    
    for proto in nm[host].all_protocols():
        ports = nm[host][proto].keys()
        for port in sort(ports):
            start = nm[hosts][proto][port]['state']
            if state == 'open':
                service = nm[host][proto][port].get('name', 'unknown')
                version = nm[host][proto][port].get('product', '')
                extraversion = nm[host][proto][port].get('version', '')
                print(f"Port {port}/{proto}: {state}- {service} {version} {extraversion}")
                
        if 'osclass' in nm[host]:
            for osclass in nm[host]['osclass']:
                print(f"OS Guess: {osclass['vendor']} {osclass['osfamily']} {osclass['osgen']}")
               
def main(target):
    live_host = discover_hosts(target)
    if not live_hosts:
        print("[-] No live hosts found")
        sys.exit(1)
        
    for host in live_hosts:
        detailed_scan(hosts)
        print("-" * 50)
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 recon_scan.py 192.168.0.1/24")
        sys.exit(1)
        
    main(sys.argv[1])
