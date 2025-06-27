# M04-L01 | Introduction to Data Types

**Date:** 2025-06-27
---
### 1. Definition & Core Concept
> Data types are classifications that specify the type of value a variable holds and the operations that can be performed on it.

In Python, every piece of data — whether it's a number, text, or a true/false value — belongs to a specific data type. These types dictate how the data is stored in memory and what kinds of manipulations are valid for that data. While Python is dynamically typed (meaning you don't explicitly declare a variable's type, it's inferred at runtime), understanding these underlying types is crucial for writing correct, efficient, and secure code.

---
### 2. Why It Matters (The Cybersecurity Context)
* **Relevance:** In cybersecurity, you will constantly interact with diverse forms of data. Correctly identifying and handling data types is fundamental for parsing information, performing analysis, and building robust security tools.
* **Use-Case 1:** **Log Analysis & SIEM Integration:** When parsing security logs (e.g., firewall logs, web server logs), you'll encounter various data points like IP addresses (strings, but sometimes needing conversion to integers for calculations), timestamps (strings, needing conversion to datetime objects for analysis), event codes (integers), and descriptive messages (strings). Misinterpreting data types can lead to faulty analysis or parsing errors.
* **Use-Case 2:** **Network Packet Manipulation:** When working with network packets (e.g., using libraries like Scapy), you'll deal with binary data, hexadecimal representations, port numbers (integers), and IP addresses. Understanding how to convert between these types (e.g., from a string IP to a packed binary representation for a packet header) is critical for crafting and analyzing network traffic. Similarly, distinguishing between numeric and string representations of data in a packet is vital for accurate interpretation and manipulation.

---
### 3. Syntax & Practical Implementation
Python handles data types implicitly, but you can always check a variable's type using the built-in `type()` function.

#### Annotated Example:
```python
# Example 1: Integer Data Type
age = 30
# 'age' is an integer, suitable for mathematical operations
print(f"Variable 'age': {age}, Type: {type(age)}") 

# Example 2: String Data Type
username = "admin_user"
# 'username' is a string, suitable for text manipulation
print(f"Variable 'username': {username}, Type: {type(username)}")

# Example 3: Boolean Data Type
is_authenticated = True
# 'is_authenticated' is a boolean, suitable for conditional logic
print(f"Variable 'is_authenticated': {is_authenticated}, Type: {type(is_authenticated)}")

# Example 4: Mixed data in a list (collection of various types)
network_data = ["192.168.1.1", 80, True, "TCP"]
# Lists can hold different data types, crucial for structured security data
print(f"Variable 'network_data': {network_data}, Type: {type(network_data)}")

# Example 5: Explicit type conversion (will be covered in detail later)
port_str = "22"
port_int = int(port_str) # Converting string to integer
print(f"Converted 'port_str' to 'port_int': {port_int}, Type: {type(port_int)}")