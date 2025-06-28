# Membership Operators Demo

# --- 1. With Strings ---
print("--- String Examples ---")
message = "The quick brown fox jumps over the lazy dog."
search_term1 = "fox"
search_term2 = "cat"

print(f"'{search_term1}' in '{message}': {search_term1 in message}") # Expected: True
print(f"'{search_term2}' in '{message}': {search_term2 in message}") # Expected: False
print(f"'{search_term1}' not in '{message}': {search_term1 not in message}") # Expected: False
print(f"'{search_term2}' not in '{message}': {search_term2 not in message}") # Expected: True

# Case sensitivity matters for strings
print(f"'Fox' in '{message}': {'Fox' in message}") # Expected: False


# --- 2. With Lists ---
print("\n--- List Examples ---")
fruits = ["apple", "banana", "cherry", "date"]
fruit1 = "banana"
fruit2 = "grape"

print(f"'{fruit1}' in {fruits}: {fruit1 in fruits}") # Expected: True
print(f"'{fruit2}' in {fruits}: {fruit2 in fruits}") # Expected: False
print(f"'{fruit1}' not in {fruits}: {fruit1 not in fruits}") # Expected: False

# --- 3. With Tuples ---
print("\n--- Tuple Examples ---")
ip_ports = ("192.168.1.1", 80, 443, "22")
port_to_check = 80
protocol = "TCP"

print(f"{port_to_check} in {ip_ports}: {port_to_check in ip_ports}") # Expected: True
print(f"'{protocol}' in {ip_ports}: {protocol in ip_ports}") # Expected: False

# --- 4. With Dictionaries (checks keys, not values) ---
print("\n--- Dictionary Examples (Checks Keys) ---")
user_roles = {"admin": True, "guest": False, "auditor": True}
role1 = "admin"
role2 = "developer"
status_value = True

print(f"'{role1}' in {user_roles}: {role1 in user_roles}") # Expected: True (checking key)
print(f"'{role2}' in {user_roles}: {role2 in user_roles}") # Expected: False (checking key)
print(f"{status_value} in {user_roles}: {status_value in user_roles}") # Expected: False (checks keys, not values)
print(f"{status_value} in user_roles.values(): {status_value in user_roles.values()}") # Expected: True (explicitly checks values)

# --- Cybersecurity Specific Example: Log Filtering ---
log_line1 = "2025-06-28 10:05:32 INFO User 'john_doe' logged in from 192.168.1.5"
log_line2 = "2025-06-28 10:06:15 ERROR Authentication failed for 'admin' from 10.0.0.10"
log_line3 = "2025-06-28 10:07:01 DEBUG System health check passed."

print("\n--- Cybersecurity Example: Log Filtering ---")
if "ERROR" in log_line1:
    print("Error found in line 1!")
else:
    print("No error in line 1.") # Expected

if "ERROR" in log_line2 and "Authentication failed" in log_line2:
    print("Critical authentication error detected!") # Expected

if "admin" in log_line3 and "failed" in log_line3:
    print("Admin failed login (false positive example if not careful).")
else:
    print("No admin failed login in line 3.") # Expected

suspicious_ips = ["10.0.0.10", "172.16.0.20"]
source_ip_from_log = "10.0.0.10"

if source_ip_from_log in suspicious_ips:
    print(f"Suspicious IP {source_ip_from_log} detected!") # Expected