# Python Dictionaries: Functions and Methods

## 1. Concept Definition

**Dictionary Functions and Methods** are built-in operations that allow you to interact with, manipulate, and query the contents of a Python dictionary. These tools enable you to add, remove, modify, retrieve, and inspect `key-value` pairs efficiently. Mastering these operations is crucial for effectively handling structured data, which is ubiquitous in cybersecurity tasks.

## 2. Key Functions and Methods

Here's a comprehensive overview of essential dictionary functions and methods:

| Method/Function           | Syntax                           | Purpose & Return Value                                                                                                 | Cybersecurity Context                                                                                                                                                                                                                                                                                                                                                                                        |
| :------------------------ | :------------------------------- | :--------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dict[key]` (Access)      | `my_dict[key]`                   | Retrieves the `value` associated with `key`. Raises `KeyError` if `key` not found.                                     | Directly accessing specific fields from parsed data (e.g., `packet['source_ip']`, `alert['severity']`).                                                                                                                                                                                                                                                                                                  |
| `dict.get()`              | `my_dict.get(key, default=None)` | Safely retrieves `value` for `key`. Returns `default` (or `None`) if `key` not found, preventing `KeyError`.             | Safely extracting optional log fields (e.g., `log.get('user_agent', 'Unknown')` to avoid script crashes).                                                                                                                                                                                                                                                                                            |
| `dict[key] = value` (Add/Modify) | `my_dict[key] = new_value`       | Adds `key-value` pair if `key` is new, or updates `value` if `key` exists.                                             | Updating a host's status (`host_info['status'] = 'Compromised'`), adding new findings to a vulnerability report, or changing configuration parameters.                                                                                                                                                                                                                                                 |
| `dict.update()`           | `my_dict.update(other_dict)`     | Merges `other_dict`'s `key-value` pairs into `my_dict`. Overwrites common keys with `other_dict`'s values.               | Combining multiple threat intelligence feeds, merging scan results from different tools, applying default configurations over existing ones.                                                                                                                                                                                                                                                            |
| `del dict[key]`           | `del my_dict[key]`               | Deletes the `key-value` pair. Raises `KeyError` if `key` not found.                                                    | Removing temporary or sensitive data after processing (e.g., `del temp_credentials['password']`).                                                                                                                                                                                                                                                                                                    |
| `dict.pop()`              | `my_dict.pop(key, default=None)` | Removes `key-value` pair and returns its `value`. Raises `KeyError` if `key` not found and no `default` is given.        | Retrieving and simultaneously removing items from a queue-like structure (e.g., processing incident tickets one by one and removing them).                                                                                                                                                                                                                                                         |
| `dict.popitem()`          | `my_dict.popitem()`              | Removes and returns an arbitrary `(key, value)` pair (last inserted in Python 3.7+). Raises `KeyError` if empty.         | Less common for specific data extraction, more for iterative processing of all items where order doesn't matter, or as a simpler way to empty a dictionary.                                                                                                                                                                                                                                           |
| `dict.clear()`            | `my_dict.clear()`                | Removes all `key-value` pairs from the dictionary.                                                                       | Resetting a session's data, clearing accumulated log entries after writing to disk, or wiping temporary evidence storage.                                                                                                                                                                                                                                                                              |
| `dict.keys()`             | `my_dict.keys()`                 | Returns a view object of all keys.                                                                                     | Listing all unique user IDs from a parsed authentication log, enumerating discovered services on a host, or getting all available threat categories.                                                                                                                                                                                                                                                    |
| `dict.values()`           | `my_dict.values()`               | Returns a view object of all values.                                                                                   | Extracting all IP addresses from a collection of host dictionaries, collecting all alert severities for reporting, or gathering all detected malware names.                                                                                                                                                                                                                                                |
| `dict.items()`            | `my_dict.items()`                | Returns a view object of all `(key, value)` tuple pairs.                                                                 | Iterating through all properties of a network device, processing each field in a log entry, or displaying full details of an attack vector. Frequently used with `for key, value in my_dict.items():`.                                                                                                                                                                                                  |
| `len()`                   | `len(my_dict)`                   | Returns the number of `key-value` pairs in the dictionary.                                                               | Checking the count of active connections, verifying the number of entries in a whitelist/blacklist, or determining how many parameters are configured.                                                                                                                                                                                                                                                   |
| `key in dict` (Membership)| `key in my_dict`                 | Returns `True` if `key` exists, `False` otherwise.                                                                     | Quickly checking if an IP is in a blacklist, if a vulnerability ID has been reported, or if a user has a specific permission defined.                                                                                                                                                                                                                                                                 |
| `dict.copy()`             | `my_dict.copy()`                 | Returns a *shallow copy* of the dictionary. Independent changes to top-level key-values; nested mutable objects are linked. | Creating a working copy of a configuration or policy so that modifications can be tested without affecting the original, or for creating a snapshot of data at a specific point in time for audit trails.                                                                                                                                                                                               |
| `dict.fromkeys()`         | `dict.fromkeys(iterable, value)` | Creates a new dictionary with keys from `iterable` and all values set to `value` (defaults to `None`).                     | Initializing a set of hosts with a default status (e.g., "pending scan"), or creating a lookup table for known malware hashes with an initial `None` status for further analysis.                                                                                                                                                                                                                    |

## 3. Core Structure and Syntax Examples

```python
# Initial dictionary representing a network scan result for a host
host_scan_data = {
    "ip_address": "192.168.1.100",
    "hostname": "kali-host",
    "os": "Linux",
    "open_ports": {
        22: "SSH",
        80: "HTTP",
        443: "HTTPS"
    },
    "vulnerabilities": ["CVE-2023-1234", "CVE-2023-5678"]
}

print("--- Initial Host Scan Data ---")
print(f"Original: {host_scan_data}")
print(f"Number of top-level items: {len(host_scan_data)}")

# 1. Accessing Elements
print("\n--- Accessing Elements ---")
print(f"IP Address: {host_scan_data['ip_address']}")
print(f"SSH Service on Port 22: {host_scan_data['open_ports'][22]}")

# Using .get() for safe access
# Attempt to get a non-existent key 'mac_address'
mac_addr = host_scan_data.get('mac_address', 'MAC Address Not Found')
print(f"MAC Address (using .get()): {mac_addr}")

# 2. Adding and Modifying Elements
print("\n--- Adding and Modifying Elements ---")
# Add a new top-level key
host_scan_data['status'] = 'Scanned'
print(f"After adding 'status': {host_scan_data}")

# Modify an existing value
host_scan_data['hostname'] = 'kali-pentest-vm'
print(f"After modifying 'hostname': {host_scan_data}")

# Use .update() to add multiple entries or overwrite
# Merging a new finding and updating OS details
update_data = {
    "last_scan_date": "2025-06-29",
    "os": "Debian GNU/Linux" # Overwrites existing 'os'
}
host_scan_data.update(update_data)
print(f"After .update(): {host_scan_data}")

# Adding a new port to the nested 'open_ports' dictionary
host_scan_data['open_ports'][3389] = 'RDP'
print(f"After adding RDP port: {host_scan_data}")

# 3. Removing Elements
print("\n--- Removing Elements ---")
# Delete 'vulnerabilities' key
del host_scan_data['vulnerabilities']
print(f"After 'del vulnerabilities': {host_scan_data}")

# Pop 'status' key and get its value
scan_status = host_scan_data.pop('status')
print(f"Popped Status: {scan_status}")
print(f"After 'pop status': {host_scan_data}")

# Pop an item that might not exist, with a default
removed_item = host_scan_data.pop('notes', 'No notes found')
print(f"Attempted to pop 'notes': {removed_item}")
print(f"Dictionary state: {host_scan_data}")

# Clear all items (making the dictionary empty)
# host_scan_data.clear()
# print(f"After .clear(): {host_scan_data}") # Uncomment to test clearing

# 4. Getting Views (keys, values, items)
print("\n--- Dictionary Views (Keys, Values, Items) ---")
print(f"All Keys: {host_scan_data.keys()}")
print(f"All Values: {host_scan_data.values()}")
print(f"All Items (key-value tuples): {host_scan_data.items()}")

# Iterating through key-value pairs (common pattern)
print("\nIterating through host_scan_data.items():")
for key, value in host_scan_data.items():
    print(f"  {key.replace('_', ' ').title()}: {value}")

# 5. Other Useful Methods
print("\n--- Other Useful Methods ---")
# Membership test: check if 'ip_address' is a key
print(f"'ip_address' in dict? {'ip_address' in host_scan_data}")
print(f"'mac_address' in dict? {'mac_address' in host_scan_data}")

# Copying a dictionary
analysis_copy = host_scan_data.copy()
analysis_copy['analyst_notes'] = "Investigate further for lateral movement."
print(f"Original dict after copy modification: {host_scan_data.get('analyst_notes', 'N/A')}")
print(f"Copy dict after modification: {analysis_copy['analyst_notes']}")

# Using fromkeys to initialize a set of new assets with a default state
new_assets = ['server-prod-01', 'db-dev-02', 'firewall-perimeter-03']
initial_asset_status = dict.fromkeys(new_assets, "Discovery Pending")
print(f"New Asset Status (fromkeys): {initial_asset_status}")