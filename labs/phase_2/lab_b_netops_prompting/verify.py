#!/usr/bin/env python3
import os
import re

def check_file_exists(path, label):
    if os.path.exists(path):
        print(f"[✓] Check: {label} exists .............. PASS")
        return True
    print(f"[✗] Check: {label} exists .............. FAIL")
    print(f"\n--> ERROR: Output file '{path}' was not found.")
    print(f"    Please save your AI-generated output to '{path}'.")
    return False

def read_file(path):
    with open(path, "r") as f:
        return f.read().lower()

def check_metadata(content):
    c = content.lower()
    return "you" in c and "current department" in c

def verify_dns():
    path = "dns_bind9.zone"
    if not check_file_exists(path, "dns_bind9.zone"):
        return False

    content = read_file(path)

    # Must contain an A record for ams-switch-01 pointing to 10.240.10.5
    has_a_record = "ams-switch-01" in content and "10.240.10.5" in content
    if has_a_record:
        print("[✓] Check: A record for ams-switch-01 (10.240.10.5) ... PASS")
    else:
        print("[✗] Check: A record for ams-switch-01 (10.240.10.5) ... FAIL")
        print("    --> Hint: Make sure the A record maps 'ams-switch-01' to '10.240.10.5'")

    # Must contain a CNAME for db-primary pointing to ams-db-srv
    has_cname = "db-primary" in content and ("cname" in content or "ams-db-srv" in content)
    if has_cname:
        print("[✓] Check: CNAME record for db-primary ............... PASS")
    else:
        print("[✗] Check: CNAME record for db-primary ............... FAIL")
        print("    --> Hint: Make sure a CNAME maps 'db-primary' to 'ams-db-srv.eu.internal.'")

    # Must contain an MX record for mail relay
    has_mx = "mx" in content and "mail-relay" in content
    if has_mx:
        print("[✓] Check: MX record for mail-relay .................. PASS")
    else:
        print("[✗] Check: MX record for mail-relay .................. FAIL")
        print("    --> Hint: Make sure an MX record references 'mail-relay.eu.internal.'")

    # Must contain default owner/requester fallback
    has_default_fallback = "you" in content and "current department" in content
    if has_default_fallback:
        print("[✓] Check: Default owner/requester fallback applied .... PASS")
    else:
        print("[✗] Check: Default owner/requester fallback applied .... FAIL")
        print("    --> Hint: Make sure unknown requesters/owners default to 'YOU' and 'your department'")

    return has_a_record and has_cname and has_mx and has_default_fallback

def verify_firewall():
    # 1. Cisco ASA Check
    cisco_path = "cisco_firewall_rules.txt"
    if not check_file_exists(cisco_path, "cisco_firewall_rules.txt"):
        return False

    c_content = read_file(cisco_path)

    has_https = re.search(r"permit\s+tcp.+eq\s+443", c_content) or \
                ("permit" in c_content and "443" in c_content and "192.168.45" in c_content)
    has_psql = re.search(r"permit\s+tcp.+eq\s+5432", c_content) or \
               ("permit" in c_content and "5432" in c_content and "192.168.45" in c_content)
    has_deny = "deny" in c_content and ("10.10.200.50" in c_content or "host" in c_content)

    cisco_passed = has_https and has_psql and has_deny and check_metadata(c_content)
    if cisco_passed:
        print("[✓] Check: Cisco ASA permit rules & deny ............... PASS")
    else:
        print("[✗] Check: Cisco ASA permit rules & deny ............... FAIL")
        print("    --> Hint: Check Cisco ASA rule syntax and targets.")

    # 2. Multi-Vendor Checks
    vendors = {
        "AWS SG": "aws_sg_rules.json",
        "Azure NSG": "azure_nsg_rules.json",
        "NSX-T DFW": "nsxt_dfw_rules.json"
    }

    all_passed = cisco_passed

    for vendor, path in vendors.items():
        if not check_file_exists(path, path):
            all_passed = False
            continue
        
        content = read_file(path)
        has_ip = "10.10.200.50" in content
        has_443 = "443" in content or "https" in content
        has_5432 = "5432" in content
        has_meta = check_metadata(content)
        
        if has_ip and has_443 and has_5432 and has_meta:
            print(f"[✓] Check: {vendor} mapping logic (IP/443/5432) ..... PASS")
        else:
            print(f"[✗] Check: {vendor} mapping logic (IP/443/5432) ..... FAIL")
            print(f"    --> Hint: Ensure {vendor} contains 10.10.200.50, 443, and 5432.")
            all_passed = False

    return all_passed

def verify_ipam():
    path = "ipam_audit.txt"
    if not check_file_exists(path, "ipam_audit.txt"):
        return False

    content = read_file(path)

    # Must identify conflict between subnet-b (10.150.35.0/24) inside subnet-a
    has_conflict_b = ("subnet-b" in content or "10.150.35" in content) and \
                     ("conflict" in content or "overlap" in content or "inside" in content)
    if has_conflict_b:
        print("[✓] Check: Conflict subnet-b inside subnet-a detected . PASS")
    else:
        print("[✗] Check: Conflict subnet-b inside subnet-a detected . FAIL")
        print("    --> Hint: subnet-b (10.150.35.0/24) falls within subnet-a (10.150.32.0/20)")

    # Must identify conflict between subnet-d (10.150.32.0/24) and subnet-a
    has_conflict_d = ("subnet-d" in content or "10.150.32.0/24" in content) and \
                     ("conflict" in content or "overlap" in content or "inside" in content)
    if has_conflict_d:
        print("[✓] Check: Conflict subnet-d inside subnet-a detected . PASS")
    else:
        print("[✗] Check: Conflict subnet-d inside subnet-a detected . FAIL")
        print("    --> Hint: subnet-d (10.150.32.0/24) conflicts with subnet-a's base address")

    # Must NOT flag subnet-c as conflicting (10.150.48.0/22 is outside /20 range)
    has_false_positive = "subnet-c" in content and \
                         ("conflict" in content.replace("no conflict", "").replace("no overlap", ""))
    
    has_meta = check_metadata(content)
    if not has_meta:
        print("[✗] Check: Default metadata (owner/requester) ........ FAIL")
        print("    --> Hint: Ensure 'YOU' and 'current department' are specified.")

    if not has_false_positive:
        print("[✓] Check: subnet-c correctly NOT flagged as conflict .. PASS")
    else:
        print("[~] Check: subnet-c may be incorrectly flagged ........ WARN")
        print("    --> Note: subnet-c (10.150.48.0/22) does NOT overlap with subnet-a (10.150.32.0/20)")

    return has_conflict_b and has_conflict_d and has_meta

def main():
    print("\n=== NETWORK HOT POTATOES SCORECARD ===")
    print()
    print("--- Task 1: DNS Migration ---")
    dns_ok = verify_dns()

    print()
    print("--- Task 2: Firewall Zone Rules ---")
    fw_ok = verify_firewall()

    print()
    print("--- Task 3: IPAM Conflict Audit ---")
    ipam_ok = verify_ipam()

    all_passed = dns_ok and fw_ok and ipam_ok

    print()
    print("======================================")
    if all_passed:
        print("🏅  ACHIEVED RANK:  [ NetOps Prompt Engineer ]")
        print("======================================")
        print("Status: 100% compliant. All three NetOps tasks validated!")
    else:
        print("Status: Some checks failed. Review the hints above and try again.")
        print("💡  Tip: Check the solutions/ folder for reference outputs if you are stuck.")
        print("======================================")

if __name__ == "__main__":
    main()
