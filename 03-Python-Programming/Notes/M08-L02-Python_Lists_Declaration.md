# M08-L02 | Python Lists: Declaration and Initialization

**Date:** 2025-06-28
---
### 1. Definition & Core Concept
> List declaration refers to the process of creating a new list, while initialization involves assigning initial values to it at the time of creation or shortly thereafter.

In Python, lists are declared using square brackets `[]` or the built-in `list()` constructor. They can be created as empty containers or populated with initial elements. The method chosen often depends on whether the list's contents are known upfront or will be gathered dynamically during program execution.

---
### 2. Why It Matters (The Cybersecurity Context)
* **Relevance:** Properly declaring and initializing lists is the foundational step for any script that needs to manage collections of data. In cybersecurity, this could involve setting up targets, storing results, or pre-defining known bad indicators.
* **Use-Case 1:** Creating an empty list to store the results of a port scan (`open_ports = []`) or a list of vulnerable services discovered during an enumeration phase. This allows for dynamic aggregation of data.
* **Use-Case 2:** Initializing a list with known values, such as a list of common weak passwords to check against a hash file (`weak_passwords = ["password", "123456", "admin"]`) or a list of C2 server domains to block.

---
### 3. Syntax & Practical Implementation
#### Annotated Example:
```python
# 1. Declaring an Empty List
# Using square brackets (most common and Pythonic)
empty_list_1 = []
print(f"Empty list (square brackets): {empty_list_1}") # Output: Empty list (square brackets): []

# Using the list() constructor
empty_list_2 = list()
print(f"Empty list (list() constructor): {empty_list_2}") # Output: Empty list (list() constructor): []


# 2. Declaring and Initializing with Values
# List of integers
ip_segments = [192, 168, 1, 1]
print(f"IP segments: {ip_segments}") # Output: IP segments: [192, 168, 1, 1]

# List of strings (e.g., hostnames)
target_hosts = ["server01.local", "kali.local", "10.0.0.50"]
print(f"Target hosts: {target_hosts}") # Output: Target hosts: ['server01.local', 'kali.local', '10.0.0.50']

# List with mixed data types (e.g., a simple log entry structure)
log_entry = ["ERROR", 404, "Page Not Found", 1678886400.0]
print(f"Mixed log entry: {log_entry}") # Output: Mixed log entry: ['ERROR', 404, 'Page Not Found', 1678886400.0]


# 3. Initializing from other Iterables using list() constructor
# From a string (each character becomes an item)
domain = "example.com"
domain_chars = list(domain)
print(f"Characters from domain: {domain_chars}") # Output: Characters from domain: ['e', 'x', 'a', 'm', 'p', 'l', 'e', '.', 'c', 'o', 'm']

# From a tuple (common if you receive data as a tuple and need mutability)
mac_address_tuple = ("00", "1A", "2B", "3C", "4D", "5E")
mac_address_list = list(mac_address_tuple)
print(f"MAC address as list: {mac_address_list}") # Output: MAC address as list: ['00', '1A', '2B', '3C', '4D', '5E']

# From a range object (useful for generating sequential numbers, e.g., port ranges)
port_range = list(range(80, 86)) # Generates numbers from 80 up to (but not including) 86
print(f"Port range 80-85: {port_range}") # Output: Port range 80-85: [80, 81, 82, 83, 84, 85]

# 4. Brief example of List Comprehension (for future reference)
# Generating a list of squared numbers for quick data transformation
squared_numbers = [x**2 for x in range(1, 5)]
print(f"Squared numbers (list comprehension): {squared_numbers}") # Output: Squared numbers (list comprehension): [1, 4, 9, 16]