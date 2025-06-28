# password_checker.py

def check_password_complexity(password):
    """
    Checks if a password meets basic complexity requirements using various operators.
    Requirements:
    - At least 8 characters long (Comparison)
    - Contains at least one uppercase letter (Membership, Logical)
    - Contains at least one lowercase letter (Membership, Logical)
    - Contains at least one digit (Membership, Logical)
    - Contains at least one special character (e.g., !@#$%^&*) (Membership, Logical)
    - Does NOT contain common, easily guessed words (Membership, Logical)
    """
    min_length = 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()-_+="
    common_bad_passwords = ["password", "123456", "qwerty", "admin", "guest"]

    # 1. Check Length (Comparison Operator)
    if len(password) >= min_length:
        print(f"Length check passed ({len(password)} >= {min_length}).")
    else:
        print(f"Length check FAILED (min {min_length} chars needed).")
        return False # Fail early if length is too short

    # 2. Check Character Types (Membership & Logical Operators)
    for char in password:
        if 'A' <= char <= 'Z': # Comparison operators
            has_uppercase = True
        if 'a' <= char <= 'z': # Comparison operators
            has_lowercase = True
        if '0' <= char <= '9': # Comparison operators
            has_digit = True
        if char in special_characters: # Membership operator
            has_special = True

    if has_uppercase and has_lowercase and has_digit and has_special: # Logical operators
        print("Character type variety check passed (uppercase, lowercase, digit, special).")
    else:
        print("Character type variety check FAILED (need uppercase, lowercase, digit, and special).")
        print(f"  Uppercase: {has_uppercase}, Lowercase: {has_lowercase}, Digit: {has_digit}, Special: {has_special}")
        return False

    # 3. Check for Common Bad Passwords (Membership & Logical Operators)
    # Convert password to lowercase for case-insensitive check against common bad words
    if password.lower() in common_bad_passwords: # Membership operator
        print("Common word check FAILED (password contains a common, easily guessed word).")
        return False
    else:
        print("Common word check passed (no common, easily guessed words detected).")

    print("\nPassword meets complexity requirements!")
    return True

# --- Test Cases ---
print("--- Testing Passwords ---\n")

print("Test Case 1: Too short")
check_password_complexity("Short1!")
print("-" * 30)

print("Test Case 2: No special character")
check_password_complexity("MyStrongPass123")
print("-" * 30)

print("Test Case 3: Common word")
check_password_complexity("Password123!")
print("-" * 30)

print("Test Case 4: Strong password")
check_password_complexity("S3cur3P@ssw0rd!")
print("-" * 30)

print("Test Case 5: Another strong password")
check_password_complexity("L0gM3InN0w%")
print("-" * 30)