In Python, **Lesson 04: Valid and invalid variables** focuses on the specific rules and conventions that determine whether a variable name is acceptable and readable. Adhering to these guidelines is essential to prevent errors and ensure your code is clear and maintainable.

As discussed in previous lessons, it's helpful to remember that variables in Python are **labels that you assign to values**, rather than "boxes" holding data. This means that when you declare a variable, you are essentially attaching a name to an object in memory.

Here are the key rules for declaring **valid** and **invalid** variable names:

### Rules for Valid Variable Names

To create a **valid** variable name in Python, it must adhere to the following rules:

*   **Allowed Characters**: A variable name can contain **only letters (a-z, A-Z), numbers (0-9), and the underscore character (`_`)**.
    *   *Example of valid characters*: `message_1`, `user_name`, `total_sum`.
*   **Starting Character**: A variable name **must start with a letter or an underscore (`_`)**, but it **cannot start with a number**.
    *   *Example*: `message_1` is valid, but `1_message` is invalid.
    *   *Example*: `_42` is a valid variable name.
*   **No Spaces**: Variable names **cannot contain spaces**. If you need to separate words, you should use underscores.
    *   *Example*: `greeting_message` is valid, but `greeting message` is invalid.
*   **Case-Sensitivity**: Python variable names are **case-sensitive**. This means that `spam`, `SPAM`, `Spam`, and `sPaM` are considered four different variables.
*   **Avoid Python Keywords**: You **must not use Python's reserved keywords** as variable names. Keywords are words that have special meaning in Python, such as `if`, `else`, `while`, `for`, `print`, `def`, `class`, `True`, `False`, `None`, `import`, `return`, `and`, `or`, `not`, `global`, etc.. Using them will result in a `SyntaxError`.
    *   *Example*: You cannot assign a value to `True` (e.g., `True = 2 + 2`) because it's a keyword.
*   **Avoid Built-in Functions**: While you won't get an error, you should **avoid using built-in function names** (like `print`, `len`, `str`, `int`, `float`, `input`, `max`, `min`, `type`) as variable names. Doing so will **override the behaviour** of that function for the duration of your variable's scope.

### Examples of Invalid Variable Names

A variable name is **invalid** if it breaks any of the strict rules above. Common reasons for invalidity include:

*   **Starting with a number**: `1_message`, `42`.
*   **Containing spaces**: `current balance`.
*   **Using hyphens (`-`) or other special characters (besides underscore)**: `current-balance`, `TOTAL_$UM`, `'hello'` (due to quotes).
*   **Being a reserved Python keyword**: `class`, `for`, `True`, `False`, `None`.

### Conventions for Good Variable Names

Beyond the strict rules, there are widely accepted **conventions** that make your code more readable and easier for you and others to understand. These are not enforced by Python, but are considered best practices:

*   **Descriptive and Concise**: Variable names should be **meaningful** and clearly indicate the data they contain. For example, `student_name` is better than `s_n`.
*   **Lowercase with Underscores (Snake Case)**: For most variables, functions, and attributes, the convention is to use **lowercase letters with underscores separating words** (e.g., `first_name`, `user_id`). This book sometimes uses camelcase for variable names, but acknowledges that PEP 8, the official Python code style, recommends underscores.
*   **Constants**: For values that are **intended to remain constant** throughout the program, the convention is to use **all uppercase letters with underscores** (e.g., `MAX_CONNECTIONS`, `PI`). This signals to anyone reading the code that the value should not be changed.
*   **Avoid Ambiguous Characters**: Be careful when using the lowercase letter `l` and the uppercase letter `O`, as they can be easily confused with the numbers `1` and `0`, respectively.
*   **Temporary/Unused Variables**: A single underscore (`_`) is often used as a dummy variable name for values you don't intend to use, particularly in unpacking assignments. This convention is widely understood.

Violating these rules can lead to `SyntaxError` or `NameError` exceptions, which Python's interpreter tries its best to help you diagnose through tracebacks. Understanding these rules is a foundational step in writing robust Python programs.