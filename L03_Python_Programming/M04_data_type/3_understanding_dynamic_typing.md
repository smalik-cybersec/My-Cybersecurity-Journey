In Python, **Lesson 03** focuses on demonstrating its **dynamically typed nature** using the `type()` function. Python is considered a dynamically typed language because **type checks occur at runtime** [previous conversation], meaning that variables do not have a fixed type and can be reassigned to values of different types or classes throughout a program's execution.

Here's how `type()` helps illustrate this:

*   **Understanding Dynamic Typing**
    *   Unlike statically typed languages (where types are checked at compile time), Python performs type checking at runtime [previous conversation, 504, 342]. This design philosophy means that Python has historically prioritised dynamic features and has not provided compile-time type safety.
    *   The flexibility of dynamic typing "increases opportunities for reuse, reducing line count, and allows interfaces to emerge naturally as protocols". Even with the introduction of optional type hints in Python 3.5, the language fundamentally remains dynamically typed, with no intention to make type hints mandatory.

*   **The `type()` Function**
    *   The `type()` function is a built-in function in Python.
    *   It is used to **determine the type (or class) of an object**. For example, `type(FancyCar)` would return `<class 'type'>` for the class itself, and `type(my_car)` would return `<class '__main__.FancyCar'>` for an instance of that class. You can also use it to confirm the type of various string declarations, all returning `<type 'str'>`.

*   **Demonstrating Dynamic Typing with `type()`**
    *   To observe dynamic typing in action, you can assign a variable to a value of one type, and then later reassign it to a value of a completely different type. The `type()` function will confirm the change in the variable's type.
    *   Consider the following example:
        ```python
        >>> big = 'large'
        >>> print(big)
        'large'
        >>> print(type(big))
        <class 'str'> # The variable 'big' is currently a string

        >>> big = 1000 * 1000
        >>> print(big)
        1000000
        >>> print(type(big))
        <class 'int'> # The variable 'big' has now been reassigned to an integer
        ```
    *   This output clearly shows that the variable `big` initially held a string value, and then, without any explicit type declaration or conversion syntax, it was successfully reassigned to an integer value, demonstrating Python's dynamic typing.

*   **Variables as Labels (Conceptual Model)**
    *   This dynamic behaviour is best understood by thinking of Python variables not as "boxes" that contain data, but rather as **"labels attached to objects"** [246, previous conversation].
    *   When you assign a value to a variable, you are essentially attaching that label to an object. When you reassign the variable, you are simply **detaching the label from the old object and attaching it to a new object**. The object itself retains its type, but the label (variable) can now point to an object of a different type. This process of associating a name with an object is called "name binding".