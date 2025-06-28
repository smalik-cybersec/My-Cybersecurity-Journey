# M07-L05 | 05 - Logical Operators

**Date:** 2025-06-28
---
### 1. Definition & Core Concept
> Logical operators (`and`, `or`, `not`) are used to combine or modify Boolean expressions, allowing for the creation of complex conditions.

They evaluate multiple `True`/`False` conditions and return a single `True` or `False` result. These operators are crucial for controlling the flow of a program based on whether multiple criteria are met or not met.

---
### 2. Why It Matters (The Cybersecurity Context)
* **Relevance:** Logical operators are indispensable for building sophisticated conditional logic in cybersecurity tools, enabling them to make intelligent decisions based on multiple security parameters.
* **Use-Case 1:** **Advanced Intrusion Detection Rules:** Combine multiple suspicious indicators to trigger an alert. For example, `if (failed_logins > 5 and source_ip == "known_bad_ip") or (port_scan_detected and not trusted_network):`
* **Use-Case 2:** **Automated Policy Enforcement:** Check if a system meets all compliance requirements before granting access or deploying software. For instance, `if (os_patched and antivirus_active) and (firewall_enabled and not suspicious_process_running):`
* **Use-Case 3:** **Refined Log Filtering and Analysis:** Precisely filter log entries to pinpoint specific events. For example, finding lines that contain "failed" AND "password" BUT NOT "locked_account".

---
### 3. Syntax & Practical Implementation
#### Annotated Example:
```python
# Variables representing security conditions
is_authenticated = True
is_admin_role = False
is_from_trusted_network = True
is_high_risk_activity = True
is_malicious_ip = False

print(f"Current security states:\n"
      f"  Authenticated: {is_authenticated}\n"
      f"  Admin Role: {is_admin_role}\n"
      f"  Trusted Network: {is_from_trusted_network}\n"
      f"  High Risk Activity: {is_high_risk_activity}\n"
      f"  Malicious IP: {is_malicious_ip}\n")

# 1. AND Operator
# Returns True if both operands are True.
# Scenario: Allow access only if authenticated AND from a trusted network
can_access_resource = is_authenticated and is_from_trusted_network
print(f"Access allowed (Authenticated AND Trusted Network): {can_access_resource}") # Expected: True

# Scenario: Trigger alert if high risk activity AND from a malicious IP
trigger_alert_and = is_high_risk_activity and is_malicious_ip
print(f"Trigger alert (High Risk AND Malicious IP): {trigger_alert_and}") # Expected: False

# 2. OR Operator
# Returns True if at least one operand is True.
# Scenario: Grant admin privileges if user is admin OR has special access
grant_admin_access = is_admin_role or is_authenticated # Let's say authenticated can temporarily get some admin access
print(f"Grant admin access (Admin Role OR Authenticated): {grant_admin_access}") # Expected: True

# Scenario: Block connection if high risk activity OR from a malicious IP
block_connection_or = is_high_risk_activity or is_malicious_ip
print(f"Block connection (High Risk OR Malicious IP): {block_connection_or}") # Expected: True

# 3. NOT Operator
# Reverses the Boolean value of the operand.
# Scenario: Proceed if NOT high risk activity
proceed_if_safe = not is_high_risk_activity
print(f"Proceed if safe (NOT High Risk Activity): {proceed_if_safe}") # Expected: False

# Scenario: Allow if NOT from malicious IP
allow_if_not_malicious = not is_malicious_ip
print(f"Allow if NOT malicious IP: {allow_if_not_malicious}") # Expected: True

# Combining Multiple Logical and Comparison Operators
user_attempts = 3
max_attempts = 5
account_locked = False

# Condition: (Attempts exceeded OR account locked) AND NOT from trusted network
deny_login = ((user_attempts >= max_attempts) or account_locked) and (not is_from_trusted_network)
print(f"\nDeny login condition (complex): {deny_login}") # Expected: False (False or False) and (False) -> False