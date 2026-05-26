# Phase 1: Environment Setup & Verification

## 🌟 Introduction
**What this phase brings:** Peace of mind that your local VS Code environment is fully configured and ready for the intensive AI workloads ahead.
**Why we are doing this:** Nothing is more frustrating than starting a complex lab only to realize your chat window is disconnected or your CLI tools aren't installed.
**What you will practice:** Basic environmental validation and a simple "Hello Copilot" test.

---

## Objective
Verify that GitHub Copilot Chat is active and that the OpenSpec CLI is installed and responsive.

## Task 1: Environment and Access Control Setup
Complete these steps to establish connectivity and prepare your workspace:
*   **Access Activation:** Ensure the `Role-VSCode-AI-Explorer` role is requested and approved in SailPoint IdentityNow.
*   **VS Code Installation:** Verify your local install or download from the [macOS Setup Guide](https://code.visualstudio.com/docs/setup/mac) or [Windows Setup Guide](https://code.visualstudio.com/docs/setup/windows).
*   **Copilot Extension:** Install the **GitHub Copilot Chat** extension from the VS Code Marketplace ([Copilot Online Docs](https://docs.github.com/en/copilot)).
*   **OpenSpec CLI Installation:**
    *   **macOS:** `brew install openspec`
    *   **Windows:** `npm install -g openspec`
    *   *Universal Fallback (On-Demand):* `npx openspec init .` ([OpenSpec Documentation](https://github.com/Fission-AI/OpenSpec)).

## Task 2: "Hello Copilot"
1. Open the **GitHub Copilot Chat** window in VS Code (usually on the left sidebar, or press `Cmd+Shift+I` on Mac / `Ctrl+Shift+I` on Windows).
2. Type the following prompt:
   > *"Explain the difference between a MAC address and an IP address in one short paragraph."*
3. Verify that Copilot responds. If it is grayed out or asks you to sign in, please complete the sign-in process now using your corporate GitHub credentials.

## Task 3: Verify OpenSpec
1. Open a new Terminal in VS Code (`Terminal -> New Terminal`).
2. Run the following command:
   ```bash
   openspec --version
   ```
3. You should see a version number printed out (e.g., `1.0.0` or similar).
   *If you see "command not found", refer to the installation steps in Task 1.*

## Task 4: Workspace Readiness
1. Ensure your VS Code workspace is open to the root of this repository. You should see the `labs/` and `.agent/` folders in your Explorer view.

---

## Lab Retrospective

Take a moment to reflect on this lab session:
* **What went OK?**
* **What could be improved?**
* **Was the AI helpful?**
* **What prompting techniques proved most effective?**
