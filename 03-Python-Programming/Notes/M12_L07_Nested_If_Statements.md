# Module 12: Conditional Statements

## Lesson 07: Nested If Statements

### 1. Purpose of Nested `if` Statements
Nested `if` statements involve placing one or more `if` (or `elif`/`else`) statements inside another conditional block. This allows for multi-level decision-making, where an inner condition is only evaluated if its outer, enclosing condition is met. It's used to model complex logic where decisions depend on a hierarchy of checks.

### 2. Syntax
```python
if outer_condition:
    # Code executed if outer_condition is True
    print("Outer condition met.")
    if inner_condition_1:
        # Code executed if outer_condition True AND inner_condition_1 True
        print("Inner condition 1 met.")
    elif inner_condition_2:
        # Code executed if outer_condition True AND inner_condition_1 False AND inner_condition_2 True
        print("Inner condition 2 met.")
    else:
        # Code executed if outer_condition True AND all inner conditions False
        print("No inner condition met.")
else:
    # Code executed if outer_condition is False
    print("Outer condition not met.")


    username_valid = True
password_correct = True
mfa_code_valid = False # Change to True to test full access

if username_valid and password_correct:
    print("Phase 1: Username and password validated.")
    if mfa_code_valid:
        print("Phase 2: MFA code validated. Full access granted.")
        # Code to grant access to critical system
    else:
        print("Phase 2: MFA code invalid. Access denied.")
        # Code to log MFA failure and block access
else:
    print("Phase 1: Invalid username or password. Access denied.")
    # Code to log authentication failure
print("Authentication process concluded.")



system_compromised = True
data_exfiltration_detected = True # Change to False

if system_compromised:
    print("STATUS: System is compromised.")
    if data_exfiltration_detected:
        print("ACTION: Data exfiltration detected! Initiate emergency containment.")
        # Trigger immediate network isolation, forensic imaging
    else:
        print("ACTION: System compromised, but no data exfiltration detected (yet). Contain and investigate.")
        # Trigger containment without immediate network cut-off, prioritize data integrity
else:
    print("STATUS: System appears secure.")
    # Continue routine monitoring
print("Incident response assessment complete.")



vulnerability_present = True
exploit_available = True # Change to False

if vulnerability_present:
    print("Vulnerability confirmed on system.")
    if exploit_available:
        print("URGENT: Public exploit available. Patch immediately to prevent compromise!")
    else:
        print("INFO: Vulnerability present, but no known public exploit. Prioritize patch, but no immediate panic.")
else:
    print("No known vulnerability found for this software.")
print("Vulnerability management decision made.") 