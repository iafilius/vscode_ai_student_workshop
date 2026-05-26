# Phase 2 Lab B: Network Hot Potatoes & Prompting Tasks

## Objective
> **Context:** Building on our foundational prompting skills from Lab A, we will now tackle common operational NetOps tasks.

Apply advanced prompting techniques (personas, constraints, few-shot examples) to solve three standard daily Network Operations tasks: DNS zone migration, firewall security rule drafting, and IPAM allocation validation.

## Online Documentation Reference
- [Bind9 Zone File Documentation](https://bind9.readthedocs.io/en/latest/reference.html#zone-file)
- [Cisco ASA Access Control Lists Reference](https://www.cisco.com/c/en/us/support/security/asa-5500-series-next-generation-firewalls/products-installation-and-configuration-guides-list.html)
- [RFC 1918 Private IP Address Allocation](https://datatracker.ietf.org/doc/html/rfc1918)

## Boilerplate Files
- [dns_legacy.txt](dns_legacy.txt) — Unstructured legacy DNS records (your input to the AI)
- [subnet_list.txt](subnet_list.txt) — IPAM allocation list with hidden overlaps (your input to the AI)

## Output Files (Save Your AI Outputs Here)
- [dns_bind9.zone](dns_bind9.zone) — Save your Bind9 zone records here
- [cisco_firewall_rules.txt](cisco_firewall_rules.txt) — Save your Cisco ASA ACL rules here
- [aws_sg_rules.json](aws_sg_rules.json) — Save your AWS Security Group rules here
- [azure_nsg_rules.json](azure_nsg_rules.json) — Save your Azure NSG rules here
- [nsxt_dfw_rules.json](nsxt_dfw_rules.json) — Save your NSX-T DFW rules here
- [ipam_audit.txt](ipam_audit.txt) — Save your IPAM conflict report here

---

## Step-by-Step Lab Tasks

### Task 1: DNS Legacy Record Migration
1. Open [dns_legacy.txt](dns_legacy.txt) and select all its contents.
2. Open **VS Code Copilot Chat** (`Cmd+Shift+I` on macOS) and submit the following prompt:
   > *"Act as a Senior Bind9 DNS Administrator. Convert this legacy unstructured log into a valid, standard Bind9 zone configuration file block. Follow standard tab-spaced zone formatting. Include inline comments explaining each record type. For each record, include a metadata comment containing the owner, requester, date_time, source_owner, and destination_owner. If the owner or requester is unknown or missing, default them to 'YOU' and 'current department'."*
3. Copy the generated Bind9 records into [dns_bind9.zone](dns_bind9.zone).

### Task 2: Multi-Vendor Firewall Rule Translation
1. Open **VS Code Copilot Chat** and submit the following prompt:
   > *"Act as a Lead Security Engineer. Generate secure, minimal firewall rules for the following request: 'Allow HTTPS web traffic and PostgreSQL traffic from the corporate DMZ network segment (192.168.45.0/24) to the Internal Database server cluster residing at IP 10.10.200.50 on port 5432. Add a constraint to deny all other DMZ traffic to that specific host.' Generate the configuration in four distinct formats: Cisco ASA, AWS Security Group (JSON), Azure NSG (JSON), and VMware NSX-T DFW (JSON). Output each format in a separate markdown code block. For each generated rule or resource, embed a metadata block containing owner, requester, date_time, source_owner, and destination_owner. Use 'YOU' and 'current department' as defaults."*
2. Copy the generated configurations into their respective files: [cisco_firewall_rules.txt](cisco_firewall_rules.txt), [aws_sg_rules.json](aws_sg_rules.json), [azure_nsg_rules.json](azure_nsg_rules.json), and [nsxt_dfw_rules.json](nsxt_dfw_rules.json).

### Task 3: IPAM Allocation Conflict Check
1. Open [subnet_list.txt](subnet_list.txt) and select all its contents.
2. Open **VS Code Copilot Chat** and submit the following prompt:
   > *"Analyze this list of requested IPAM allocations for any subnet overlapping or CIDR layout errors. Explain exactly where the overlaps occur:*
   > *1. subnet-a: 10.150.32.0/20*
   > *2. subnet-b: 10.150.35.0/24*
   > *3. subnet-c: 10.150.48.0/22*
   > *4. subnet-d: 10.150.32.0/24*
   > 
   > *Include a metadata comment for each finding that specifies owner, requester, date_time, source_owner, and destination_owner. Default unknown values to 'YOU' and 'current department'."*
3. Copy the AI's conflict analysis into [ipam_audit.txt](ipam_audit.txt).

### Task 4: Validate Your Work
1. Run the local self-checking validation tool in your terminal:
   ```bash
   python verify.py
   ```
2. Verify that all three tasks pass the diagnostic checks!

---

## Hints
* *Task 1 Tip:* Make sure the Bind9 output maps `@ IN SOA` details correctly if asked for a full zone block, or strictly maps `A`, `CNAME`, and `MX` records if parsing individual entries.
* *Task 2 Tip:* Ensure the Cisco ASA ACL statements specify exact port definitions: `eq 443` and `eq 5432` and correctly map the subnet mask. The deny rule must explicitly target `host 10.10.200.50`.
* *Task 3 Tip:* Convert the IP addresses and CIDR masks to binary ranges to verify that the AI's explanation of sub-CIDR collisions matches mathematically. Note that `subnet-c` is clean — it falls outside the conflicting range.
* **Peekable Solution:** If you get stuck, you can inspect the reference outputs under the [solutions/](solutions/) folder.

---

## Expected Output

### Expected DNS Output (`dns_bind9.zone`):
```text
ams-switch-01.eu.internal.  3600  IN  A      10.240.10.5
db-primary.eu.internal.     1800  IN  CNAME  ams-db-srv.eu.internal.
@                           86400 IN  MX 10  mail-relay.eu.internal.
```

### Expected Firewall Output (`cisco_firewall_rules.txt`):
```text
access-list DMZ_TO_INTERNAL extended permit tcp 192.168.45.0 255.255.255.0 host 10.10.200.50 eq 443
access-list DMZ_TO_INTERNAL extended permit tcp 192.168.45.0 255.255.255.0 host 10.10.200.50 eq 5432
access-list DMZ_TO_INTERNAL extended deny ip 192.168.45.0 255.255.255.0 host 10.10.200.50
```

### Expected AWS SG Output (`aws_sg_rules.json`):
```json
{
  "SecurityGroupIngress": [
    { "IpProtocol": "tcp", "FromPort": 443, "ToPort": 443, "IpRanges": [{"CidrIp": "192.168.45.0/24"}] },
    { "IpProtocol": "tcp", "FromPort": 5432, "ToPort": 5432, "IpRanges": [{"CidrIp": "192.168.45.0/24"}] }
  ]
}
```

### Expected Azure NSG Output (`azure_nsg_rules.json`):
*(Snipped for brevity)* Should contain `Allow_DMZ_HTTPS` (port 443), `Allow_DMZ_PostgreSQL` (port 5432), and a `Deny_DMZ_Other` block.

### Expected NSX-T DFW Output (`nsxt_dfw_rules.json`):
*(Snipped for brevity)* Should contain `ALLOW` rules for `HTTPS` and `TCP_5432`, and a `DROP` rule for any other traffic from `192.168.45.0/24` to `10.10.200.50`.

### Expected IPAM Audit Output (`ipam_audit.txt`):
```text
=== IPAM AUDIT CONFLICT REPORT ===
- CONFLICT: 'subnet-b' (10.150.35.0/24) resides completely inside the range of 'subnet-a' (10.150.32.0/20: 10.150.32.0 - 10.150.47.255).
- CONFLICT: 'subnet-d' (10.150.32.0/24) resides completely inside the range of 'subnet-a' (10.150.32.0/20) and overlaps with the base address of subnet-a.
==================================
```

---

## Lab Retrospective

Take a moment to reflect on this lab session:
* **What went OK?**
* **What could be improved?**
* **Was the AI helpful?**
* **What prompting techniques proved most effective?**
