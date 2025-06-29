# M12_L07_Nested_If_Statements_Examples.py

# Header Block
# This script demonstrates the use of nested 'if' statements in Python.
# Nested conditionals allow for multi-layered decision-making, where an
# inner condition is evaluated only after an outer condition is met.

print("--- Example 1: Multi-Factor Authentication (MFA) Flow ---")
# Simulate a multi-stage authentication process.
# First, check password; then, if password is correct, check MFA token.
is_password_correct_ex1 = True  # Try with False
is_mfa_token_valid_ex1 = True   # Try with False if password is True

if is_password_correct_ex1:
    print("Phase 1: Password authenticated successfully.")
    # Now, check the second factor
    if is_mfa_token_valid_ex1:
        print("Phase 2: MFA token validated. User fully authenticated.")
        print("Action: Granting access to sensitive resources.")
    else:
        print("Phase 2: MFA token invalid. Access denied, suspicious activity logged.")
        print("Action: Revoking temporary session.")
else:
    print("Phase 1: Invalid password. Access denied.")
    print("Action: Logging failed login attempt and notifying security.")
print("--- Authentication process complete. ---\n")


print("--- Example 2: Vulnerability Scan Result and Severity Assessment ---")
# Assess a system's vulnerability status and, if vulnerable, its severity.
vulnerability_detected_ex2 = True  # Try with False
vulnerability_score_ex2 = 88       # If detected, test with 95, 70, 45

if vulnerability_detected_ex2:
    print("STATUS: Vulnerability identified on the system.")
    # Now, categorize severity based on score
    if vulnerability_score_ex2 >= 90:
        print("SEVERITY: CRITICAL - Immediate emergency patching required!")
        print("Action: Alerting CISO and patching team.")
    elif vulnerability_score_ex2 >= 70:
        print("SEVERITY: HIGH - Prioritize fix within 24 hours.")
        print("Action: Creating high-priority ticket.")
    else:
        print("SEVERITY: MEDIUM/LOW - Schedule for next patch cycle.")
        print("Action: Documenting for routine maintenance.")
else:
    print("STATUS: No vulnerabilities detected in this scan.")
    print("Action: Proceeding with routine system health checks.")
print("--- Vulnerability assessment complete. ---\n")


print("--- Example 3: File Access and Integrity Check ---")
# First, check if a file exists, then check its integrity (e.g., hash validity).
file_found_ex3 = True             # Try with False
file_hash_matches_ex3 = False     # If found, try with True

if file_found_ex3:
    print("File Status: File located.")
    # Now, check the file's integrity
    if file_hash_matches_ex3:
        print("Integrity Check: File hash matches. File is intact and trusted.")
        print("Action: Proceeding with file operation (e.g., execution, processing).")
    else:
        print("Integrity Check: File hash DOES NOT match! File may be tampered or corrupted.")
        print("Action: Quarantining file and alerting security.")
else:
    print("File Status: File not found.")
    print("Action: Cannot perform requested operation. Logging error.")
print("--- File operation and integrity check complete. ---\n")