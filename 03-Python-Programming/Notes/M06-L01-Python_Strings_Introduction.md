# M06-L01 | Strings: Introduction

**Date:** 2025-06-27
---
### 1. Definition & Core Concept
> A string in Python is an immutable sequence of characters.

A string is a fundamental data type used to represent text. It can contain letters, numbers, symbols, and spaces. In Python, strings are considered **immutable**, which means that once a string is created, its individual characters cannot be changed. Any operation that appears to "modify" a string, such as concatenation or replacement, actually results in the creation of a *new* string in memory.

---
### 2. Why It Matters (The Cybersecurity Context)
* **Relevance:** Strings are ubiquitous in cybersecurity. From parsing configuration files to analyzing network traffic and user input, almost every piece of information you interact with in a security context will involve strings. Understanding how to declare, manipulate, and analyze strings is paramount for building effective security tools and scripts.
* **Use-Case 1:** **Log Analysis:** Security analysts constantly deal with log files (e.g., firewall logs, web server logs, SIEM data). These logs are essentially large strings or collections of strings. Python's string manipulation capabilities are crucial for extracting relevant information, identifying patterns (like suspicious IP addresses or error codes), and filtering out noise.
* **Use-Case 2:** **Network Protocol Parsing:** When developing tools for network analysis (e.g., packet sniffers, port scanners), you'll often receive raw data as bytes. Converting this data into human-readable strings (e.g., HTTP headers, DNS queries) is a common task, and then using string methods to extract specific fields is essential for understanding network communications.
---
### 3. Syntax & Practical Implementation
#### Annotated Example:
```python
# Strings can be declared using single quotes, double quotes, or triple quotes.

# 1. Single-quoted string
single_quote_string = 'This is a string declared with single quotes.'
print(f"Single quoted: {single_quote_string}")

# 2. Double-quoted string
double_quote_string = "This is a string declared with double quotes."
print(f"Double quoted: {double_quote_string}")

# 3. Triple-quoted strings (for multi-line strings or docstrings)
# These can use three single quotes or three double quotes.
multi_line_string = """This is a multi-line string.
It can span across
multiple lines of code."""
print(f"\nMulti-line string:\n{multi_line_string}")

# Triple-quoted strings are also useful for docstrings (documentation strings)
def example_function():
    """This is a docstring. It explains what the function does."""
    return "Function executed!"

print(f"\nFunction docstring: {example_function.__doc__}")

# Basic string concatenation (creates a new string)
part1 = "Cyber"
part2 = "Security"
full_word = part1 + part2
print(f"\nConcatenated string: {full_word}")

# Immutability example: attempting to change a character
my_string = "Python"
# my_string[0] = 'J' # This would raise a TypeError: 'str' object does not support item assignment
print(f"\nOriginal string (immutable): {my_string}")

# To "change" a string, you create a new one:
new_string = 'J' + my_string[1:]
print(f"New string after 'modification': {new_string}")