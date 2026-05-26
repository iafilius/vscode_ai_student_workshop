# Phase 7: The AI-Driven Incident Simulation (Game Day!)

## Objective
Put your newly acquired AI prompting, Agent SKILLs, and Knowledge Items context into action to solve a live simulated datacenter outage under a tight timeframe!

## Online Reference
- [Cisco BGP Peering Troubleshooting Guide](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/215652-troubleshoot-bgp-session-flapping.html)
- [Dell SONiC Jumbo Frames Configuration Guide](https://www.dell.com/support/manuals/en-us/enterprise-sonic-distribution-by-dell-technologies/sonic-cli-config-guide-pub/jumbo-frames-configuration?guid=guid-3315a6b0-77a8-4c22-9f33-ef7218ea0281)

## Boilerplate Files
- [outage_syslog.log](outage_syslog.log) (Live syslog flapping event log)
- [bgp_state.txt](bgp_state.txt) (Router state output printout)

---

## The Situation (Game Day Scenario!)
At 13:58:12, our Primary Datacenter Core Switch (`ams-core-switch-01`) started reporting BGP routing session drops with its neighbor `10.250.12.2` (`ams-leaf-02`). The peer session comes UP briefly but drops again within 60 seconds (flapping). 

A customer ticket has been escalated reporting massive packet drops on transactions to Datacenter 2. The operations team is panicking!

---

## Step-by-Step Lab Tasks

### Task 1: Load Your Custom SKILL
1. Open your chat assistant and make sure it has the context of the Cisco route parser SKILL you created in Phase 3 (`labs/phase_3/skills_automation/basic_text_skill/SKILL.md`).

### Task 2: Filter the Noise
The provided `outage_syslog.log` is a massive 500+ line log file full of operational noise (SSH failures, topology changes, etc.) typical of a real enterprise network. 
1. Open the [outage_syslog.log](outage_syslog.log), [bgp_state.txt](bgp_state.txt), and [interface_state.txt](interface_state.txt) files.
2. Select all three files and ask Copilot to summarize the anomalies. 
   *(Notice how the AI might get distracted by the SSH login failures or spanning-tree changes!)*
3. **Iterative Prompting:** Refine your prompt to instruct the AI to filter out security and environmental logs, and strictly focus on Layer 2 and Layer 3 routing protocol state changes. Ask it to identify which specific physical interface and BGP peer is flapping.

### Task 3: Deduce the Root Cause and Remediate
1. Now that the AI has isolated the flapping interface, ask it to look at the interface configurations in `interface_state.txt` to deduce *why* the packets are dropping. (Do not give it the answer!)
2. Once the AI correctly identifies the configuration mismatch, ask it to generate the exact Cisco IOS CLI commands to fix the issue on the core switch.
3. Save these commands in a new file named `remediation.cfg` in this lab directory.

### Task 4: Validate Your Solution
1. Run the local self-checking validation tool:
   ```bash
   python verify.py
   ```
2. Verify that your configuration passes the diagnostic checks!

### Task 5: Extract a Repeatable Diagnostic SKILL and KI
1. Now that you have the exact prompt sequence to isolate BGP flap logs, create a new SKILL file (e.g., `parse_bgp_flap/SKILL.md`) that codifies these instructions.
2. Inside your SKILL, instruct the AI to use **prompt caching** (e.g., using `[CACHE]` directives or explicit system instructions) so that future 500-line log ingestions are lightning fast.
3. Next, create a Knowledge Item (KI) in `knowledge/mtu_standards/artifacts/standard.md`. In this file, explicitly define the domain knowledge that "Jumbo MTU for Trunks = 9216".
4. By doing this, you ensure the AI "remembers" the MTU standard and has a high-speed parsing tool ready for the next incident!
5. **Pro-Tip**: Consider this the foundation of your own autonomous troubleshooting collection! While AI helped you create these assets, once they are codified and cached, they can potentially be executed standalone (e.g. by local, offline agents) independently of expensive online AI services.
6. **Pro-Tip**: SKILLs and Knowledge Items are just text files in standard formats, meaning they can easily be shared! If you build a great diagnostic workflow, you can commit it to version control and share it across your entire team or organization.

---

## Hints
* Compare the MTU config of interface `GigabitEthernet1/0/12` (which is `1500`) against the other interfaces (`1/0/11` and `1/0/13`) which are configured with MTU `9216`. 
* When BGP peers have an MTU mismatch, small Keepalive packets succeed (bringing the peer UP), but large updates containing full routing tables fail to pass (triggering a timeout and bringing the peer DOWN again).
* **Peekable Solution:** If you get stuck during Game Day, you can inspect the reference files under the `solutions/` folder.

---

## Expected Output

### Expected AI Diagnostic Analysis:
```text
=== INCIDENT DIAGNOSTIC REPORT ===
1. Flapping Neighbor: 10.250.12.2 (ams-leaf-02)
2. Affected Interface: GigabitEthernet1/0/12 on ams-core-switch-01
3. Root Cause: MTU size mismatch. The core switch interface is set to standard MTU 1500, while the leaf peer ams-leaf-02 is set to Jumbo MTU 9216. Small keepalives pass, but large BGP updates exceed 1500 bytes and get dropped, timing out the session.
==================================
```

### Expected Cisco IOS Remediation:
```text
ams-core-switch-01# configure terminal
ams-core-switch-01(config)# interface GigabitEthernet1/0/12
ams-core-switch-01(config-if)# mtu 9216
ams-core-switch-01(config-if)# end
ams-core-switch-01# copy running-config startup-config
```
