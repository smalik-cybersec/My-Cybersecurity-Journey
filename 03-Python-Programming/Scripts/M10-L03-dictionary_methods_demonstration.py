# A dictionary representing a live security alert
current_alert = {
    "alert_id": "SIEM-2025-007",
    "event_type": "Port Scan Detected",
    "source_ip": "203.0.113.12",
    "target_ip": "192.168.1.100",
    "port_range": "1-1024",
    "detection_time": "2025-06-29T14:30:00Z",
    "status": "New"
}

print("--- Initial Alert ---")
print(current_alert)

# Use .get() to retrieve detection time, provide a default if missing
time = current_alert.get('detection_time', 'Time Unknown')
print(f"\nDetection Time: {time}")

# Add an 'analyst' field
current_alert['assigned_analyst'] = 'John Doe'
print(f"After assigning analyst: {current_alert}")

# Update the status and add a 'severity' field
current_alert.update({'status': 'Investigating', 'severity': 'Medium'})
print(f"After updating status and adding severity: {current_alert}")

# Check if 'source_ip' exists in the alert
if 'source_ip' in current_alert:
    print(f"\nSource IP for alert: {current_alert['source_ip']}")

# Get all keys to list alert fields
print(f"Alert Fields: {list(current_alert.keys())}")

# Iterate over all items to print a summary
print("\n--- Full Alert Details ---")
for field, value in current_alert.items():
    print(f"  {field.replace('_', ' ').title()}: {value}")

# Simulate closing the alert by popping relevant details
closed_status = current_alert.pop('status')
print(f"\nAlert Status Popped: {closed_status}")
print(f"Alert after popping status: {current_alert}")

# Clear the dictionary to reset for a new alert
current_alert.clear()
print(f"Alert after clearing: {current_alert}")

# Create a new alert using fromkeys for a standard template
new_alert_template = dict.fromkeys(
    ['alert_id', 'event_type', 'source_ip', 'target_ip', 'status'], 'N/A'
)
print(f"\nNew Alert Template (fromkeys): {new_alert_template}")





"""
Script to demonstrate various functions and methods for manipulating Python dictionaries.

This script covers common dictionary operations such as accessing, adding, modifying,
and removing elements, as well as obtaining dictionary views (keys, values, items).
Each operation is illustrated with examples relevant to cybersecurity data handling,
such as managing security alerts, host scan data, or threat intelligence.

Args:
    None: This script does not accept any command-line arguments.

Returns:
    None: This script prints the results of dictionary operations to the console.
"""

def demonstrate_dictionary_methods():
    """
    Executes a series of demonstrations for Python dictionary functions and methods.
    """
    print("--- Python Dictionary Functions and Methods Demonstration ---")

    # Initial dictionary representing a simulated security alert
    security_alert = {
        "alert_id": "ALERT-2025-06-29-001",
        "timestamp": "2025-06-29T10:00:00Z",
        "event_type": "Suspicious Login Attempt",
        "source_ip": "192.168.1.50",
        "username": "unauthorized_user",
        "severity": "Medium",
        "details": "Multiple failed login attempts from unknown source."
    }

    print("\nInitial Security Alert:")
    print(security_alert)
    print(f"Current number of fields: {len(security_alert)}")

    # 1. Accessing Elements
    print("\n--- 1. Accessing Elements ---")
    print(f"  Event Type (direct access): {security_alert['event_type']}")
    # Using .get() for safe access to a potentially missing key
    target_asset = security_alert.get('target_asset', 'N/A (Target Unknown)')
    print(f"  Target Asset (safe access with .get()): {target_asset}")
    # Using .get() with an existing key
    severity_level = security_alert.get('severity')
    print(f"  Severity Level (get existing): {severity_level}")

    # 2. Adding and Modifying Elements
    print("\n--- 2. Adding and Modifying Elements ---")
    # Add a new key-value pair
    security_alert['status'] = 'Investigating'
    print(f"  After adding 'status': {security_alert}")

    # Modify an existing key's value
    security_alert['severity'] = 'High'
    print(f"  After modifying 'severity': {security_alert}")

    # Use .update() to add multiple new fields and overwrite an existing one
    additional_context = {
        "action_taken": "Blocked IP",
        "analyst_notes": "Initial review complete, escalating.",
        "status": "Escalated" # This will overwrite the previous 'Investigating' status
    }
    security_alert.update(additional_context)
    print(f"  After .update() with additional context: {security_alert}")

    # 3. Removing Elements
    print("\n--- 3. Removing Elements ---")
    # Delete 'username' using del keyword
    if 'username' in security_alert:
        del security_alert['username']
        print(f"  After 'del username': {security_alert}")

    # Pop 'source_ip' and retrieve its value
    popped_source_ip = security_alert.pop('source_ip')
    print(f"  Popped Source IP: {popped_source_ip}")
    print(f"  Alert after popping source_ip: {security_alert}")

    # Attempt to pop a non-existent key with a default value
    non_existent_key_pop = security_alert.pop('destination_port', 'Port info not available')
    print(f"  Attempted to pop 'destination_port': {non_existent_key_pop}")

    # Pop an arbitrary item (typically the last inserted in modern Python)
    # This is less common for specific data, more for processing items from a queue
    if security_alert: # Ensure dictionary is not empty before popping item
        arbitrary_item = security_alert.popitem()
        print(f"  Popped arbitrary item (key, value): {arbitrary_item}")
        print(f"  Alert after popping an item: {security_alert}")

    # Clear all elements from the dictionary
    security_alert.clear()
    print(f"  After .clear(): {security_alert}")
    print(f"  Current number of fields: {len(security_alert)}")

    # 4. Getting Views (keys, values, items)
    print("\n--- 4. Getting Dictionary Views (keys, values, items) ---")
    # Re-initialize a dictionary for view demonstration
    host_inventory = {
        "host001": {"ip": "10.0.0.1", "os": "Linux", "role": "Web Server"},
        "host002": {"ip": "10.0.0.2", "os": "Windows", "role": "Database"},
        "host003": {"ip": "10.0.0.3", "os": "Linux", "role": "Firewall"}
    }
    print(f"  Host Inventory: {host_inventory}")

    # Get all host IDs (keys)
    print(f"  Host IDs: {list(host_inventory.keys())}") # Convert to list for direct printing

    # Get all host details (values)
    print(f"  Host Details (values): {list(host_inventory.values())}")

    # Get all host ID and detail pairs (items)
    print(f"  Host ID and Details (items): {list(host_inventory.items())}")

    # Iterate through items - a very common pattern for processing all dictionary data
    print("\n  Iterating through Host Inventory Items:")
    for host_id, details in host_inventory.items():
        print(f"    Host ID: {host_id}, Details: {details}")

    # 5. Other Useful Methods
    print("\n--- 5. Other Useful Methods ---")
    # Membership Test: Check if a key exists
    print(f"  'host001' in host_inventory? {'host001' in host_inventory}")
    print(f"  'host004' in host_inventory? {'host004' in host_inventory}")

    # Using .copy() for a shallow copy
    temp_host_config = host_inventory.copy()
    temp_host_config['host001']['status'] = 'Under Maintenance' # Modifies nested dict in both
    temp_host_config['new_host'] = {"ip": "10.0.0.4", "os": "Windows", "role": "Workstation"} # Adds only to copy
    print(f"  Original Host Inventory after copy modification: {host_inventory.get('host001', {}).get('status', 'N/A')}")
    print(f"  Copied Host Config ('host001' status): {temp_host_config.get('host001', {}).get('status', 'N/A')}")
    print(f"  Copied Host Config ('new_host'): {temp_host_config.get('new_host', 'N/A')}")
    print(f"  Original Host Inventory (new_host not present): {'new_host' in host_inventory}")

    # Using .fromkeys() to initialize a dictionary with default values for new alerts
    standard_alert_fields = ['id', 'source', 'destination', 'severity', 'timestamp']
    new_alert_template = dict.fromkeys(standard_alert_fields, 'N/A')
    print(f"  New Alert Template (fromkeys): {new_alert_template}")

if __name__ == "__main__":
    demonstrate_dictionary_methods()