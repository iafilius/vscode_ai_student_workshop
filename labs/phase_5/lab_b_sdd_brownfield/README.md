# Phase 5 Lab B: Brownfield Refinement (OpenSpec)

## Objective
Learn how to use Spec-Driven Development to maintain and upgrade legacy, poorly-documented network code. You will reverse-engineer a specification from a legacy subnet parsing script, and then execute a change to support IPv6 address validation.

## Online Documentation Reference
- [Python ipaddress Standard Library Docs](https://docs.python.org/3/library/ipaddress.html)
- [OpenSpec Spec Migration and Delta Compilation Guides](https://github.com/Fission-AI/OpenSpec/blob/main/docs/migration.md)

---

## Step-by-Step Lab Tasks

### Task 1: Audit the Legacy Script
1. Navigate to the `labs/phase_5/lab_b_sdd_brownfield/` folder.
2. Open and inspect the messy legacy script: [legacy_parser.py](legacy_parser.py). It parses basic IPv4 subnet ranges but lacks robust checks or any IPv6 support.

### Task 2: Auto-Propose the Subnet Parser Upgrade
Instead of manually creating OpenSpec files, we will use the AI to generate the proposal and reverse-engineer the legacy script into a formal specification.
1. In Copilot Chat, run the propose command:
   > *"/opsx-propose Create a brownfield-parser-refinement change for the legacy-subnet-parser capability. Reverse-engineer an OpenSpec spec.md file based on the existing legacy_parser.py script in labs/phase_5/lab_b_sdd_brownfield/. Add a new requirement: The parsing function MUST accept an IPv6 address string and validate its CIDR formatting (e.g. 2001:db8::/32)."*
2. Wait for the AI to auto-generate the `proposal.md`, `design.md`, `tasks.md`, and `spec.md` artifacts.

### Task 3: Review and Refine Specifications
1. Open the generated file: `openspec/changes/brownfield-parser-refinement/specs/legacy-subnet-parser/spec.md`.
2. Review the reverse-engineered requirements and the new IPv6 requirement. 
3. Ensure the AI followed the strict OpenSpec format (SHALL/MUST keywords, exactly 4 hashtags `####` for Scenarios). Refine it if necessary.

### Task 4: Compile and Refactor
1. Verify the change status:
   ```bash
   openspec status --change "brownfield-parser-refinement"
   ```
2. Run `/opsx-apply brownfield-parser-refinement` to prompt the agent to refactor `legacy_parser.py` seamlessly, adding high-performance IPv6 capability while keeping the legacy IPv4 functions untouched.
3. Test your upgraded script:
   ```bash
   python legacy_parser.py --ip "2001:db8::1" --mask "32"
   ```

---

## Hints
* *Task 3 Tip:* Make sure the reverse-engineered spec matches OpenSpec standards (normative SHALL/MUST keywords, exactly 4 hashtags `####` for Scenarios).
* *Python Tip:* Leverage Python's built-in `ipaddress` module (`ipaddress.IPv6Network` and `ipaddress.IPv4Network`) inside `legacy_parser.py` to achieve bulletproof CIDR validation.

---

## Expected Output

### Expected Upgraded Parser Output:
```text
$ python legacy_parser.py --ip "2001:db8::1" --mask "32"
Subnet: 2001:db8::/32 - VALID IPv6 Subnet Allocation.
Hosts in Subnet: 79228162514264337593543950336
```
