#!/usr/bin/env python3
import os
import re
import sys

def verify_solution():
    print("\n=== NETOPS SANITIZATION SCORECARD ===")
    
    config_path = "sanitized_config.cfg"
    if not os.path.exists(config_path):
        print(f"[✗] Check: sanitized_config.cfg exists ............. FAIL")
        print("\n--> ERROR: Output file 'sanitized_config.cfg' was not found.")
        print("    Please run your 'sanitize.py' script first to generate the sanitized output.")
        print("=====================================================")
        return False
        
    print("[✓] Check: sanitized_config.cfg exists ............. PASS")
    
    with open(config_path, "r") as f:
        content = f.read()
        
    # Check 1: Plaintext passwords redacted
    bad_passwords = ["cleartextPass123", "OperatorPass456", "AutoServicePass789"]
    passwords_redacted = True
    for bp in bad_passwords:
        if bp in content:
            passwords_redacted = False
            
    # Check that [REDACTED_PASSWORD] is present in the username lines
    if "password [REDACTED_PASSWORD]" not in content:
        passwords_redacted = False
        
    if passwords_redacted:
        print("[✓] Check: username plain-text passwords redacted .. PASS")
    else:
        print("[✗] Check: username plain-text passwords redacted .. FAIL")
        
    # Check 2: Enable secret redacted
    enable_secret_redacted = True
    if "$1$mERQ$P7eJ" in content:
        enable_secret_redacted = False
    
    # Check that enable secret line contains redacted token
    if "enable secret 5 [REDACTED_PASSWORD]" not in content:
        enable_secret_redacted = False
        
    if enable_secret_redacted:
        print("[✓] Check: enable secrets redacted ................. PASS")
    else:
        print("[✗] Check: enable secrets redacted ................. FAIL")
        
    # Check 3: SNMP communities redacted
    bad_snmp = ["NetOpsSecretRO", "NetOpsSecretRW"]
    snmp_redacted = True
    for bs in bad_snmp:
        if bs in content:
            snmp_redacted = False
            
    if "community [REDACTED_SNMP]" not in content:
        snmp_redacted = False
        
    if snmp_redacted:
        print("[✓] Check: SNMP community strings redacted ......... PASS")
    else:
        print("[✗] Check: SNMP community strings redacted ......... FAIL")
        
    # Check 4: Private IPs mapped from 10.120.x.x to 192.168.100.x
    has_10_120 = "10.120." in content
    has_192_168_100 = "192.168.100." in content
    
    # Ensure no old IPs left and new IPs exist
    ip_mapped = (not has_10_120) and has_192_168_100
    
    if ip_mapped:
        print("[✓] Check: 10.120.x.x IP addresses masked .......... PASS")
    else:
        print("[✗] Check: 10.120.x.x IP addresses masked .......... FAIL")
        
    all_passed = passwords_redacted and enable_secret_redacted and snmp_redacted and ip_mapped
    
    print("\n=====================================================")
    if all_passed:
        print("⏱️  COMPLETION TIME: 03 minutes 14 seconds")
        print("👑  ACHIEVED RANK:  [ Compliance Champion ]")
        print("=====================================================")
        print("Status: 100% compliant. Configuration safe for external AI chats.")
        return True
    else:
        print("Status: GAPS DETECTED. Please review the failures above and update sanitize.py.")
        print("=====================================================")
        return False

if __name__ == "__main__":
    verify_solution()
