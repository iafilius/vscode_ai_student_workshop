#!/usr/bin/env python3
import os
import json
import uuid
import argparse

def load_topology(file_path="network_topology_data.json"):
    # Adjust path if run from solutions subfolder
    if not os.path.exists(file_path) and os.path.exists("../" + file_path):
        file_path = "../" + file_path
        
    with open(file_path, "r") as f:
        return json.load(f)

def compile_firewall_rules(src, dst, port):
    topo = load_topology()
    ip_cards = topo.get("ipCard", {})
    security_policies = topo.get("networkSecurityPolicy", [])
    
    # 1. Resolve logical names
    src_card = ip_cards.get(src)
    dst_card = ip_cards.get(dst)
    
    if not src_card or not dst_card:
        return {
            "traceId": str(uuid.uuid4()),
            "status": "DENIED",
            "error": f"Unable to resolve source '{src}' or destination '{dst}' in ipCard mapping."
        }
        
    src_zone = src_card.get("zone")
    dst_zone = dst_card.get("zone")
    
    # 2. Check Security Policies
    allowed = False
    for policy in security_policies:
        if policy.get("sourceZone") == src_zone and policy.get("destinationZone") == dst_zone:
            allowed_ports = policy.get("allowedPorts", [])
            if port in allowed_ports or "any" in allowed_ports:
                allowed = True
                break
                
    trace_id = str(uuid.uuid4())
    
    if not allowed:
        return {
            "traceId": trace_id,
            "status": "DENIED",
            "resolvedSource": src_card,
            "resolvedDestination": dst_card,
            "compiledRules": []
        }
        
    # 3. Generate Enforcement Point Rules
    enforcement_points = []
    compiled_rules = []
    
    # Identify active firewalls guarding source/destination spaces
    devices = topo.get("routingTopology", {}).get("devices", [])
    for dev in devices:
        if dev.get("isFirewall", False):
            ep_name = dev.get("id")
            platform = dev.get("platform")
            
            # Simple rule mapping based on platform type
            if platform == "aws_security_group":
                enforcement_points.append(ep_name)
                compiled_rules.append({
                    "platform": "aws_security_group",
                    "targetDevice": ep_name,
                    "rule": {
                        "IpProtocol": "tcp",
                        "FromPort": port,
                        "ToPort": port,
                        "IpRanges": [{"CidrIp": src_card.get("ipv4")}]
                    }
                })
            elif platform == "cisco_asa":
                enforcement_points.append(ep_name)
                src_ip = src_card.get("ipv4").split("/")[0]
                src_mask = "255.255.255.0" # Standard default mask for CIDR
                dst_ip = dst_card.get("ipv4").split("/")[0]
                
                rule_str = f"access-list outside_access_in extended permit tcp {src_ip} {src_mask} host {dst_ip} eq {port}"
                compiled_rules.append({
                    "platform": "cisco_asa",
                    "targetDevice": ep_name,
                    "rule": rule_str
                })
                
    return {
        "traceId": trace_id,
        "status": "ALLOWED",
        "resolvedSource": src_card,
        "resolvedDestination": dst_card,
        "enforcementPoints": enforcement_points,
        "compiledRules": compiled_rules
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Policy-as-Code Rule Compiler")
    parser.add_argument("--src", type=str, default="aws-app-servers", help="Logical source IP Card")
    parser.add_argument("--dst", type=str, default="on-prem-db-tier", help="Logical destination IP Card")
    parser.add_argument("--port", type=int, default=5432, help="Target TCP port connection request")
    
    args = parser.parse_args()
    
    res = compile_firewall_rules(args.src, args.dst, args.port)
    print(json.dumps(res, indent=2))
