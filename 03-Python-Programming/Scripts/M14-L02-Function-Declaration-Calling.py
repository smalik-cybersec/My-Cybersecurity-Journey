# M14-L02-Function-Declaration-Calling.py
#
# Module: 14 - Functions
# Lesson: 02 - Declaration and Calling of Functions
#
# Description:
# This script demonstrates how to declare (define) and call functions in Python,
# including examples with no arguments, with arguments, and with return values.
# These concepts are fundamental for writing modular and reusable code in cybersecurity.
#
# Author: Your Name/Alias (Placeholder - Replace with your actual name/alias)
# Date: Current Date (e.g., June 30, 2025)
#
# Usage:
# Run this script directly from your terminal: python M14-L02-Function-Declaration-Calling.py
# Observe the output to understand function execution flow.

# --- Section 1: Function with no parameters and no return value ---

def display_simple_message():
    """
    Displays a generic informational message.
    This function takes no arguments and returns nothing.
    """
    print("\n--- Displaying Simple Message ---")
    print("This function demonstrates a basic call.")
    print("---------------------------------")

# Calling the function
print("Calling display_simple_message()...")
display_simple_message()


# --- Section 2: Function with parameters but no return value ---

def log_event(event_type, message):
    """
    Logs a simulated security event with a given type and message.
    This function takes two string arguments (event_type, message) and returns nothing.
    """
    print(f"\n--- Security Event Logged ---")
    print(f"Event Type: {event_type}")
    print(f"Message: {message}")
    print(f"Timestamp: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}") # Example of including a timestamp
    print(f"-----------------------------")

# Calling the function with different arguments
print("\nCalling log_event() for different security scenarios...")
log_event("Login Attempt", "User 'admin' failed login from 192.168.1.100")
log_event("File Access", "Unauthorized access attempt on /etc/shadow by user 'guest'")


# --- Section 3: Function with parameters and a return value ---

def calculate_hash(data_string, algorithm="sha256"):
    """
    Calculates the cryptographic hash of a given string using a specified algorithm.
    Defaults to SHA256 if no algorithm is provided.

    Args:
        data_string (str): The input string to hash.
        algorithm (str): The hashing algorithm to use (e.g., "md5", "sha256", "sha512").

    Returns:
        str: The hexadecimal representation of the calculated hash, or an error message.
    """
    import hashlib # Import hashlib module inside the function (or at top) for specific use

    try:
        if algorithm.lower() == "md5":
            hasher = hashlib.md5()
        elif algorithm.lower() == "sha256":
            hasher = hashlib.sha256()
        elif algorithm.lower() == "sha512":
            hasher = hashlib.sha512()
        else:
            return "Error: Unsupported hashing algorithm."

        hasher.update(data_string.encode('utf-8'))
        return hasher.hexdigest()
    except Exception as e:
        return f"An error occurred during hashing: {e}"

# Calling the function and using its return value
print("\n--- Demonstrating Hashing Function ---")
file_content = "This is a sensitive configuration file content."
file_hash_sha256 = calculate_hash(file_content, "sha256")
print(f"Content: '{file_content}'")
print(f"SHA256 Hash: {file_hash_sha256}")

password_candidate = "MySecurePassword123!"
password_hash_md5 = calculate_hash(password_candidate, "md5")
print(f"Password Candidate: '{password_candidate}'")
print(f"MD5 Hash: {password_hash_md5}")

unsupported_hash = calculate_hash("test", "unknown")
print(f"Unsupported algorithm test: {unsupported_hash}")

print("\nScript execution complete.")