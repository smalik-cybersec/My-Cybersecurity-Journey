# Module 12: Conditional Statements

## Lesson 06: Elif Statement Introduction

### 1. Purpose of the `elif` Statement
The `elif` (short for "else if") statement allows for handling multiple, mutually exclusive conditions. When you have more than two possible outcomes for a decision, an `if-elif-else` chain provides a structured way to check conditions sequentially and execute a specific code block corresponding to the first `True` condition encountered.

### 2. Syntax
The general syntax for an `if-elif-else` statement is:

```python
if condition1:
    # Code block 1 (executed if condition1 is True)
elif condition2:
    # Code block 2 (executed if condition1 is False AND condition2 is True)
elif condition3:
    # Code block 3 (executed if condition1 and condition2 are False AND condition3 is True)
# ... (you can have multiple elif blocks)
else:
    # Code block 4 (executed if all preceding conditions are False)


    alert_score = 85 # Test with 95, 70, 45, 20

if alert_score >= 90:
    print("Threat Level: CRITICAL - Immediate investigation!")
elif alert_score >= 70:
    print("Threat Level: HIGH - Requires urgent attention.")
elif alert_score >= 40:
    print("Threat Level: MEDIUM - Prioritize investigation.")
else:
    print("Threat Level: LOW - Log for routine review.")
print("Alert classification complete.")



scanned_port = 25 # Test with 22, 80, 443, 25, 53, 110, 12345

if scanned_port == 22:
    print(f"Port {scanned_port}: SSH (Secure Shell) - Remote administration.")
elif scanned_port == 80:
    print(f"Port {scanned_port}: HTTP (Web Server) - Unencrypted web traffic.")
elif scanned_port == 443:
    print(f"Port {scanned_port}: HTTPS (Secure Web Server) - Encrypted web traffic.")
elif scanned_port == 25:
    print(f"Port {scanned_port}: SMTP (Simple Mail Transfer Protocol) - Email sending.")
elif scanned_port == 53:
    print(f"Port {scanned_port}: DNS (Domain Name System) - Name resolution.")
else:
    print(f"Port {scanned_port}: Unknown or non-standard port.")
print("Service identification finished.")



user_group = "auditors" # Test with "admin", "developers", "guests"

if user_group == "admin":
    print("Privileges: Full System Control.")
elif user_group == "developers":
    print("Privileges: Code Repository Access, Development Tools.")
elif user_group == "auditors":
    print("Privileges: Read-Only Access to Logs and System Configuration.")
else:
    print("Privileges: Basic User Access.")
print("User privilege assignment complete.")