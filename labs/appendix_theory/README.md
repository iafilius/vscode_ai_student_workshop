# Appendix: The AI Survival Guide (Theory & Tools)

Welcome to the **AI Survival Guide**. Before we dive into parsing routing tables and generating Python scripts, it is absolutely critical to understand the theory of *how* these AI tools interact with your code, your network, and your mind.

If you don't understand the meta-skills—the rules of the game—you will get frustrated the first time the AI hallucinates a non-existent Cisco command or forgets what you told it five minutes ago.

Read through this theory section. Keep it open as a cheat sheet. 

---

## 1. The Modes of Engagement

Modern AI in VS Code operates in distinct "modes." Knowing which one to use is half the battle.

*   **Ask Mode (The Chatbot):** The standard chat window. It is reactive. It's great for quick questions ("What does this regex do?"), code explanations, and generating quick snippets. It does exactly what you ask and nothing more.
*   **Plan Mode (The Architect):** This is the core of Spec-Driven Development (OpenSpec). Instead of immediately spitting out code, the AI reads your workspace, thinks, and drafts a proposed course of action *before* executing. It asks for your approval. This is mandatory for complex network designs to prevent "spaghetti code."
*   **Agent Mode (The Operator):** The AI acts autonomously. It can run terminal commands (`ping`, `curl`, `pip install`), create files, and compile code. You are no longer writing code; you are managing an operator who is doing the work on your machine.

---

## 2. Models & Architecture Selection

Not all AI models are created equal. If a task fails, your first instinct should be to switch models, not to fix the code yourself.

*   **Fast Models (e.g., Claude 3.5 Haiku, GPT-4o-mini):** Optimized for low latency. Use these for simple log formatting, regex parsing, and basic shell configuration generation.
*   **Reasoning / Heavy Models (e.g., Claude 3.5 Sonnet, o1):** These models "think" before they speak. They are mandatory for complex multi-DC spine-leaf designs, legacy code auditing, and security compliance analyses.

---

## 3. The "Embrace the Error" Philosophy

**AI is non-deterministic.** Errors are not just common; they are guaranteed. How you handle them defines your success.

1.  **Do Not Fix It Yourself:** If the AI generates a Python script that throws a `SyntaxError`, or an Ansible playbook that fails linting, *do not manually fix it*.
2.  **The Power of the Retry:** Copy the error output (e.g., the Python traceback or the Ansible fatal error) and paste it directly back into the chat. Make the AI debug its own work.
3.  **Switch Sessions:** An AI's "context window" (its memory) can get polluted. If the AI starts going in circles, hallucinating, or getting confused, **open a fresh chat session**. It’s like turning it off and on again. 

---

## 4. The Integration Ecosystem (The Big Picture)

How do all these acronyms fit together?

*   **Skills (`SKILL.md`):** Think of these as "Standard Operating Procedures (SOPs)." They teach the AI *how* to do a specific task consistently (e.g., how your enterprise parses a specific F5 load balancer log).
*   **Knowledge Items (KIs):** "The Encyclopedia." You pass static data (IPAM tables, Topology Maps) to the AI so it doesn't hallucinate subnets.
*   **OpenSpec:** The "Project Manager." A framework that forces the AI to read the KIs and follow the Skills rigidly before writing code.
*   **MCP (Model Context Protocol):** The bridge. MCP Servers allow your local VS Code AI to securely connect to external tools (like GitHub, Jira, or a live Arista CloudVision API) to pull live data into the chat.

---

## 5. Graphic Generation Tooling

In Phase 5, we will generate network architecture drawings using AI. Why do we use three different tools?

*   **Mermaid Flowcharts:** Best for quick, inline markdown flowcharts. It's natively supported in GitHub and VS Code, but lacks complex spatial routing.
*   **Draw.io XML:** Best for generating complex block diagrams that a human engineer will need to manually open, click, drag, and tweak later in the Visio/Draw.io GUI.
*   **Python `diagrams` Library:** Best for massive, deterministic, programmatic architectures (e.g., a 100-node AWS multi-region deployment). The AI writes Python code; the Python code uses Graphviz to route the lines perfectly. 

---

## 6. System Storage Pathways for AI Agents

To effectively manage your AI workspaces, it is helpful to know where the agent stores its data and specifications:

*   **OpenSpec Data (`openspec/`):**
    *   `openspec/config.yaml`: Defines developer workflows, project scope, and per-artifact rules.
    *   `openspec/changes/<change-name>/`: Temporary directories housing active proposals, designs, specs, and checklists.
    *   `openspec/specs/<capability>/spec.md`: Permanent specs reflecting the master state of the codebase.

*   **Agent SKILLs (`.agent/skills/` & `~/.agent/skills/`):**
    *   **Workspace-Local Skills:** Stored in `.agent/skills/<skill-name>/` at the root of your project. These are specific to this codebase and should be committed to Git.
    *   **Global User Skills:** Stored in `~/.agent/skills/`. These are shared globally across all local projects for your user profile.
    *   **Global Plugins:** Stored in `~/.agent/plugins/`. These are bundles of specialized subagents, tools, and configurations.

*   **Knowledge Items (KIs):**
    *   **Workspace Knowledge Directory:** Stored in `knowledge/`. Contains workspace-specific KIs (like your topology diagrams or IPAM tables) tied to the current codebase.
    *   **Global Knowledge Directory:** Stored in `~/.agent/knowledge/`. Contains global KIs shared across all your projects.

---

> [!TIP]
> **Your Golden Rule for the Workshop:**
> If it feels like you are doing manual labor, you are doing it wrong. Stop typing, open a fresh chat session, provide better context (KIs), and tell the AI to do the work.
