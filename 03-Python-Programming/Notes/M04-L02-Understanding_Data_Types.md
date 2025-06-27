# M04-L02 | Understanding Data Types

**Date:** 2025-06-27
---
### 1. Definition & Core Concept
> Python's built-in data types classify values, defining their characteristics and the operations that can be performed on them.

Python automatically infers the data type of a variable, a feature known as dynamic typing. Despite this, a clear understanding of the various data types is essential for writing accurate, efficient, and robust code, especially when dealing with the diverse information encountered in cybersecurity. Each type is optimized for different kinds of data and operations.

---
### 2. Why It Matters (The Cybersecurity Context)
* **Relevance:** Cybersecurity operations heavily rely on processing and manipulating various forms of data. Choosing and correctly handling the appropriate data type is fundamental for tasks ranging from parsing raw log data to analyzing network packets and managing security configurations.
* **Use-Case 1:** **Incident Response Automation:** When automating incident response, you might need to collect data like compromised hostnames (strings), affected user IDs (integers), timestamps of incidents (often strings or datetime objects), and lists of malicious indicators (lists or sets of strings). Correctly typing this data allows for efficient searching, filtering, and cross-referencing.
* **Use-Case 2:** **Vulnerability Management and Reporting:** Storing vulnerability details in a dictionary (e.g., `{"CVE": "CVE-2023-XXXX", "Severity": "High", "Description": "..."}`) allows for structured access and reporting. Maintaining a set of unique malicious file hashes enables rapid lookup and de-duplication when analyzing malware samples.

---
### 3. Syntax & Practical Implementation
The `type()` function is invaluable for inspecting the data type of any Python variable.

#### Annotated Example:
```python
# M04-L02-Data_Type_Examples.py

# --- 1. Numeric Types ---

# Integer (int): Whole numbers
packet_count = 1250 # Used for counts, IDs
user_id = 456789
print(f"Packet Count: {packet_count}, Type: {type(packet_count)}")
print(f"User ID: {user_id}, Type: {type(user_id)}")

# Float (float): Numbers with decimal points
malware_detection_rate = 98.75 # Used for percentages, measurements
average_response_time = 0.056
print(f"Malware Detection Rate: {malware_detection_rate}, Type: {type(malware_detection_rate)}")
print(f"Average Response Time: {average_response_time}, Type: {type(average_response_time)}")

# Complex (complex): Numbers with real and imaginary parts (niche use in security)
signal_strength = 2 + 3j
print(f"Signal Strength (Complex): {signal_strength}, Type: {type(signal_strength)}")

print("-" * 30) # Separator

# --- 2. Boolean Type ---

# Boolean (bool): True or False values
is_admin = True # Used for logical checks, flags
is_attack_detected = False
print(f"Is Admin: {is_admin}, Type: {type(is_admin)}")
print(f"Is Attack Detected: {is_attack_detected}, Type: {type(is_attack_detected)}")

print("-" * 30) # Separator

# --- 3. Sequence Types ---

# String (str): Ordered sequence of characters, immutable
log_message = "ALERT: Unauthorized access attempt from 192.168.1.100" # Used for text, logs, paths
protocol_name = "HTTPS"
print(f"Log Message: '{log_message}', Type: {type(log_message)}")
print(f"Protocol Name: '{protocol_name}', Type: {type(protocol_name)}")

# List (list): Ordered, mutable collection of items
suspicious_ips = ["192.168.1.10", "10.0.0.5", "172.16.0.20"] # Used for dynamic lists of items
open_ports = [22, 80, 443, 3389]
print(f"Suspicious IPs: {suspicious_ips}, Type: {type(suspicious_ips)}")
print(f"Open Ports: {open_ports}, Type: {type(open_ports)}")

# Adding an item to a list (demonstrates mutability)
suspicious_ips.append("192.168.1.101")
print(f"Suspicious IPs (after append): {suspicious_ips}")

# Tuple (tuple): Ordered, immutable collection of items
credential_pair = ("admin", "secure_password_hash") # Used for fixed pairs/records
server_endpoint = ("192.168.1.5", 8080)
print(f"Credential Pair: {credential_pair}, Type: {type(credential_pair)}")
print(f"Server Endpoint: {server_endpoint}, Type: {type(server_endpoint)}")

# Attempting to modify a tuple will raise an error (e.g., credential_pair[0] = "new_user")

print("-" * 30) # Separator

# --- 4. Mapping Type ---

# Dictionary (dict): Unordered collection of unique key-value pairs, mutable
vulnerability_details = { # Used for structured data, configurations
    "CVE": "CVE-2023-4567",
    "Description": "Buffer Overflow in X App",
    "Severity": "Critical",
    "Affected Version": "1.2.0"
}
user_profile = {
    "username": "jdoe",
    "roles": ["analyst", "responder"],
    "last_login": "2025-06-26 10:30:00"
}
print(f"Vulnerability Details: {vulnerability_details}, Type: {type(vulnerability_details)}")
print(f"User Profile: {user_profile}, Type: {type(user_profile)}")

# Accessing dictionary values
print(f"Vulnerability Severity: {vulnerability_details['Severity']}")

print("-" * 30) # Separator

# --- 5. Set Types ---

# Set (set): Unordered, mutable collection of unique items
unique_attack_sources = {"1.1.1.1", "2.2.2.2", "1.1.1.1", "3.3.3.3"} # Automatically handles uniqueness
known_good_hashes = {"hashA", "hashB", "hashC"}
print(f"Unique Attack Sources: {unique_attack_sources}, Type: {type(unique_attack_sources)}")
print(f"Known Good Hashes: {known_good_hashes}, Type: {type(known_good_hashes)}")

# Adding to a set
unique_attack_sources.add("4.4.4.4")
print(f"Unique Attack Sources (after add): {unique_attack_sources}")

# Frozenset (frozenset): Immutable version of a set
immutable_protocols = frozenset({"TCP", "UDP", "ICMP"}) # Can be used as dictionary keys
print(f"Immutable Protocols: {immutable_protocols}, Type: {type(immutable_protocols)}")

# Attempting to add to a frozenset will raise an error (e.g., immutable_protocols.add("SSH"))

print("-" * 30) # Separator

# --- 6. None Type ---

# NoneType (None): Represents the absence of a value
scan_status = None # Useful for initial variable states or indicating no result
if scan_status is None:
    print(f"Scan Status: {scan_status}, Type: {type(scan_status)} (Scan not yet started or completed with no result).")

scan_status = "Completed Successfully"
if scan_status is not None:
    print(f"Scan Status updated: {scan_status}")