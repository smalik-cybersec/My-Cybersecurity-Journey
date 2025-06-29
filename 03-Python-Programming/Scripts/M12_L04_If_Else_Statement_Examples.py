# M12_L04_If_Else_Statement_Examples.py

# Header Block
# This script demonstrates the use of Python's 'if-else' statement.
# It provides examples where different code blocks are executed based on
# whether a condition is True or False, within cybersecurity contexts.

print("--- Example 1: User Authentication Check ---")
# Simulate a user authentication process.
valid_username = "cyber_analyst"
valid_password = "StrongPassword!23"

# Test cases:
user_input_username = "cyber_analyst"
user_input_password = "StrongPassword!23"  # Try changing this to "WrongPassword"

if user_input_username == valid_username and user_input_password == valid_password:
    print("Authentication Status: SUCCESS. Access granted to privileged system.")
    print("Log: User 'cyber_analyst' logged in successfully.")
else:
    print("Authentication Status: FAILED. Invalid credentials.")
    print(f"Log: Failed login attempt for user '{user_input_username}' from unknown source.")
print("--- End of authentication process ---\n")


print("--- Example 2: Firewall Traffic Decision ---")
# Determine whether to allow or block network traffic based on the destination port.
destination_port = 443  # Test with 22 (SSH), 80 (HTTP), 443 (HTTPS), 53 (DNS)
# destination_port = 53

if destination_port == 80 or destination_port == 443:
    print(f"Traffic on port {destination_port} (HTTP/HTTPS) is ALLOWED.")
    print("Applying web content filtering rules.")
else:
    print(f"Traffic on port {destination_port} is BLOCKED by default policy.")
    print("Alert: Suspicious port activity detected.")
print("--- End of firewall rule evaluation ---\n")


print("--- Example 3: Malware Scan Result and Action ---")
# Based on a malware scan result, take appropriate security actions.
malware_found = True  # Try changing this to False

if malware_found:
    print("ALERT: Malware detected on system!")
    print("Action: Initiating automated system isolation and forensic data collection.")
    print("Notifying incident response team.")
else:
    print("STATUS: No malware detected.")
    print("Action: Performing routine system defragmentation and update checks.")
print("--- End of malware scan and response ---\n")