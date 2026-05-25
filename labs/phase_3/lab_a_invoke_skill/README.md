# Lab A: Invoking an Agent SKILL

Welcome to Phase 3! In Phase 2, we learned how to instruct an AI using conversational prompting. But what if you have a complex set of instructions you want the AI to follow consistently, every single time, without re-typing it? 

That's where **Agent SKILLs** come in. A SKILL is a pre-packaged set of rules and logic that you can give to an AI agent to permanently extend its capabilities.

Think of a SKILL as a **Persistent Standard Operating Procedure (SOP)** for your AI. Instead of teaching the AI how to do its job every time you talk to it, you write the SOP once, and the AI follows it flawlessly forever.

## The Goal
In this lab, we have provided a pre-written SKILL for you. Your goal is simply to trigger it and watch the magic happen.

## Task 1: Meet the Jargon Translator
1. Open the file `SKILL.md` in this directory.
2. Notice the structure: It has a name, a description, and strict rules for translating complex Network Engineering terminology into simple, non-technical explanations suitable for a business executive.

## Task 2: Trigger the Skill
1. Open your AI Copilot/Agent chat.
2. We want the AI to explain the concept of **"BGP Route Flapping"**, but we want it to strictly follow the rules in our skill. 
3. Send this prompt to your AI:
   > "Use the Network Jargon Translator skill to explain what BGP Route Flapping is."
4. Watch the output! Notice how the AI adopts the strict formatting, tone, and analogy requirements defined in the SKILL file, rather than just giving its standard Wikipedia-style answer.

## The "Aha!" Moment
You just extended the AI's brain. By storing instructions in a SKILL file, you guarantee the AI will act exactly how you want it to, every single time, across your entire team.

## Note on Invocation: Natural Language vs. Slash Commands (`/`)
You might be wondering: *"Could I just invoke this with a slash command, like `/jargon`?"*
- **Slash Commands** (like `/goal` or `/opsx-explore`) are usually hardcoded at the system level for specific, rigid workflows. 
- **Agent SKILLs** are designed to be much more fluid. By using natural language, the AI can seamlessly combine the skill with conversational context. You don't have to remember a specific `/` syntax; you just speak to the agent normally and it dynamically retrieves the right skill based on the `name` and `description` in the `SKILL.md` file!

## Where do SKILLs actually live?
In this lab, we placed the `SKILL.md` file right here in the lab folder so you could easily read it. However, in a real-world VS Code project, your AI agent automatically scans a specific hidden folder at the root of your workspace to find all your team's skills:
- **Project-Level Skills:** You should place them inside `.agent/skills/<skill-name>/SKILL.md`
Once you place a skill folder in that `.agent/` directory, your AI will automatically discover it and it becomes permanently available anytime you are working in that repository!

Next, let's learn how to update a SKILL on the fly in **Lab B**.
