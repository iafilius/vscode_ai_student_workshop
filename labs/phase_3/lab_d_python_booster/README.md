# Lab D: The Python Booster (Caching)

In Lab C, you built a text-based SKILL. While text-based skills are incredibly flexible for mapping contexts, relying on the LLM to execute them line-by-line is **slow** and **expensive**. It consumes thousands of tokens per run.

**The Networking Reality:** Imagine asking an AI to parse a raw BGP feed with 10,000 routes. Reading that line-by-line would take hours and cost a fortune! 

To solve this, we graduate mature SKILLs into standalone, lightning-fast scripts.

## Task 1: Write the Python Booster
1. Open `booster.py` in this folder.
2. Complete the Python script to parse the Cisco routing table text. **Pro Tip**: Do not write the complex regex yourself! Ask your AI Copilot to *"Complete the parse_routing_table function in booster.py to parse Cisco routing tables using regex."*
3. Import `functools` and apply the `@lru_cache` decorator to your parsing function. This introduces **memoization**: if the agent asks the script to parse the exact same routing table twice, the script instantly returns the cached result without recalculating!

## Task 2: The Agent Hand-off (Updating the SKILL)
This is where the magic happens. We aren't just going to run the script ourselves; we are going to upgrade the AI's brain so *it* knows how to run the script.

1. Open the `SKILL.md` file in this directory. 
2. Notice the new instructions: Instead of telling the AI *how* to parse the text, we are telling the AI to **delegate** the work to `booster.py`.
3. Open your AI Copilot chat and trigger the skill:
   > "Use the high-speed route parser skill to parse the routing table contained in `routing_table.txt`."
4. Watch as the AI realizes it doesn't need to reason through the text itself—it autonomously executes your local Python script (passing the text file as input) and returns the cached result!

## Task 3: Validate Your Booster
1. Run the local self-checking validation tool in your terminal:
   ```bash
   python3 verify.py
   ```
2. Ensure you achieve the **Cache Commander** rank!

> **Stuck?** If `verify.py` says you failed, don't bang your head against the wall! Just copy the exact error output and tell your AI Copilot: *"My verify.py script failed with this output, how do I fix booster.py?"*

---

## Pro-Tip

**The Goldfish Memory:** To temper expectations, remember that the AI is stateless across sessions—it has a "Goldfish Memory." By moving deterministic logic *out* of the AI prompt and *into* traditional code (using the AI merely to generate the script, as you did here), you make operations exponentially faster, 100% predictable, and vastly cheaper.

---

## Expected Output

When your script runs successfully, it should output these metrics to prove the value of caching:

```text
=== SKILL GRADUATION METRICS ===
AI Token-Based Parser: 4.8 seconds (Cost: ~3000 tokens)
Python-Cached Skill:   0.002 seconds (Cost: 0 tokens!)
================================
Status: Graduated successfully. Repeatability: 100% stable.
```
