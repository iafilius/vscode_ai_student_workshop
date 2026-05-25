# AI Mastery Workshop: Enterprise Network Engineering & Automation

This workshop is a comprehensive, progressive, full-day training guide designed to empower Network Engineering colleagues to leverage AI tools (VS Code Copilot, Agent SKILLs, Knowledge Items, and Spec-Driven Development) to exponentially improve operational efficiency, repeatability, and security.

> [!NOTE]
> This session is structured to support all proficiency levels—from absolute beginners to expert network developers. The labs are self-supporting, providing online reference pointers, detailed hints, and expected outcome templates so you can learn at your own pace.

---

## 📅 Agenda (09:30 - 17:30)

| Time | Activity | Description |
| :--- | :--- | :--- |
| **09:30 - 10:15** | **🚀 Phase 1: Environment Setup & Prompting Basics** | Infrastructure configuration, IdentityNow access, and prompt engineering fundamentals. |
| **10:15 - 11:45** | **🧠 Phase 2: Practical Prompting Labs** | JSON schema, IPAM, DNS, Firewall, Mermaid Flowcharting, and Draw.io XML. |
| **11:45 - 12:45** | **☕ Phase 3: Agent SKILLs (Know-How Automation)** | Designing custom capabilities using markdown templates and Python-cached boosters. |
| **12:45 - 13:30** | **🍱 Lunch Break** | Intermission. |
| **13:30 - 14:30** | **🛡️ Phase 4: Knowledge Items (KIs) & Fact Retention** | Querying and storing localized repository facts to persist state across sessions. |
| **14:30 - 16:30** | **📐 Phase 5: Spec-Driven Development & OpenSpec** | Spec-driven code construction (Greenfield, Brownfield, Python Diagrams, and ASCII Graphics). |
| **16:30 - 17:00** | **🛡️ Phase 6: Operational Case Studies** | Event log parsing, PII sanitization, and multi-model strategic selection. |
| **17:00 - 17:30** | **🏆 Phase 7: The AI-Driven Incident Simulation (Game Day!)** | Diagnose and resolve a simulated network outage under time constraints. |
| **17:30 - 18:30** | **🔌 Phase 8: Advanced Integration & Security Automation** | Automated firewall rule generation using Policy-as-Code datasets, and Python REST API clients. |

---

## 🚀 Phase 1: Environment Setup & Prompting Basics (09:30 - 10:15)

### 1. Environment and Access Control Setup
Complete these steps to establish connectivity and prepare your workspace:
*   **Access Activation:** Ensure the `Role-VSCode-AI-Explorer` role is requested and approved in SailPoint IdentityNow.
*   **VS Code Installation:** Verify your local install or download from the [macOS Setup Guide](https://code.visualstudio.com/docs/setup/mac) or [Windows Setup Guide](https://code.visualstudio.com/docs/setup/windows).
*   **Copilot Extension:** Install the **GitHub Copilot Chat** extension from the VS Code Marketplace ([Copilot Online Docs](https://docs.github.com/en/copilot)).
*   **OpenSpec CLI Installation:**
    *   **macOS:** `brew install openspec`
    *   **Windows:** `npm install -g openspec`
    *   *Universal Fallback (On-Demand):* `npx openspec init .` ([OpenSpec Documentation](https://github.com/Fission-AI/OpenSpec)).

### 2. Prompting 101 for NetOps Engineers
To achieve high-quality results from Copilot, use structured prompting techniques:
*   **System Prompts vs. User Prompts:** Always assign a clear persona and target boundaries (e.g. *"Act as a Senior Network Architect specializing in Dell SONiC configurations. You must restrict suggestions to enterprise-validated syntax."*).
*   **Prompt Constraints:** Explicitly tell the AI what to exclude (e.g., *"Do not include passwords, private IP ranges, or deprecated commands."*).
*   **Few-Shot Formatting:** Provide examples of the expected input and output.
    *   *Input Example:* `VLAN 10, Port Eth1/1 (Trunk)`
    *   *Output Example:*
        ```
        interface Ethernet1/1
          switchport mode trunk
          switchport trunk allowed vlan 10
        ```

---



## 🧠 Phase 2: Practical Prompting Labs (10:15 - 11:45)

### 🟢 Lab A: JSON Schema Mastery
**The Concept:** Converting unstructured, raw network configurations into strictly validated JSON schemas to programmatically enforce enterprise standards.
*   **Directory:** `labs/phase_2/lab_a_json_mastery/` ([Open README](./labs/phase_2/lab_a_json_mastery/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_2/lab_a_json_mastery/`

### 🟢 Lab B: Network Hot Potatoes
**The Concept:** Solving common, messy operational NetOps tasks (like parsing dirty DNS logs, migrating firewalls, and catching IPAM collisions) using targeted AI prompts.
*   **Directory:** `labs/phase_2/lab_b_netops_prompting/` ([Open README](./labs/phase_2/lab_b_netops_prompting/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_2/lab_b_netops_prompting/`

### 🟢 Lab C: Mermaid Flowcharting
**The Concept:** Generating dynamic, code-based logical network topology drawings (Spine-Leaf, Core-Dist-Access) using the Mermaid rendering language instead of manual Visio dragging.
*   **Directory:** `labs/phase_2/lab_c_mermaid/` ([Open README](./labs/phase_2/lab_c_mermaid/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_2/lab_c_mermaid/`

### 🟢 Lab D: Draw.io XML Prompting
**The Concept:** Instructing the AI to generate raw XML schema data compatible with Draw.io, introducing the complexity of programmatic coordinate alignment.
*   **Directory:** `labs/phase_2/lab_d_drawio/` ([Open README](./labs/phase_2/lab_d_drawio/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_2/lab_d_drawio/`

### 🟢 Lab E: Python Diagrams (diagrams package)
**The Concept:** Writing Python automation scripts that automatically calculate routing topography math and generate high-fidelity PNG architecture diagrams.
*   **Directory:** `labs/phase_2/lab_e_python_diagrams/` ([Open README](./labs/phase_2/lab_e_python_diagrams/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_2/lab_e_python_diagrams/`


---

## ☕ Phase 3: Agent SKILLs (Know-How Automation) (11:45 - 12:45)

Agent SKILLs let you package complex, repetitive AI instructions into modular, reusable capabilities. This phase answers the critical **"WHY"** behind Skills:
1. **Cost & Speed:** Execute locally for 0 tokens in milliseconds, rather than spending thousands of tokens waiting seconds for LLM inference.
2. **Determinism vs. Hallucination:** A Python regex script *never* hallucinates an IP address. It is 100% reliable.
3. **Local Fallback:** If the LLM provider goes offline, your compiled skills still run locally.

### 🟢 Lab A: Invoking a SKILL (The "Aha" Moment)
**The Concept:** Understanding how SKILLs fundamentally extend the AI's capabilities by triggering a pre-written "Network Jargon Translator" skill.
*   **Directory:** `labs/phase_3/lab_a_invoke_skill/` ([Open README](./labs/phase_3/lab_a_invoke_skill/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_3/lab_a_invoke_skill/`

### 🟢 Lab B: Updating a SKILL (Hot-Swapping)
**The Concept:** Modifying the rules of an existing skill to change the AI's behavior in real-time without retraining or restarting.
*   **Directory:** `labs/phase_3/lab_b_update_skill/` ([Open README](./labs/phase_3/lab_b_update_skill/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_3/lab_b_update_skill/`

### 🟢 Lab C: Writing a SKILL from Scratch
**The Concept:** Writing a custom text-based skill to parse notorious Cisco routing logs.
*   **Directory:** `labs/phase_3/lab_c_text_skill/` ([Open README](./labs/phase_3/lab_c_text_skill/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_3/lab_c_text_skill/`

### 🟢 Lab D: Graduate to a Python-Cached SKILL (Booster)
**The Concept:** Solving the token/speed bottleneck of text-based skills by graduating mature logic into a cached Python script, then instructing the AI to execute it autonomously.
*   **Directory:** `labs/phase_3/lab_d_python_booster/` ([Open README](./labs/phase_3/lab_d_python_booster/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_3/lab_d_python_booster/`

---

## 🛡️ Phase 4: Native Knowledge Items & Fact Retention (13:30 - 14:30)

Native IDE Knowledge Items allow your AI assistant to persist architectural definitions, configurations, and network facts between separate, isolated conversation sessions.

### 🟢 Lab A: The "Goldfish" Memory (Statelessness)
**The Concept:** Standard AI chatbots suffer from "amnesia"—they forget everything the moment you clear the chat. In this lab, we will intentionally break the AI by feeding it a complex IPAM table and watching it lose context.
*   **Directory:** `labs/phase_4/lab_a_statelessness/` ([Open README](./labs/phase_4/lab_a_statelessness/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_4/lab_a_statelessness/`

### 🟢 Lab B: Native IDE Knowledge Items
**The Concept:** Fixing the amnesia from Lab A by natively persisting the IPAM table as a Knowledge Item.
*   **Directory:** `labs/phase_4/lab_b_native_ki/` ([Open README](./labs/phase_4/lab_b_native_ki/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_4/lab_b_native_ki/`

### 🟢 Lab C: Multi-Domain Knowledge Correlation
**The Concept:** Proving that the AI can dynamically search and correlate across multiple disconnected Knowledge Items simultaneously to answer complex architectural questions.
*   **Directory:** `labs/phase_4/lab_c_correlation/` ([Open README](./labs/phase_4/lab_c_correlation/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_4/lab_c_correlation/`

---

## 📐 Phase 5: Spec-Driven Development (SDD) & OpenSpec (14:30 - 16:30)

Spec-Driven Development ensures your codebase remains strictly aligned with documented business and technical requirements. OpenSpec automates the proposal, design, verification, and checklist cycle.

### 🟢 Lab A: Greenfield Development (Internal Network Scanner)
**The Concept:** Designing and generating a brand-new internal network scanning utility using the strict OpenSpec workflow.
*   **Directory:** `labs/phase_5/lab_a_sdd_greenfield/` ([Open README](./labs/phase_5/lab_a_sdd_greenfield/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_5/lab_a_sdd_greenfield/`

### 🟢 Lab B: Brownfield Development (Refining Legacy Parsers)
**The Concept:** Taking a legacy, poorly-documented Python parsing utility, reverse-engineering its requirements into an OpenSpec specification, and enhancing it.
*   **Directory:** `labs/phase_5/lab_b_sdd_brownfield/` ([Open README](./labs/phase_5/lab_b_sdd_brownfield/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_5/lab_b_sdd_brownfield/`

### 🟢 Lab C: Spec-Driven Mermaid Flowcharting
**The Concept:** Using OpenSpec to repeat the Phase 2 simple topology, and then massively scaling it to a complex Multi-DC design to demonstrate the scalability of Spec-Driven Development.
*   **Directory:** `labs/phase_5/lab_c_sdd_mermaid/` ([Open README](./labs/phase_5/lab_c_sdd_mermaid/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_5/lab_c_sdd_mermaid/`

### 🟢 Lab D: Spec-Driven Draw.io XML
**The Concept:** Using OpenSpec to generate Draw.io XML programmatically, scaling from a simple block diagram to a large SD-WAN overlay representation.
*   **Directory:** `labs/phase_5/lab_d_sdd_drawio/` ([Open README](./labs/phase_5/lab_d_sdd_drawio/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_5/lab_d_sdd_drawio/`

### 🟢 Lab E: Spec-Driven Python Diagrams
**The Concept:** Using OpenSpec to design network architecture specifications, and running code-generation to write scalable Python scripts utilizing the `diagrams` library.
*   **Directory:** `labs/phase_5/lab_e_sdd_python_diagrams/` ([Open README](./labs/phase_5/lab_e_sdd_python_diagrams/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_5/lab_e_sdd_python_diagrams/`


---

## 🛡️ Phase 6: Operational Case Studies & Advanced Topics (16:30 - 17:00)

### 1. Multi-Model Selection Strategy
Choose the appropriate AI reasoning model for your NetOps tasks:
*   **Flash Models (Copilot Quick):** Highly optimized for low-latency log formatting, regex parsing, and basic shell configurations.
*   **Reasoning Models (Copilot Deep Dive):** Required for complex multi-DC spine-leaf designs, legacy code auditing, and security compliance analyses.

### 🟢 Lab A: PII & IP Masking Compliance (AI Security Sanitizer)
**The Concept:** Before submitting configuration logs to external AI providers, you MUST sanitize the data. In this lab, we develop a Python configuration cleaner using the OpenSpec flow to ingest a high-risk Cisco switch configuration and automatically redact sensitive tokens.
*   **Directory:** `labs/phase_6/lab_a_pii_sanitization/` ([Open README](./labs/phase_6/lab_a_pii_sanitization/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_6/lab_a_pii_sanitization/`


---

## 🏆 Phase 7: The AI-Driven Incident Simulation (Game Day!) (17:00 - 17:30)

Test your newly acquired AI automation and prompting skills in a simulated high-stakes datacenter outage!

**The Concept:** Form troubleshooting teams to diagnose and resolve a BGP peering flapping issue caused by an interface MTU configuration mismatch, leveraging your Phase 3 routing parsers and log correlation prompts.
*   **Directory:** `labs/phase_7/incident_simulation/` ([Open README](./labs/phase_7/incident_simulation/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_7/incident_simulation/`


---

## 🔌 Phase 8: Advanced Integration & Security Automation (17:30 - 18:30)

In this final phase, learn how to build complex security orchestrators and rapid API client base applications, cementing your generative AI skills with deep programmatic integrations.

### 🟢 Lab A: Policy-as-Code & Automated Multi-Platform Firewall Generation
**The Concept:** Developing a Python multi-platform Firewall policy-as-code compiler that parses a complex enterprise hybrid multi-cloud routing topology JSON file and automatically generates valid JSON firewall rules for targeted zones.
*   **Directory:** `labs/phase_8/lab_a_firewall_generation/` ([Open README](./labs/phase_8/lab_a_firewall_generation/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_8/lab_a_firewall_generation/`

### 🟢 Lab B: Automated REST Client Base App
**The Concept:** Applying the Spec-Driven Development flow to construct a lightweight, fully working Python REST API consumer application querying free public internet mock endpoints in under five minutes.
*   **Directory:** `labs/phase_8/lab_b_rest_client/` ([Open README](./labs/phase_8/lab_b_rest_client/README.md))
    *   *Open as workspace (Mac & Windows):* `code labs/phase_8/lab_b_rest_client/`


---

## 📚 Appendix: The AI Survival Guide (Theory & Concepts)

A theoretical briefing on the core meta-skills of AI-assisted NetOps. This short reading covers the critical differences between Ask vs. Agent mode, how to handle inevitable AI errors ("The Power of the Retry"), and how Skills, Knowledge Items, and MCP servers fit together. Keep this open as a cheat sheet!
*   **Directory:** `labs/appendix_theory/` ([Open README](./labs/appendix_theory/README.md))
