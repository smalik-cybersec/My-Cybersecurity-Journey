Building upon our previous discussion about the introduction to **conditional statements** in Module 12, Lesson 02 focuses specifically on the **`if` statement** and its practical examples within Python programming.

The **`if` statement** is a fundamental building block for allowing your programs to make decisions and control their flow. It enables you to execute specific blocks of code only when a certain **condition** is met.

Here's an introduction to the `if` statement with examples:

*   **Purpose**: The primary purpose of an `if` statement is to **examine a condition** and execute a particular **action** or set of actions if that condition evaluates to `True`. If the condition is `False`, the code block associated with the `if` statement is skipped.

*   **Conditional Tests (Boolean Expressions)**:
    *   At the core of every `if` statement is a **conditional test**. This is an expression that Python evaluates to either `True` or `False`.
    *   These tests often involve **comparison operators**, which compare two values and yield a Boolean result. Common comparison operators include:
        *   `==` (equal to)
        *   `!=` (not equal to)
        *   `<` (less than)
        *   `>` (greater than)
        *   `<=` (less than or equal to)
        *   `>=` (greater than or equal to)

*   **Structure of a Simple `if` Statement**:
    A simple `if` statement typically consists of:
    1.  The **`if` keyword**.
    2.  A **conditional test** (the expression that evaluates to `True` or `False`).
    3.  A **colon (`:`)** marking the end of the `if` line.
    4.  An **indented block of code** (known as the `if` clause), which contains the instructions to be executed if the condition is `True`. **Indentation is crucial in Python** as it defines code blocks.

*   **Execution Flow**:
    When Python encounters an `if` statement:
    1.  It first evaluates the `conditional_test`.
    2.  If the test evaluates to `True`, the **indented code block** immediately following the `if` statement is executed.
    3.  If the test evaluates to `False`, Python **ignores** the indented code block and continues with the rest of the program. This contrasts with a `while` loop, which would repeatedly check the condition and execute the clause as long as it's `True`.

*   **Examples**:

    *   **Simple Voting Eligibility Check**:
        ```python
        age = 19
        if age >= 18:  # Conditional test: Is age greater than or equal to 18?
            print("You are old enough to vote!")  # This line is executed if condition is True
            print("Have you registered to vote yet?") # This line is also executed if condition is True
        ```
        In this example, since `age` is 19, `age >= 18` evaluates to `True`, and both print statements will execute. If `age` were, for instance, 17, the condition would be `False`, and nothing within the `if` block would be printed.

    *   **Conditional Output based on Value**:
        ```python
        i = 45
        if i == 45: # Checks if the value of 'i' is equal to 45
            print('i is 45') # This line runs if the condition is True
        ```
        Since `i` is 45, the condition `i == 45` evaluates to `True`, and `'i is 45'` will be printed.

    *   **Checking for specific items in a loop (using `if` logic)**:
        While this example from the sources also includes an `else` clause, it clearly demonstrates the core `if` test for a special condition:
        ```python
        cars = ['audi', 'bmw', 'subaru', 'toyota']

        for car in cars:
            if car == 'bmw': # If the current car is 'bmw'
                print(car.upper()) # Print it in uppercase
            else: # Otherwise
                print(car.title()) # Print it in title case
        ```
        This code iterates through the `cars` list. For each `car`, it checks if it's 'bmw' using an `if` test. If `True`, it prints in uppercase; if `False`, it prints in title case.

*   **Styling**: For improved readability, the PEP 8 style guide suggests using a **single space around comparison operators**. For instance, `if age < 4:` is preferred over `if age<4:`. While this does not change how Python interprets the code, it makes it easier for humans to read and understand.

Understanding simple `if` statements is a crucial first step in building more complex decision-making logic in your Python programs, which will be further explored with `if-else` and `if-elif-else` constructs.