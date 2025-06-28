# Python Dictionaries: An Introduction

## 1. Concept Definition

A **dictionary** in Python is a built-in data structure that stores data in `key-value` pairs. It is an *unordered* collection (prior to Python 3.7, where insertion order is guaranteed) that is *mutable* (changeable). Each `key` within a dictionary must be unique and immutable (e.g., strings, numbers, tuples), while the `value` associated with a key can be of any data type and can be duplicated.

Think of it like a real-world dictionary where you look up a `word` (the key) to find its `definition` (the value), or a phone book where a `name` (the key) maps to a `phone number` (the value).

> **Key-Value Pair:** The fundamental unit of a dictionary, where a `key` uniquely identifies and provides access to its corresponding `value`.

## 2. Analogies

* **Physical Dictionary:** Words are keys, definitions are values.
* **Phone Book:** Names are keys, phone numbers are values.
* **Database Record:** Field names are keys, the data in those fields are values.
* **Security Incident Report:** Fields like "Incident ID", "Affected System", "Severity" are keys, and their respective details are values.

## 3. Core Structure and Syntax

Dictionaries are created using curly braces `{}`. Each `key: value` pair is separated by a colon, and pairs are separated by commas.

```python
# General syntax for a dictionary
my_dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

# Example: A dictionary storing basic host information
host_details = {
    "ip_address": "192.168.1.100",
    "hostname": "webserver01.local",
    "os": "Ubuntu Server 22.04",
    "open_ports": [80, 443, 22] # Values can be lists or other complex types
}

# Accessing values using keys
print(f"IP Address: {host_details['ip_address']}")
print(f"Operating System: {host_details['os']}")


# Define a dictionary to represent a security alert
security_alert = {
    "alert_id": "INC-2025-001A",
    "event_type": "Unauthorized Access Attempt",
    "source_ip": "103.45.67.89",
    "target_system": "database_server_prod",
    "severity": "Critical",
    "timestamp": "2025-06-28T23:59:00Z",
    "details": "Multiple failed login attempts detected from unknown IP."
}

print("--- Security Alert Details ---")
print(f"Alert ID: {security_alert['alert_id']}")
print(f"Event Type: {security_alert['event_type']}")
print(f"Source IP: {security_alert['source_ip']}")
print(f"Severity: {security_alert['severity']}")
print(f"Timestamp: {security_alert['timestamp']}")

# Check if a specific key exists before accessing it
if "target_system" in security_alert:
    print(f"Target System: {security_alert['target_system']}")
else:
    print("Target System: N/A")

# Example of iterating through key-value pairs
print("\n--- All Alert Data ---")
for key, value in security_alert.items():
    print(f"{key.replace('_', ' ').title()}: {value}")