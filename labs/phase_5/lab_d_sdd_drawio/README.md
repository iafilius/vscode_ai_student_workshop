# Phase 5 Lab D: Spec-Driven Draw.io XML

## Objective
Apply the principles of Spec-Driven Development (SDD) to programmatically generate complex Draw.io XML schemas. In Phase 2, you saw how raw prompting fails spectacularly at calculating absolute X/Y spatial coordinates. Here, you will see how OpenSpec specifications can enforce coordinate mathematical logic to build clean, un-overlapped diagrams.

## Online References
- [Draw.io Online Diagramming Tool](https://app.diagrams.net/)
- [OpenSpec Documentation](https://github.com/Fission-AI/OpenSpec)

---

## Step-by-Step Lab Tasks

### Task 1: Initialize the SDD Change Context
1. Open your terminal in the workspace root and initialize a new OpenSpec change:
   ```bash
   openspec new change "sdd-drawio-xml"
   ```
2. Open `openspec/changes/sdd-drawio-xml/proposal.md` and define the scope:
   *   **Why:** Generating raw XML vector diagrams through unstructured chat results in overlapping shapes and floating lines. We need strict SDD constraints to govern coordinate mapping.
   *   **Capabilities:** Introduce a new capability `drawio-xml-automation`.

### Task 2: Part 1 - The Simple Web Topology
1. Open the specification file: `openspec/changes/sdd-drawio-xml/specs/drawio-xml-automation/spec.md`.
2. Write clear, testable requirements mapping out the simple AWS architecture from Phase 2:
   *   **Requirement:** The output MUST be a valid Draw.io XML file named `topology.drawio` in the `labs/phase_5/lab_d_sdd_drawio/` directory.
   *   **Requirement:** It MUST contain 1 Cloud Edge Firewall (Red), 2 Application Load Balancers (Purple), 4 Web Servers (Blue), and a Primary/Standby DB Cluster (Green cylinders).
   *   **Requirement:** All shapes MUST have explicitly calculated, non-overlapping `x` and `y` geometry coordinates.
   *   **Requirement:** All connections MUST be explicitly mapped using proper `source` and `target` vertex IDs.
3. Validate the change and apply it:
   ```bash
   openspec status --change "sdd-drawio-xml"
   /opsx-apply "sdd-drawio-xml"
   ```
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
