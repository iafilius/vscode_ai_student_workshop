#!/usr/bin/env python3
import os
import subprocess
import sys

def verify_brownfield():
    print("\n=== BROWNFIELD REFLECTION SCORECARD ===")
    
    file_path = "legacy_parser.py"
    if not os.path.exists(file_path):
        print("[✗] Check: legacy_parser.py exists ........... FAIL")
        print("\n--> ERROR: Output file 'legacy_parser.py' was not found.")
        print("    Please run '/opsx-apply brownfield-parser-refinement' first.")
        print("====================================================")
        return False
        
    print("[✓] Check: legacy_parser.py exists ........... PASS")
    
    with open(file_path, "r") as f:
        content = f.read()
        
    # Check 1: Check if ipaddress standard library is leveraged
    uses_ipaddress = "ipaddress" in content
    if uses_ipaddress:
        print("[✓] Check: leverages ipaddress module ........ PASS")
    else:
        print("[✗] Check: leverages ipaddress module ........ FAIL")
        
    # Check 2: Check dry-run execution with IPv4 address
    try:
        res_v4 = subprocess.run(
            [sys.executable, "legacy_parser.py", "192.168.1.1", "24"],
            capture_output=True, text=True, timeout=2
        )
        v4_passed = "VALID" in res_v4.stdout and "192.168.1.0/24" in res_v4.stdout or "VALID" in res_v4.stdout and "192.168.1." in res_v4.stdout
    except Exception as e:
        v4_passed = False
        
    if v4_passed:
        print("[✓] Check: supports legacy IPv4 parsing ....... PASS")
    else:
        print("[✗] Check: supports legacy IPv4 parsing ....... FAIL")
        
    # Check 3: Check dry-run execution with IPv6 address
    try:
        res_v6 = subprocess.run(
            [sys.executable, "legacy_parser.py", "2001:db8::1", "32"],
            capture_output=True, text=True, timeout=2
        )
        v6_passed = "VALID" in res_v6.stdout and "2001:db8::/32" in res_v6.stdout or "IPv6" in res_v6.stdout
    except Exception as e:
        v6_passed = False
        
    if v6_passed:
        print("[✓] Check: supports upgraded IPv6 parsing ..... PASS")
    else:
        print("[✗] Check: supports upgraded IPv6 parsing ..... FAIL")
        
    all_passed = uses_ipaddress and v4_passed and v6_passed
    
    print("\n====================================================")
    if all_passed:
        print("⏱️  COMPLETION TIME: 04 minutes 45 seconds")
        print("👑  ACHIEVED RANK:  [ Dual-Stack Architect ]")
        print("====================================================")
        print("Status: 100% compliant. Subnet parser upgraded successfully!")
        return True
    else:
        print("Status: GAPS DETECTED. Please review the failures and update legacy_parser.py.")
        print("====================================================")
        return False

if __name__ == "__main__":
    verify_brownfield()
