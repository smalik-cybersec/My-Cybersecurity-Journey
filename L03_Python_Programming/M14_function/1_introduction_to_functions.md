Module 14: Function, Lesson 01: Introduction function, as outlined in one of the sources, covers the **introduction to functions** in Python. Functions are a fundamental programming concept that help organise and manage code.

Here's a detailed explanation of functions in Python:

*   **What is a Function?**
    *   A function is a **named block of code** that performs a specific job. It can be thought of as a "miniprogram within a program".
    *   Python provides several **built-in functions**, such as `print()`, `input()`, and `len()`. Beyond these, you can also **write your own functions**.
    *   In Python, functions are considered **first-class objects**. This means they can be created at runtime, assigned to variables or elements in data structures, passed as arguments to other functions, and returned as the result of a function. This enables programming in a functional style, using higher-order functions.

*   **Why Use Functions? (Benefits)**
    *   **Organisational Tool**: Functions are the first organisational tool programmers use in Python, allowing you to break large programs into smaller, simpler, named pieces.
    *   **Readability**: They improve readability and make code more approachable.
    *   **Reuse and Refactoring**: Functions enable code reuse, meaning you only have to write a block of code once and can then use it multiple times. This also makes code easier to troubleshoot and maintain.
    *   **Encapsulation**: Functions encapsulate a block of code, allowing you to repeat its behaviour without duplicating the code.
    *   **Modularity**: Storing functions in separate files, called modules, allows you to hide implementation details, focus on higher-level logic, and easily share code with others.

*   **Anatomy and Definition of a Function**
    *   A function definition **starts with the `def` keyword**, followed by the **function name**, **parentheses `()`**, and then a **colon `:`**.
    *   The **body of the function** consists of all the **indented lines** that follow the `def` statement. This code is executed when the function is *called*, not when it is first defined.
    *   **Docstrings**: If the first line in the indented block is a string using multiline syntax, it acts as a **docstring**. Docstrings describe what the function does, explain its parameters, and what it returns. Python uses docstrings when generating documentation for your functions, and they are considered a best practice for communicating with future users of your code.

*   **Calling a Function**
    *   To use a function, you **call it**. A function call tells Python to execute the code within the function.
    *   You call a function by writing its name, followed by any necessary information (arguments) in parentheses. For example, `greet_user()`.
    *   **Arguments and Parameters**: Values passed to a function call are called **arguments**, and variables that receive these arguments in the function definition are called **parameters**. The parentheses in the function definition (e.g., `def greet_user(username):`) hold the parameters.

By understanding these fundamental aspects of functions, programmers can write more organised, readable, and reusable Python code.