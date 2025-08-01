```markdown
# 🧪 Lab 19: A Simple Threat Intelligence Tool with Python

### Date: 2025-07-25
### Mentor: *The Da Vinci Cypher*
### Protocol Tier: Tier 1 — The Sentinel's Forge
### Module: Module 1.7 — Scripting for Automation

---

## 🎯 1. Objective
To write a basic but functional Python script that demonstrates core programming concepts (variables, lists, functions, conditional logic). The goal is to create a simple "threat checker" tool that can determine if a given IP address is present in a predefined blacklist.

## 🧰 2. Tools Used
| Tool/Language | Purpose |
|---------------|---------|
| `nano`        | A text editor used to write the Python script. |
| `chmod +x`    | A command to make the script file executable. |
| `Python 3`    | The high-level programming language used to build the tool. |

---

## 📜 3. Script: `threat_checker.py`

```python
#!/usr/bin/env python3

# 1. Define our "Threat Intelligence" - a list of known-bad IPs
IP_BLACKLIST = ["104.18.32.12", "45.33.32.11", "198.51.100.10"]

# 2. Define a function to perform the check
def check_ip(ip_address):
    """Checks if a given IP is in our blacklist."""
    print(f"[*] Checking IP address: {ip_address}")

    if ip_address in IP_BLACKLIST:
        print(f"[!] ALERT: IP address {ip_address} is ON the blacklist!")
    else:
        print(f"[*] OK: IP address {ip_address} is not on the blacklist.")

# 3. This is the main part of our script that runs
print("--- Simple Threat Intelligence Tool ---")
ip_to_check = "45.33.32.11"
check_ip(ip_to_check)

print("-" * 20)

ip_to_check_2 = "8.8.8.8"
check_ip(ip_to_check_2)
```

---

## 🔎 4. Execution & Analysis

* **Execution Command:** `./threat_checker.py`
* **Output:**

    ```plaintext
    --- Simple Threat Intelligence Tool ---
    [*] Checking IP address: 45.33.32.11
    [!] ALERT: IP address 45.33.32.11 is ON the blacklist!
    --------------------
    [*] Checking IP address: 8.8.8.8
    [*] OK: IP address 8.8.8.8 is not on the blacklist.
    ```

* **Analysis:** The script performed exactly as designed. The `check_ip` function successfully used an `if/else` statement to compare the input IPs against the `IP_BLACKLIST`. It correctly identified `45.33.32.11` as malicious and `8.8.8.8` as benign, demonstrating the power of conditional logic.

---

## ✅ 5. Conclusion

This lab served as a powerful introduction to the potential of Python for building custom security tools. By implementing variables, lists, functions, and conditional logic, we created a simple but effective automated threat intelligence checker. This exercise demonstrates that the core of many complex security products is the same logic we have written here: defining what is "bad" and writing a program to automatically check for it. This is the foundation of detection engineering and security automation.

```
