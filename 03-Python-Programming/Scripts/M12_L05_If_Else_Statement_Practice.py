# M12_L05_If_Else_Statement_Practice.py

# Header Block
# This script contains practice questions for Python's 'if-else' statement.
# For each scenario, implement the specified conditional logic using 'if-else'.

print("--- Scenario 1: User Role Authorization ---")
# Problem: Grant admin or limited access based on user role.
# Task: Use if-else to print appropriate access messages.

user_role_s1 = "guest"  # Test with "administrator", "user", "guest"
# user_role_s1 = "administrator"

# Your code for Scenario 1 goes here:
if user_role_s1 == "administrator":
    print("Access Granted: Administrator privileges.")
else:
    print("Access Granted: Limited user privileges.")


print("\n--- Scenario 2: Secure Password Check ---")
# Problem: Check if a password meets a minimum length of 8 characters.
# Task: Use if-else to indicate if the password is "Strong enough" or "Weak".

password_s2 = "short"  # Test with "MySuperSecretPassword"
# password_s2 = "MySuperSecretPassword"

# Your code for Scenario 2 goes here:
if len(password_s2) >= 8:
    print("Password Strength: Strong enough.")
else:
    print("Password Strength: Weak. Requires at least 8 characters.")


print("\n--- Scenario 3: Suspicious Login Time ---")
# Problem: Flag logins outside of business hours (9 AM - 5 PM inclusive) as suspicious.
# Task: Use if-else to determine if a login hour is "Normal" or "Suspicious".

current_hour_s3 = 20  # Test with 9, 12, 17, 8, 18
# current_hour_s3 = 10

# Your code for Scenario 3 goes here:
if 9 <= current_hour_s3 <= 17:
    print("Login Time: Normal business hours.")
else:
    print("Login Time: Suspicious (outside business hours). Review immediately.")

print("\n--- Practice complete. ---")