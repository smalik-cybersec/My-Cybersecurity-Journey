Lesson 05 focuses on **Logical Operators** in Python, which are crucial for building complex conditional logic in your programs. These operators are used to combine Boolean values (which are `True` or `False`) or expressions that evaluate to Boolean values, and they themselves always evaluate down to a single Boolean value.

Python has three primary logical (or Boolean) operators:

*   **`and` Operator**
    *   The `and` operator is a **binary operator**, meaning it takes two Boolean values or expressions.
    *   It evaluates to `True` only if **both** Boolean values it connects are `True`.
    *   If either, or both, of the values are `False`, the `and` expression evaluates to `False`.
    *   **Truth Table for `and`**:
        *   `True and True` evaluates to `True`
        *   `True and False` evaluates to `False`
        *   `False and True` evaluates to `False`
        *   `False and False` evaluates to `False`
    *   For example, you might use `(age_0 >= 21) and (age_1 >= 21)` to check if two people are both 21 or older.

*   **`or` Operator**
    *   The `or` operator is also a **binary operator**, taking two Boolean values or expressions.
    *   It evaluates to `True` if **either or both** of the individual tests pass.
    *   An `or` expression fails (evaluates to `False`) only when **both** individual tests fail.
    *   **Truth Table for `or`**:
        *   `True or True` evaluates to `True`
        *   `True or False` evaluates to `True`
        *   `False or True` evaluates to `True`
        *   `False or False` evaluates to `False`
    *   For example, `age_0 >= 21 or age_1 >= 21` would be `True` if at least one person is 21 or older.

*   **`not` Operator**
    *   Unlike `and` and `or`, the `not` operator is a **unary operator**, meaning it operates on only one Boolean value or expression.
    *   It simply evaluates to the **opposite Boolean value**.
    *   **Truth Table for `not`**:
        *   `not True` evaluates to `False`
        *   `not False` evaluates to `True`
    *   While you can nest `not` operators (e.g., `not not not not True` evaluates to `True`), there is rarely a practical reason to do so in real programs.

**Key Considerations for Logical Operators:**

*   **Combining with Comparison Operators:** Since comparison operators (like `==`, `!=`, `<`, `>`, `<=`, `>=`) evaluate to Boolean values (`True` or `False`), you can directly use them in expressions with logical operators to create more complex conditions. For instance, `(4 < 5) and (5 < 6)`.
*   **Order of Operations (Precedence):** When mixing different types of operators, Python follows a specific order of operations:
    1.  First, any **math operators** (e.g., `+`, `-`, `*`, `/`) are evaluated.
    2.  Next, **comparison operators** are evaluated.
    3.  Finally, **Boolean (logical) operators** are evaluated in this order: `not` first, then `and`, and then `or`.
    *   Parentheses can be used to override this default precedence and improve readability, although they are not always strictly required.
*   **Boolean Expressions:** Any conditional test, including those using logical operators, is referred to as a **Boolean expression**, as it always results in a `True` or `False` value. These Boolean values are often used to track the state of a program or specific conditions.
*   **Usage in Flow Control:** Logical operators are fundamental in **flow control statements** such as `if`, `elif`, and `while` loops, as they define the conditions that determine which blocks of code are executed.
*   **Distinction from Bitwise Operators:** It is important to distinguish the logical operators (`and`, `or`, `not`) from their bitwise counterparts (`&`, `|`, `~`). Logical operators work with Boolean values, while bitwise operators perform operations on the individual bits of integer values. The logical operators (`is`, `and`, `or`, `not`) also cannot be overloaded in Python, unlike many other operators.
*   **`all()` and `any()` Functions:** Python also provides built-in functions `all()` and `any()` that perform similar logical checks on iterables:
    *   `all(iterable)` returns `True` if every element of the iterable is "truthy" (evaluates to `True` in a Boolean context). It returns `True` for an empty iterable.
    *   `any(iterable)` returns `True` if any element of the iterable is "truthy." It returns `False` for an empty iterable.