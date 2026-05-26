# Phase 5 Lab C: Spec-Driven Mermaid Flowcharting

## Objective
> **Context:** Spec-Driven Development isn't just for code. Let's use OpenSpec to massively scale a Mermaid topology drawing to a complex Multi-DC design.

Apply the principles of Spec-Driven Development (SDD) to programmatically generate Mermaid Flowcharts. You will compare this structured, deterministic approach to the raw, unstructured prompting approach you experienced in Phase 2. First, you will recreate the simple office topology. Then, you will instantly scale it up to a complex Multi-DC Spine-Leaf fabric simply by updating your specifications.

## Online References
- [Mermaid Flowchart Syntax](https://mermaid.js.org/syntax/flowchart.html)
- [OpenSpec Documentation](https://github.com/Fission-AI/OpenSpec)

---

## Step-by-Step Lab Tasks

### Task 1: Auto-Propose the SDD Change Context via AI
Instead of manually creating OpenSpec files, we will use the AI to generate the proposal and specifications.
1. Run the propose command in Copilot Chat:
   > *"/opsx-propose Create a sdd-mermaid-flowchart change for a mermaid-topology-automation capability. The diagram MUST be a Top-Down Mermaid Flowchart. It MUST contain 1 Core Switch (AMS-CORE-01), 2 Distribution Switches in a mesh to the Core, and 4 Access Switches dual-homed to the Distribution switches. Access switches MUST be grouped into Mermaid subgraphs by VLAN (VLAN 10 and VLAN 20). The output file MUST be named topology.mmd and saved in labs/phase_5/lab_c_sdd_mermaid/."*
2. Wait for the AI to auto-generate the `proposal.md`, `design.md`, `tasks.md`, and `spec.md` artifacts.

### Task 2: Part 1 - Review Specs and Generate The Simple Topology
1. Open the specification file: `openspec/changes/sdd-mermaid-flowchart/specs/mermaid-topology-automation/spec.md`.
2. Review the generated requirements mapping out the simple office topology. Ensure the AI used strict normative language (`MUST` or `SHALL`). Adjust the requirements manually if necessary.
3. Validate and apply the change:
   ```bash
   openspec status --change "sdd-mermaid-flowchart"
   ```
   *Then run this in Copilot Chat:*
   > *"/opsx-apply sdd-mermaid-flowchart"*
4. **Compare:** Look at the generated `topology.mmd`. How does the code and the layout compare to what you got in Phase 2?

### Task 3: Part 2 - The Complex Scale-Up
Raw prompting struggles with scale because LLMs lose track of implicit constraints in massive meshes. SDD solves this because specifications act as rigid rails.
1. Return to your `spec.md` and **delete** the old requirements.
2. Write **new** requirements for a massive scale-up:
   *   **Requirement:** The diagram MUST represent a redundant datacenter fabric.
   *   **Requirement:** There MUST be 2 datacenters: DC1 and DC2.
   *   **Requirement:** Each datacenter MUST have 2 Spine switches (4 Spines total).
   *   **Requirement:** Each datacenter MUST have 8 Leaf switches (16 Leafs total).
   *   **Requirement:** Every Leaf switch MUST be dual-homed to both Spine switches within its own datacenter (Full Mesh).
   *   **Requirement:** The output MUST use the multi-edge operator `&` (e.g. `Spine1 & Spine2 --> Leaf1 & Leaf2`) to maintain concise syntax.
   *   **Requirement:** The output file MUST be named `spine_leaf.mmd` and saved in the `labs/phase_5/lab_c_sdd_mermaid/` directory.
3. Re-run `/opsx-apply "sdd-mermaid-flowchart"`.
4. **Audit the output:** Did the agent successfully generate the massive mesh using the `&` operator without tangling the syntax?

### Task 4: Validate Your Work
Run the local self-checking validation tool in your terminal:
```bash
python verify.py
```

---

## Expected Output

You should see both a `topology.mmd` and a `spine_leaf.mmd` file generated directly into this directory, with flawlessly structured Mermaid syntax that renders perfectly in VS Code's Markdown Preview.
