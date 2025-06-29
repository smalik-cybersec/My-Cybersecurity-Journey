# M12_L06_Elif_Statement_Examples.py

# Header Block
# This script demonstrates the use of Python's 'elif' (else if) statement.
# It shows how to handle multiple conditions sequentially in a single
# conditional structure, with examples relevant to cybersecurity.

print("--- Example 1: Security Alert Level Classification ---")
# Classify a security alert based on its severity score.
# A higher score indicates higher severity.
alert_severity_score = 75  # Test with 95, 70, 45, 20, 100, 0

if alert_severity_score >= 90:
    print("CLASSIFICATION: CRITICAL - Immediate incident response required.")
    print("Action: Triggering automated containment measures.")
elif alert_severity_score >= 70:
    print("CLASSIFICATION: HIGH - Escalation to Tier 2 SOC team.")
    print("Action: Initiating detailed log analysis.")
elif alert_severity_score >= 40:
    print("CLASSIFICATION: MEDIUM - Review by Tier 1 analyst.")
    print("Action: Adding to investigation queue.")
else:
    print("CLASSIFICATION: LOW - Log for routine monitoring and historical analysis.")
    print("Action: No immediate action required.")
print("--- Alert classification complete. ---\n")


print("--- Example 2: Network Protocol Identification by Port ---")
# Identify common network protocols based on their standard port numbers.
scanned_network_port = 80  # Test with 22, 443, 21, 23, 53, 12345, 3389

if scanned_network_port == 22:
    print(f"Port {scanned_network_port}: SSH (Secure Shell) - Used for secure remote access.")
elif scanned_network_port == 80:
    print(f"Port {scanned_network_port}: HTTP (Hypertext Transfer Protocol) - Standard for web Browse.")
elif scanned_network_port == 443:
    print(f"Port {scanned_network_port}: HTTPS (HTTP Secure) - Encrypted web Browse.")
elif scanned_network_port == 21:
    print(f"Port {scanned_network_port}: FTP (File Transfer Protocol) - Used for file transfers (often insecure).")
elif scanned_network_port == 23:
    print(f"Port {scanned_network_port}: Telnet - Unencrypted remote command-line access (highly insecure).")
elif scanned_network_port == 53:
    print(f"Port {scanned_network_port}: DNS (Domain Name System) - Translates domain names to IP addresses.")
elif scanned_network_port == 3389:
    print(f"Port {scanned_network_port}: RDP (Remote Desktop Protocol) - Windows remote desktop access.")
else:
    print(f"Port {scanned_network_port}: Unrecognized or non-standard port. Requires further investigation.")
print("--- Network port identification complete. ---\n")


print("--- Example 3: User Access Level Based on Security Group ---")
# Assign different access levels based on a user's primary security group.
user_security_group = "developers"  # Test with "admin", "auditors", "guests", "engineers"

if user_security_group == "admin":
    print("Access Level: FULL ADMINISTRATOR - Unrestricted system access.")
    print("Warning: Requires multi-factor authentication and strict auditing.")
elif user_security_group == "developers":
    print("Access Level: DEVELOPMENT - Access to source code repositories and build environments.")
elif user_security_group == "auditors":
    print("Access Level: READ-ONLY AUDIT - Access to logs and compliance reports only.")
elif user_security_group == "guests":
    print("Access Level: LIMITED GUEST - Public network access only.")
else:
    print("Access Level: DEFAULT USER - Standard business application access.")
print("--- User access provisioning decision complete. ---\n")