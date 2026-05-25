# Phase 5 Lab E: Spec-Driven Python Diagrams

## Objective
Apply the principles of Spec-Driven Development (SDD) to programmatically generate professional infrastructure drawings using the Python `diagrams` library. In Phase 2, you prompted the AI to write a Python script for a Dual Datacenter. Now, you will use rigid specifications to generate that same script deterministically, and then scale it up to a massive Multi-Region Cloud Native Architecture.

## Online References
- [Python diagrams Library Official Documentation](https://diagrams.mingrammer.com/)
- [Graphviz Layout Visualization Tool](https://graphviz.org/)
- [OpenSpec Documentation](https://github.com/Fission-AI/OpenSpec)

---

## Step-by-Step Lab Tasks

### Task 1: Auto-Propose the SDD Change Context via AI
Instead of manually creating OpenSpec files, we will use the AI to generate the proposal and specifications.
1. Run the propose command in Copilot Chat:
   > *"/opsx-propose Create a sdd-python-graphics change for a python-graphics-automation capability. Programmatic, repeatable network documentation is required. The script MUST programmatically represent two Datacenters: DC1 and DC2 using the diagrams Cluster grouping. Each DC MUST contain a Spine Layer (2 switches) and a Compute Leaf Layer (4 switches). The script MUST use diagrams.generic.network.Switch. The script MUST be written in Python, using the diagrams library to generate a PNG file named dual_dc_topology.png."*
2. Wait for the AI to auto-generate the `proposal.md`, `design.md`, `tasks.md`, and `spec.md` artifacts.

### Task 2: Part 1 - Review Specs and Generate The Dual-Datacenter Topology
1. Open the specification file: `openspec/changes/sdd-python-graphics/specs/python-graphics-automation/spec.md`.
2. Review the generated requirements mapping out the Dual-DC layout. Ensure the AI used strict normative language (`MUST` or `SHALL`) and exactly 4 hashtags (`#### Scenario:`) for scenarios. Adjust the requirements manually if necessary.
3. Validate and apply the change:
   ```bash
   openspec status --change "sdd-python-graphics"
   ```
   *Then run this in Copilot Chat:*
   > *"/opsx-apply sdd-python-graphics"*
5. Install the required Python library and run the script locally to render the drawing:
   ```bash
   pip install diagrams
   python dual_dc_builder.py
   ```
   *(Note: This library relies on Graphviz. If local Graphviz is not installed, install it via `brew install graphviz`).*

### Task 3: Part 2 - The Complex Cloud Scale-Up
1. Return to your `spec.md` and **delete** the old requirements.
2. Write **new** requirements for a complex AWS Cloud-Native scale-up:
   *   **Requirement:** The script MUST represent a Global Multi-Region AWS Architecture.
   *   **Requirement:** There MUST be two regions: `us-east-1` and `eu-west-1`.
   *   **Requirement:** Each region MUST contain a VPC Cluster, with a public subnet (containing an ALB) and a private subnet (containing an ASG of EC2 instances and an RDS database).
   *   **Requirement:** A global Route53 DNS node MUST load balance traffic between the two ALBs.
   *   **Requirement:** The script MUST use specific AWS nodes (e.g. `diagrams.aws.network.Route53`, `diagrams.aws.network.ELB`, `diagrams.aws.compute.EC2`, `diagrams.aws.database.RDS`).
   *   **Requirement:** The script MUST generate a PNG named `global_aws_topology.png`.
3. Re-run `/opsx-apply "sdd-python-graphics"`.
4. **Audit the output:** Run the generated script. Did the agent successfully import the AWS node namespaces and cluster them correctly?

### Task 4: Validate Your Work
Run the local self-checking validation tool in your terminal:
```bash
python verify.py
```

---

## Expected Output

You should see both a `dual_dc_topology.png` and a `global_aws_topology.png` rendered locally by your Python scripts.
