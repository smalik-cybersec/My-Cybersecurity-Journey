# M08-L03 | Python Lists: Functions and Methods

**Date:** 2025-06-28
---
### 1. Definition & Core Concept
> Python lists come with a rich set of built-in functions and methods that enable comprehensive manipulation, modification, and querying of their elements. These operations allow for dynamic data management.

Python's list objects provide various methods (functions associated with the object) and interact with several built-in Python functions to perform actions such as adding, removing, accessing, sorting, and counting elements. These capabilities are crucial for managing collections of data efficiently.

---
### 2. Why It Matters (The Cybersecurity Context)
* **Relevance:** The ability to dynamically manipulate lists is paramount in cybersecurity for tasks ranging from data collection and parsing to analysis and response. Efficient list operations can significantly improve the performance and readability of security tools.
* **Use-Case 1 (Data Collection & Analysis):** Using `append()` or `extend()` to gather network scan results (e.g., discovered hosts, open ports) into a list. Then using `remove()` or `pop()` to process and remove items as they are dealt with, or `count()` to find occurrences of specific events in a log list.
* **Use-Case 2 (Vulnerability Management & Incident Response):** Sorting (`sort()`, `sorted()`) lists of vulnerabilities by severity, or reversing (`reverse()`) a list of incident events to analyze them chronologically. Using `index()` to quickly locate a specific indicator of compromise (IOC) within a large threat intelligence list. The `copy()` method is vital to create a working copy of sensitive data without altering the original.

---
### 3. Syntax & Practical Implementation
#### Annotated Example:
```python
# --- 1. Adding Elements ---

# append(): Adds a single item to the end
scan_results = []
scan_results.append("192.168.1.10:80")
scan_results.append("192.168.1.15:443")
print(f"After append: {scan_results}")
# Output: After append: ['192.168.1.10:80', '192.168.1.15:443']

# extend(): Adds all items from an iterable to the end
new_ports = ["22", "8080"]
scan_results.extend(new_ports)
print(f"After extend: {scan_results}")
# Output: After extend: ['192.168.1.10:80', '192.168.1.15:443', '22', '8080']

# insert(): Inserts an item at a specified index
scan_results.insert(1, "192.168.1.12:21") # Insert after the first element
print(f"After insert: {scan_results}")
# Output: After insert: ['192.168.1.10:80', '192.168.1.12:21', '192.168.1.15:443', '22', '8080']


# --- 2. Removing Elements ---

# remove(): Removes the first occurrence of a specified value
vulnerable_services = ["ftp", "ssh", "telnet", "ssh"]
vulnerable_services.remove("ssh")
print(f"After remove 'ssh': {vulnerable_services}")
# Output: After remove 'ssh': ['ftp', 'telnet', 'ssh']

# pop(): Removes and returns item at index (default last)
last_service = vulnerable_services.pop() # Removes 'ssh'
print(f"Popped last service: {last_service}, List: {vulnerable_services}")
# Output: Popped last service: ssh, List: ['ftp', 'telnet']

first_service = vulnerable_services.pop(0) # Removes 'ftp'
print(f"Popped first service: {first_service}, List: {vulnerable_services}")
# Output: Popped first service: ftp, List: ['telnet']

# clear(): Empties the list
remaining_services = ["telnet", "http"]
remaining_services.clear()
print(f"After clear: {remaining_services}")
# Output: After clear: []

# del statement: Deletes by index or slice
ip_blacklist = ["1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4"]
del ip_blacklist[1] # Delete item at index 1 ("2.2.2.2")
print(f"After del index: {ip_blacklist}")
# Output: After del index: ['1.1.1.1', '3.3.3.3', '4.4.4.4']
del ip_blacklist[1:] # Delete from index 1 to end ("3.3.3.3", "4.4.4.4")
print(f"After del slice: {ip_blacklist}")
# Output: After del slice: ['1.1.1.1']


# --- 3. Accessing and Querying Elements ---

# Indexing []: Accessing elements
log_severity = ["INFO", "WARNING", "ERROR", "CRITICAL"]
print(f"Second severity: {log_severity[1]}") # Output: Second severity: WARNING
print(f"Last severity: {log_severity[-1]}")  # Output: Last severity: CRITICAL

# Slicing [start:end:step]: Getting sub-lists
full_range = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Slice from 3 to 7 (exclusive): {full_range[3:7]}") # Output: Slice from 3 to 7 (exclusive): [3, 4, 5, 6]
print(f"First 5 elements: {full_range[:5]}") # Output: First 5 elements: [0, 1, 2, 3, 4]
print(f"Elements from index 5 onwards: {full_range[5:]}") # Output: Elements from index 5 onwards: [5, 6, 7, 8, 9]
print(f"Every other element: {full_range[::2]}") # Output: Every other element: [0, 2, 4, 6, 8]
print(f"Reversed list: {full_range[::-1]}") # Output: Reversed list: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# index(): Find index of an item
threat_indicators = ["phishing.com", "malware.exe", "phishing.com", "exploit.py"]
print(f"Index of 'malware.exe': {threat_indicators.index('malware.exe')}") # Output: Index of 'malware.exe': 1

# count(): Count occurrences of an item
print(f"Count of 'phishing.com': {threat_indicators.count('phishing.com')}") # Output: Count of 'phishing.com': 2

# len() (built-in): Get list length
print(f"Number of threat indicators: {len(threat_indicators)}") # Output: Number of threat indicators: 4

# in (membership operator): Check for item existence
active_sessions = ["userA", "admin", "userC"]
print(f"'admin' in sessions: {'admin' in active_sessions}") # Output: 'admin' in sessions: True
print(f"'guest' in sessions: {'guest' in active_sessions}") # Output: 'guest' in sessions: False


# --- 4. Reordering and Copying Lists ---

# sort(): Sorts in-place
unsorted_ports = [80, 22, 443, 21]
unsorted_ports.sort()
print(f"Sorted ports (in-place): {unsorted_ports}")
# Output: Sorted ports (in-place): [21, 22, 80, 443]

# sorted() (built-in): Returns a new sorted list
data_packet_sizes = [1500, 64, 128, 1024]
sorted_sizes = sorted(data_packet_sizes, reverse=True) # Sort descending
print(f"Original packet sizes: {data_packet_sizes}") # Output: Original packet sizes: [1500, 64, 128, 1024]
print(f"Newly sorted sizes: {sorted_sizes}") # Output: Newly sorted sizes: [1500, 1024, 128, 64]

# reverse(): Reverses in-place
command_history = ["ls", "cd ..", "pwd"]
command_history.reverse()
print(f"Reversed command history: {command_history}")
# Output: Reversed command history: ['pwd', 'cd ..', 'ls']

# copy(): Creates a shallow copy
original_targets = ["host1", "host2"]
working_copy = original_targets.copy()
working_copy.append("host3")
print(f"Original targets: {original_targets}") # Output: Original targets: ['host1', 'host2']
print(f"Working copy: {working_copy}") # Output: Working copy: ['host1', 'host2', 'host3']


# --- 5. Other Useful Built-in Functions ---

# min(): Smallest value
numerical_ids = [5, 1, 9, 3]
print(f"Minimum ID: {min(numerical_ids)}") # Output: Minimum ID: 1

# max(): Largest value
print(f"Maximum ID: {max(numerical_ids)}") # Output: Maximum ID: 9

# sum(): Sum of numerical values
bytes_transferred = [1024, 512, 2048]
print(f"Total bytes transferred: {sum(bytes_transferred)}") # Output: Total bytes transferred: 3584