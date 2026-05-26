# Phase 4 Lab B: Native IDE Knowledge Items (KIs)

## Objective
> **Context:** Now that we have experienced the AI's "amnesia", let's fix it by natively persisting the IPAM table as a Knowledge Item.

Understand the concept of Knowledge Items (KIs) and learn how to use them to persist key repository architecture decisions, configurations, and network facts across isolated conversation sessions.

## Online Documentation Reference
- IDE Knowledge Bases: Native Agent Context Directories
- RAG (Retrieval-Augmented Generation) Basics

---

## Step-by-Step Lab Tasks

### Task 1: Register a Local Knowledge Item (KI)
In Lab A, you saw the AI forget the IPAM table. We will fix this by persisting the table as a **Knowledge Item (KI)** natively in the workspace.
1. Navigate to the templates folder: `labs/phase_4/lab_b_native_ki/templates/`.
2. Review the metadata schema: [templates/metadata.json](templates/metadata.json). Fill in details representing the Datacenter topology (e.g. `Datacenter-1-Fabric`).
3. Review the fact file: [templates/artifact.md](templates/artifact.md). **Copy the contents of `ipam_table.txt` from Lab A into this markdown file.**
4. Save the files to your active environment's knowledge folder to register the KI:
   * **Target location:** `<WORKSPACE_DIR>/knowledge/datacenter_1_fabric/` (or your local IDE-configured workspace directory).

### Task 2: Verify Multi-Session Fact Retention
1. Close your current Copilot or AI chat window to clear the conversation buffer (simulating a session restart).
2. Start a brand new, clean chat session.
3. Submit the following query:
   > *"@workspace Based on the registered Knowledge Items, what is the VM subnet for Leaf-02?"*
4. Observe how the agent seamlessly reads your registered KI files from the local directory and accurately answers `10.250.11.0/24`—without you needing to upload the file!

### Task 3: Validate Your Knowledge Item
1. Run the local self-checking validation tool in your terminal:
   ```bash
   python verify.py
   ```
2. Confirm that your registered Knowledge Item successfully passes all validation checks in the system database!

---

## Hints
* *Task 1 Tip:* When filling in `metadata.json`, ensure standard JSON format is preserved (no trailing commas).
* *Task 2 Tip:* If the agent states it doesn't have access to KIs, remind it to inspect the local `<WORKSPACE_DIR>/knowledge/` directory.
* **Peekable Solution:** If you get stuck, you can inspect the completed metadata schema and fact details under the `solutions/` folder!

---

## Pro-Tip

**Global Version Control:** Version-controlling your `knowledge/` folder across your organization means a senior architect can codify a standard (like a complex network schema or security policy) once, and junior engineers globally will instantly inherit that domain expertise in their local IDEs via the shared repository.

---

## Expected Output

### Expected Metadata.json:
```json
{
  "title": "Datacenter 1 Spine-Leaf Network Fabric",
  "version": "1.0.0",
  "owner": "Enterprise Network Engineering",
  "references": [
    "artifact.md"
  ]
}
```

### Expected Fact Verification Session:
```text
User: Based on the registered Knowledge Items, what is the VM subnet for Leaf-02?

Agent: According to the 'Datacenter 1 Spine-Leaf Network Fabric' Knowledge Item in your workspace, the VM subnet for Leaf-02 is 10.250.11.0/24.
```

---

## Lab Retrospective

Take a moment to reflect on this lab session:
* **What went OK?**
* **What could be improved?**
* **Was the AI helpful?**
* **What prompting techniques proved most effective?**
