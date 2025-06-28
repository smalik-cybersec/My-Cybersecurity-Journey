# M07-L07 | 07 - Bitwise Operators

**Date:** 2025-06-28
---
### 1. Definition & Core Concept
> Bitwise operators act directly on the individual bits (binary digits) of integers, allowing for low-level manipulation of data.

When applied, Python converts the numbers to their binary representation, performs the operation on each corresponding bit, and then converts the result back into an integer. Understanding binary is essential for mastering these operators.

---
### 2. Why It Matters (The Cybersecurity Context)
* **Relevance:** Bitwise operations are fundamental for low-level data manipulation, network protocol parsing, and understanding cryptographic primitives, making them indispensable for advanced cybersecurity programming.
* **Use-Case 1:** **Network Protocol Parsing and Crafting:** Network protocols often define flags and data fields at the bit level. Bitwise `AND` (`&`) is used to extract specific flags (e.g., checking if a SYN flag is set in a TCP header), while `OR` (`|`) is used to set flags or combine header values. Shifts (`<<`, `>>`) are vital for packing and unpacking values within bytes/words.
* **Use-Case 2:** **Basic Cryptography and Obfuscation:** The Bitwise `XOR` (`^`) operator is a core component in many cryptographic algorithms (like stream ciphers or block ciphers such as AES) due to its property of self-invertibility (`A ^ B ^ B = A`). It's also used for simple data obfuscation.
* **Use-Case 3:** **Malware Analysis and Reverse Engineering:** When analyzing binary executables or shellcode, security researchers often use bitwise operations to inspect, modify, or extract specific patterns, flags, or embedded data directly from the binary stream.
* **Use-Case 4:** **Permission and Flag Management:** Many systems represent permissions (e.g., read, write, execute) as a bitmask. Bitwise operators allow for efficient checking, setting, and clearing of these individual permissions within a single integer.

---
### 3. Syntax & Practical Implementation
#### Annotated Example:
```python
# Example values in decimal and their 4-bit binary representation (for simplicity)
# 6  -> 0110
# 3  -> 0011
# 12 -> 1100
# 7  -> 0111
# 5  -> 0101
# 24 -> 11000

a = 6  # Binary: 0110
b = 3  # Binary: 0011
c = 12 # Binary: 1100
d = 7  # Binary: 0111

print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})")
print(f"c = {c} (binary: {bin(c)})")
print(f"d = {d} (binary: {bin(d)})\n")


# 1. Bitwise AND (&)
# Result bit is 1 if BOTH corresponding bits are 1.
# 0110 & 0011 = 0010 (2)
result_and = a & b
print(f"a & b ({bin(a)} & {bin(b)}): {result_and} (binary: {bin(result_and)})")

# 2. Bitwise OR (|)
# Result bit is 1 if AT LEAST ONE corresponding bit is 1.
# 0110 | 0011 = 0111 (7)
result_or = a | b
print(f"a | b ({bin(a)} | {bin(b)}): {result_or} (binary: {bin(result_or)})")

# 3. Bitwise XOR (^)
# Result bit is 1 if corresponding bits are DIFFERENT.
# 0110 ^ 0011 = 0101 (5)
result_xor = a ^ b
print(f"a ^ b ({bin(a)} ^ {bin(b)}): {result_xor} (binary: {bin(result_xor)})")

# 4. Bitwise NOT (~)
# Inverts all bits. Python uses two's complement, so ~x = -(x + 1).
result_not_a = ~a
print(f"~a (~{bin(a)}): {result_not_a}") # Expected: ~6 = -7

# 5. Left Shift (<<)
# Shifts bits left by n positions, filling with zeros on the right. Equivalent to x * (2**n).
# 0110 (6) << 2 -> 110000 (24)
result_lshift = a << 2
print(f"a << 2 ({bin(a)} << 2): {result_lshift} (binary: {bin(result_lshift)})")

# 6. Right Shift (>>)
# Shifts bits right by n positions, filling with zeros on the left (for positive numbers). Equivalent to x // (2**n).
# 1100 (12) >> 2 -> 0011 (3)
result_rshift = c >> 2
print(f"c >> 2 ({bin(c)} >> 2): {result_rshift} (binary: {bin(result_rshift)})")

# Practical Example: Manipulating Permissions (using bitmasks)
# Define constant masks for different permissions
PERMISSION_READ  = 0b001 # 1
PERMISSION_WRITE = 0b010 # 2
PERMISSION_EXEC  = 0b100 # 4

# Simulate a user's current permissions (e.g., only read and execute)
user_perms = PERMISSION_READ | PERMISSION_EXEC # 001 | 100 = 101 (5)
print(f"\nUser's initial permissions: {user_perms} (binary: {bin(user_perms)})")

# Check if user has WRITE permission using AND
has_write_access = (user_perms & PERMISSION_WRITE) != 0
print(f"Does user have WRITE access? {has_write_access}") # Expected: False

# Grant user WRITE permission using OR
user_perms |= PERMISSION_WRITE # Add 010 to current 101 -> 111 (7)
print(f"User's permissions after granting WRITE: {user_perms} (binary: {bin(user_perms)})")

# Check again if user has WRITE permission
has_write_access_now = (user_perms & PERMISSION_WRITE) != 0
print(f"Does user have WRITE access now? {has_write_access_now}") # Expected: True