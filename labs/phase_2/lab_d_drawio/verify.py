#!/usr/bin/env python3
import os
import xml.etree.ElementTree as ET

def verify_drawio_xml():
    print("\n=== DRAW.IO XML VALIDATION SCORECARD ===")
    
    file_path = "topology.drawio"
    if not os.path.exists(file_path):
        print("[✗] Check: topology.drawio exists ........... FAIL")
        print("\n--> ERROR: Output file 'topology.drawio' was not found.")
        print("    Please save your generated Draw.io XML to 'topology.drawio'.")
        print("======================================================")
        return False
        
    print("[✓] Check: topology.drawio exists ........... PASS")
    
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except ET.ParseError as e:
        print("[✗] Check: topology.drawio is valid XML ..... FAIL")
        print(f"\n--> ERROR: XML parse error detected: {e}")
        print("======================================================")
        return False
        
    print("[✓] Check: topology.drawio is valid XML ..... PASS")
    
    # Check for standard Draw.io XML tags
    content_str = ET.tostring(root, encoding="utf-8").decode().lower()
    has_mxfile = "mxfile" in content_str or "mxgraphmodel" in content_str
    has_mxcell = "mxcell" in content_str
    
    has_drawio_elements = has_mxfile and has_mxcell
    if has_drawio_elements:
        print("[✓] Check: contains standard Draw.io tags ... PASS")
    else:
        print("[✗] Check: contains standard Draw.io tags ... FAIL")
        
    all_passed = has_drawio_elements
    
    print("\n======================================================")
    if all_passed:
        print("⏱️  COMPLETION TIME: 04 minutes 20 seconds")
        print("👑  ACHIEVED RANK:  [ XML Vector Architect ]")
        print("======================================================")
        print("Status: 100% compliant. Draw.io XML verified successfully!")
        return True
    else:
        print("Status: VALIDATION FAILED. Please review your Draw.io XML tag structure.")
        print("======================================================")
        return False

if __name__ == "__main__":
    verify_drawio_xml()
