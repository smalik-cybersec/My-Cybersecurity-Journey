# M04-L02-Data_Type_Examples.py

# --- 1. Numeric Types ---

# Integer (int)
packet_count = 1250
user_id = 456789
print(f"Packet Count: {packet_count}, Type: {type(packet_count)}")
print(f"User ID: {user_id}, Type: {type(user_id)}")

# Float (float)
malware_detection_rate = 98.75
average_response_time = 0.056
print(f"Malware Detection Rate: {malware_detection_rate}, Type: {type(malware_detection_rate)}")
print(f"Average Response Time: {average_response_time}, Type: {type(average_response_time)}")

# Complex (complex) - Less common in general cybersecurity, but included for completeness
signal_strength = 2 + 3j
print(f"Signal Strength (Complex): {signal_strength}, Type: {type(signal_strength)}")

print("-" * 30) # Separator

# --- 2. Boolean Type ---

# Boolean (bool)
is_admin = True
is_attack_detected = False
print(f"Is Admin: {is_admin}, Type: {type(is_admin)}")
print(f"Is Attack Detected: {is_attack_detected}, Type: {type(is_attack_detected)}")

print("-" * 30) # Separator

# --- 3. Sequence Types ---

# String (str)
log_message = "ALERT: Unauthorized access attempt from 192.168.1.100"
protocol_name = "HTTPS"
print(f"Log Message: '{log_message}', Type: {type(log_message)}")
print(f"Protocol Name: '{protocol_name}', Type: {type(protocol_name)}")

# List (list)
# Mutable, ordered collection - useful for blacklists, scan targets
suspicious_ips = ["192.168.1.10", "10.0.0.5", "172.16.0.20"]
open_ports = [22, 80, 443, 3389]
print(f"Suspicious IPs: {suspicious_ips}, Type: {type(suspicious_ips)}")
print(f"Open Ports: {open_ports}, Type: {type(open_ports)}")

# Adding an item to a list (demonstrates mutability)
suspicious_ips.append("192.168.1.101")
print(f"Suspicious IPs (after append): {suspicious_ips}")

# Tuple (tuple)
# Immutable, ordered collection - useful for fixed configurations
credential_pair = ("admin", "secure_password_hash")
server_endpoint = ("192.168.1.5", 8080)
print(f"Credential Pair: {credential_pair}, Type: {type(credential_pair)}")
print(f"Server Endpoint: {server_endpoint}, Type: {type(server_endpoint)}")

# Attempting to modify a tuple will raise an error (uncomment to test)
# credential_pair[0] = "new_user" 

print("-" * 30) # Separator

# --- 4. Mapping Type ---

# Dictionary (dict)
# Key-value pairs - useful for structured data like system configurations, CVE details
vulnerability_details = {
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

# Set (set)
# Unordered, mutable collection of unique items - useful for eliminating duplicates
unique_attack_sources = {"1.1.1.1", "2.2.2.2", "1.1.1.1", "3.3.3.3"} # '1.1.1.1' appears only once
known_good_hashes = {"hashA", "hashB", "hashC"}
print(f"Unique Attack Sources: {unique_attack_sources}, Type: {type(unique_attack_sources)}")
print(f"Known Good Hashes: {known_good_hashes}, Type: {type(known_good_hashes)}")

# Adding to a set
unique_attack_sources.add("4.4.4.4")
print(f"Unique Attack Sources (after add): {unique_attack_sources}")

# Frozenset (frozenset)
# Immutable version of a set - can be used as dictionary keys
immutable_protocols = frozenset({"TCP", "UDP", "ICMP"})
print(f"Immutable Protocols: {immutable_protocols}, Type: {type(immutable_protocols)}")

# Attempting to add to a frozenset will raise an error (uncomment to test)
# immutable_protocols.add("SSH") 

print("-" * 30) # Separator

# --- 6. None Type ---

# NoneType (None)
# Represents absence of a value
scan_status = None
if scan_status is None:
    print(f"Scan Status: {scan_status}, Type: {type(scan_status)} (Scan not yet started or completed with no result).")

scan_status = "Completed Successfully"
if scan_status is not None:
    print(f"Scan Status updated: {scan_status}")