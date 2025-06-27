# 06-03-string_operations.py

print("--- Module 06: Strings - Lesson 03: All Functions with Examples ---\n")

# --- 1. Changing Case: lower(), upper(), capitalize(), title(), swapcase() ---
print("### 1. Changing Case Methods ###")
log_entry_raw = "ATTEMPTED login from 192.168.1.100 - INVALID CREDENTIALS"
print(f"Original Log Entry: {log_entry_raw}")

# Normalize to lowercase for easier keyword matching (e.g., 'invalid' vs 'INVALID')
normalized_log = log_entry_raw.lower()
print(f"lower(): {normalized_log}")

# Convert to uppercase for displaying important alerts or status messages
alert_message = normalized_log.upper()
print(f"upper(): {alert_message}")

# Capitalize the first letter (less common in direct security parsing, but good to know)
sentence = "this is a warning."
print(f"capitalize(): {sentence.capitalize()}")

# Title case for formatting reports or display names
report_title = "cyber incident response plan"
print(f"title(): {report_title.title()}")

# Swap case (rarely used in security, but demonstrates case manipulation)
mixed_case_data = "PaSsWoRd_FiLe"
print(f"swapcase(): {mixed_case_data.swapcase()}\n")


# --- 2. Stripping Whitespace: strip(), lstrip(), rstrip() ---
print("### 2. Stripping Whitespace Methods ###")
user_input = "  admin@example.com   \n" # Common with user input or parsed data
print(f"Original User Input (raw): '{user_input}'")

# Remove leading/trailing whitespace (including newlines, tabs)
cleaned_input = user_input.strip()
print(f"strip(): '{cleaned_input}'")

# Remove specific characters (e.g., common delimiters or unwanted symbols)
malformed_data = "###BAD_DATA$$$"
cleaned_malformed = malformed_data.strip('#$')
print(f"strip('#$'): '{cleaned_malformed}'")

# Remove only leading whitespace
leading_space = "   username_input"
print(f"lstrip(): '{leading_space.lstrip()}'")

# Remove only trailing whitespace
trailing_space = "password_input   "
print(f"rstrip(): '{trailing_space.rstrip()}'\n")


# --- 3. Searching and Finding: find(), rfind(), index(), rindex(), count(), startswith(), endswith() ---
print("### 3. Searching and Finding Methods ###")
log_line = "2025-06-27 10:30:15 - [ERROR] - User 'john_doe' from 192.168.1.5 failed login."

# Find the first occurrence of a substring
error_index = log_line.find("[ERROR]")
print(f"find('[ERROR]'): {error_index}") # Output: 22

# Find a substring that doesn't exist
no_match_index = log_line.find("SUCCESS")
print(f"find('SUCCESS'): {no_match_index}") # Output: -1 (important for conditional checks)

# Find from the right (useful for last occurrences, e.g., last delimiter in a path)
last_dot_index = "report.2025.txt".rfind('.')
print(f"rfind('.'): {last_dot_index}") # Output: 10

# index() vs find() - index() raises ValueError if not found
try:
    log_line.index("SUCCESS")
except ValueError as e:
    print(f"index('SUCCESS') error: {e}")

# Count occurrences of a substring (e.g., number of specific attacks in a string)
ip_address_segment_count = "192.168.1.100".count('.')
print(f"count('.'): {ip_address_segment_count}") # Output: 3

# Check if a log entry starts with a specific pattern (e.g., a timestamp)
starts_with_timestamp = log_line.startswith("2025-06")
print(f"startswith('2025-06'): {starts_with_timestamp}")

# Check if a file name ends with a specific extension
file_name = "malware.exe"
is_exe = file_name.endswith(".exe")
print(f"endswith('.exe'): {is_exe}\n")


# --- 4. Replacing: replace() ---
print("### 4. Replacing Method ###")
dirty_data = "This system has been compromised. Compromised again."

# Replace all occurrences of a substring
cleaned_data = dirty_data.replace("Compromised", "!!!ALERT!!!")
print(f"replace('Compromised', '!!!ALERT!!!'): {cleaned_data}")

# Replace only the first occurrence
single_replace = dirty_data.replace("Compromised", "!!!ALERT!!!", 1)
print(f"replace (first only): {single_replace}\n")


# --- 5. Splitting and Joining: split(), join() ---
print("### 5. Splitting and Joining Methods ###")
csv_data = "admin,john@example.com,active,2025-01-15"

# Split a CSV line into a list of elements
user_info = csv_data.split(',')
print(f"split(','): {user_info}") # Output: ['admin', 'john@example.com', 'active', '2025-01-15']

# Split a log message by whitespace (default behavior)
log_parts = "2025-06-27 INFO User logged in".split()
print(f"split() (whitespace): {log_parts}") # Output: ['2025-06-27', 'INFO', 'User', 'logged', 'in']

# Join a list of parts back into a string (e.g., reconstruct a path or a command)
path_elements = ['/var', 'log', 'apache2', 'access.log']
full_path = "/".join(path_elements)
print(f"join('/'): {full_path}") # Output: /var/log/apache2/access.log

# Joining with different separators
ip_segments = ['192', '168', '1', '1']
ip_address = ".".join(ip_segments)
print(f"join('.'): {ip_address}\n")


# --- 6. Checking Content: isalpha(), isdigit(), isalnum(), isspace(), islower(), isupper() ---
print("### 6. Checking Content Methods ###")

# Check if a username is purely alphabetic (input validation)
username_alpha = "john_doe" # Contains underscore, so false
username_alpha_only = "johndoe"
print(f"'john_doe'.isalpha(): {username_alpha.isalpha()}")
print(f"'johndoe'.isalpha(): {username_alpha_only.isalpha()}")

# Check if a port number is a digit (input validation)
port = "8080"
print(f"'8080'.isdigit(): {port.isdigit()}")
non_digit_port = "8080a"
print(f"'8080a'.isdigit(): {non_digit_port.isdigit()}")

# Check if a password contains only alphanumeric characters (simple validation)
password_alphanum = "Pass123"
print(f"'Pass123'.isalnum(): {password_alphanum.isalnum()}")
password_with_symbol = "Pass@123"
print(f"'Pass@123'.isalnum(): {password_with_symbol.isalnum()}")

# Check for empty or purely whitespace strings
empty_string = ""
space_string = "   "
print(f"Empty string.isspace(): {empty_string.isspace()}") # False (requires at least one char)
print(f"Space string.isspace(): {space_string.isspace()}") # True

# Check case
lower_text = "secret"
upper_text = "SECRET"
mixed_text = "Secret"
print(f"'{lower_text}'.islower(): {lower_text.islower()}")
print(f"'{upper_text}'.isupper(): {upper_text.isupper()}")
print(f"'{mixed_text}'.islower(): {mixed_text.islower()}")
print(f"'{mixed_text}'.isupper(): {mixed_text.isupper()}")

print("\n--- End of String Operations Script ---")