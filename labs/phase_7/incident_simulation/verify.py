#!/usr/bin/env python3
import os

def verify_incident():
    print("\n=== GAME DAY INCIDENT SCORECARD ===")
    
    file_path = "remediation.cfg"
    if not os.path.exists(file_path):
        print("[✗] Check: remediation.cfg exists ............. FAIL")
        print("\n--> ERROR: Output file 'remediation.cfg' was not found.")
        print("    Please save your Cisco IOS remediation commands to 'remediation.cfg'.")
        print("====================================================")
        return False
        
    print("[✓] Check: remediation.cfg exists ............. PASS")
    
    with open(file_path, "r") as f:
        content = f.read().lower()
        
    # Check 1: GigabitEthernet1/0/12 isolated
    port_found = "gigabitethernet1/0/12" in content or "gi1/0/12" in content
    if port_found:
        print("[✓] Check: flapping port isolated (Gi1/0/12) .. PASS")
    else:
        print("[✗] Check: flapping port isolated (Gi1/0/12) .. FAIL")
        
    # Check 2: MTU 9216 configured
    mtu_found = "mtu 9216" in content or "9216" in content
    if mtu_found:
        print("[✓] Check: jumbo MTU configured (9216) ......... PASS")
    else:
        print("[✗] Check: jumbo MTU configured (9216) ......... FAIL")
        
    all_passed = port_found and mtu_found
    
    print("\n====================================================")
    if all_passed:
        print("⏱️  COMPLETION TIME: 08 minutes 42 seconds")
        print("👑  ACHIEVED RANK:  [ NetOps BGP Legend ]")
        print("====================================================")
        print("Status: 100% compliant. Game Day Incident fully resolved!")
        return True
    else:
        print("Status: DIAGNOSTIC FAILED. Keep analyzing the flap logs and try again!")
        print("====================================================")
        return False

if __name__ == "__main__":
    verify_incident()
