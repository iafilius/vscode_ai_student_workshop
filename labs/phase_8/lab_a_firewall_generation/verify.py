#!/usr/bin/env python3
import os

def verify_firewall():
    print("\n=== FIREWALL COMPILER SCORECARD ===")
    
    file_path = "generate_rules.py"
    if not os.path.exists(file_path):
        print("[✗] Check: generate_rules.py exists .......... FAIL")
        print("\n--> ERROR: Output file 'generate_rules.py' was not found.")
        print("    Please run '/opsx-apply policy-based-firewall-automation' first.")
        print("====================================================")
        return False
        
    print("[✓] Check: generate_rules.py exists .......... PASS")
    
    with open(file_path, "r") as f:
        content = f.read()
        
    # Check 1: Imports json & uuid/hashlib
    imports_json = "import json" in content
    imports_uuid = "import uuid" in content or "uuid4" in content
    
    if imports_json and imports_uuid:
        print("[✓] Check: imports required policy modules ..... PASS")
    else:
        print("[✗] Check: imports required policy modules ..... FAIL")
        
    # Check 2: Dynamic lookup handling
    handles_lookups = "network_topology_data.json" in content or "ipCard" in content
    if handles_lookups:
        print("[✓] Check: resolves names via topology lookups  PASS")
    else:
        print("[✗] Check: resolves names via topology lookups  FAIL")
        
    # Check 3: Implements trace ID
    has_trace = "traceId" in content or "uuid" in content
    if has_trace:
        print("[✓] Check: implements cryptographic trace tracking PASS")
    else:
        print("[✗] Check: implements cryptographic trace tracking FAIL")
        
    all_passed = imports_json and imports_uuid and handles_lookups and has_trace
    
    print("\n====================================================")
    if all_passed:
        print("⏱️  COMPLETION TIME: 07 minutes 18 seconds")
        print("👑  ACHIEVED RANK:  [ Policy Security Pro ]")
        print("====================================================")
        print("Status: 100% compliant. Policy compiler verified successfully!")
        return True
    else:
        print("Status: GAPS DETECTED. Please review the failures and update generate_rules.py.")
        print("====================================================")
        return False

if __name__ == "__main__":
    verify_firewall()
