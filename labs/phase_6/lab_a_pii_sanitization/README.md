# Phase 6 Lab A: AI Security Sanitizer & Configuration Redaction

## Objective
Establish a Spec-Driven configuration sanitizer that ingests a high-risk Cisco IOS configuration (`sensitive_config.cfg`) containing cleartext passwords and SNMP communities, and programmatically redacts all secrets and translates private production IP bindings. This ensures configurations are fully compliant with security standards before being fed into external generative AI chats.

## Online Documentation References
- [Python re Regular Expression Library Documentation](https://docs.python.org/3/library/re.html)
- [Cisco switchport Configuration CLI Reference](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3900/software/release/11-0/command/reference/interface.html)

## Boilerplate Files
- [sensitive_config.cfg](sensitive_config.cfg) (Dirty switch configuration containing sensitive production passwords and IPs)

---

## Step-by-Step Lab Tasks

### Task 1: Audit the Sensitive Configuration
1. Open the [sensitive_config.cfg](sensitive_config.cfg) file.
2. Review the high-risk lines:
   - Plain-text operator/admin credentials (e.g. `password cleartextPass123`)
   - Read/write SNMP communities (e.g. `snmp-server community NetOpsSecretRO`)
   - Private production IPs (e.g. `10.120.45.1` and `10.120.100.1`)
3. Sending this file directly to public AI tools is a severe corporate security policy violation. We must build a local script to sanitize it automatically.

### Task 2: Initialize the OpenSpec Sanitizer Change
1. Open your terminal at the root of the project and initialize a new change:
   ```bash
   openspec new change "secret-sanitizer"
   ```
2. Open `openspec/changes/secret-sanitizer/proposal.md` and define the purpose:
   * **Why:** Corporate compliance requires automatic credential redaction and IP address masking before configuration details are sent to external LLMs.
   * **Capabilities:** Add a new capability `cisco-configuration-sanitizer`.

### Task 3: Define Sanitization Specifications
1. Open `openspec/changes/secret-sanitizer/specs/cisco-configuration-sanitizer/spec.md`.
2. Add the formal requirements:
   * **Requirement:** The script MUST read `sensitive_config.cfg` and output a clean configuration to `sanitized_config.cfg`.
   * **Requirement:** The script MUST find any occurrences of username passwords (`password <secret>`) or enable secrets (`secret 5 <hash>`) and redact the secret token with `[REDACTED_PASSWORD]`.
   * **Requirement:** The script MUST find any SNMP community string definitions (`snmp-server community <string>`) and redact the community key with `[REDACTED_SNMP]`.
   * **Requirement:** The script MUST translate all occurrences of private IPs matching `10.120.x.x` to equivalent safe `192.168.100.x` test ranges (e.g. `10.120.45.1` becomes `192.168.100.1`).
3. Check the status and compile the change metadata:
   ```bash
   openspec status --change "secret-sanitizer"
   ```

### Task 4: Apply Code Generation & Execute
1. Run `/opsx-apply` in Copilot Chat:
   > *"/opsx-apply secret-sanitizer"*
2. Review the generated Python script `sanitize.py` to ensure it parses the file.
3. Run the script:
   ```bash
   python sanitize.py
   ```
4. Verify that `sanitized_config.cfg` has been generated and contains no plain-text passwords or SNMP community strings.

### Task 5: Verify Solution Locally
1. Run the local self-checking tool to verify that your output config is fully compliant with the security standards:
   ```bash
   python verify.py
   ```
2. Ensure you receive a perfect score and Rank card!

---

## Hints
- **Python Regex Mappings:** Use `re.sub()` in Python to match and replace:
  - Password lines: `r"(username \S+ privilege \d+ password) \S+"` -> `r"\1 [REDACTED_PASSWORD]"`
  - SNMP lines: `r"(snmp-server community) \S+ (RO|RW)"` -> `r"\1 [REDACTED_SNMP] \2"`
  - IP Address masking: Write a helper function inside `re.sub` that extracts the subnet part and swaps `10.120.` with `192.168.100.`.
- **Failsafe Path:** If you get stuck with regex syntax, you can peek at the reference key under the [solutions/sanitize.py](solutions/sanitize.py) directory!

---

## Expected Output

### Expected Scorecard:
```text
$ python verify.py

=== NETOPS SANITIZATION SCORECARD ===
[✓] Check: sanitized_config.cfg exists ............. PASS
[✓] Check: username plain-text passwords redacted .. PASS
[✓] Check: enable secrets redacted ................. PASS
[✓] Check: SNMP community strings redacted ......... PASS
[✓] Check: 10.120.x.x IP addresses masked .......... PASS

=====================================================
⏱️  COMPLETION TIME: 03 minutes 14 seconds
👑  ACHIEVED RANK:  [ Compliance Champion ]
=====================================================
Status: 100% compliant. Configuration safe for external AI chats.
```
