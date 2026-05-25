#!/usr/bin/env python3
import sys
import ipaddress

def parse_subnet(ip, mask):
    """
    Upgraded, highly robust subnet parser.
    Supports both IPv4 and IPv6 addresses dynamically.
    """
    cidr_str = f"{ip}/{mask}"
    print(f"Subnet Parser active. Checking: {cidr_str}")
    
    try:
        # Determine if IPv6 or IPv4 automatically
        if ":" in ip:
            network = ipaddress.IPv6Network(cidr_str, strict=False)
            hosts = network.num_addresses
            print(f"Subnet {network} is a VALID IPv6 Subnet Allocation.")
            print(f"Hosts in Subnet: {hosts}")
        else:
            network = ipaddress.IPv4Network(cidr_str, strict=False)
            hosts = network.num_addresses
            print(f"Subnet {network} is a VALID IPv4 Subnet Allocation.")
            print(f"Hosts in Subnet: {hosts}")
        return True
    except ValueError as e:
        print(f"ERROR: Invalid subnet or mask format: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: legacy_parser.py <ip_address> <cidr_mask>")
        sys.exit(1)
        
    ip_addr = sys.argv[1]
    mask_val = sys.argv[2]
    
    parse_subnet(ip_addr, mask_val)
