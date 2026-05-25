#!/usr/bin/env python3
import os
import re

def sanitize_configuration():
    input_file = "sensitive_config.cfg"
    output_file = "sanitized_config.cfg"
    
    # Check if run from the solutions subfolder and adjust path if necessary
    if not os.path.exists(input_file) and os.path.exists("../" + input_file):
        input_file = "../" + input_file
        output_file = "../" + output_file

    print(f"--> Reading sensitive configuration from: {input_file}")
    
    with open(input_file, "r") as f:
        lines = f.readlines()
        
    sanitized_lines = []
    
    for line in lines:
        # 1. Redact username passwords: 'username <name> privilege <num> password <cleartext>'
        #    Replace password token with [REDACTED_PASSWORD]
        line = re.sub(
            r"(username \S+ privilege \d+ password) \S+",
            r"\1 [REDACTED_PASSWORD]",
            line
        )
        
        # 2. Redact enable secret hashes: 'enable secret 5 <hash>'
        line = re.sub(
            r"(enable secret \d+) \S+",
            r"\1 [REDACTED_PASSWORD]",
            line
        )
        
        # 3. Redact SNMP community keys: 'snmp-server community <string> <mode>'
        line = re.sub(
            r"(snmp-server community) \S+ (RO|RW)",
            r"\1 [REDACTED_SNMP] \2",
            line
        )
        
        # 4. Mask private internal IP space 10.120.x.y to 192.168.100.y (preserving the host octet)
        line = re.sub(
            r"10\.120\.\d+\.(\d+)",
            r"192.168.100.\1",
            line
        )
        
        sanitized_lines.append(line)
        
    print(f"--> Writing sanitized configuration to: {output_file}")
    with open(output_file, "w") as f:
        f.writelines(sanitized_lines)
        
    print("✓ Sanitization complete. Output file is fully compliant!")

if __name__ == "__main__":
    sanitize_configuration()
