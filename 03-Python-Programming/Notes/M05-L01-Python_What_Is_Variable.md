# M05-L01 | What is a Variable

**Date:** 2025-06-27
---
### 1. Definition & Core Concept
> A variable in Python is a named storage location used to hold data, making your code more organized, readable, and dynamic.

Variables act as containers for various types of data, such as numbers, text (strings), lists, or boolean values. When you assign a value to a variable, Python allocates a space in memory to store that value and associates it with the variable's name. This allows you to refer to and manipulate the data using its descriptive name throughout your program, rather than hardcoding values directly. This abstraction is fundamental to writing flexible and maintainable code.

---
### 2. Why It Matters (The Cybersecurity Context)
* **Relevance:** Variables are indispensable for creating dynamic and adaptable cybersecurity tools. They allow scripts to handle varying inputs (e.g., target IPs, port numbers, usernames, file paths) without requiring code modification.
* **Use-Case 1:** Storing target information. Instead of hardcoding an IP address or domain name into a network scanner, you can store it in a variable like `target_host = "192.168.1.1"` or `target_domain = "example.com"`. This makes the script reusable for different targets.
* **Use-Case 2:** Managing credentials or configuration. While not recommended for sensitive data directly in code, variables can temporarily hold configuration parameters like `default_port = 22` or `log_file_path = "/var/log/app.log"`, which can be easily changed without altering the core logic. They are crucial when dealing with data fetched from secure configuration files or environment variables.

---
### 3. Syntax & Practical Implementation
#### Annotated Example:
```python
# Declare a variable to store a target IP address for a scan
target_ip = "192.168.1.100" # 'target_ip' is the variable name, "192.168.1.100" is the string value

# Declare a variable to store the port number we want to check
port_to_scan = 443 # 'port_to_scan' is the variable name, 443 is the integer value

# Declare a variable to store a boolean state (True/False)
is_vulnerable = False # 'is_vulnerable' is the variable name, False is the boolean value

# Use the variables in a simulated action or print statement
print(f"[*] Starting scan on {target_ip} on port {port_to_scan}")
if is_vulnerable:
    print(f"[!] Target {target_ip} is vulnerable!")
else:
    print(f"[+] Target {target_ip} appears secure on port {port_to_scan}.")

# Variables can also be reassigned
scan_port = 80 # The 'scan_port' variable now holds a new value
print(f"[*] Re-scanning port: {scan_port}")