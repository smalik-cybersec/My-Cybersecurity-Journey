# Script: Password Complexity Checker

**Date:** 2025-06-28
---
### 1. Overview
> This script implements a basic password complexity checker, evaluating a given password against several common security requirements.

Its purpose is to demonstrate the practical application of various Python operators (comparison, logical, membership) in building a foundational security utility. The script checks for length, presence of different character types (uppercase, lowercase, digit, special), and absence of common weak passwords.

---
### 2. How it Works (Technical Details)
* **Core Logic:** The `check_password_complexity` function takes a password string as input. It first performs a length check. If the password meets the minimum length, it then iterates through each character to determine if it contains uppercase letters, lowercase letters, digits, and special characters. Finally, it checks if the lowercase version of the password is present in a predefined list of common weak passwords.
* **Operators Used & Why:**
    * **Comparison Operators (`>=`, `<=`)**: Used for the length check (`len(password) >= min_length`) and for character type range checks (e.g., `'A' <= char <= 'Z'`).
    * **Logical Operators (`and`, `or`, `not`)**: Crucial for combining multiple Boolean conditions, such as `has_uppercase and has_lowercase and has_digit and has_special` to ensure all character types are present. Also implicitly used in `if password.lower() in common_bad_passwords` where a `True` result dictates the flow.
    * **Membership Operators (`in`, `not in`)**: Used extensively for:
        * Checking if a character is within the `special_characters` string (`char in special_characters`).
        * Determining if the password (converted to lowercase) is present in the `common_bad_passwords` list (`password.lower() in common_bad_passwords`).
* **Key Functions/Components:**
    * `check_password_complexity(password)`: The main function encapsulating all validation logic.
    * `len()`: Built-in function to get the length of the password string.
    * `.lower()`: String method used to convert the password to lowercase for case-insensitive comparison against common weak passwords.

---
### 3. Usage
```bash
python3 M07-Small_Challenge_Password_Complexity_Checker.py