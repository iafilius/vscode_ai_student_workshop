# Phase 5 Lab D (Bonus): Spec-Driven Draw.io XML

## Objective
> **Context:** Let's use OpenSpec to generate Draw.io XML programmatically, scaling to a large SD-WAN overlay representation.

Apply the principles of Spec-Driven Development (SDD) to programmatically generate complex Draw.io XML schemas. In Phase 2, you saw how raw prompting fails spectacularly at calculating absolute X/Y spatial coordinates. Here, you will see how OpenSpec specifications can enforce coordinate mathematical logic to build clean, un-overlapped diagrams.

## Online References
- [Draw.io Online Diagramming Tool](https://app.diagrams.net/)
- [OpenSpec Documentation](https://github.com/Fission-AI/OpenSpec)

---

## Step-by-Step Lab Tasks

### Task 1: Auto-Propose the SDD Change Context via AI
Instead of manually creating OpenSpec files, we will use the AI to generate the proposal and specifications.
1. Run the propose command in Copilot Chat:
   > *"/opsx-propose Create a sdd-drawio-xml change for a drawio-xml-automation capability. Generating raw XML vector diagrams through unstructured chat results in overlapping shapes; we need strict SDD constraints. The output MUST be a valid Draw.io XML file named topology.drawio in labs/phase_5/lab_d_sdd_drawio/. It MUST contain 1 Cloud Edge Firewall (Red), 2 Application Load Balancers (Purple), 4 Web Servers (Blue), and a Primary/Standby DB Cluster (Green cylinders). All shapes MUST have explicitly calculated, non-overlapping x and y geometry coordinates. All connections MUST be explicitly mapped using proper source and target vertex IDs."*
2. Wait for the AI to auto-generate the `proposal.md`, `design.md`, `tasks.md`, and `spec.md` artifacts.

### Task 2: Part 1 - Review Specs and Generate The Simple Web Topology
1. Open the specification file: `openspec/changes/sdd-drawio-xml/specs/drawio-xml-automation/spec.md`.
2. Review the generated requirements mapping out the simple AWS architecture from Phase 2. Ensure the AI used strict normative language (`MUST` or `SHALL`) and exactly 4 hashtags (`#### Scenario:`) for scenarios. Adjust the requirements manually if necessary.
3. Validate and apply the change:
   ```bash
   openspec status --change "sdd-drawio-xml"
   ```
   *Then run this in Copilot Chat:*
   > *"/opsx-apply sdd-drawio-xml"*
4. **Compare:** Open the generated `topology.drawio` in VS Code (with the Draw.io extension installed) or web. Are the shapes still overlapping like they did in Phase 2? Or did the rigid spec constraints force the AI to do the coordinate math correctly?

### Task 3: Part 2 - The Complex Scale-Up
1. Return to your `spec.md` and **delete** the old requirements.
2. Write **new** requirements for an advanced SD-WAN overlay scale-up:
   *   **Requirement:** The output MUST be a valid Draw.io XML file named `sdwan_overlay.drawio` in the `labs/phase_5/lab_d_sdd_drawio/` directory.
   *   **Requirement:** The topology MUST represent a Global SD-WAN Overlay.
   *   **Requirement:** It MUST contain a central transit hub (composed of 2 Hub Routers).
   *   **Requirement:** It MUST contain 10 regional branch sites, each with a single Edge Router.
   *   **Requirement:** All branch Edge Routers MUST be connected to BOTH Hub Routers via IPsec tunnel lines (dashed lines).
   *   **Requirement:** The layout MUST be a circular or star layout, calculating `x` and `y` coordinates radially around the central hub to prevent overlapping.
3. Re-run `/opsx-apply "sdd-drawio-xml"`.
4. **Audit the output:** Did the agent manage to calculate radial geometry based on the spec? 

### Task 4: Validate Your Work
Run the local self-checking validation tool in your terminal:
```bash
python verify.py
```

---

## Expected Output

You should see both a `topology.drawio` and an `sdwan_overlay.drawio` file generated directly into this directory. When opened, the shapes should have distinct, calculated spatial coordinates rather than stacking awkwardly in the corner of the canvas.

---

## Lab Retrospective

Take a moment to reflect on this lab session:
* **What went OK?**
* **What could be improved?**
* **Was the AI helpful?**
* **What prompting techniques proved most effective?**
