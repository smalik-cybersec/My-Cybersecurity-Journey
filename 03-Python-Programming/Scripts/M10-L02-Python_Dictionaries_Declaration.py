"""
Script to demonstrate various methods of declaring and initializing Python dictionaries.

This script illustrates the use of dictionary literals (curly braces), the dict() constructor
with different arguments (empty, keyword arguments, and from iterables), and dictionary
comprehensions. It provides practical examples relevant to cybersecurity data handling.

Args:
    None: This script does not accept any command-line arguments.

Returns:
    None: This script prints dictionary creation examples and their outputs to the console.
"""

def demonstrate_dictionary_declaration():
    """
    Demonstrates different ways to declare and initialize Python dictionaries.
    """
    print("--- Python Dictionary Declaration Methods ---")

    # 1. Using Curly Braces {} (Dictionary Literal)
    print("\n1. Declaring Dictionaries using Curly Braces {} (Literal)")
    # Example 1.1: An empty dictionary for future data collection
    empty_packet_data = {}
    print(f"  Empty packet data: {empty_packet_data}")

    # Example 1.2: A dictionary representing a static threat actor profile
    threat_actor_profile = {
        "actor_name": "Fancy Bear",
        "aliases": ["APT28", "STRONTIUM"],
        "origin": "Russia",
        "primary_motivations": ["Espionage", "Disruption"]
    }
    print(f"  Threat Actor Profile: {threat_actor_profile}")
    print(f"  Type of threat_actor_profile: {type(threat_actor_profile)}")

    # 2. Using the dict() Constructor
    print("\n2. Declaring Dictionaries using the dict() Constructor")

    # Example 2.1: Empty dictionary using dict()
    empty_vulnerability_list = dict()
    print(f"  Empty vulnerability list (dict()): {empty_vulnerability_list}")

    # Example 2.2: From keyword arguments (keys become strings)
    # Useful for representing a simple event record
    security_event_record = dict(
        event_id=1001,
        event_type="Authentication Success",
        username="john.doe",
        source_ip="192.168.5.10"
    )
    print(f"  Security Event Record (keywords): {security_event_record}")

    # Example 2.3: From an iterable of key-value pairs (list of tuples)
    # Common when parsing structured text or API responses
    parsed_header_fields = [
        ("Host", "example.com"),
        ("Connection", "keep-alive"),
        ("Content-Length", "123")
    ]
    http_request_headers = dict(parsed_header_fields)
    print(f"  HTTP Request Headers (list of tuples): {http_request_headers}")

    # Example 2.4: From an iterable of key-value pairs (list of lists)
    # Simulating data parsed from a log file where each sub-list is a field
    log_line_parsed_data = [
        ['timestamp', '2025-06-29 11:30:00'],
        ['process_id', '5678'],
        ['action', 'file_access'],
        ['file_path', '/etc/passwd']
    ]
    detailed_log_entry = dict(log_line_parsed_data)
    print(f"  Detailed Log Entry (list of lists): {detailed_log_entry}")

    # 3. Using Dictionary Comprehensions
    print("\n3. Declaring Dictionaries using Dictionary Comprehensions")

    # Example 3.1: Mapping a list of network protocols to their common port status
    network_protocols = ["TCP", "UDP", "ICMP", "SSH", "HTTP"]
    protocol_status = {proto: "Enabled" for proto in network_protocols}
    print(f"  Protocol Status (comprehension): {protocol_status}")

    # Example 3.2: Creating a dictionary of active users with default roles
    user_list = ["alice", "bob", "charlie"]
    active_user_roles = {user: "User" for user in user_list}
    # Modify one role for demonstration
    active_user_roles["alice"] = "Administrator"
    print(f"  Active User Roles (comprehension + update): {active_user_roles}")

    # Example 3.3: Filter and transform existing data
    # Imagine a list of vulnerability objects, we want a dict of only critical ones
    all_vulnerabilities = [
        {"id": "CVE-2023-001", "severity": "High", "status": "Active"},
        {"id": "CVE-2023-002", "severity": "Low", "status": "Closed"},
        {"id": "CVE-2023-003", "severity": "Critical", "status": "Active"}
    ]
    critical_active_vulnerabilities = {
        vuln["id"]: vuln["severity"]
        for vuln in all_vulnerabilities
        if vuln["severity"] == "Critical" and vuln["status"] == "Active"
    }
    print(f"  Critical Active Vulnerabilities (comprehension with filter): {critical_active_vulnerabilities}")


if __name__ == "__main__":
    demonstrate_dictionary_declaration()