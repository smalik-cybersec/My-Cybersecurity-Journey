# M04-L03 | Dynamic Typing with type() Function

**Date:** 2025-06-27
---
### 1. Definition & Core Concept
> Python is a **dynamically typed language**, meaning variable types are determined at runtime based on the value assigned, rather than being explicitly declared by the programmer.

In Python, you don't declare a variable's type before using it (e.g., `int x;`). Instead, Python automatically infers the data type when a value is assigned. A key characteristic of dynamic typing is that a single variable can hold values of different data types throughout its execution, adapting its type based on the last assigned value. The built-in `type()` function is used to inspect the current type of a variable.

---
### 2. Why It Matters (The Cybersecurity Context)
* **Relevance:** Dynamic typing offers significant flexibility and speeds up development, which is highly beneficial in agile cybersecurity operations where rapid prototyping and adaptation to new data formats are common.
* **Use-Case 1:** **Flexible Data Ingestion:** When writing parsers for diverse security logs (e.g., firewall logs, web server access logs, endpoint detection logs), the format and types of fields can vary. Dynamic typing allows your Python script to ingest these varied data points (which might come in as strings) and automatically infer their types, or allow you to explicitly convert them as needed, without rigid pre-declarations. This simplifies handling heterogeneous security data.
* **Use-Case 2:** **API Interaction & Data Processing:** Interacting with security APIs (e.g., threat intelligence platforms, SIEMs) often involves receiving JSON or XML responses where data types might not be strictly consistent or fully known beforehand. Dynamic typing allows you to directly work with the parsed data, which Python often represents as dictionaries and lists, without complex type mapping. You can then dynamically check types with `type()` and perform conversions if specific operations require it.

---
### 3. Syntax & Practical Implementation
The `type()` function is your primary tool for understanding the current data type of a variable in a dynamically typed environment.

#### Annotated Example:
```python
# M04-L03-Dynamic_Typing_Example.py

# --- Demonstrating Dynamic Typing ---

# 1. Initial assignment: 'security_data' is an integer
security_data = 12345
print(f"Variable: 'security_data', Value: {security_data}, Initial Type: {type(security_data)}")

# 2. Reassignment: 'security_data' changes to a string
security_data = "CVE-2023-9876"
print(f"Variable: 'security_data', Value: '{security_data}', New Type: {type(security_data)}")

# 3. Another reassignment: 'security_data' changes to a list
security_data = ["IP: 192.168.1.1", "Port: 80", "Status: Open"]
print(f"Variable: 'security_data', Value: {security_data}, New Type: {type(security_data)}")

# 4. Final reassignment: 'security_data' changes to a boolean
security_data = False
print(f"Variable: 'security_data', Value: {security_data}, Final Type: {type(security_data)}")

print("-" * 30)

# --- Handling user input (common dynamic typing scenario) ---

# User input is always read as a string by default
user_input_attempts = input("Enter number of failed login attempts: ")
print(f"User Input Value: '{user_input_attempts}', Type: {type(user_input_attempts)}")

# Attempting arithmetic directly on string input will cause an error
# failed_attempts_numeric = user_input_attempts + 5 # This would raise a TypeError

# Best practice: Explicitly convert when a numeric type is required
try:
    failed_attempts_numeric = int(user_input_attempts)
    print(f"Numeric Value: {failed_attempts_numeric}, Type: {type(failed_attempts_numeric)}")
    print(f"Failed attempts plus 5: {failed_attempts_numeric + 5}")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")

print("-" * 30)

# --- Conditional logic based on type ---
def process_security_event(event_data):
    if isinstance(event_data, str):
        print(f"Processing string event: {event_data.upper()}")
    elif isinstance(event_data, int):
        print(f"Processing integer event (e.g., event ID): {event_data * 10}")
    elif isinstance(event_data, list):
        print(f"Processing list of events: {', '.join(event_data)}")
    else:
        print(f"Unknown event type: {type(event_data)}")

process_security_event("malware_detected")
process_security_event(1024)
process_security_event(["alert", "critical", "compromise"])
process_security_event({"user": "guest"}) # This will hit the 'else' case