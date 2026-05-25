---
name: cisco-route-parser-fast
description: A high-speed parser for Cisco routing tables.
---

# High-Speed Route Parser

Use this skill whenever you are asked to parse a Cisco routing table into JSON.

## Instructions
Instead of parsing the routing table text manually (which is slow and token-heavy), you MUST delegate the work to our local caching script.

1. Take the raw routing table text provided by the user.
2. Execute the `booster.py` script located in this directory. 
3. (Hint to AI: You can pipe the text into the script or write it to a temp file and pass it as an argument).
4. Return the exact JSON output produced by `booster.py`. Do not alter the JSON.
