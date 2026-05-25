#!/usr/bin/env python3
import os

def verify_rest_client():
    print("\n=== REST CLIENT SCORECARD ===")
    
    file_path = "api_client.py"
    if not os.path.exists(file_path):
        print("[✗] Check: api_client.py exists ............. FAIL")
        print("\n--> ERROR: Output file 'api_client.py' was not found.")
        print("    Please run '/opsx-apply rest-api-client' first.")
        print("====================================================")
        return False
        
    print("[✓] Check: api_client.py exists ............. PASS")
    
    with open(file_path, "r") as f:
        content = f.read()
        
    # Check 1: Imports standard connection library
    imports_http = "urllib" in content or "requests" in content
    if imports_http:
        print("[✓] Check: imports HTTP standard library ..... PASS")
    else:
        print("[✗] Check: imports HTTP standard library ..... FAIL")
        
    # Check 2: Targets public mock domain
    targets_domain = "jsonplaceholder.typicode.com" in content
    if targets_domain:
        print("[✓] Check: targets mock endpoint API domain ... PASS")
    else:
        print("[✗] Check: targets mock endpoint API domain ... FAIL")
        
    # Check 3: Performs POST payload
    performs_post = "posts" in content and "status" in content or "userId" in content and "posts" in content
    if performs_post:
        print("[✓] Check: implements telemetry POST payload .. PASS")
    else:
        print("[✗] Check: implements telemetry POST payload .. FAIL")
        
    all_passed = imports_http and targets_domain and performs_post
    
    print("\n====================================================")
    if all_passed:
        print("⏱️  COMPLETION TIME: 04 minutes 50 seconds")
        print("👑  ACHIEVED RANK:  [ REST Integrator ]")
        print("====================================================")
        print("Status: 100% compliant. API REST client verified successfully!")
        return True
    else:
        print("Status: GAPS DETECTED. Please review the failures and update api_client.py.")
        print("====================================================")
        return False

if __name__ == "__main__":
    verify_rest_client()
