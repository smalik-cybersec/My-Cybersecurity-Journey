# M09-L02 | Python Tuples: Declaration

**Date:** 2025-06-28
---
### 1. Definition & Core Concept
> Tuple declaration refers to the various methods used to create or define a tuple in Python, including using parentheses, tuple packing, and the `tuple()` constructor.

Understanding the different ways to declare tuples is essential for writing clear, correct, and Pythonic code. While parentheses are the most common and recommended way for readability, other methods serve specific purposes, especially when dealing with single elements or converting existing iterable data into an immutable tuple.

---
### 2. Why It Matters (The Cybersecurity Context)
* **Relevance:** Correct and explicit tuple declaration ensures data integrity by defining immutable data structures from the outset. Misunderstandings in declaration can lead to unexpected mutability or type errors.
* **Use-Case 1: Immutable Data Conversion:** When fetching sensitive data (e.g., a list of compromised hashes, a set of forbidden IP addresses) from a database or log file, using `tuple()` to convert it ensures that this critical data cannot be accidentally modified later in the script.
    ```python
    # Example: Converting a list of suspicious IPs to an immutable tuple
    suspicious_ips_list = ["192.168.1.100", "10.0.0.5", "172.16.0.20"]
    immutable_suspicious_ips = tuple(suspicious_ips_list)
    print(f"Immutable IPs: {immutable_suspicious_ips}")
    # immutable_suspicious_ips[0] = "new_ip" # This would raise a TypeError
    ```
* **Use-Case 2: Defining Fixed Security Policies:** Hardcoding or defining static security policies, such as allowed protocols or specific port configurations, as tuples ensures these foundational rules remain constant.
    ```python
    # Example: Defining allowed protocols as a tuple
    ALLOWED_PROTOCOLS = ("HTTP", "HTTPS", "SSH")
    # This ensures consistency across the application.
    ```
* **Use-Case 3: Function Signature for Multiple Returns:** When a function in a security tool needs to return multiple related values (e.g., `(is_vulnerable, vulnerability_score, details)`), it inherently returns them as a tuple. Understanding how to declare and unpack these returns is vital for robust tool development.

---
### 3. Syntax & Practical Implementation
#### Annotated Example:
```python
# 1. Declaration using Parentheses () - The most common and recommended way
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}, Type: {type(empty_tuple)}")

credentials = ("admin", "password123") # User credentials pair
print(f"Credentials tuple: {credentials}")

log_entry_metadata = ("2025-06-28", "INFO", "login_attempt", "192.168.1.5")
print(f"Log entry metadata: {log_entry_metadata}")

# 2. Tuple Packing (without parentheses)
# Python automatically interprets comma-separated values as a tuple
ip_port_pair = "127.0.0.1", 8080
print(f"IP-Port pair (packed tuple): {ip_port_pair}, Type: {type(ip_port_pair)}")

# 3. Single-Element Tuple (CRUCIAL trailing comma)
# Without the comma, it's not a tuple!
single_arg_tuple = ("payload_data",) # Note the comma!
print(f"Single item tuple: {single_arg_tuple}, Type: {type(single_arg_tuple)}")

not_a_tuple_str = ("single_string")
print(f"Not a tuple (string): {not_a_tuple_str}, Type: {type(not_a_tuple_str)}")

not_a_tuple_int = (123)
print(f"Not a tuple (integer): {not_a_tuple_int}, Type: {type(not_a_tuple_int)}")

# 4. Using the tuple() constructor
# Converts an iterable (list, string, set, etc.) into a tuple
attack_phases_list = ["reconnaissance", "exploitation", "post-exploitation"]
attack_phases_tuple = tuple(attack_phases_list)
print(f"Tuple from list: {attack_phases_tuple}, Type: {type(attack_phases_tuple)}")

raw_sensor_data_string = "0101110010"
binary_tuple = tuple(raw_sensor_data_string)
print(f"Tuple from string: {binary_tuple}, Type: {type(binary_tuple)}")

# Common scenario: Function returning multiple values
def get_scan_results():
    success = True
    scanned_hosts = 150
    vulnerabilities_found = ["CVE-2023-1234", "CVE-2023-5678"]
    return success, scanned_hosts, vulnerabilities_found # Returns a tuple implicitly

scan_status, hosts_count, detected_cves = get_scan_results() # Tuple unpacking
print(f"Scan Status: {scan_status}, Hosts Scanned: {hosts_count}, CVEs: {detected_cves}")