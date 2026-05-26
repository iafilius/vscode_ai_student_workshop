# Lab E (Bonus): Python Diagrams (Diagrams Package)

> **Context:** For the ultimate visual automation, let's write Python automation scripts that automatically calculate routing topography and generate diagrams.

Welcome to **Phase 2, Lab E**! 

In Lab C and D, you explored Markdown (Mermaid) and XML (Draw.io) based generation. In this lab, we bridge the gap. Python's `diagrams` library uses Python code to define the architecture, and it relies on Graphviz to handle the complex mathematical layout and coordinate positioning automatically. This allows you to combine **high-fidelity icons** (like AWS, Azure, Cisco) with **automatic layout routing**.

## Prerequisites

Because `diagrams` renders the images locally, you need the Graphviz C-library installed on your operating system, along with the python package.

1. Install Graphviz (Mac):
   ```bash
   brew install graphviz
   ```
2. Install the Python diagrams package:
   ```bash
   pip3 install diagrams
   ```

## Task 1: Generate the Python Code

We are going to ask the AI to generate the **Ultimate Dual-Datacenter Spine-Leaf Architecture** using the `diagrams` package. The AI knows how to import standard networking icons and group them into logical clusters.

1. Submit the following prompt to **VS Code Copilot Chat**:
   ```text
   Act as a Senior Network Architect. Write a Python script using the 'diagrams' library to generate a 'Dual Datacenter Spine-Leaf' architecture. 
   
   Requirements:
   - Use 'diagrams.generic.network.Switch' for switches and 'diagrams.onprem.compute.Server' for ESXi hosts.
   - Use 'diagrams.generic.network.Router' for the Core Routers.
   - Group the diagram into two main Clusters: "Datacenter 1 (DC1)" and "Datacenter 2 (DC2)".
   - Outside the Datacenters, create a DCI WAN cloud (use generic internet or cloud icon) and connect it to DCI Core Routers in both DCs.
   - In each DC, create a Cluster for "Spine Layer" containing 2 Spine switches.
   - In each DC, create a Cluster for "Compute Leaf Layer" containing 4 Compute switches.
   - In each DC, create a Cluster for "Compute Payload" containing 8 ESXi hosts (2 hosts connected to each Compute Leaf).
   
   Connect them properly:
   - Every Compute Leaf connects to both Spines in its respective DC.
   - Core Routers connect to both Spines in their respective DC.
   - Core Routers connect to the DCI WAN cloud.
   
   Output only valid Python code. Name the diagram output file "ultimate_datacenter_topology".
   ```

2. Open the `generate_diagram.py` file in this lab directory.
3. Replace the placeholder text by pasting the generated Python code into the file and save it.

## Task 2: Render the Diagram

1. Run the Python script in your terminal to render the PNG:
   ```bash
   python3 generate_diagram.py
   ```
2. If successful, you should see a new `.png` file appear in this directory (e.g., `ultimate_datacenter_topology.png`).
3. Open the `.png` file in VS Code or your default image viewer. Notice how Graphviz automatically handled the grouping, clustering, and line routing for you!

## Task 3: Validate Your Work

1. Run the local self-checking validation tool:
   ```bash
   python3 verify.py
   ```
2. The script will verify that your Python file exists, executes successfully, and produces a PNG output.

### Optional Task: Push the Boundaries
The `diagrams` library supports a huge variety of cloud providers (AWS, Azure, GCP), on-premise hardware, and custom styling. Try generating a brand new prompt to explore its limits! Ask the AI to:
* **Use Specific Vendor Icons:** Switch out the generic shapes for Cisco routers, AWS EC2 instances, or Kubernetes pods.
* **Customize Edge Attributes:** Instruct the AI to make the connections between the Spine and Leaf switches *thicker*, change the line *colors*, or use *dashed* lines for the DCI WAN connection.
* **Change Cluster Backgrounds:** Ask the AI to give the "Datacenter 1" cluster a blue background and "Datacenter 2" a green background.

---

## Hints
* **ModuleNotFoundError:** If the script fails with `No module named 'diagrams'`, ensure you ran `pip3 install diagrams`.
* **ExecutableNotFound:** If the script fails with `ExecutableNotFound: failed to execute PosixPath('dot')`, you missed the Graphviz OS-level installation (`brew install graphviz`).
* **Sneak Peek:** Want to see what the ultimate setup looks like? Check out the `solutions` folder for a reference implementation!

---

## Lab Retrospective

Take a moment to reflect on this lab session:
* **What went OK?**
* **What could be improved?**
* **Was the AI helpful?**
* **What prompting techniques proved most effective?**
