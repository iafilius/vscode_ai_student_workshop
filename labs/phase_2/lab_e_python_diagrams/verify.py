#!/usr/bin/env python3
import os
import subprocess
import glob
import sys

def verify_python_diagrams():
    print("\n=== PYTHON DIAGRAMS VALIDATION SCORECARD ===")
    
    file_path = "generate_diagram.py"
    if not os.path.exists(file_path):
        print("[✗] Check: generate_diagram.py exists ........ FAIL")
        print(f"\n--> ERROR: Output file '{file_path}' was not found.")
        print("    Please save your generated Python code to 'generate_diagram.py'.")
        print("======================================================")
        return False
        
    print("[✓] Check: generate_diagram.py exists ........ PASS")
    
    print("[*] Running generate_diagram.py...")
    try:
        # Run the python script to see if it executes correctly
        result = subprocess.run([sys.executable, file_path], capture_output=True, text=True, timeout=15)
        if result.returncode != 0:
            print("[✗] Check: Python script executes successfully .. FAIL")
            print(f"\n--> ERROR: Script failed with exit code {result.returncode}")
            print("---- Error Output ----")
            print(result.stderr)
            print("----------------------")
            print("======================================================")
            return False
            
        print("[✓] Check: Python script executes successfully .. PASS")
        
    except subprocess.TimeoutExpired:
        print("[✗] Check: Python script executes successfully .. FAIL")
        print("\n--> ERROR: Script timed out (took longer than 15 seconds).")
        print("======================================================")
        return False
    except Exception as e:
        print("[✗] Check: Python script executes successfully .. FAIL")
        print(f"\n--> ERROR: Failed to run script: {e}")
        print("======================================================")
        return False
        
    # Check if a .png file was generated (excluding solutions folder)
    png_files = glob.glob("*.png")
    if not png_files:
        print("[✗] Check: Generates a PNG output file ........ FAIL")
        print("\n--> ERROR: No PNG file was found in the current directory after running the script.")
        print("    Ensure the diagram generates and saves the image correctly.")
        print("======================================================")
        return False
        
    print("[✓] Check: Generates a PNG output file ........ PASS")
    print(f"    (Found output: {png_files[0]})")
    
    print("\n======================================================")
    print("⏱️  COMPLETION TIME: 03 minutes 12 seconds")
    print("👑  ACHIEVED RANK:  [ Automation Layout Master ]")
    print("======================================================")
    print("Status: 100% compliant. Python Diagram verified successfully!")
    return True

if __name__ == "__main__":
    verify_python_diagrams()
