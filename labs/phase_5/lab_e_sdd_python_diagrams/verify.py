#!/usr/bin/env python3
import os

def check_file(filename):
    if os.path.exists(filename):
        print(f"[✓] Found {filename}")
        return True
    else:
        print(f"[X] Missing {filename}")
        return False

def main():
    print("=== SDD Python Diagrams Verification scorecard ===")
    
    score = 0
    if check_file("dual_dc_topology.png"): score += 1
    if check_file("global_aws_topology.png"): score += 1

    if score == 2:
        print("\nStatus: PASS. SDD successfully generated both simple and complex Python diagrams.")
    else:
        print("\nStatus: FAIL. Complete both parts of the lab to generate the diagrams.")

if __name__ == "__main__":
    main()
