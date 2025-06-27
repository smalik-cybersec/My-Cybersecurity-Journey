# M05-L03 | Multiple Variable Declaration

**Date:** 2025-06-27
---
### 1. Definition & Core Concept
> Python allows for the assignment of values to multiple variables in a single line, enhancing code conciseness and readability through methods like simultaneous assignment and unpacking.


---
### 2. Why It Matters (The Cybersecurity Context)
* **Relevance:** Efficient variable declaration is crucial for writing compact and clear cybersecurity scripts, particularly when dealing with configurations, parsing data, or managing states.
* **Use-Case 1:** Initializing multiple flags or counters. In a network monitoring script, you might initialize several status flags to `False` at the beginning: `port_open = host_reachable = scan_completed = False`. This is cleaner than three separate lines.
* **Use-Case 2:** Parsing structured data. When processing logs or network packets, you often extract multiple pieces of information simultaneously. For instance, if a log line consistently provides `(timestamp, source_ip, event_type)`, you can use `ts, src_ip, event = parse_log_entry(line)` to unpack these values directly, making the code more readable and direct for incident response or forensics tools.

---
### 3. Syntax & Practical Implementation
#### Annotated Example:
```python
# 1. Assigning the same value to multiple variables:
# Useful for initializing multiple variables to a default state or value.
threat_level = alert_triggered = False
print(f"Initial State -> Threat Level: {threat_level}, Alert Triggered: {alert_triggered}")

# Simulate an event
threat_level = True
print(f"After Event -> Threat Level: {threat_level}, Alert Triggered: {alert_triggered}") # alert_triggered is still False


# 2. Assigning different values to multiple variables (unpacking):
# The number of variables on the left must match the number of values on the right.
source_ip, dest_port, protocol = "192.168.1.10", 80, "TCP"
print(f"Connection details: Source IP: {source_ip}, Destination Port: {dest_port}, Protocol: {protocol}")

# Common use-case: Swapping variable values
value_a = 100
value_b = 200
print(f"Before swap: A={value_a}, B={value_b}")
value_a, value_b = value_b, value_a # Pythonic way to swap without a temporary variable
print(f"After swap: A={value_a}, B={value_b}")

# Unpacking from a list or tuple (common in data processing)
scanner_config = ["Nmap", "192.168.1.0/24", ["80", "443", "22"]]
tool, target_range, ports = scanner_config
print(f"Tool: {tool}, Target Range: {target_range}, Ports to Scan: {ports}")