# M07-L04 | 04 - Comparison Operators

**Date:** 2025-06-28
---
### 1. Definition & Core Concept
> Comparison (or Relational) operators are used to compare two values, yielding a Boolean result (`True` or `False`).

These operators are fundamental for making decisions in programming. They evaluate whether a relationship between two operands holds true or false, providing the logical basis for conditional statements and control flow in any Python program.

---
### 2. Why It Matters (The Cybersecurity Context)
* **Relevance:** Comparison operators are the backbone of decision-making logic in cybersecurity scripts, enabling programs to react dynamically to various conditions, identify anomalies, and enforce policies.
* **Use-Case 1:** **Conditional Execution in Security Tools:** Used extensively in `if`/`elif`/`else` statements to control program flow based on security checks. For example, `if port_status == "OPEN":` or `if len(password) < 8:`.
* **Use-Case 2:** **Vulnerability Detection & Log Analysis:** Comparing software versions (`if installed_version < patched_version:`), checking if a hash matches a known malicious one (`if computed_hash != expected_hash:`), or filtering log entries based on severity levels (`if event_level >= "WARNING":`) are common applications.
* **Use-Case 3:** **Access Control Logic:** While not directly implementing operating system ACLs, scripts that manage or audit user permissions might use comparisons to check if a user's role `==` "admin" or if their privileges `in` allowed_privileges.

---
### 3. Syntax & Practical Implementation
#### Annotated Example:
```python
# Variables for comparison
num1 = 50
num2 = 75
num3 = 50
text1 = "password123"
text2 = "Password123" # Different due to case
text3 = "password123"


print(f"Comparing: num1={num1}, num2={num2}, num3={num3}")
print(f"Comparing strings: text1='{text1}', text2='{text2}', text3='{text3}'\n")

# 1. Equal to (==)
# Checks if the values of two operands are equal.
print(f"num1 == num2: {num1 == num2}") # Expected: False
print(f"num1 == num3: {num1 == num3}") # Expected: True
print(f"text1 == text2: {text1 == text2}") # Expected: False (case sensitive)
print(f"text1 == text3: {text1 == text3}") # Expected: True

# 2. Not Equal to (!=)
# Checks if the values of two operands are not equal.
print(f"num1 != num2: {num1 != num2}") # Expected: True
print(f"num1 != num3: {num1 != num3}") # Expected: False

# 3. Greater Than (>)
# Checks if the left operand is greater than the right.
print(f"num2 > num1: {num2 > num1}") # Expected: True
print(f"num1 > num2: {num1 > num2}") # Expected: False

# 4. Less Than (<)
# Checks if the left operand is less than the right.
print(f"num1 < num2: {num1 < num2}") # Expected: True
print(f"num2 < num1: {num2 < num1}") # Expected: False

# 5. Greater Than or Equal to (>=)
# Checks if the left operand is greater than or equal to the right.
print(f"num1 >= num3: {num1 >= num3}") # Expected: True
print(f"num2 >= num1: {num2 >= num1}") # Expected: True
print(f"num1 >= num2: {num1 >= num2}") # Expected: False

# 6. Less Than or Equal to (<=)
# Checks if the left operand is less than or equal to the right.
print(f"num1 <= num3: {num1 <= num3}") # Expected: True
print(f"num1 <= num2: {num1 <= num2}") # Expected: True
print(f"num2 <= num1: {num2 <= num1}") # Expected: False