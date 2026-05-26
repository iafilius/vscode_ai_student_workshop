# Phase 4 Lab A: The "Goldfish" Memory (AI Statelessness)

## 🌟 Introduction
**What this phase brings:** Long-term memory for your AI environment.
**Why we are doing this:** Resolving the "Goldfish Problem" requires the AI to have access to absolute facts (like an IPAM table or Datacenter topology) without you needing to paste them into the chat every time.
**What you will practice:**
- Registering local Knowledge Items natively in the IDE
- Cross-referencing KIs to solve network routing issues
- Persisting state across isolated chat sessions

---

## Objective
Experience the fundamental limitation of conversational AI: **Statelessness**. By default, an AI agent only remembers what is currently in its active conversation buffer. When you start a new session, its memory is completely wiped.

---

## Step-by-Step Lab Tasks

### Task 1: Provide Context
1. Open [ipam_table.txt](ipam_table.txt).
2. Use the IDE's chat window to feed this file to the AI (drag and drop the file, or use `@workspace`).
3. Ask the AI: 
   > *"Based on the IPAM table, what is the VM subnet for Leaf-02?"*
4. The AI will correctly answer `10.250.11.0/24`.

### Task 2: Trigger AI Amnesia
1. **Clear the conversation!** (Click the `+` icon or "New Chat" button in your AI Copilot window to start a fresh, empty session).
2. Ask the exact same question again:
   > *"What is the VM subnet for Leaf-02 in our Datacenter 1 layout?"*
3. Watch the AI fail, hallucinate, or ask you for the document. 

### Why did this happen?
The AI's memory is tied directly to the chat window's context window. Once the chat is cleared, the context is destroyed. 

In **Lab B**, we will fix this by persisting facts directly into the IDE's native Knowledge Base.
