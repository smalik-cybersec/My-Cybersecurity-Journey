# Module 14, Lesson 1: Introduction to Functions

## 1. What is a Function?
A function is a block of organized, reusable code that performs a single, related action. It allows for modularity and code reuse, making programs easier to manage and debug.

## 2. Why Use Functions?
* **Modularity:** Breaks down complex problems into smaller, manageable pieces.
* **Reusability:** Avoids redundant code; functions can be called multiple times.
* **Readability:** Improves code clarity by giving descriptive names to code blocks.
* **Abstraction:** Hides implementation details, focusing on "what" a function does rather than "how."
* **Easier Debugging:** Isolates issues to specific function blocks.

## 3. Function Definition Syntax
Functions are defined using the `def` keyword.

```python
def function_name(parameter1, parameter2, ...):
    """
    Docstring: A concise explanation of the function's purpose,
    its arguments, and what it returns.
    """
    # Function body: code that performs the function's task
    # ...
    return [expression] # Optional: returns a value from the function