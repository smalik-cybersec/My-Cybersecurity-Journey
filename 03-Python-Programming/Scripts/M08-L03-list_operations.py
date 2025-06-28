# M08-L03-list_operations.py

"""
Module 08: Python Lists - Functions and Methods Demonstration

This script demonstrates various built-in list methods and functions in Python.
Understanding these operations is crucial for dynamic data manipulation
in cybersecurity and general programming tasks.
"""

print("--- Module 08: Python Lists - Functions and Methods Demonstration ---")
print("\n--- 1. List Declaration and Initial State ---")
# Initializing an empty list
my_list = []
print(f"Initial empty list: {my_list}")

# Initializing a list with some values
security_tasks = ["reconnaissance", "scanning", "enumeration"]
print(f"Initial security tasks: {security_tasks}")

# List with mixed data types
mixed_data = ["alert", 101, True, 2025.5]
print(f"Mixed data list: {mixed_data}")


print("\n--- 2. Adding Elements to a List ---")

# append(item): Adds a single item to the end
security_tasks.append("exploitation")
print(f"After append('exploitation'): {security_tasks}")
# Expected: ['reconnaissance', 'scanning', 'enumeration', 'exploitation']

# extend(iterable): Adds all items from an iterable to the end
more_tasks = ["post-exploitation", "reporting"]
security_tasks.extend(more_tasks)
print(f"After extend(['post-exploitation', 'reporting']): {security_tasks}")
# Expected: ['reconnaissance', 'scanning', 'enumeration', 'exploitation', 'post-exploitation', 'reporting']

# insert(index, item): Inserts an item at a specified index
security_tasks.insert(1, "passive_info_gathering") # Insert at index 1
print(f"After insert(1, 'passive_info_gathering'): {security_tasks}")
# Expected: ['reconnaissance', 'passive_info_gathering', 'scanning', ..., 'reporting']


print("\n--- 3. Removing Elements from a List ---")

# remove(item): Removes the first occurrence of the specified value
# Let's add a duplicate for demonstration
security_tasks.append("scanning")
print(f"List before remove (with duplicate): {security_tasks}")
security_tasks.remove("scanning") # Removes the first 'scanning'
print(f"After remove('scanning'): {security_tasks}")
# Expected: The first 'scanning' is gone, the second might remain if present

# pop(index=-1): Removes and returns the item at the specified index (default last)
removed_task = security_tasks.pop() # Removes 'scanning' (the last one appended)
print(f"Popped last item ('{removed_task}'): {security_tasks}")
# Expected: 'reporting' removed if it was last. If not, the last item.

if security_tasks: # Check if list is not empty before popping by index
    removed_specific_task = security_tasks.pop(0) # Removes the first item
    print(f"Popped item at index 0 ('{removed_specific_task}'): {security_tasks}")
    # Expected: 'reconnaissance' removed

# clear(): Removes all items from the list
temp_list = [1, 2, 3]
print(f"Before clear: {temp_list}")
temp_list.clear()
print(f"After clear: {temp_list}")
# Expected: []

# del statement: Deletes items by index or slice, or the entire list object
network_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4"]
print(f"Original network IPs: {network_ips}")
del network_ips[1] # Deletes "192.168.1.2"
print(f"After del network_ips[1]: {network_ips}")
# Expected: ['192.168.1.1', '192.168.1.3', '192.168.1.4']

del network_ips[1:] # Deletes from index 1 to the end
print(f"After del network_ips[1:]: {network_ips}")
# Expected: ['192.168.1.1']


print("\n--- 4. Accessing and Querying Elements ---")
vulnerability_scores = [7.5, 9.0, 5.0, 7.5, 8.0]

# Indexing []: Access single element
print(f"First score: {vulnerability_scores[0]}") # Expected: 7.5
print(f"Last score using negative index: {vulnerability_scores[-1]}") # Expected: 8.0

# Slicing [start:end:step]: Access sub-sections
print(f"Scores from index 1 to 3 (exclusive): {vulnerability_scores[1:4]}") # Expected: [9.0, 5.0, 7.5]
print(f"First three scores: {vulnerability_scores[:3]}") # Expected: [7.5, 9.0, 5.0]
print(f"Scores from index 2 onwards: {vulnerability_scores[2:]}") # Expected: [5.0, 7.5, 8.0]
print(f"Every second score: {vulnerability_scores[::2]}") # Expected: [7.5, 5.0, 8.0]
print(f"List reversed using slicing: {vulnerability_scores[::-1]}") # Expected: [8.0, 7.5, 5.0, 9.0, 7.5]

# index(item, start, end): Returns the index of the first occurrence
print(f"Index of first '7.5': {vulnerability_scores.index(7.5)}") # Expected: 0
# Find index of 7.5 starting from index 1
print(f"Index of '7.5' starting from index 1: {vulnerability_scores.index(7.5, 1)}") # Expected: 3

# count(item): Returns the number of times an item appears
print(f"Count of '7.5': {vulnerability_scores.count(7.5)}") # Expected: 2

# len(list) (built-in function): Returns the number of items
print(f"Number of scores: {len(vulnerability_scores)}") # Expected: 5

# 'in' membership operator: Checks if an item exists
print(f"Is 9.0 in scores? {'9.0' in vulnerability_scores}") # Expected: False (type mismatch)
print(f"Is 9.0 (float) in scores? {9.0 in vulnerability_scores}") # Expected: True
print(f"Is 6.0 in scores? {6.0 in vulnerability_scores}") # Expected: False


print("\n--- 5. Reordering and Copying Lists ---")

# sort(): Sorts the list in-place
unsorted_ports = [80, 22, 443, 21, 53]
print(f"Before sort: {unsorted_ports}")
unsorted_ports.sort()
print(f"After sort (in-place): {unsorted_ports}")
# Expected: [21, 22, 53, 80, 443]

# sort(reverse=True): Sorts in descending order
unsorted_ports_desc = [80, 22, 443, 21, 53]
unsorted_ports_desc.sort(reverse=True)
print(f"After sort(reverse=True): {unsorted_ports_desc}")
# Expected: [443, 80, 53, 22, 21]

# sorted(iterable) (built-in function): Returns a *new* sorted list
original_data = [100, 50, 200, 25]
new_sorted_data = sorted(original_data)
print(f"Original data: {original_data}") # Unchanged
print(f"New sorted data: {new_sorted_data}")
# Expected: Original data: [100, 50, 200, 25], New sorted data: [25, 50, 100, 200]

# reverse(): Reverses the order of elements in-place
log_entries = ["Login success", "Attempted login", "Failed login"]
print(f"Before reverse: {log_entries}")
log_entries.reverse()
print(f"After reverse (in-place): {log_entries}")
# Expected: ['Failed login', 'Attempted login', 'Login success']

# copy(): Returns a shallow copy of the list
original_ioc_list = ["malicious_ip", "phishing_domain", "bad_hash"]
copied_ioc_list = original_ioc_list.copy()
copied_ioc_list.append("new_ioc")
print(f"Original IOC list: {original_ioc_list}") # Unchanged
print(f"Copied IOC list (modified): {copied_ioc_list}")
# Expected: Original: ['malicious_ip', 'phishing_domain', 'bad_hash']
#           Copied: ['malicious_ip', 'phishing_domain', 'bad_hash', 'new_ioc']


print("\n--- 6. Other Useful Built-in Functions with Lists ---")

numbers_for_calc = [10, 20, 5, 30]

# min(list): Returns the item with the lowest value
print(f"Minimum value: {min(numbers_for_calc)}") # Expected: 5

# max(list): Returns the item with the highest value
print(f"Maximum value: {max(numbers_for_calc)}") # Expected: 30

# sum(list): Returns the sum of all numerical items
print(f"Sum of values: {sum(numbers_for_calc)}") # Expected: 65

print("\n--- End of List Operations Demonstration ---")