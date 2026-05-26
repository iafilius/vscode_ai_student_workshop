# Phase 2 Lab D (Bonus): Draw.io XML Prompting

## Objective
> **Context:** Taking visual generation a step further, let's learn how to instruct the AI to generate raw XML schema data compatible with Draw.io.

Explore the limitations of AI coordinate mapping when generating complex, vector-based XML diagrams. You will prompt the AI to generate raw XML compatible with the **Draw.io** schema, then import the result to audit spatial alignment and overlapping.

## Online References
- [Draw.io Online Diagramming Tool](https://app.diagrams.net/)
- [Draw.io XML Schema Format Reference](https://www.drawio.com/doc/faq/xml-schema-details)

---

## Step-by-Step Lab Tasks

> [!IMPORTANT]
> **Important Note on Viewing `.drawio` Files**
> 
> `.drawio` files are raw XML documents under the hood. By default, VS Code displays this XML code instead of the visual diagram. 
> 
> **To view diagrams natively in VS Code:**
> 1. Open the Extensions view (`Cmd+Shift+X` on Mac).
> 2. Search for **Draw.io Integration** (by Henning Dieterichs).
> 3. Click **Install**.
> 4. Close and re-open any `.drawio` file to see the interactive canvas!
> 
> **Alternative 1: Desktop App (Local)**
> Install the standalone Draw.io desktop app via Homebrew:
> `brew install --cask drawio`
> 
> **Alternative 2: Web App (No Install)**
> Go to [app.diagrams.net](https://app.diagrams.net/), click **Open Existing Diagram**, and select the file from your computer.
> 
> *⚠️ **Warning:** Using the public web app could expose confidential infrastructure details to a third-party service. For proprietary designs, please use the local VS Code extension or the desktop app.*

### Task 1: Generate Raw Draw.io XML
Draw.io uses compressed XML schemas to map nodes, visual properties, connection pathways, and strict geometric coordinates. Asking a text-based LLM to calculate absolute spatial coordinates is a challenging mathematical task that exposes severe visual quality and alignment limitations.

1. Submit the following switch topology prompt to **VS Code Copilot Chat**:
   ```text
   Act as a Senior Cloud Solutions Architect. Write a raw, valid, uncompressed XML file compatible with the Draw.io schema representing an Enterprise Multi-AZ Web Architecture:
   - 1 Cloud Edge Firewall named 'EDGE-FW-01' positioned at the top center. Use a Red fill color (#FFCCCC) and a dark red stroke.
   - 2 Application Load Balancers named 'ALB-AZ1' and 'ALB-AZ2' positioned below the firewall. Use a Purple fill color (#E1BEE7) and dark purple stroke.
   - 4 Web Servers named 'WEB-01' through 'WEB-04' positioned in the middle. Use a Blue fill color (#BBDEFB) and dark blue stroke.
   - 2 Primary/Standby Database Clusters named 'DB-MASTER' and 'DB-STANDBY' at the bottom. Use a Green fill color (#C8E6C9), dark green stroke, and make them Cylinder shapes.
   
   Connect them with lines matching the topology flow:
   - EDGE-FW-01 connects to both ALBs.
   - ALB-AZ1 connects to WEB-01 and WEB-02.
   - ALB-AZ2 connects to WEB-03 and WEB-04.
   - All 4 Web Servers connect to the DB-MASTER.
   - DB-MASTER connects to DB-STANDBY for replication.
   
   Make sure you calculate distinct X and Y coordinates for each node so they do not overlap. Output ONLY valid XML code blocks.
   ```

2. Copy the AI's XML code blocks.
3. Open the existing `topology.drawio` file inside this lab directory.
4. Select all text (`Cmd+A` / `Ctrl+A`) and paste the AI's XML code to overwrite the placeholder. Save the file.

### Task 2: Import & Audit Visual Quality
1. Open [Draw.io](https://app.diagrams.net/) in your web browser.
2. Select **File -> Open From -> Device...** and choose your saved `topology.drawio` file.
3. **Analyze the imported drawing:**
   *   **Shape Overlap:** Are the switches sitting cleanly next to each other, or are they stacked directly on top of each other?
   *   **Floating Connections:** Do connection lines snap perfectly to the edge of the switch boxes, or are they floating in empty space or pointing to arbitrary canvas locations?
   *   **Layout Symmetry:** Does the resulting topology look visually professional, or is there major alignment skew?
   *   **Manual Effort:** Estimate how much manual repositioning is required to make the diagram readable.

### Task 3: Validate Your Work
1. Run the local self-checking validation tool in your terminal:
   ```bash
   python verify.py
   ```
2. Verify that your XML successfully passes the validation check!

### Optional Task: Push the Boundaries
Now that you've seen both the magic and the madness of AI-generated vector topologies, try experimenting with more complex requests in a new prompt! Discover what works well and where the AI completely loses spatial awareness. Try asking the AI to:
* **Add Multiple Tabs:** Generate a second `<diagram>` page inside the XML for a "Logical Data Flow" view.
* **Use Realistic Icons:** Ask the AI to use standard AWS, Azure, or Cisco networking icons instead of basic rectangles.
* **Get Fancy with Styling:** Instruct the AI to apply isometric 3D shapes, drop shadows, or gradient fills.

---

## Hints
*   **Import Mismatched Tag Errors:** If Draw.io fails to open the file, the AI may have cut off the XML generation halfway through or introduced bad tags. Highlight the error and ask: *"Your XML was truncated or syntax-flawed. Generate only the raw XML diagram structure cleanly and close all tags."*
*   **Grid Reference:** Suggest specific grid sizes: *"Calculate positions assuming a 1000x800 pixel canvas. Give EDGE-FW-01 coordinates of X=440, Y=50. Place ALBs on Y=200, spaced 200px apart."*
*   **Peekable Solution:** If you get stuck, you can inspect the reference files under the [solutions/topology.drawio](solutions/topology.drawio) directory!

---

## Quality Comparison Matrix

The table below illustrates the varying success rates and design suitability of the primary visual formats you will encounter when generating network graphics with AI:

| Diagram Format | visual quality | setup complexity | LLM success rate | primary use case | common failure points |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Mermaid** | High (auto-layout) | Zero (markdown) | **95% (Excellent)** | In-line markdown docs | Line-crossing tangles on complex meshes |
| **Draw.io XML** | Low (overlapping) | Medium (importing) | **20% (Very Poor)** | High-fidelity vectors | Shape stacking, coordinate drift, broken tags |
| **Python diagrams** | High (custom PNG) | High (requires CLI) | **75% (Good)** | Programmatic automation | Library import deprecation, Graphviz path errors |
| **ASCII Art** | Medium (retro) | Zero (code block) | **80% (Good)** | Source-code headers | Asymmetric box edges, broken diagonal links |

---

## Lab Retrospective

Take a moment to reflect on this lab session:
* **What went OK?**
* **What could be improved?**
* **Was the AI helpful?**
* **What prompting techniques proved most effective?**
