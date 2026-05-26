# Phase 8 Lab A: Policy-as-Code & Automated Multi-Platform Firewall Generation

## 🌟 Introduction
**What this phase brings:** Bridging the gap between isolated scripts and enterprise CI/CD automation.
**Why we are doing this:** The ultimate goal of AI in NetOps is Policy-as-Code. We need systems that can autonomously generate multi-cloud firewall rules based on logical intent, rather than manual CLI typing.
**What you will practice:**
- Developing a Python rule compiler
- Parsing multi-cloud network topology datasets
- Generating cryptographic trace IDs for rule audits

---

## Objective
Fabricate an OpenSpec specification and develop a Python rule generator that accepts logical connection requests, performs spatial and policy lookups against a pre-populated hybrid multi-cloud dataset (`network_topology_data.json`), and automatically constructs vendor-specific firewall rules with cryptographic trace tracking.

## Online References
- [Python JSON Library Documentation](https://docs.python.org/3/library/json.html)
- [OpenSpec Change Specification and Design Compilation](https://github.com/Fission-AI/OpenSpec/blob/main/docs/compilation.md)

---

## Step-by-Step Lab Tasks

### Task 1: Auto-Propose the OpenSpec Change via AI
Instead of manually creating OpenSpec files, we will use the AI to generate the proposal and specifications.
1. Run the propose command in Copilot Chat:
   > *"/opsx-propose Create a policy-based-firewall-automation change for a policy-based-firewall-compilation capability. Cloud-native and hybrid multi-cloud firewalls require programmatic policy compilation. The script MUST load network_topology_data.json dynamically from the filesystem. The script MUST accept name-based source and destination connectivity queries. The script MUST perform lookups in the ipCard map to resolve logical names. The script MUST validate if the requested connection is explicitly allowed under the networkSecurityPolicy list. If the connection crosses zone boundaries without an explicit permit rule, it MUST return a status of DENIED. The script MUST output a single JSON telemetry block containing traceId, status, resolvedSourceIp, resolvedDestinationIp, enforcementPoints, and compiledRules."*
2. Wait for the AI to auto-generate the `proposal.md`, `design.md`, `tasks.md`, and `spec.md` artifacts.

### Task 2: Review and Refine Specifications
1. Open the specification file: `openspec/changes/policy-based-firewall-automation/specs/policy-based-firewall-compilation/spec.md`.
2. Review the generated requirements for the firewall compiler. Ensure the AI used strict normative language (`MUST` or `SHALL`) and exactly 4 hashtags (`#### Scenario:`) for scenarios. Adjust the requirements manually if necessary.
3. Validate and apply the change:
   ```bash
   openspec status --change "policy-based-firewall-automation"
   ```

### Task 3: Generate the Rules Compiler Script
1. Run the `/opsx-apply` command in your terminal to let the agent compile the Python utility `generate_rules.py` directly inside this lab directory:
   ```bash
   /opsx-apply "policy-based-firewall-automation"
   ```
2. Inspect the generated script `generate_rules.py`. Make sure the Python file handles parsing arguments or has high-quality mocked test executions.

### Task 4: Test Multi-Cloud & Cross-Zone Connectivity Cases
Verify that your firewall script handles all of the following scenarios:
1.  **Scenario A (Intra-Zone Allowed):** On-prem web tier to On-prem DB tier (`on-prem-web-tier` -> `on-prem-db-tier`) on port `5432`.
    *   *Result:* Resolves to `ALLOWED` because policy exists. Enforcement point should be `AMS-SEC-FW-01`.
2.  **Scenario B (Inter-Zone Cloud-to-On-Prem):** AWS app servers to On-prem secure database (`aws-app-servers` -> `on-prem-db-tier`) on port `5432`.
    *   *Result:* Resolves to `ALLOWED` based on multi-cloud transport policy. Enforcement points include `AWS-SEC-GROUP-01` and `AMS-SEC-FW-01`.
3.  **Scenario C (Blocked / Denied Case):** On-prem web tier to Azure management hosts (`on-prem-web-tier` -> `azure-mgmt-hosts`) on port `22`.
    *   *Result:* Resolves to `DENIED` since there is no explicit permit policy between these zones.

---

## Hints
*   **Unique Trace ID:** In Python, import the standard `uuid` library and generate a unique trace context via `str(uuid.uuid4())`.
*   **Argument Handling:** Make sure your Python script is executable via CLI, for example:
    ```bash
    python generate_rules.py --src aws-app-servers --dst on-prem-db-tier --port 5432
    ```

---

## Pro-Tip

**Pipeline Automation:** Agents don't just live in the IDE. You can integrate these exact same SKILLs and KIs into your CI/CD pipelines (e.g., GitHub Actions, GitLab CI) to automatically audit firewall policy Pull Requests against your security baselines before human review.

---

## Expected Output

### Expected JSON Telemetry Rule Output:
```json
{
  "traceId": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "status": "ALLOWED",
  "resolvedSource": {
    "name": "aws-app-servers",
    "ipv4": "172.16.1.0/24",
    "ipv6": "2001:db8:abc:1::/64",
    "zone": "aws-vpc-app"
  },
  "resolvedDestination": {
    "name": "on-prem-db-tier",
    "ipv4": "10.100.20.0/24",
    "ipv6": "2001:db8:100:20::/64",
    "zone": "on-prem-secure"
  },
  "enforcementPoints": [
    "AWS-SEC-GROUP-01",
    "AMS-SEC-FW-01"
  ],
  "compiledRules": [
    {
      "platform": "aws_security_group",
      "targetDevice": "AWS-SEC-GROUP-01",
      "rule": {
        "IpProtocol": "tcp",
        "FromPort": 5432,
        "ToPort": 5432,
        "IpRanges": [{"CidrIp": "172.16.1.0/24"}]
      }
    },
    {
      "platform": "cisco_asa",
      "targetDevice": "AMS-SEC-FW-01",
      "rule": "access-list outside_access_in extended permit tcp 172.16.1.0 255.255.255.0 host 10.100.20.0 eq 5432"
    }
  ]
}
```

---

## Lab Retrospective

Take a moment to reflect on this lab session:
* **What went OK?**
* **What could be improved?**
* **Was the AI helpful?**
* **What prompting techniques proved most effective?**
