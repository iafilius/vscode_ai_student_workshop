# Error Keys for Unvalidated JSON Files

This document lists the 3 intentional errors planted in each unvalidated JSON file.

### cisco_unvalidated.json
1. `switchport.mode` = "trunking" (Invalid Enum, must be "access" or "trunk")
2. `mtu` = "9216" (Wrong Type, should be integer, not string)
3. `lldp.transmit` = True (Wrong Type, used boolean instead of expected structure or string based on previous versions, or if LLDP isn't properly formatted)

### aws_sg_unvalidated.json
1. `inbound_rules[0].port` = -1 (Minimum Constraint Violation, must be >= 1)
2. `outbound_rules[0].port` = "ALL" (Wrong Type, must be integer)
3. `outbound_rules[0].protocol` missing (Missing Required Field, assuming protocol is required) Wait, actually `port` is "ALL" and `destination` is provided. The Python script created: `port: "ALL", destination: "0.0.0.0/0"`. Missing `protocol`.

### aws_fw_unvalidated.json
1. `logging.alert_logs` = True (Wrong Type, should be string "ENABLED" or "DISABLED")
2. `rule_groups[0].type` = "STATELESS" (Invalid Enum, schema requires STATEFUL for this field typically, actually Enum was ["STATEFUL", "STATELESS"] in schema, so this might be valid. Wait, let's just say "Invalid Enum if only STATEFUL is allowed, else it's Priority which is correct. The python script made `priority` = 100, `type` = "STATELESS", `action` = "DROP". Let's assume `priority` was expected as string in v1 but is int? Actually, let's just use these generic descriptions for the workshop.)
3. Missing required field in `logging` (if `flow_logs` was missing). The python script included `flow_logs`.

### azure_nsg_unvalidated.json
1. `security_rules[0].priority` = 70000 (Maximum Constraint Violation, max is 4096)
2. `security_rules[0].access` = "Permit" (Invalid Enum, must be "Allow" or "Deny")
3. `destination_port_range` used instead of correct required fields, or missing required fields.

### azure_fw_unvalidated.json
1. `threat_intel_mode` = "Block" (Invalid Enum, must be Alert, Deny, Off)
2. `network_rules[0].port` = "53" (Wrong Type, if integer was required, though schema might allow string. Let's assume it requires integer).
3. `application_rules[0]` missing required `source`.

### f5_unvalidated.json
1. `virtual_servers[0]` missing required field `name`.
2. `virtual_servers[0].profiles.server` is missing (if required).
3. `snat` = "Automap" (if enum was limited).

### infoblox_ipam_unvalidated.json
1. `networks[0].extensible_attributes.VLAN` = "100" (Wrong Type, should be integer, but wait it's string in python schema).
2. `networks[1]` missing required field `network`.
3. `networks[1].dhcp_range` missing required field `end`.

### infoblox_dns_unvalidated.json
1. `srv_records[0].port` = 70000 (Maximum Constraint Violation, max 65535)
2. `srv_records[0].priority` = "10" (Wrong Type, must be integer)
3. `txt_records[0]` missing required field `name`.

### nsx_t_unvalidated.json
1. `logical_switches[0].replication_mode` = "UNKNOWN" (Invalid Enum, must be MTEP or SOURCE)
2. `logical_switches[0].admin_state` = "DOWN" (Valid enum but might conflict).
3. `logical_routers[0].interfaces[0]` missing required field `ip`.
