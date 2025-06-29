# M12_L08_Shorthand_If_Else_Examples.py

# Header Block
# This script demonstrates the shorthand 'if-else' statement, also known as the ternary operator.
# It shows how to write concise conditional expressions for assigning values or returning results.

print("--- Example 1: User Authentication Result ---")
# Determine an access message based on an authentication status.
is_user_authenticated = True  # Try changing to False

authentication_message = "Access Granted" if is_user_authenticated else "Access Denied - Invalid Credentials"
print(f"Authentication Result: {authentication_message}")

# Another use case: setting a boolean flag
can_proceed = True if is_user_authenticated else False
print(f"Can User Proceed: {can_proceed}\n")


print("--- Example 2: Firewall Policy Decision ---")
# Decide if a port is "Allowed" or "Blocked" based on common secure ports.
# Assume 80, 443, 22, 53 are allowed, others are blocked for this example.
destination_port = 80  # Test with 22, 443, 53, 23, 139, 8080

action_status = "ALLOWED" if destination_port in [80, 443, 22, 53] else "BLOCKED"
print(f"Firewall Policy for Port {destination_port}: {action_status}")

# Dynamic message based on the action
log_entry = f"Traffic {'permitted' if action_status == 'ALLOWED' else 'denied'} on port {destination_port}."
print(f"Log: {log_entry}\n")


print("--- Example 3: Incident Priority Assignment ---")
# Assign an incident priority (High/Low) based on whether critical assets are involved.
critical_asset_compromised = False  # Try changing to True

incident_priority = "HIGH" if critical_asset_compromised else "LOW"
print(f"Incident Priority: {incident_priority}")

# Determine required response team
response_team = "IR Team" if incident_priority == "HIGH" else "Security Analyst"
print(f"Assigned to: {response_team}\n")


print("--- Example 4: File Scan Outcome Message ---")
# Generate a scan outcome message based on malware detection.
malware_found_in_scan = False  # Try changing to True

scan_outcome_message = "Clean - No threats detected." if not malware_found_in_scan else "Threat Detected - Immediate action required!"
print(f"File Scan Outcome: {scan_outcome_message}")