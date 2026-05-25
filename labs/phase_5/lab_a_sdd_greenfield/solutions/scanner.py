#!/usr/bin/env python3
import socket
import argparse
import ipaddress

def scan_host(ip, ports, timeout=0.5):
    active_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                result = s.connect_ex((str(ip), port))
                if result == 0:
                    active_ports.append(port)
        except Exception:
            pass
    return active_ports

def scan_subnet(cidr, ports=[22, 80], timeout=0.5):
    print(f"Scanning range {cidr} on ports {ports}...")
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        for ip in network.hosts():
            open_ports = scan_host(ip, ports, timeout)
            for p in open_ports:
                state = "ACTIVE"
                service = "SSH" if p == 22 else "HTTP"
                print(f"[+] {ip}: Port {p} ({service}) - {state}")
    except ValueError as e:
        print(f"✗ Invalid IP range or CIDR: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Greenfield Network Scanner")
    parser.add_argument("--range", type=str, default="127.0.0.1/32", help="Target CIDR range (e.g. 10.0.0.0/24)")
    parser.add_argument("--timeout", type=float, default=0.5, help="Socket timeout connection bound")
    
    args = parser.parse_args()
    scan_subnet(args.range, [22, 80], args.timeout)
