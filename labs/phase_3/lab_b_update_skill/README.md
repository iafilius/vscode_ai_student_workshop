# Lab B: Updating an Agent SKILL
> **Context:** Now that you know how to invoke a SKILL, let's learn how to modify its behavior on the fly without retraining.

In Lab A, you triggered a SKILL and watched the AI follow its strict instructions. But what if the instructions aren't exactly what you need? What if your manager wants the output formatted differently?

One of the greatest strengths of SKILLs is that they are **hot-swappable**. You don't need to retrain a model or restart a server to change how your AI behaves. You just edit the text file!

## Task 1: Modify the Skill Rules
1. Open the `SKILL.md` file in this directory (it's a copy of the Jargon Translator from Lab A).
2. Let's change the behavior. Modify the **Translation Rules** section:
   - Add a new rule: `4. **The Action Item**: Provide one clear next step the business should take regarding this concept.`
3. Modify the **Restrictions** section:
   - Add a new restriction: `- The entire response must be formatted as a Markdown Table.`
4. Save the file.

## Task 2: Trigger the Updated Skill
1. Go back to your AI chat.
2. Ask the exact same question you asked in Lab A:
   > "Use the Network Jargon Translator skill to explain what BGP Route Flapping is."
3. Watch the output! The AI should instantly adapt to your new rules, presenting the answer as a Markdown Table and including the new Action Item row.

## The "Aha!" Moment
You just fundamentally altered the AI's behavior by changing a few lines of text. This is how you iterate and improve Agent automation workflows. 

Next, let's create a SKILL entirely from scratch in **Lab C**.

---

## Lab Retrospective

Take a moment to reflect on this lab session:
* **What went OK?**
* **What could be improved?**
* **Was the AI helpful?**
* **What prompting techniques proved most effective?**
