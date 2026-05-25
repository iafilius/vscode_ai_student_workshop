# Lab C: Writing a SKILL from Scratch

Now it's time to codify your own domain knowledge. As a Network Engineer, you know that Cisco routing tables are notoriously hard for standard LLMs to parse reliably without hallucinating next-hop IP addresses. 

Let's write a SKILL that strictly tells the AI how to parse these routing logs.

## Task 1: Write the Parsing Rules
You can author a skill manually, or you can use your AI to write it for you. Choose the option you prefer!

### Option A: The Manual Way
1. Open the `SKILL.md` file in this directory. We have provided a basic skeleton.
2. Fill in the **Instructions** section. Give the AI strict rules on how to map the Cisco routing protocol codes to human-readable names:
   - `C` -> `Connected`
   - `O` -> `OSPF`
   - `D` -> `EIGRP`
3. Tell the AI exactly what JSON keys to output (e.g., `protocol`, `prefix`, `metric`, `next_hop`, `interface`).

### Option B: The AI-Assisted Way
1. Open the `SKILL.md` file in this directory so you can watch it update.
2. Open your AI Copilot chat and ask it to write the rules for you:
   > "Please update the `SKILL.md` file in the `lab_c_text_skill` folder. Add rules instructing the AI to parse Cisco routing tables. Map the protocol codes: 'C' to 'Connected', 'O' to 'OSPF', and 'D' to 'EIGRP'. Ensure the output is strictly a JSON array with the keys: `protocol`, `prefix`, `metric`, `next_hop`, and `interface`."
3. Watch the AI write the markdown rules for you! Save the file when it is done.

## Task 2: Test Your SKILL
1. Open your AI Copilot chat.
2. Ask it to apply your new skill to the file we prepared for you:
   > "Use the cisco route parser skill to parse the routing table contained in `routing_table.txt`."
3. Verify that the JSON output perfectly matches the keys and mappings you defined in your `SKILL.md`.

## The "Aha!" Moment
You have successfully taken a complex piece of network engineering logic and modularized it into a repeatable AI capability! 

However, running a text skill via prompt is still slow and costs thousands of tokens per execution. In **Lab D**, we are going to graduate this logic into a lightning-fast Python script.
