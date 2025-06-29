# Module 12: Conditional Statements

## Lesson 03: If Statement Practice Questions

### 1. Purpose of Practice Questions
This lesson provides practical exercises to reinforce the understanding and application of the `if` statement in Python. By working through these scenarios, you will gain hands-on experience with conditional logic, Boolean expressions, and proper code structure, all within relevant cybersecurity contexts.

### 2. Practice Scenarios & Solutions

#### Scenario 1: Network Intrusion Alert
**Problem:** Monitor network traffic for potential brute-force attacks. If the number of failed login attempts from a single IP exceeds 5, generate an alert.

**Instructions:**
Write a Python script that accepts `failed_attempts` (integer) and `source_ip` (string). If `failed_attempts` is greater than 5, print an alert message:
`ALERT: Potential brute-force attack from [source_ip]! Failed attempts: [failed_attempts]`

**Solution Example:**
```python
failed_attempts = 7
source_ip = "192.168.1.10"

if failed_attempts > 5:
    print(f"ALERT: Potential brute-force attack from {source_ip}! Failed attempts: {failed_attempts}")
print("Monitoring continues.")


software_version = 0.9 # Test with 1.0, 1.5, 2.0
# software_version = 1.5

if software_version <= 1.0:
    print(f"WARNING: Software version {software_version} is outdated. Please update immediately for security patches.")
print("Version check complete.")



file_size_bytes = 12000000 # Test with 5000000
# file_size_bytes = 5000000

if file_size_bytes > 10000000:
    print(f"SUSPICIOUS: Large file detected ({file_size_bytes} bytes). Requires manual review.")
print("File size scan complete.")