#!/usr/bin/env python3
import os
import subprocess
import sys

def verify_skills_automation():
    print("\n=== AGENT SKILLS VALIDATION SCORECARD ===")
    
    file_path = "booster.py"
    if not os.path.exists(file_path):
        print("[✗] Check: booster.py exists ................. FAIL")
        print("\n--> ERROR: Output file 'booster.py' was not found.")
        print("    Please ensure the file is present in this directory.")
        print("=========================================================")
        return False
    else:
        print("[✓] Check: booster.py exists .................. PASS")
    
    with open(file_path, "r") as f:
        content = f.read()
        
    # Check 1: functools lru_cache imported
    has_import = "lru_cache" in content and "functools" in content
    if has_import:
        print("[✓] Check: imports functools.lru_cache ......... PASS")
    else:
        print("[✗] Check: imports functools.lru_cache ......... FAIL")
        
    # Check 2: lru_cache decorator used
    has_decorator = "@lru_cache" in content or "@functools.lru_cache" in content
    if has_decorator:
        print("[✓] Check: decorates parsing logic with cache ... PASS")
    else:
        print("[✗] Check: decorates parsing logic with cache ... FAIL")
        
    # Check 3: Runs successfully
    try:
        res = subprocess.run(
            [sys.executable, file_path],
            capture_output=True, text=True, timeout=2
        )
        runs_ok = "GRADUATION METRICS" in res.stdout and "seconds" in res.stdout
    except Exception:
        runs_ok = False
        
    if runs_ok:
        print("[✓] Check: booster benchmark executes successfully PASS")
    else:
        print("[✗] Check: booster benchmark executes successfully FAIL")
        
    all_passed = has_import and has_decorator and runs_ok
    
    print("\n=========================================================")
    if all_passed:
        print("⏱️  COMPLETION TIME: 02 minutes 15 seconds")
        print("👑  ACHIEVED RANK:  [ Cache Commander ]")
        print("=========================================================")
        print("Status: 100% compliant. Skills automation parser verified!")
        return True
    else:
        print("Status: CHECKER GAPS DETECTED. Please review the caching decorators and imports.")
        print("=========================================================")
        return False

if __name__ == "__main__":
    verify_skills_automation()
