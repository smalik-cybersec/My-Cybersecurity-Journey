# M07-L02 | 02 - Arithmetic Operators

**Date:** 2025-06-28
---
### 1. Definition & Core Concept
> Arithmetic operators are symbols that perform mathematical calculations on numerical values.

These are the most fundamental operators, allowing you to carry out standard mathematical operations like addition, subtraction, multiplication, division, and more advanced operations like exponentiation and modulo. They are the backbone of any numerical processing in Python.

---
### 2. Why It Matters (The Cybersecurity Context)
* **Relevance:** Arithmetic operators are critical for processing numerical data encountered in various cybersecurity tasks, from calculating data sizes to cryptographic operations.
* **Use-Case 1:** **Packet Manipulation and Checksums:** When dealing with network protocols, you might use arithmetic operators to calculate header lengths, data offsets, or even rudimentary checksums (though usually handled by libraries, understanding the underlying math is key) to verify data integrity. For example, summing byte values and using the modulus operator (`%`) could be part of a simple checksum algorithm.
* **Use-Case 2:** **Basic Cryptographic Concepts & Data Analysis:** While complex cryptography relies on sophisticated algorithms, some fundamental concepts (like modular arithmetic in RSA or key derivation processes) involve addition, multiplication, and especially modulus and exponentiation. In data analysis for security, these operators are used for calculating statistics like averages of attack attempts, standard deviations of network traffic, or success rates of exploits.

---
### 3. Syntax & Practical Implementation
#### Annotated Example:
```python
# Declare some variables for demonstration
num_a = 25
num_b = 7

print(f"Numbers: num_a = {num_a}, num_b = {num_b}\n")

# 1. Addition (+)
# Adds the values of two operands.
result_add = num_a + num_b
print(f"Addition (num_a + num_b): {result_add}") # Expected: 32

# 2. Subtraction (-)
# Subtracts the right operand from the left.
result_sub = num_a - num_b
print(f"Subtraction (num_a - num_b): {result_sub}") # Expected: 18

# 3. Multiplication (*)
# Multiplies the values of two operands.
result_mul = num_a * num_b
print(f"Multiplication (num_a * num_b): {result_mul}") # Expected: 175

# 4. Division (/)
# Divides the left operand by the right. Always returns a float.
result_div = num_a / num_b
print(f"Division (num_a / num_b): {result_div}") # Expected: 3.5714...

# 5. Floor Division (//)
# Divides the left operand by the right and returns the integer portion of the quotient.
result_floor_div = num_a // num_b
print(f"Floor Division (num_a // num_b): {result_floor_div}") # Expected: 3 (integer part of 3.57...)

# 6. Modulus (%)
# Returns the remainder of the division. Useful for checking divisibility or cyclical operations.
result_mod = num_a % num_b
print(f"Modulus (num_a % num_b): {result_mod}") # Expected: 4 (25 = 3*7 + 4)

# 7. Exponentiation (**)
# Raises the left operand to the power of the right operand.
result_exp = 2 ** 5 # 2 to the power of 5 (2*2*2*2*2)
print(f"Exponentiation (2 ** 5): {result_exp}") # Expected: 32