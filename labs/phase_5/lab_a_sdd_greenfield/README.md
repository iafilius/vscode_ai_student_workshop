# Phase 5 Lab A: Greenfield Development (OpenSpec)

## Objective
Learn the lifecycle of Spec-Driven Development (SDD) by proposing, designing, spec'ing, and automatically implementing a brand-new internal network scanning utility from scratch using the OpenSpec CLI tool.

## Online Documentation Reference
- [OpenSpec CLI Command Reference](https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md)
- [Spec-Driven Development Best Practices](https://github.com/Fission-AI/OpenSpec/blob/main/docs/sdd.md)

---

## Step-by-Step Lab Tasks

### Task 1: Propose the Greenfield Scan Tool
OpenSpec enforces a strict, robust requirement and design loop before any code is generated.
1. Navigate your terminal to the current directory: `labs/phase_5/lab_a_sdd_greenfield/`.
2. Propose a new change using the CLI:
   ```bash
   openspec new change "greenfield-network-scanner"
   ```
3. Open the newly created proposal file: `openspec/changes/greenfield-network-scanner/proposal.md` and describe the scanning script:
   * **Why:** Need a lightweight, local scanning utility to check availability of host SSH (22) and HTTP (80) ports across standard subnets.
   * **Capabilities:** Add a new capability `network-scan-utility`.
4. Open the design file: `openspec/changes/greenfield-network-scanner/design.md`. Document the design choice to use Python's built-in `socket` module (avoiding external dependencies like `nmap` to keep runtime environments simple).

### Task 2: Write Specifications
1. Open the spec file: `openspec/changes/greenfield-network-scanner/specs/network-scan-utility/spec.md`.
2. Add normative requirements detailing port verification:
   * **Requirement:** The script SHALL iterate through a given CIDR block, attempting to open socket connections on port 22 and 80.
   * **Requirement:** The timeout for each connection attempt SHALL be limited to `0.5` seconds to ensure fast scanning.
   * Add a `#### Scenario:` block detailing successful scan outcomes.

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
