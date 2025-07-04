Building on the foundational understanding of strings from Lesson 01, **Lesson 02: Declaration** focuses specifically on the various methods of creating and defining string values in Python.

Here's a comprehensive overview of string declaration in Python:

*   **What is a String?**
    *   A string is a **sequence of characters**. In Python 3, instances of the `str` type contain **Unicode code points**, representing textual characters from human languages. Strings default to using **UTF-8 encoding** as of Python 3. Essentially, a string is a **collection of ordered characters** [Conversation History].

*   **Primary Methods of Declaration (String Literals)**
    *   The most common way to create a string, often called a "string literal", is by **surrounding the text with quotation marks** [Conversation History, 49, 510].
    *   Python offers flexibility by allowing the use of **single quotes (`'Hello'`) or double quotes (`"Hello"`)** [Conversation History, 49, 94]. These are **interchangeable** for string creation.
    *   You can also declare strings using **triple quotation marks (single `'''` or double `"""`)**. All three types of quotation marks (single, double, and triple) create an object of type `str`.

*   **Handling Quotes Within Strings**
    *   This flexibility is particularly useful when your string itself contains quotation marks or apostrophes. For example, if your string includes an apostrophe, you can enclose the entire string in double quotes to avoid syntax errors.
        *   Example: `"One of Python's strengths is its diverse and supportive community."`.
    *   Conversely, if the string contains double quotes, you can use single quotes for the string literal.
    *   If you need to use **both single and double quotes** within the same string, or if you need to embed a quote character that matches the string's enclosing quotes, you must use **escape characters**.

*   **Escape Characters**
    *   Python recognises **backslash escape characters** within strings to represent special characters or to embed quotes that would otherwise prematurely terminate the string.
    *   Common escape characters include:
        *   `\'`: Single quote
        *   `\"`: Double quote
        *   `\t`: Tab
        *   `\n`: Newline (line break)
        *   `\\`: Backslash
    *   Alternatively, you can use **raw strings** by prefixing the string literal with `r` (e.g., `r'\b[a-z]+\b'`). Raw strings do not interpret escape sequences, which is particularly useful for regular expressions where backslashes are common.

*   **The `str()` Constructor**
    *   Strings can also be created using the **built-in `str()` constructor** [Conversation History, 468]. This function is powerful because it can convert other types of values into their string representation [Conversation History, 145, 468].
    *   For example, `str(42)` will result in the string `'42'` [Conversation History]. If called without arguments, `str()` returns an empty string `''`.

*   **Distinction Between `str` and `bytes`**
    *   Python 3 introduced a **sharp distinction between strings of human text (`str`) and sequences of raw binary data (`bytes`)**.
    *   `str` instances do not have an associated binary encoding, and `bytes` instances do not have an associated text encoding.
    *   To convert **Unicode data (a `str`) to binary data (a `bytes` object), you must call the `encode()` method** on the `str` object [Conversation History, 5, 271].
    *   To convert **binary data (a `bytes` object) to Unicode data (a `str`), you must call the `decode()` method** on the `bytes` object [Conversation History, 5, 271].
    *   You can **explicitly specify the desired encoding** (e.g., `'utf_8'`) when performing these conversions, or accept the system default, which is commonly UTF-8 [Conversation History, 5, 271]. It is crucial that `__repr__`, `__str__`, and `__format__` methods in Python 3 must return Unicode strings (`str`), while only `__bytes__` is expected to return a byte sequence (`bytes`).