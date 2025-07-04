In Python, **Lesson 03: Multiple variable declaration** refers to the technique of **assigning values to several variables in a single statement**. This capability, often referred to as **multiple assignment** or **unpacking**, allows for more concise and readable code.

Here's how it works and its various applications:

*   **Core Concept and Syntax**
    *   You can assign values to more than one variable on a single line.
    *   The syntax involves listing **variable names separated by commas** on the left side of the assignment operator (`=`), and **values (or an expression that evaluates to multiple values, like a tuple or list) separated by commas** on the right side. Python then assigns each value to its corresponding variable by position.
    *   **Example**: To initialise `x`, `y`, and `z` to zero, you can write: `x, y, z = 0, 0, 0`.

*   **Unpacking Sequences**
    *   Multiple assignment is a form of **unpacking**, which is a shortcut for assigning multiple variables from a sequence (like a list or tuple).
    *   **Example**: If you have a tuple `item = ('Peanut butter', 'Jelly')`, you can unpack its values into separate variables: `first, second = item`.
    *   A critical rule for simple unpacking is that **the number of variables on the left must exactly match the length of the sequence on the right**; otherwise, Python will raise a `ValueError`.

*   **Functions Returning Multiple Values**
    *   Python functions can "return" multiple values by packaging them into a **tuple**. The calling code can then directly unpack this tuple into individual variables.
    *   **Example**: A function calculating minimum and maximum lengths might return `minimum, maximum = get_stats(lengths)`. This works because `get_stats` actually returns a two-item tuple.
    *   However, it's advised to **never unpack more than three variables when functions return multiple values** to avoid error-prone and less readable code. If more values are needed, it's better to define and return a lightweight class or a `namedtuple` instance instead.

*   **Catch-All Unpacking with the Starred Expression (`*`)**
    *   Python's unpacking syntax also supports a **starred expression (`*`)** to catch all remaining values into a list. This can appear in any position within the unpacking pattern.
    *   **Example**: `a, b, *rest = range(5)` would assign `a=0`, `b=1`, and `rest=`.
    *   **Limitations**:
        *   A starred expression **must be accompanied by at least one other required part** in the unpacking pattern; it cannot be used on its own for single-level unpacking.
        *   You **cannot use multiple starred expressions** in a single-level unpacking pattern. While possible in multi-level unpacking, it is generally not recommended.

*   **Variables as Labels**
    *   This dynamic behavior of variable assignment, including multiple assignment, reinforces the conceptual model of variables as **"labels attached to objects"** [Conversation]. When you reassign a variable, the label is simply detached from one object and reattached to another [Conversation]. This helps explain concepts like tuple immutability paradoxes, where a `TypeError` can be raised during an augmented assignment to a mutable item within a tuple, even though the item's value *is* modified.