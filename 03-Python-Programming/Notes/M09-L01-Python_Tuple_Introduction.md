# M09-L01 | Python Tuples: An Introduction

**Date:** 2025-06-28
---
### 1. Definition & Core Concept
> A tuple in Python is an ordered, immutable collection of items, allowing for duplicate members and heterogeneous data types.

Tuples are a fundamental data structure in Python, similar to lists but with one crucial difference: they are **immutable**. This means that once a tuple is created, its elements cannot be changed, added, or removed. They maintain the order of insertion, and elements can be accessed via indexing, just like strings or lists. Tuples can store a mix of different data types within the same collection.

---
### 2. Why It Matters (The Cybersecurity Context)
* **Relevance:** Tuples are ideal for storing data that should not be altered, ensuring data integrity. This immutability provides a level of security and reliability crucial in many cybersecurity scenarios.
* **Use-Case 1: Configuration Settings:** Storing critical, static configuration parameters (e.g., hardcoded API keys, server addresses, or allowed port ranges) that should not be accidentally modified during program execution. This helps prevent tampering with sensitive settings.
* **Use-Case 2: Representing Fixed Data Structures:** When you need to represent a fixed record, like IP address/port pairs (`("192.168.1.1", 8080)`) or credentials that are loaded once and shouldn't change. This ensures that the structure and values of such data remain consistent.
* **Use-Case 3: Function Return Values:** Functions can return multiple values as a tuple, which is then unpacked. This ensures that the set of returned values remains together and is treated as a single, unchangeable unit.

---
### 3. Syntax & Practical Implementation
#### Annotated Example:
```python
# 1. Basic Tuple Declaration
# Items are enclosed in parentheses ()
my_tuple = ("apple", "banana", "cherry")
print(f"My first tuple: {my_tuple}")

# 2. Tuple with mixed data types
mixed_tuple = ("user_admin", 12345, True, 3.14)
print(f"Mixed data type tuple: {mixed_tuple}")

# 3. Accessing elements (like lists, 0-indexed)
first_element = my_tuple[0]
print(f"First element of my_tuple: {first_element}")

# 4. Attempting to modify a tuple (will raise a TypeError)
try:
    my_tuple[0] = "orange"
except TypeError as e:
    print(f"Error attempting to modify tuple: {e}")

# 5. Tuple with a single item (requires a trailing comma)
single_item_tuple = ("hello",) # The comma is essential!
not_a_tuple = ("hello") # This is just a string
print(f"Single item tuple type: {type(single_item_tuple)}")
print(f"Not a tuple type: {type(not_a_tuple)}")

# 6. Tuples can contain mutable objects, but the references are immutable
# The list inside the tuple can be modified, but the tuple itself cannot be reassigned
mutable_inside_tuple = ("immutable_part", [1, 2, 3])
print(f"Original tuple with mutable object: {mutable_inside_tuple}")
mutable_inside_tuple[1].append(4) # This is allowed because the list itself is mutable
print(f"Modified list inside tuple: {mutable_inside_tuple}")
# mutable_inside_tuple[0] = "new_value" # This would still be a TypeError