Lesson 08 introduces **Membership Operators** in Python. These operators are used to test whether a specified value is present within a sequence. They evaluate to a **Boolean value**, either `True` or `False`.

Python provides two membership operators:

*   **`in`**: This operator returns `True` if the specified value is found **within** the sequence.
*   **`not in`**: This operator returns `True` if the specified value is **not found** within the sequence. For example, `if user not in banned_users:` clearly checks if a user is not in a list of banned users. Using `if a is not b` is a recommended style for negation, but `not in` is the specific operator for membership negation.

**How Membership Operators Work with Different Data Types:**

*   **Lists**: The `in` and `not in` operators can be used to determine if an item exists within a list.
    *   For example, `'mushrooms' in requested_toppings` would return `True` if 'mushrooms' is in the list `requested_toppings`.
*   **Strings**: These operators are used to check if a substring is present within a larger string. For instance, `'Hello' in 'Hello, World'` would evaluate to `True`.
*   **Tuples**: Membership operators function with tuples in a similar way to lists and strings.
*   **Sets**: The `in` operator works efficiently with sets to check for value membership. Sets do not maintain any specific order for their items. Due to their underlying hash table implementation, membership tests with sets are **extremely fast**, even with a large number of items.
*   **Dictionaries**:
    *   When used with a dictionary, the `in` operator checks for the existence of a **key** by default.
    *   To check if a specific **value** exists within a dictionary (rather than a key), you would typically use `value in dictionary.values()`.

**Custom Types and Operator Overloading:**

*   For user-defined classes, the `in` operator internally relies on the special method **`__contains__`**. By implementing this `__contains__` method in your custom class, you can define how instances of your class respond to the `in` operator.
*   Unlike certain other operators such as `is`, `and`, `or`, and `not`, which cannot be overloaded in Python, bitwise operators (like `&`, `|`, `~`, `<<`, `>>`, `^`) *can* be overloaded. The ability to implement `__contains__` for custom types allows for flexible and "Pythonic" behavior for membership testing.