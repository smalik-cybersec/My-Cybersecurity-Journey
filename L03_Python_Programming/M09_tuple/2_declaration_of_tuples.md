Lesson 02 of Module 09 focuses on the **Declaration of Tuples** in Python.

As discussed previously, a tuple is a sequence data type that can hold multiple values [conversation history]. The primary way to declare a tuple is by using **parentheses `()`**, which distinguishes them from lists that use square brackets `[]`.

Here's how tuples are declared:

*   **Syntax**: Tuples are defined with their elements enclosed within parentheses, with individual elements separated by commas.
    *   For example, you can define a tuple called `dimensions` like this: `dimensions = (200, 50)`.
    *   Another example is `eggs = ('hello', 42, 0.5)`.
*   **Single-Element Tuple**: If you need to declare a tuple with only one element, a **trailing comma is mandatory** after the element within the parentheses. For instance, to declare a tuple containing only the number 42, it would be `(42,)`. Without the comma, Python would interpret `(42)` as simply the integer 42 within parentheses (for grouping), not a tuple.
*   **Accessing Elements**: Once a tuple is defined, you can access its individual elements by using their **index in square brackets**, just as you would with a list. For example, `dimensions` would access the first element of the `dimensions` tuple.

This method of declaration aligns with Python's approach to sequence data types, where the enclosing characters (parentheses for tuples, square brackets for lists, and quotes for strings) signify their type.