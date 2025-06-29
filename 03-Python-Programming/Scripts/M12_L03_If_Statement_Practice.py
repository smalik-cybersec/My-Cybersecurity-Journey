# M12_L03_If_Statement_Practice.py

# Header Block
# This script contains practice questions for Python's 'if' statement.
# Each section presents a cybersecurity scenario.
# Your task is to write the 'if' statement logic for each scenario.

print("--- Scenario 1: Network Intrusion Alert ---")
# Problem: If failed login attempts from a single IP exceed 5, print an alert.
# Task: Write an 'if' statement to check this condition.

failed_attempts_s1 = 7 # Test case 1: Should trigger alert
source_ip_s1 = "192.168.1.10"
# failed_attempts_s1 = 3 # Test case 2: Should NOT trigger alert
# source_ip_s1 = "10.0.0.5"

# Your code for Scenario 1 goes here:
if failed_attempts_s1 > 5:
    print(f"ALERT: Potential brute-force attack from {source_ip_s1}! Failed attempts: {failed_attempts_s1}")


print("\n--- Scenario 2: Software Version Check ---")
# Problem: If software version is 1.0 or lower, print a warning.
# Task: Write an 'if' statement to check this condition.

software_version_s2 = 0.9 # Test case 1: Should trigger warning
# software_version_s2 = 1.0 # Test case 2: Should trigger warning
# software_version_s2 = 1.5 # Test case 3: Should NOT trigger warning

# Your code for Scenario 2 goes here:
if software_version_s2 <= 1.0:
    print(f"WARNING: Software version {software_version_s2} is outdated. Please update immediately for security patches.")


print("\n--- Scenario 3: Suspicious File Size ---")
# Problem: If a file is larger than 10 MB (10,000,000 bytes), flag it as suspicious.
# Task: Write an 'if' statement to check this condition.

file_size_bytes_s3 = 12000000 # Test case 1: Should trigger suspicious flag
# file_size_bytes_s3 = 5000000 # Test case 2: Should NOT trigger suspicious flag

# Your code for Scenario 3 goes here:
if file_size_bytes_s3 > 10000000:
    print(f"SUSPICIOUS: Large file detected ({file_size_bytes_s3} bytes). Requires manual review.")

print("\n--- Practice complete. ---")