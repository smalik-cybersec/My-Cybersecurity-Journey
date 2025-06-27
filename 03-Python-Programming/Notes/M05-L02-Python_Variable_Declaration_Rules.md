# M05-L02 | Variable Declaration Rules

**Date:** 2025-06-27
---
### 1. Definition & Core Concept
> Python variables must adhere to specific naming conventions and rules to be considered valid and avoid syntax errors, despite Python being dynamically typed.

Python does not require explicit type declaration for variables; their type is inferred at runtime based on the assigned value. However, the names given to these variables must follow a set of rules to be syntactically correct and readable. Adhering to these rules prevents errors and ensures your code is robust.

---
### 2. Why It Matters (The Cybersecurity Context)
* **Relevance:** Proper variable naming is crucial for writing clear, maintainable, and debuggable security scripts. Misleading or invalid variable names can lead to `SyntaxError` or `NameError`, halting critical security operations (e.g., live incident response scripts, automated vulnerability scans).
* **Use-Case 1:** Script reliability. In an automated vulnerability scanner, if a variable `target-ip` is used instead of `target_ip`, the script will fail with a `SyntaxError`, preventing the scan from running. Understanding these rules ensures your tools execute reliably.
* **Use-Case 2:** Code clarity for team collaboration. When security analysts collaborate on Python tools, consistent and valid variable naming (e.g., `packet_header`, `exploit_payload`, `auth_token`) improves readability and reduces the likelihood of errors when others review or modify the code.

---
### 3. Syntax & Practical Implementation
#### Annotated Example:
```python
# --- VALID VARIABLE DECLARATIONS ---

# 1. Starts with a letter:
user_input = "malicious_payload"

# 2. Starts with an underscore (often for internal use or special cases):
_temp_file_path = "/tmp/data.log"

# 3. Contains alphanumeric characters and underscores:
http_status_code_200 = 200
log_entry_id = "abc123xyz"

# 4. Case-sensitive: 'username' and 'userName' are different variables
username = "admin"
userName = "guest"
print(f"User 1: {username}, User 2: {userName}")


# --- INVALID VARIABLE DECLARATIONS (Uncomment to see errors) ---

# Invalid: Starts with a number
# 1_attempt = "failed_login" # SyntaxError: invalid decimal literal

# Invalid: Contains hyphens (hyphens are treated as subtraction operators)
# threat-level = "high" # SyntaxError: can't assign to operator

# Invalid: Contains special characters like @, $, %
# email@address = "user@example.com" # SyntaxError: invalid syntax
# $cost = 50 # SyntaxError: invalid syntax

# Invalid: Uses a Python keyword (e.g., 'if', 'for', 'class', 'print')
# if = True # SyntaxError: invalid syntax
# for = "loop_variable" # SyntaxError: invalid syntax
# Note: Assigning to 'print' (e.g., print = "hello") is syntactically valid but overwrites the built-in function,
# which is extremely bad practice and will break your print statements later.