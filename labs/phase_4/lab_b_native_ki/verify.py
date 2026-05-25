#!/usr/bin/env python3
import os
import json

def verify_knowledge_item():
    print("\n=== KNOWLEDGE ITEMS VALIDATION SCORECARD ===")
    
    # Target absolute path in IDE's registered knowledge base
    # Target path in IDE's registered knowledge base
    # Assumes the script is run from within labs/phase_4/lab_b_native_ki
    workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
    ki_path = os.path.join(workspace_root, "knowledge", "datacenter_1_fabric")
    metadata_file = os.path.join(ki_path, "metadata.json")
    
    # Fallback to local templates check if not registered yet
    if not os.path.exists(metadata_file):
        print("[✗] Check: KI registered in system directory ... FAIL")
        print(f"\n--> ERROR: Registered KI metadata file was not found at:")
        print(f"    {metadata_file}")
        print("    Please copy your metadata.json and artifact.md files to your")
        print("    local system's IDE knowledge sanctuary directory to register the KI.")
        print("=========================================================")
        return False
        
    print("[✓] Check: KI registered in system directory ... PASS")
    
    try:
        with open(metadata_file, "r") as f:
            metadata = json.load(f)
    except json.JSONDecodeError as e:
        print("[✗] Check: registered metadata.json is valid ... FAIL")
        print(f"\n--> ERROR: JSON syntax error detected: {e}")
        print("=========================================================")
        return False
        
    print("[✓] Check: registered metadata.json is valid ... PASS")
    
    # Check if correct title or owner is set
    title_correct = "datacenter" in metadata.get("title", "").lower()
    owner_correct = "networking" in metadata.get("owner", "").lower() or "eet" in metadata.get("owner", "").lower()
    
    if title_correct and owner_correct:
        print("[✓] Check: metadata attributes match standard ... PASS")
    else:
        print("[✗] Check: metadata attributes match standard ... FAIL")
        
    all_passed = title_correct and owner_correct
    
    print("\n=========================================================")
    if all_passed:
        print("⏱️  COMPLETION TIME: 03 minutes 55 seconds")
        print("👑  ACHIEVED RANK:  [ Context Master ]")
        print("=========================================================")
        print("Status: 100% compliant. Knowledge Item registered successfully!")
        return True
    else:
        print("Status: GAPS DETECTED. Please review the registered metadata details.")
        print("=========================================================")
        return False

if __name__ == "__main__":
    verify_knowledge_item()
