#!/usr/bin/env python3
import sys

def parse_ipv4_subnet(ip, mask):
    """
    Messy, poorly documented legacy parser.
    Supports only IPv4 addresses. Lacks IPv6 compatibility.
    """
    print(f"Legacy parser active. Checking subnet: {ip}/{mask}")
    
    parts = ip.split('.')
    if len(parts) != 4:
        print("ERROR: Invalid IPv4 address format.")
        return False
        
    for part in parts:
        try:
            val = int(part)
            if val < 0 or val > 255:
                print("ERROR: Octet range out of bounds.")
                return False
        except ValueError:
            print("ERROR: Non-integer octet detected.")
            return False
            
    try:
        cidr = int(mask)
        if cidr < 0 or cidr > 32:
            print("ERROR: CIDR mask out of bounds.")
            return False
    except ValueError:
        print("ERROR: Non-integer mask detected.")
        return False
        
    # Calculate hosts (simplistic calculation)
    hosts = 2 ** (32 - cidr)
    print(f"Subnet {ip}/{mask} is a VALID IPv4 range containing {hosts} addresses.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: legacy_parser.py <ip_address> <cidr_mask>")
        sys.exit(1)
        
    ip_addr = sys.argv[1]
    mask_val = sys.argv[2]
    
    parse_ipv4_subnet(ip_addr, mask_val)
