# Module 12: Conditional Statements

## Lesson 05: If-Else Statement Practice Questions

### 1. Purpose of Practice Questions
This lesson provides hands-on practice with the `if-else` statement, encouraging the application of this dual-path conditional logic to common cybersecurity problems. Successfully completing these exercises will solidify your ability to implement binary decision-making in your Python scripts.

### 2. Practice Scenarios & Solutions

#### Scenario 1: User Role Authorization
**Problem:** Implement an access control mechanism where users are granted `admin` or `limited` access based on their role.

**Instructions:**
Write a Python script that takes `user_role` (string). If `user_role` is `"administrator"`, print `Access Granted: Administrator privileges.`. Otherwise, print `Access Granted: Limited user privileges.`.

**Solution Example:**
```python
user_role = "administrator" # Test with "guest", "user"

if user_role == "administrator":
    print("Access Granted: Administrator privileges.")
else:
    print("Access Granted: Limited user privileges.")
print("Authorization check complete.")


current_hour = 14 # Test with 8, 17, 18, 9

if 9 <= current_hour <= 17: # or (current_hour >= 9 and current_hour <= 17)
    print("Login Time: Normal business hours.")
else:
    print("Login Time: Suspicious (outside business hours). Review immediately.")
print("Login time analysis complete.")



