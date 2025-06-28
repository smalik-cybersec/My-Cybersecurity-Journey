# Logical Operators Demo

# Define some Boolean variables
is_logged_in = True
is_admin = False
has_permission = True
is_vip = True
is_throttled = False

print(f"Initial states: logged_in={is_logged_in}, admin={is_admin}, permission={has_permission}, vip={is_vip}, throttled={is_throttled}\n")

# AND operator
# Both conditions must be True
print(f"Logged in AND has permission: {is_logged_in and has_permission}") # Expected: True
print(f"Logged in AND is admin: {is_logged_in and is_admin}") # Expected: False

# OR operator
# At least one condition must be True
print(f"Is admin OR has permission: {is_admin or has_permission}") # Expected: True
print(f"Is admin OR is throttled: {is_admin or is_throttled}") # Expected: False

# NOT operator
# Reverses the Boolean value
print(f"NOT is_logged_in: {not is_logged_in}") # Expected: False
print(f"NOT is_admin: {not is_admin}") # Expected: True

# Combining logical and comparison operators
user_score = 85
required_score = 70
has_certificate = True

# Check if user passed AND has certificate
can_advance = (user_score >= required_score) and has_certificate
print(f"\nCan user advance (score >= {required_score} AND has certificate)? {can_advance}") # Expected: True

# Check if user is VIP OR has high score
special_privilege = is_vip or (user_score > 90)
print(f"Has special privilege (is VIP OR score > 90)? {special_privilege}") # Expected: True

# Check if not throttled AND (is admin OR is VIP)
system_status_ok = not is_throttled and (is_admin or is_vip)
print(f"System status OK (NOT throttled AND (admin OR VIP))? {system_status_ok}") # Expected: True (True and (False or True) -> True and True -> True)