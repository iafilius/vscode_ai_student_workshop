# Phase 6 Lab A: AI Security Sanitizer & Configuration Redaction

## 🌟 Introduction
**What this phase brings:** Practical application of AI for high-stakes security operations.
**Why we are doing this:** Sending sensitive production configurations (with cleartext passwords and IPs) to external cloud AI providers is a severe security violation. We need automated ways to redact this data *before* it leaves our perimeter.
**What you will practice:**
- Building an automated PII/Configuration sanitizer
- Using regex to scrub secrets and mask IP addresses
- Validating configurations for compliance

---

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

### Task 2: Auto-Propose the Sanitizer via AI
Instead of creating files manually, let the AI generate the entire OpenSpec scaffolding using the `/opsx-propose` command.
1. Run this command in Copilot Chat:
   > *"/opsx-propose Create a secret-sanitizer change with a cisco-configuration-sanitizer capability. The script MUST read sensitive_config.cfg and output sanitized_config.cfg. It MUST redact 'password <secret>' and 'secret 5 <hash>' with [REDACTED_PASSWORD]. It MUST redact 'snmp-server community <string>' with [REDACTED_SNMP]. It MUST translate 10.120.x.x private IPs to safe 192.168.100.x IPs."*
2. Watch as the AI automatically generates the `proposal.md`, `design.md`, `tasks.md`, and `spec.md` artifacts in sequence!

### Task 3: Review and Refine Specifications
Because the AI generates the initial draft of the `spec.md`, you MUST verify it before applying the code.
1. Open the generated file: `openspec/changes/secret-sanitizer/specs/cisco-configuration-sanitizer/spec.md`.
2. Review the `## ADDED Requirements` section. 
3. Ensure the AI used strict normative language (`MUST` or `SHALL`) and exactly included the redaction strings (`[REDACTED_PASSWORD]`, `[REDACTED_SNMP]`). Adjust the requirements manually if the AI missed any nuance.
4. Verify the syntax is valid:
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

## Pro-Tip

**Local Offline Agents:** Utilizing local, offline-capable agents guarantees that highly sensitive configuration files and PII never leave your secure perimeter. This makes AI viable for high-compliance environments like finance and healthcare where transmitting data to external third-party cloud models is strictly prohibited.

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

---

## Lab Retrospective

Take a moment to reflect on this lab session:
* **What went OK?**
* **What could be improved?**
* **Was the AI helpful?**
* **What prompting techniques proved most effective?**
