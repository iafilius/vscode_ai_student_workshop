#!/usr/bin/env python3
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
