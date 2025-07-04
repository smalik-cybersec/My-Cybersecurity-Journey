Building on Lesson 01: Introduction and Lesson 02: Declaration, **Lesson 03: All String Functions with Examples** delves into the comprehensive set of operations and methods available for manipulating string data in Python [403, Conversation History].

A string in Python is fundamentally a **sequence of characters**. In Python 3, these are Unicode code points, defaulting to UTF-8 encoding [4, 244, 467, Conversation History]. It's crucial to remember that strings are **immutable**, meaning their content cannot be changed after they are created. Any operation that appears to modify a string will, in fact, return a *new* string.

Here are the key string functions and methods in Python, along with examples:

### 1. Declaration (Quick Recap)
The primary way to declare a string is by enclosing text within quotation marks [47, 109, 130, 467, 506, 507, Conversation History]:
*   **Single quotes**: `'Hello, world!'`.
*   **Double quotes**: `"Hello, world!"`. These are interchangeable.
*   **Triple quotes**: `'''...'''` or `"""..."""` are used for multiline strings or to easily include both single and double quotes within the string without escape characters.
*   **`str()` constructor**: This built-in function can convert other data types into their string representation [99, 114, 467, Conversation History]. If called without arguments, it returns an empty string `''`.
    *   Example: `str(42)` results in `'42'` [Conversation History].
    *   Example: `str(['a', 'b'])` results in `'['a', 'b']'`.

### 2. Basic String Operations

*   **Concatenation (`+`)**: Joins two or more string values together [99, 115, Conversation History].
    *   Example: `'It is good to meet you, ' + 'Al'` would result in `'It is good to meet you, Al'` [Conversation History].
    *   Example: `'spam' + 'spamspam'` evaluates to `'spamspamspam'`.
    *   Note: You cannot concatenate strings directly with other data types like integers using `+`.

*   **Replication (`*`)**: Creates a new string by repeating an existing string multiple times [99, 115, Conversation History].
    *   Example: `'spam' * 3` evaluates to `'spamspamspam'`.

*   **Indexing and Slicing**: Allows access to individual characters or portions of a string, similar to lists because strings are sequences [102, 130, 132, 466, 511, Conversation History]. Python uses **zero-based indexing** [31, Conversation History].
    *   **Indexing**: Access a single character by its position.
        *   Example: `name = 'Zophie'`, `name` yields `'Z'`, `name[-2]` yields `'i'`.
    *   **Slicing**: Extracts a substring from a string.
        *   Example: `spam = 'Hello, world!'`, `spam[0:5]` yields `'Hello'`, `spam[:5]` yields `'Hello'`, `spam[7:]` yields `'world!'`.
        *   Example: `s = 'bicycle'`, `s[::-1]` yields `'elcycib'` (reverses the string).

### 3. String Methods for Case Modification

These methods return new strings with modified casing [29, 48, 49, 135, 468, 516, Conversation History]:

*   **`.title()`**: Converts the first letter of each word to uppercase and the rest to lowercase [29, 49, 468, Conversation History].
    *   Example: `'ada lovelace'.title()` yields `'Ada Lovelace'` [48, Conversation History].
*   **`.upper()`**: Converts all characters in the string to uppercase [49, 135, 468, 516, Conversation History].
    *   Example: `'Ada Lovelace'.upper()` yields `'ADA LOVELACE'`.
*   **`.lower()`**: Converts all characters in the string to lowercase [49, 135, 468, 516, Conversation History].
    *   Example: `'Ada Lovelace'.lower()` yields `'ada lovelace'`.
*   **`.capitalize()`**: Capitalizes only the first character of the entire string [468, Conversation History].
    *   Example: `'bill monroe'.capitalize()` yields `'Bill monroe'`.
*   **`.swapcase()`**: Swaps the case of all characters (uppercase becomes lowercase, and vice-versa) [468, Conversation History].
    *   Example: `'BILL MONROE'.swapcase()` yields `'bill monroe'`.

### 4. String Methods for Whitespace Handling

These methods are used to remove leading, trailing, or both types of whitespace characters (spaces, tabs `\t`, newlines `\n`, carriage returns `\r`) from a string [29, 51, 52, 54, 142, 513, 514, Conversation History]. They return a *new* string object.

*   **`.strip()`**: Removes any leading and trailing whitespace [52, 142, 513, 515, Conversation History].
    *   Example: `spacious_string = "\n\t Some Non-Spacious Text\n \t\r"`, `spacious_string.strip()` yields `'Some Non-Spacious Text'`.
*   **`.lstrip()`**: Removes whitespace from the left (leading) side of the string [52, 142, 513, 514, Conversation History].
*   **`.rstrip()`**: Removes whitespace from the right (trailing) side of the string [52, 142, 513, 515, Conversation History].
    *   These methods can also take an optional string argument to specify characters to be stripped, not just whitespace.

### 5. String Formatting

*   **Formatted String Literals (f-strings)**: A powerful and concise way to embed expressions inside string literals, available from Python 3.6+ [19, 50, 469, Conversation History].
    *   Example: `first_name = "ada"`, `last_name = "lovelace"`, `full_name = f"{first_name} {last_name}"`, `print(f"Hello, {full_name.title()}!")` yields `'Hello, Ada Lovelace!'`.

*   **`format()` method (or `str.format()` )**: Another powerful way to embed values into strings, available in older Python versions too [15, 19, 224, 311, Conversation History].
    *   Example: `"{0} {1}".format("Hello", "World")` yields `'Hello World'`.
    *   Example: `format(42, 'b')` yields `'101010'` (binary representation).

### 6. String Inspection Methods (`isX()` Methods)

These methods return a **Boolean value** (`True` or `False`) indicating whether the string contents match a specific criteria [102, 136, 137, 138, 145, 249, 468, 469, Conversation History]. They are particularly useful for **validating user input**.

*   **`.isalpha()`**: Returns `True` if the string consists only of letters and is not blank.
    *   Example: `'hello'.isalpha()` yields `True`, `'hello123'.isalpha()` yields `False`.
*   **`.isalnum()`**: Returns `True` if the string consists only of letters and numbers and is not blank.
    *   Example: `'hello123'.isalnum()` yields `True`.
*   **`.isdecimal()`**: Returns `True` if the string consists only of numeric characters (decimals) and is not blank.
    *   Example: `'123'.isdecimal()` yields `True`.
*   **`.isspace()`**: Returns `True` if the string consists only of spaces, tabs, and newlines and is not blank.
    *   Example: `'    '.isspace()` yields `True`.
*   **`.istitle()`**: Returns `True` if the string follows title case rules (words start with an uppercase letter followed by lowercase letters).
    *   Example: `'This Is Title Case'.istitle()` yields `True`.
*   **`.isupper()`**: Returns `True` if all characters in the string are uppercase [135, 469, Conversation History].
*   **`.islower()`**: Returns `True` if all characters in the string are lowercase [135, 469, Conversation History].
*   **`.isnumeric()`**: Returns `True` if all characters in the string are numeric (can include digits from other writing systems, unlike `isdecimal()`).

### 7. Membership Operators (`in` and `not in`)

These operators check for the presence or absence of a substring within a larger string [102, 130, 131, 466, 510, 511, Conversation History].

*   **`in`**: Returns `True` if the substring is found.
    *   Example: `'Zo' in 'Zophie'` yields `True`.
    *   Example: `2 in` yields `True`.
*   **`not in`**: Returns `True` if the substring is not found.
    *   Example: `'z' not in 'Zophie'` yields `True`.
    *   Example: `'a' not in 'cat'` yields `False`.

### 8. Splitting and Joining Strings

*   **`.join(iterable)`**: A string method that concatenates elements of an iterable (e.g., a list of strings) into a single string, using the string it's called on as a separator.
    *   Example: `', '.join(['cats', 'rats', 'bats'])` yields `'cats, rats, bats'`.
    *   Example: `'ABC'.join(['My', 'name', 'is', 'Simon'])` yields `'MyABCnameABCisABCSimon'`.

*   **`.split(separator)`**: A string method that breaks a string into a list of substrings based on a specified delimiter (separator). If no separator is given, it splits by any whitespace and discards empty strings.
    *   Example: `'Hello, world!'.split()` yields `['Hello,', 'world!']`.
    *   Example: `'pos1,pos2,pos3'.split(',')` yields `['pos1', 'pos2', 'pos3']`.
    *   Example: `'pos1XXXpos2XXXpos3'.split('XXX')` yields `['pos1', 'pos2', 'pos3']`.

### 9. Prefix and Suffix Checking

*   **`.startswith(prefix)`**: Returns `True` if the string begins with the specified prefix [102, 138, 139, 469, 511, 512, Conversation History].
    *   Example: `'Hello, world!'.startswith('Hello')` yields `True`.
    *   Example: `"William".startswith('W')` yields `True`.
*   **`.endswith(suffix)`**: Returns `True` if the string ends with the specified suffix [102, 138, 139, 469, 511, 512, Conversation History].
    *   Example: `'Hello, world!'.endswith('world!')` yields `True`.
    *   Example: `"Molly".endswith('olly')` yields `True`.

### 10. String Partitioning and Justification

*   **`.partition(separator)`**: Splits the string at the *first* occurrence of the specified separator, returning a 3-tuple containing the part before the separator, the separator itself, and the part after the separator.
    *   Example: `'Hello, world!'.partition('w')` yields `('Hello, ', 'w', 'orld!')`.

*   **`.rjust(width, fillchar=' ')`**: Returns a new string right-justified within a specified `width`, padded with `fillchar` (default is space).
    *   Example: `'Hello'.rjust(10)` yields `'     Hello'`.
*   **`.ljust(width, fillchar=' ')`**: Returns a new string left-justified within a specified `width`.
    *   Example: `'Hello'.ljust(10)` yields `'Hello     '`.
*   **`.center(width, fillchar=' ')`**: Returns a new string centered within a specified `width`.

### 11. Other Useful String Methods and Functions

*   **`.count(substring)`**: Returns the number of non-overlapping occurrences of a substring in the string.
    *   Example: Counting how many times "row" appears in a string.
*   **`.replace(old, new)`**: Returns a new string with all occurrences of `old` substring replaced by `new` substring.
    *   Example: `'The time has come'.replace(' ', '-')` yields `'The-time-has-come'`.
*   **`len(string)`**: A built-in function that returns the number of characters in a string.
    *   Example: `len('café')` yields `4` (representing four Unicode characters).
*   **`ord(character)`**: Returns the Unicode code point (an integer) of a single character.
    *   Example: `ord('A')` yields `65`, `ord('4')` yields `52`.
*   **`chr(integer)`**: Returns the character corresponding to the given Unicode code point.
    *   Example: `chr(65)` yields `'A'`.
*   **`encode(encoding)`**: A method of `str` objects used to convert Unicode data (`str`) into raw binary data (`bytes`) [4, 5, 244, 247, 250, 358, Conversation History].
    *   Example: `s = 'café'`, `b = s.encode('utf8')` results in `b'caf\xc3\xa9'`.
*   **`decode(encoding)`**: A method of `bytes` objects used to convert binary data (`bytes`) into Unicode data (`str`) [4, 5, 244, 247, 250, 265, 358, Conversation History].
    *   Example: `b'caf\xc3\xa9'.decode('utf8')` results in `'café'`.
    *   It is important to explicitly specify the encoding (e.g., `'utf_8'`) for these conversions [4, 5, Conversation History].

### 12. String Representations (`__repr__` and `__str__`)

*   **`repr()`**: Returns a string representation of an object primarily for **developers**, useful for debugging and logging. It should ideally be unambiguous and, importantly, **never raise an exception**.
    *   Example: If you type a variable name at an IPython prompt, its `__repr__` is displayed.
*   **`str()`**: Returns a string representation of an object primarily for **end-users**, designed to be readable and presentable.
    *   Example: The `print()` function interprets escape sequences and displays the `__str__` representation.
*   If a custom `__str__` method is not defined, Python will fall back to using `__repr__`. In Python 3, both `__repr__` and `__str__` (and `__format__`) must return Unicode strings (`str`), while `__bytes__` should return a byte sequence (`bytes`).