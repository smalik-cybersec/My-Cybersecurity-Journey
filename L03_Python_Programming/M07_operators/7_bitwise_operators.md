Lesson 07 focuses on **Bitwise Operators** in Python. These operators perform operations directly on the individual **bits** of integer values. Unlike logical operators (`and`, `or`, `not`), which work with Boolean values (`True` or `False`), bitwise operators are used for low-level manipulation of data's binary representation.

Python provides the following bitwise operators:

*   **Bitwise AND (`&`)**:
    *   Performs a logical AND operation on each corresponding bit of its two operands. If both bits are 1, the result for that bit is 1; otherwise, it is 0.
    *   For instance, to get the low-order nybble (the last 4 bits) of a byte, you can use the bitwise AND operator with `0xF` (which is `00001111` in binary). This operation effectively "deletes" the first 4 bits, as anything ANDed with 0 will be 0, while leaving the last 4 bits unaltered, as anything ANDed with 1 returns the original value.

*   **Bitwise OR (`|`)**:
    *   Performs a logical OR operation on each corresponding bit. If at least one of the bits is 1, the result for that bit is 1; otherwise, it is 0.

*   **Bitwise XOR (`^`)**:
    *   Performs a logical exclusive OR (XOR) operation on each corresponding bit. If the bits are different (one is 0 and the other is 1), the result for that bit is 1; if they are the same (both 0 or both 1), the result is 0.
    *   The `operator` module provides a function form, `operator.xor`, which can be used with `functools.reduce` for aggregating XOR operations.

*   **Bitwise NOT (`~`)**:
    *   This is a **unary operator**, meaning it operates on a single Boolean value or expression.
    *   It flips the bits of its operand; 0s become 1s and 1s become 0s.
    *   In Python, `~x` is defined as `-(x+1)`.

*   **Left Shift (`<<`)**:
    *   Shifts the bits of the left operand to the left by the number of positions specified by the right operand. New bits shifted in from the right are 0s. This is equivalent to multiplying by powers of 2.

*   **Right Shift (`>>`)**:
    *   Shifts the bits of the left operand to the right by the number of positions specified by the right operand. New bits shifted in from the left are 0s for positive numbers (sign bit extension for negative numbers, though typically less common in basic use cases).
    *   For example, to get the high-order nybble of a byte, you would right-shift the byte by four places, which is equivalent to prepending four 0s to the front of the byte, causing the last 4 bits to fall off.

**Key Characteristics and Usage:**

*   **Operator Overloading:** Unlike identity (`is`) and logical operators (`and`, `or`, `not`), bitwise operators (`&`, `|`, `~`, `<<`, `>>`, `^`) *can* be overloaded for user-defined types. This means you can define how these operators behave when applied to instances of your custom classes.
*   **Augmented Assignment Operators:** There are augmented assignment versions for bitwise operators, such as `&=`, `|=`, `^=`, `<<=`, and `>>=`. These combine the operation with assignment (e.g., `x &= y` is equivalent to `x = x & y`).
*   **Binary Data Manipulation:** Bit-shifting and bitwise operations are common techniques when dealing with **binary data**. For structured binary information, the `struct` module is invaluable, often working alongside `bytes` and `memoryview` objects.
*   **Readability:** Although bitwise manipulation can be powerful, the sources note that in some contexts, such as regular expressions, the use of `bit-shifting` might make code harder to read.