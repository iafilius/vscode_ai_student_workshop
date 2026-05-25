# Phase 5 Lab A: Greenfield Development (OpenSpec)

## Objective
Learn the lifecycle of Spec-Driven Development (SDD) by proposing, designing, spec'ing, and automatically implementing a brand-new internal network scanning utility from scratch using the OpenSpec CLI tool.

## Online Documentation Reference
- [OpenSpec CLI Command Reference](https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md)
- [Spec-Driven Development Best Practices](https://github.com/Fission-AI/OpenSpec/blob/main/docs/sdd.md)

---

## Step-by-Step Lab Tasks

### Task 1: Auto-Propose the Greenfield Scan Tool
Instead of manually creating OpenSpec files, we will use the AI to generate the proposal and specifications.
1. Navigate your terminal to the current directory: `labs/phase_5/lab_a_sdd_greenfield/`.
2. Run the propose command in Copilot Chat:
   > *"/opsx-propose Create a greenfield-network-scanner change for a network-scan-utility capability. We need a lightweight, local scanning utility to check availability of host SSH (22) and HTTP (80) ports across standard subnets. It should use Python's built-in socket module. The script SHALL iterate through a given CIDR block attempting to open socket connections on port 22 and 80. The timeout for each connection attempt SHALL be limited to 0.5 seconds."*
3. Wait for the AI to auto-generate the `proposal.md`, `design.md`, `tasks.md`, and `spec.md` artifacts.

### Task 2: Review and Refine Specifications
1. Open the spec file: `openspec/changes/greenfield-network-scanner/specs/network-scan-utility/spec.md`.
2. Review the generated requirements detailing port verification.
3. Ensure the AI used strict normative language (`MUST` or `SHALL`) and exactly 4 hashtags (`#### Scenario:`) for scenario blocks. Adjust the requirements manually if the AI missed any nuance.

### Task 3: Compile and Apply the Change
1. Validate the OpenSpec change:
   ```bash
   openspec status --change "greenfield-network-scanner"
   ```
2. Once validated, run the apply task in Copilot Chat:
   > *"/opsx-apply greenfield-network-scanner"*
3. The AI agent will autonomously read your specs and write the complete, high-performance scanning script directly to your greenfield directory!
4. Verify by running the generated script:
   ```bash
   python scanner.py --range 127.0.0.1/32
   ```

---

## Hints
* If the compiler errors on your spec, verify that every `### Requirement:` block is immediately followed by at least one `#### Scenario:` (exactly 4 hashtags).
* Keep timeouts small (`0.5` or `1.0` seconds) so the scanner doesn't hang on dead ports.

---

## Expected Output

### Expected Specs Structure:
```markdown
## ADDED Requirements

### Requirement: Single Host Port Scanning
The scanner script SHALL iterate through a user-specified CIDR IP subnet block and check availability of ports 22 and 80.

#### Scenario: Active host discovered
- **WHEN** port 22 or 80 accepts socket connection
- **THEN** output the host IP address and state 'ACTIVE'
```

### Expected Execution Log:
```text
$ python scanner.py --range 127.0.0.1/32
Scanning 127.0.0.1/32...
[+] 127.0.0.1: Port 22 (SSH) - ACTIVE
[+] 127.0.0.1: Port 80 (HTTP) - ACTIVE
Scan complete. 1 host scanned.
```
