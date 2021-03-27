#!/usr/bin/env python3
import sys
import subprocess
import socket

if(len(sys.argv)==1):
    print("Usage : ./port-scanner.py <IP>")
    sys.exit(0)

def ping(ip):
    res = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if(res.returncode == 0):
        return True
    else:
        return False

def port_scan(ip):
    open_ports = []
    try:
        for port in range(1,65536):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((ip,port)) 
            if result == 0: 
                open_ports.append(port)
                print(f"  Port {port} is open")
            s.close()
        return open_ports
    except:
        print("Error occurred")
        sys.exit(0)
        s.close()

ip = sys.argv[1]
# CHECK IF IP IS REACHABLE
if(ping(ip)):
    print(f"[+] {ip} is up")
else:
    print(f"[-] {ip} is unreachable")
    sys.exit(0)

# SCAN PORTS
print("[+] Port scan started")
open_ports = port_scan(ip)
print(open_ports)
