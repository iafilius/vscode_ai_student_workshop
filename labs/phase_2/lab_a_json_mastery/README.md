# Phase 2 Lab A: JSON Schema Mastery & Network Device Configuration

## Objective
Learn how to use AI prompting to take raw network device configuration text, convert it to a structured JSON file, then generate a valid JSON Schema draft-07 document enforcing enterprise parameters. Finish by picking an unfamiliar device type and creating its schema independently.

## Online Documentation Reference
- [JSON Schema Specification Draft-07](https://json-schema.org/specification-html/draft-07/json-schema-validation.html)
- [Cisco switchport Configuration CLI Reference](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3900/software/release/11-0/command/reference/interface.html)

## Boilerplate Input Files
| File | Device / Technology |
|------|---------------------|
| [cisco_raw_config.txt](cisco_raw_config.txt) | Cisco IOS switchport interface |
| [f5_raw_config.txt](f5_raw_config.txt) | F5 LTM virtual server + pool |
| [infoblox_ipam_raw.txt](infoblox_ipam_raw.txt) | Infoblox IPAM network & host records |
| [infoblox_dns_raw.txt](infoblox_dns_raw.txt) | Infoblox DNS zone export |
| [nsx_t_raw_config.txt](nsx_t_raw_config.txt) | VMware NSX-T logical switch + firewall |
| [aws_sg_raw_config.txt](aws_sg_raw_config.txt) | AWS Security Group |
| [aws_fw_raw_config.txt](aws_fw_raw_config.txt) | AWS Network Firewall |
| [azure_nsg_raw_config.txt](azure_nsg_raw_config.txt) | Azure Network Security Group |
| [azure_fw_raw_config.txt](azure_fw_raw_config.txt) | Azure Firewall |

## Output Files
- [cisco_schema.json](cisco_schema.json) — Your Cisco JSON Schema (Tasks 1–3 target)

---

## Step-by-Step Lab Tasks

### Task 1: Convert the Cisco Config to JSON

**✋ Classic approach — select & paste:**
1. Open [cisco_raw_config.txt](cisco_raw_config.txt) and **select all** the text (`Cmd+A`).
2. Open **VS Code Copilot Chat** (`Cmd+Shift+I` on macOS). Your selected text is automatically attached as context.
3. Submit the prompt:
   > *"Convert the highlighted raw Cisco interface configuration into a clean JSON structure. Do not use an external schema. Keep the structure flat and easy to read."*
4. Copy the generated JSON from the chat response.

**⚡ Alternative — drag the file into Copilot Chat:**
1. Open **VS Code Copilot Chat** (`Cmd+Shift+I`).
2. **Drag** [cisco_raw_config.txt](cisco_raw_config.txt) from the Explorer sidebar **directly into the chat input box** — the file icon will appear as an attachment.
3. Submit the same prompt above. Copilot reads the file content directly — no selecting or copying needed.
4. Ask Copilot to **write the JSON output directly to a file**:
   > *"Save the generated JSON configuration to a new file named `cisco_config.json` in the current lab directory."*

> 💡 **Tip:** Both approaches produce the same result. The drag approach is faster for large files — no more hunting for the right selection boundary!

---

### Task 2: Generate the Cisco JSON Schema
1. In the same Copilot Chat session, ask the AI to write a validation schema:
   > *"Based on the generated JSON configuration, generate a valid JSON Schema following draft-07 standards to validate this switch port layout."*

---

### Task 3: Enforce Custom Constraints
1. Enhance the JSON Schema to enforce standard enterprise bounds:
   * Require a boolean parameter `VlanTaggingEnabled`.
   * Add a numeric property `MtuRange` that must be an integer between `1500` and `9216` inclusive.
   > *"Modify the JSON Schema to enforce that: 1. A boolean property named 'VlanTaggingEnabled' is required. 2. An integer property named 'MtuRange' must exist and be strictly bounded between 1500 and 9216 inclusive."*
2. Save the final JSON schema to [cisco_schema.json](cisco_schema.json).

   > 💡 **Tip:** You can ask Copilot to write the file directly:
   > *"Save the final JSON Schema to `cisco_schema.json` in the current lab directory."*

---

### Task 4: Validate Your Cisco Schema
1. Run the local self-checking validation tool in your terminal:
   ```bash
   python verify.py
   ```
2. Verify that your schema successfully passes all checks!

---

### Task 5: Free-Form Challenge — Schema Your Own Device 🏆
Now do it on your own. Pick **one** of the remaining input files and generate its complete JSON + JSON Schema from scratch using only Copilot.

| Pick a file | Device type |
|-------------|-------------|
| [f5_raw_config.txt](f5_raw_config.txt) | F5 LTM load balancer |
| [infoblox_ipam_raw.txt](infoblox_ipam_raw.txt) | Infoblox IPAM |
| [infoblox_dns_raw.txt](infoblox_dns_raw.txt) | Infoblox DNS |
| [nsx_t_raw_config.txt](nsx_t_raw_config.txt) | VMware NSX-T SDN |
| [aws_sg_raw_config.txt](aws_sg_raw_config.txt) | AWS Security Group |
| [aws_fw_raw_config.txt](aws_fw_raw_config.txt) | AWS Network Firewall |
| [azure_nsg_raw_config.txt](azure_nsg_raw_config.txt) | Azure Network Security Group |
| [azure_fw_raw_config.txt](azure_fw_raw_config.txt) | Azure Firewall |

**Your goal:**
1. Drag the chosen file into Copilot Chat.
2. Prompt Copilot to convert it to a clean JSON structure.
3. Prompt Copilot to generate a draft-07 JSON Schema for the output.
4. Add at least **two custom constraints** of your own choice (required fields, enum values, numeric bounds — whatever makes sense for the device type).
5. Save the schema to a file named `<device>_schema.json` (e.g. `f5_schema.json`).

> 💡 **There's no verify.py for this task** — compare your schema against the raw config yourself, or ask a colleague to review it. Good schemas tell a story about what's valid and what isn't.

---

### Task 6: Guided Schema Evolution (Cisco)
Configurations evolve over time. Let's update our Cisco schema to support a new version of the configuration.
1. Drag both `cisco_raw_config.txt` (v1) and the new `cisco_raw_config_2.txt` (v2) into Copilot Chat.
2. Submit the prompt:
   > *"Analyze both v1 and v2 of this Cisco raw configuration. Generate an updated draft-07 JSON Schema that successfully accommodates all properties and structures found in both files. Save it to a new file named `cisco_schema_v2.json`."*

---

### Task 7: Free-Form Schema Evolution
Now, take the device you selected in Task 5 and evolve its schema to v2!
1. Drag both the v1 and v2 raw config files for your chosen device (e.g., `f5_raw_config.txt` and `f5_raw_config_2.txt`) into Copilot.
2. Instruct the AI to generate a unified `[device]_schema_v2.json`.

---

### Task 8: Schema Validation in Action (Cisco)
The true power of a JSON Schema is validating unstructured or user-provided data.
1. Drag the `cisco_unvalidated.json` file (which contains 3 subtle, planted errors) and your newly created `cisco_schema_v2.json` into Copilot Chat.
2. Submit the prompt:
   > *"Validate the unvalidated JSON file against the provided JSON Schema. Identify every validation failure. For each error, provide a detailed report naming the exact field path, the violation type, and the specific schema constraint that was breached."*

---

### Task 9: Free-Form Schema Validation
Now, repeat the validation exercise for the device you evolved in Task 7.
1. Drag your `[device]_unvalidated.json` and your `[device]_schema_v2.json` into Copilot Chat.
2. Ask for a validation report highlighting the exact errors.
3. *Check your work:* Cross-reference the errors Copilot found with the [solutions/error_keys.md](solutions/error_keys.md) file!

---

## Hints
* If the AI generates an empty MTU check in Task 3, remind it to use standard JSON Schema constraints: `"minimum": 1500, "maximum": 9216` inside the `properties` block.
* For the free-form task: richer raw files like NSX-T produce interesting schemas with nested objects and enums (`"ALLOW"`, `"DROP"`). Start there if you want a challenge.
* **Peekable Solution (Tasks 1–3 and 6–9):** Inspect the reference schemas and the `error_keys.md` file under the [solutions/](solutions/) folder.

---

## Expected Output (Tasks 1–3)

Your completed `cisco_schema.json` should pass all `verify.py` checks.

<details>
<summary>🔍 Peek at the solution (click to expand)</summary>

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "SwitchPortConfiguration",
  "type": "object",
  "properties": {
    "interface": { "type": "string" },
    "description": { "type": "string" },
    "mode": { "type": "string", "enum": ["access", "trunk"] },
    "allowed_vlans": {
      "type": "array",
      "items": { "type": "integer" }
    },
    "VlanTaggingEnabled": { "type": "boolean" },
    "MtuRange": {
      "type": "integer",
      "minimum": 1500,
      "maximum": 9216
    }
  },
  "required": ["interface", "mode", "VlanTaggingEnabled", "MtuRange"]
}
```

</details>

---

## Pro-Tip

**LLM Prompt Caching:** In enterprise environments, repeatedly sending large, complex JSON schemas or XML templates in every prompt gets expensive and slow. By utilizing **LLM Prompt Caching** (pinning the schema/template in the AI's memory cache), you can reduce token consumption by up to 90% and drop response latency to milliseconds when generating configurations at scale.

---

## Lab Retrospective

Take a moment to reflect on this lab session:
* **What went OK?**
* **What could be improved?**
* **Was the AI helpful?**
* **What prompting techniques proved most effective?**
