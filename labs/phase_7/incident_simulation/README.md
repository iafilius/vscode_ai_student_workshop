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

### Task 2: Correlate Logs to Diagnose the Flap
1. Open the [outage_syslog.log](outage_syslog.log) and [bgp_state.txt](bgp_state.txt) files.
2. Select the contents of both files, open Copilot Chat, and submit the following correlation prompt:
   > *"Correlate the syslog lines in outage_syslog.log and the BGP session metrics in bgp_state.txt. 1. Identify which peer is flapping. 2. Identify the exact physical interface causing the BGP flaps. 3. Deduce the exact root cause of the drops (Hint: Look at interface configurations and MTU parameters)."*

### Task 3: Draft the CLI Remediation Commands
1. Ask the AI to write the exact Cisco CLI commands to repair the mismatch and prevent further BGP flaps on the Core Switch:
   > *"Based on your diagnostic, generate the exact Cisco IOS configuration command sequence to configure the flapping interface to allow Jumbo Frames (MTU 9216) matching the other active trunks."*
2. Save these commands in a new file named `remediation.cfg` in this lab directory.

### Task 4: Validate Your Solution
1. Run the local self-checking validation tool:
   ```bash
   python verify.py
   ```
2. Verify that your configuration passes the diagnostic checks!

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
