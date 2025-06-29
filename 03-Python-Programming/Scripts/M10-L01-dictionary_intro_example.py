"""
A basic script to demonstrate the introduction and fundamental usage of Python dictionaries.

This script initializes a simple dictionary to represent cybersecurity-related information
(e.g., a simplified vulnerability record) and demonstrates how to access its elements
using keys. It serves as a foundational example for understanding dictionary structure.

Args:
    None: This script does not accept any command-line arguments.

Returns:
    None: This script prints dictionary contents to the console.
"""

def main():
    """
    Main function to execute the dictionary introduction example.
    """
    # Define a dictionary to represent a simplified vulnerability record
    vulnerability_record = {
        "vulnerability_id": "CVE-2023-12345",
        "description": "SQL Injection vulnerability in web application login.",
        "severity": "High",
        "cve_score": 9.8,
        "affected_product": "WebApp v1.0",
        "status": "Detected"
    }

    print("--- Vulnerability Record Details ---")
    # Access and print individual values using their keys
    print(f"Vulnerability ID: {vulnerability_record['vulnerability_id']}")
    print(f"Description: {vulnerability_record['description']}")
    print(f"Severity: {vulnerability_record['severity']}")
    print(f"CVSS Score: {vulnerability_record['cve_score']}")

    # Demonstrating how to add a new key-value pair
    vulnerability_record["remediation_status"] = "Pending Patch"
    print(f"Remediation Status: {vulnerability_record['remediation_status']}")

    # Demonstrating how to modify an existing value
    vulnerability_record["status"] = "Under Review"
    print(f"Updated Status: {vulnerability_record['status']}")

    print("\n--- Full Vulnerability Record (after updates) ---")
    # Iterate through and print all key-value pairs
    for key, value in vulnerability_record.items():
        # Enhance readability by capitalizing and replacing underscores in keys
        print(f"{key.replace('_', ' ').title()}: {value}")

if __name__ == "__main__":
    main()