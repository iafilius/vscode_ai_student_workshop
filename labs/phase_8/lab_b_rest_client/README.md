# Phase 8 Lab B: Automated REST Client Base App

## Objective
Apply the Spec-Driven Development flow to construct a lightweight, fully working Python REST API consumer application in under five minutes. You will target a public mock REST endpoint to query, filter, and post structured telemetry records, establishing a reusable baseline for API integrations.

## Online References
- [JSONPlaceholder Mock API Guide](https://jsonplaceholder.typicode.com/)
- [Python requests Library Quickstart Guide](https://requests.readthedocs.io/en/latest/)

---

## Step-by-Step Lab Tasks

### Task 1: Auto-Propose the API Client Context via AI
Instead of manually creating OpenSpec files, we will use the AI to generate the proposal and specifications.
1. Run the propose command in Copilot Chat:
   > *"/opsx-propose Create a rest-api-client change for a rest-api-integration capability. Modern NetOps rely heavily on REST APIs. The script MUST perform a GET request to the public JSONPlaceholder users endpoint (https://jsonplaceholder.typicode.com/users). The script MUST parse the response and filter user objects, extracting only those whose location city contains a specified keyword or whose company.name contains 'Group'. The script MUST perform a POST request to https://jsonplaceholder.typicode.com/posts transmitting a JSON-formatted configuration update payload with title 'Config-Sync-Status'. The script MUST output the resulting HTTP status code (expected 201 Created) and the returned server response payload. The script MUST include robust exception handling to capture HTTP status errors, connection timeouts, and DNS failures."*
2. Wait for the AI to auto-generate the `proposal.md`, `design.md`, `tasks.md`, and `spec.md` artifacts.

### Task 2: Review and Refine Specifications
1. Open the specification file: `openspec/changes/rest-api-client/specs/rest-api-integration/spec.md`.
2. Review the generated requirements for the REST API client. Ensure the AI used strict normative language (`MUST` or `SHALL`) and exactly 4 hashtags (`#### Scenario:`) for scenarios. Adjust the requirements manually if necessary (e.g. adding the specific JSON payload string for the POST request if the AI missed it).
3. Validate and apply the change:
   ```bash
   openspec status --change "rest-api-client"
   ```

### Task 3: Generate the Client Application
1. Run the `/opsx-apply` command to prompt the agent to compile the Python utility `api_client.py` inside this lab directory:
   ```bash
   /opsx-apply "rest-api-client"
   ```
2. Inspect the generated script `api_client.py`.
3. Install the required requests library and run the script:
   ```bash
   pip install requests
   python api_client.py
   ```
4. **Audit the output:** Did the script successfully connect, retrieve the user list, filter them correctly, and post the sync status payload with a `201` status code? Notice how quickly a spec-driven requirement can be compiled into a working base integration client!

---

## Hints
*   **Requests vs. Urllib:** The `requests` library is the most popular HTTP library for Python, but it requires local installation (`pip install requests`). If you want zero external dependencies, ask the AI to generate the script using Python's standard built-in `urllib.request` and `urllib.error` libraries!
*   **Timeout Guard:** Always specify a reasonable connection timeout parameter (e.g. `timeout=5` seconds) to prevent scripts from hanging indefinitely.

---

## Expected Output

### Expected Python API Client Script (`api_client.py`):
```python
import json
import urllib.request
import urllib.error

def fetch_and_filter_users():
    url = "https://jsonplaceholder.typicode.com/users"
    print(f"--> Performing GET request to {url}")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "NetOps-Client/1.0"})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            print(f"✓ Retrieved {len(data)} device records.")
            
            # Filter users whose company name contains 'Group'
            filtered = [u for u in data if "Group" in u.get("company", {}).get("name", "")]
            print(f"\n=== Filtered Devices (Company contains 'Group') ===")
            for u in filtered:
                print(f"- ID: {u['id']} | Name: {u['name']} | Company: {u['company']['name']} | City: {u['address']['city']}")
            
    except urllib.error.URLError as e:
        print(f"✗ GET request failed: {e}")

def post_telemetry_status():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Config-Sync-Status",
        "body": "BGP Session restored on AMS-CORE-01. Port Eth1/1 brought up.",
        "userId": 1
    }
    print(f"\n--> Performing POST request to {url}")
    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url, 
            data=data, 
            headers={"Content-Type": "application/json", "User-Agent": "NetOps-Client/1.0"}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            res_code = response.getcode()
            res_payload = json.loads(response.read().decode())
            print(f"✓ POST succeeded with HTTP Status Code: {res_code} (Created)")
            print(f"=== Server Response ===")
            print(json.dumps(res_payload, indent=2))
            
    except urllib.error.URLError as e:
        print(f"✗ POST request failed: {e}")

if __name__ == "__main__":
    fetch_and_filter_users()
    post_telemetry_status()
```
