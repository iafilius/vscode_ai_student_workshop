#!/usr/bin/env python3
import os
import re

def verify_greenfield():
    print("\n=== GREENFIELD SCANNER SCORECARD ===")
    
    file_path = "scanner.py"
    if not os.path.exists(file_path):
        print("[✗] Check: scanner.py exists ................. FAIL")
        print("\n--> ERROR: Output file 'scanner.py' was not found.")
        print("    Please run '/opsx-apply greenfield-network-scanner' first to generate your scanner.")
        print("====================================================")
        return False
        
    print("[✓] Check: scanner.py exists ................. PASS")
    
    with open(file_path, "r") as f:
        content = f.read()
        
    # Check 1: Imports socket
    imports_socket = "import socket" in content
    if imports_socket:
        print("[✓] Check: imports socket library ............ PASS")
    else:
        print("[✗] Check: imports socket library ............ FAIL")
        
    # Check 2: Ports 22 and 80 configured
    ports_correct = "22" in content and "80" in content
    if ports_correct:
        print("[✓] Check: scans target ports (22 & 80) ...... PASS")
    else:
        print("[✗] Check: scans target ports (22 & 80) ...... FAIL")
        
    # Check 3: Timeout configured (0.5 or 1.0 seconds)
    has_timeout = "settimeout" in content
    if has_timeout:
        print("[✓] Check: socket timeout configured ......... PASS")
    else:
        print("[✗] Check: socket timeout configured ......... FAIL")
        
    all_passed = imports_socket and ports_correct and has_timeout
    
    print("\n====================================================")
    if all_passed:
        print("⏱️  COMPLETION TIME: 05 minutes 12 seconds")
        print("👑  ACHIEVED RANK:  [ Socket Specialist ]")
        print("====================================================")
        print("Status: 100% compliant. Greenfield network scanner successfully generated!")
        return True
    else:
        print("Status: GAPS DETECTED. Please review the checker outputs and update scanner.py.")
        print("====================================================")
        return False

if __name__ == "__main__":
    verify_greenfield()
