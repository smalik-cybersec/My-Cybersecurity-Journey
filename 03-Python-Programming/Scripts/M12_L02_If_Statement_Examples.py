# M12_L02_If_Statement_Examples.py

# Header Block
# This script demonstrates the basic functionality of Python's 'if' statement
# with examples relevant to cybersecurity concepts.
# It covers checking conditions and executing code blocks conditionally.

print("--- Example 1: Checking for Administrative Privileges ---")
# Simulate whether the current user has administrative privileges.
# In a real application, this would involve OS-specific calls (e.g., os.getuid() on Linux, win32api on Windows).
user_is_admin = True
# Try changing user_is_admin to False and re-run the script to see the difference.

if user_is_admin:
    print("Status: Administrative privileges detected.")
    print("Action: Initiating privileged system configuration changes.")
    # Placeholder for actual sensitive operations (e.g., modifying registry, installing services)
    print("Note: In a real scenario, this would be highly restricted.")
print("--- Privilege check complete. Program continues. ---\n")


print("--- Example 2: Basic Network Port Status Check ---")
# Simulate a network scan result for a specific port (e.g., SSH port 22).
port_22_open = False
# Try changing port_22_open to True and re-run the script.

if port_22_open:
    print("ALERT: Port 22 (SSH) is found OPEN.")
    print("Recommendation: Investigate for potential unauthorized access or misconfigurations.")
    # Placeholder for further actions (e.g., initiating a more detailed scan, logging the event)
print("--- Port scan summary complete. ---\n")


print("--- Example 3: File Extension Validation for Log Processing ---")
# This example shows how to use 'if' to validate a file type before processing it.
file_to_process = "web_server.log"
# Try changing file_to_process to "image.jpg" and re-run the script.

if file_to_process.endswith(".log"):
    print(f"Validation: '{file_to_process}' is identified as a log file.")
    print("Action: Beginning log parsing for suspicious entries.")
    # Placeholder for log parsing logic (e.g., searching for error codes, unusual IP addresses)
print("--- File validation finished. ---\n")


print("--- Example 4: Checking for Specific Malware Signature ---")
# Imagine a simplified antivirus check
file_signature = "EICAR-Test-File"
# file_signature = "harmless_document.txt" # Uncomment to test other path

if file_signature == "EICAR-Test-File":
    print("DANGER: Known EICAR test string detected!")
    print("Action: Initiating quarantine procedures and alerting security team.")
print("--- Malware scan complete. ---\n")