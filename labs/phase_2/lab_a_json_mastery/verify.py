#!/usr/bin/env python3
import os
import json

def verify_json_schema():
    print("\n=== JSON SCHEMA VALIDATION SCORECARD ===")
    
    file_path = "cisco_schema.json"
    if not os.path.exists(file_path):
        print("[✗] Check: cisco_schema.json exists .......... FAIL")
        print("\n--> ERROR: Output file 'cisco_schema.json' was not found.")
        print("    Please save your generated JSON Schema to 'cisco_schema.json'.")
        print("======================================================")
        return False
        
    print("[✓] Check: cisco_schema.json exists .......... PASS")
    
    try:
        with open(file_path, "r") as f:
            schema = json.load(f)
    except json.JSONDecodeError as e:
        print("[✗] Check: cisco_schema.json is valid JSON ... FAIL")
        print(f"\n--> ERROR: JSON syntax error detected: {e}")
        print("======================================================")
        return False
        
    print("[✓] Check: cisco_schema.json is valid JSON ... PASS")
    
    properties = schema.get("properties", {})
    required = schema.get("required", [])
    
    # Check 1: VlanTaggingEnabled exists and is boolean and required
    vlan_prop = properties.get("VlanTaggingEnabled", {})
    has_vlan = vlan_prop.get("type") == "boolean" and "VlanTaggingEnabled" in required
    if has_vlan:
        print("[✓] Check: VlanTaggingEnabled is required & bool  PASS")
    else:
        print("[✗] Check: VlanTaggingEnabled is required & bool  FAIL")
        
    # Check 2: MtuRange exists, is integer and restricted [1500, 9216]
    mtu_prop = properties.get("MtuRange", {})
    has_mtu = (
        mtu_prop.get("type") == "integer" 
        and mtu_prop.get("minimum") == 1500 
        and mtu_prop.get("maximum") == 9216
        and "MtuRange" in required
    )
    if has_mtu:
        print("[✓] Check: MtuRange integer limits enforced [1500-9216] PASS")
    else:
        print("[✗] Check: MtuRange integer limits enforced [1500-9216] FAIL")
        
    all_passed = has_vlan and has_mtu
    
    print("\n======================================================")
    if all_passed:
        print("⏱️  COMPLETION TIME: 03 minutes 45 seconds")
        print("👑  ACHIEVED RANK:  [ JSON Schema Master ]")
        print("======================================================")
        print("Status: 100% compliant. JSON Schema validation succeeded!")
        return True
    else:
        print("Status: SCHEMA VERIFICATION FAILED. Please review the constraints and update cisco_schema.json.")
        print("======================================================")
        return False

if __name__ == "__main__":
    verify_json_schema()
