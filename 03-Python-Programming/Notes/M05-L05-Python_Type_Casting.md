# M05-L05 | Type Casting

**Date:** 2025-06-27
---
### 1. Definition & Core Concept
> Type casting, or type conversion, is the process of converting a variable's data type from one to another (e.g., from a string to an integer, or an integer to a float) using Python's built-in type conversion functions.

Every value in Python has a data type. Sometimes, data arrives in a format that isn't suitable for the operation you need to perform (e.g., numerical calculations on a string). Type casting allows you to explicitly change the type of a value, enabling compatibility between different data types in operations. Python also performs implicit type conversion in certain contexts, but explicit casting provides precise control and is often necessary.

---
### 2. Why It Matters (The Cybersecurity Context)
* **Relevance:** Type casting is fundamental in cybersecurity for robust input validation, data manipulation, and ensuring the correct interpretation of data received from various sources (e.g., network traffic, log files, user input).
* **Use-Case 1:** Input validation for network tools. When a user inputs a port number (e.g., '80' or '443') through a command-line interface, it's read as a string. For a port scanner to use it numerically, it *must* be type-cast to an integer using `int()`. Failure to do so will result in `TypeError` or `ValueError`, crashing the tool.
* **Use-Case 2:** Processing forensic data. If you extract hexadecimal values (as strings) from memory dumps or log files, you might need to convert them to integers (`int(hex_string, 16)`) for arithmetic operations or comparisons. Similarly, timestamps might need conversion to `datetime` objects for proper analysis.

---
### 3. Syntax & Practical Implementation
#### Annotated Example:
```python
# --- Common Type Casting Examples ---

# 1. String to Integer (for numerical operations)
user_port_input = "22" # Data often comes as string (e.g., from input() or a file)
print(f"Original type of user_port_input: {type(user_port_input)}")
try:
    target_port = int(user_port_input)
    print(f"Casted type of target_port: {type(target_port)}, Value: {target_port}")
    print(f"Can now perform math: {target_port + 100}")
except ValueError:
    print(f"Error: '{user_port_input}' is not a valid integer for a port.")

# 2. String to Float (for decimal numbers)
threat_score_str = "8.5"
threat_score_float = float(threat_score_str)
print(f"Type of threat_score_float: {type(threat_score_float)}, Value: {threat_score_float}")

# 3. Integer/Float to String (for concatenation or display)
response_code = 200
status_message = "HTTP Status: " + str(response_code) # Convert int to str for string concatenation
print(status_message)

# 4. To Boolean (evaluating truthiness)
# Useful for conditional logic, especially with empty values or zeros
is_admin_session = 1       # Non-zero integer is True
has_permissions = []       # Empty list is False
security_log = "Entry found" # Non-empty string is True

print(f"Is Admin Session: {bool(is_admin_session)}")
if not bool(has_permissions): # More Pythonic: 'if not has_permissions:'
    print("User has no specific permissions granted.")
if bool(security_log):
    print("Security log has content.")

# 5. Implicit Type Conversion (Python handles automatically in some cases)
# When an integer and a float are involved in arithmetic, the integer is promoted to a float.
int_value = 10
float_value = 3.14
result = int_value + float_value # int_value becomes 10.0 for the operation
print(f"Result of 10 + 3.14: {result}, Type: {type(result)}") # Result is a float