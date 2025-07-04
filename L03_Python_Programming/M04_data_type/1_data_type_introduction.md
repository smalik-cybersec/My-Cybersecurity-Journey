Based on your query regarding **"Module 4 Data Type – Lesson 01: Introduction"**, here's a comprehensive overview of data types in Python, drawing from the provided sources:

### Introduction to Data Types in Python

In Python, a **data type** is a fundamental concept that categorises values, with every value belonging to exactly one data type. Understanding data types is essential for writing effective Python programs, as they dictate how data is stored and the operations that can be performed on it.

The Python programming language is known for its readability and simplicity. It offers a variety of built-in data types that are both versatile and easy to use.

#### Key Data Types in Python:

1.  **Integers (int)**:
    *   These are **whole numbers** (e.g., -2, -1, 0, 1, 2, 30).
    *   Python 3.6 and later versions allow the use of underscores for readability in large numbers (e.g., 14_000_000_000 is displayed as 14000000000).

2.  **Floating-point numbers (float)**:
    *   These are numbers with a **decimal point** (e.g., 3.14, 0.5).

3.  **Strings (str)**:
    *   These represent **text values**.
    *   Strings are typically surrounded by **single quote characters ('')** or double quotes ("") to mark their beginning and end.
    *   You can use string methods to change case (e.g., `upper()`, `lower()`) or strip whitespace.
    *   Python 3 allows f-strings for easier variable inclusion [previous conversation].
    *   It's important to **know the differences between `bytes` and `str`**. Python does not automatically convert between strings and numbers; attempting to compare different types (e.g., `str` and `bytes`) will result in `TypeError` [previous conversation].

4.  **Lists**:
    *   A list is a **collection of items in a particular order**.
    *   In Python, lists are indicated by **square brackets (`[]`)**, with individual elements separated by commas.
    *   Lists can store diverse types of information, whether a few items or millions, and are one of Python's most powerful features for new programmers.
    *   **Index positions start at 0**, not 1, which is common in many programming languages.
    *   Lists are a **mutable data type**, meaning their values can be added, removed, or changed. You can modify elements, add with `append()` or `insert()`, or remove with `remove()`.
    *   You can sort lists permanently with `sort()` or temporarily with `sorted()`.
    *   **Slicing a list** allows you to work with a part of it.
    *   Python offers **list comprehensions** as a concise way to generate lists in a single line of code.

5.  **Tuples**:
    *   The tuple data type is almost identical to the list data type.
    *   They are defined using **parentheses (`()`)** instead of square brackets.
    *   The main difference is that **tuples, like strings, are immutable**; their values cannot be modified, appended, or removed after creation.

6.  **Dictionaries (dict)**:
    *   Like lists, a dictionary is a **mutable collection of many values**.
    *   Unlike lists, dictionaries use **keys to access values**, not just integers. A key with its associated value is called a **key-value pair**.
    *   Dictionaries are defined using **curly brackets (`{}`)**.
    *   The items stored in a dictionary are **unordered**.
    *   You can use the `get()` method to retrieve values, which can return a default value if a key doesn't exist.

7.  **Sets**:
    *   A set is a **collection of unique items**.
    *   Sets are built using **braces (`{}`) and separating elements with commas**, similar to dictionaries, but they do not contain key-value pairs.
    *   Unlike lists and dictionaries, sets **do not retain items in any specific order**.

8.  **Boolean (bool)**:
    *   The Boolean data type has only **two values: `True` and `False`**.
    *   When entered as Python code, these values lack quotes and start with a capital `T` or `F`.

#### Python's Dynamic Typing and Object Model:

Python is a **dynamically typed language**, meaning type checks occur at runtime [previous conversation]. Variables in Python are better understood as **"labels attached to objects"** rather than "boxes" containing data. This allows for greater code reuse and flexibility in evolving interfaces [previous conversation].

The Python data model defines how objects behave, allowing user-defined types to act like built-in types by implementing special methods. Python offers operator overloading, which enables a rich selection of numeric types that support infix arithmetic operators.