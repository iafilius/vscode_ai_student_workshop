# Phase 4 Lab C: Multi-Domain Knowledge Correlation

## Objective
Scale your use of Native Knowledge Items (KIs). Prove that an AI Agent can cross-reference multiple disparate documentation domains (e.g., Firewall rules, BGP configurations, and IPAM tables) simultaneously to troubleshoot complex network issues without requiring massive prompt engineering.

---

## Step-by-Step Lab Tasks

### Task 1: Load the Extended Knowledge Base
1. We have provided two pre-packaged KIs in the `mock_kis/` folder:
   * **Firewall Policy KI**: Documents egress rules.
   * **BGP Peering KI**: Documents external transit peers.
2. Copy these two folders into your IDE's native knowledge directory, alongside the IPAM KI you created in Lab B:
   * **Target location:** `<WORKSPACE_DIR>/knowledge/` (or your local IDE-configured workspace directory).

### Task 2: The Multi-Domain Correlation Query
1. Start a **clean, new chat session** in your AI Copilot to ensure the memory buffer is completely empty.
2. Ask the agent the following complex troubleshooting question:
   > *"@workspace Based on the registered Knowledge Items, if Spine-01 from Datacenter 1 tries to establish a BGP session with the Primary External Peer, will the firewall permit it? Show your work by cross-referencing the IPAM, BGP, and Firewall KIs."*
3. **Observe the magic:** The agent does not have any of these documents in the active chat. It will dynamically search the local Knowledge Base, read the IPAM table to find Spine-01's IP (`10.250.0.1`), read the BGP KI to find the Primary Peer IP (`10.255.1.2`), and check the Firewall KI to see if a rule allows it (Rule: `FW-ALLOW-BGP`).

### Why is this powerful?
In traditional workflows, you would have to manually open an IPAM spreadsheet, log into a BGP router to find the neighbor IP, and then query a firewall management tool to check policies. By maintaining KIs, the AI performs this cross-domain correlation in seconds.

---

## Expected Output
```text
User: Based on the registered Knowledge Items, if Spine-01 from Datacenter 1 tries to establish a BGP session with the Primary External Peer, will the firewall permit it?

Agent: Yes, the firewall will permit the BGP session. Here is the correlation across your Knowledge Items:
1. **IPAM (Datacenter 1 Fabric):** Spine-01's IP is 10.250.0.1.
2. **BGP (External Peering Architecture):** The Primary Peer IP is 10.255.1.2.
3. **Firewall (Perimeter Egress Policies):** Rule `FW-ALLOW-BGP` explicitly PERMITS TCP port 179 traffic from Source IP 10.250.0.1 to Destination IP 10.255.1.2.
```
