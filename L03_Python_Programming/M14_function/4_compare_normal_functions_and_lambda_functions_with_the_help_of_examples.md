Both normal functions (defined using the `def` statement) and lambda functions (anonymous functions defined using the `lambda` keyword) are fundamental callable entities in Python, though they serve different primary purposes and have distinct characteristics.

### Normal Functions (`def` functions)

**Normal functions** are **named blocks of code** designed to perform a specific job. They are created using the `def` statement.

**Key characteristics of normal functions**:
*   **Named**: They have a specific name, which makes them easier to identify, call, debug, and reference throughout a program.
*   **Reusable**: Once defined, they can be called multiple times, promoting code reuse, clarifying intention, and reducing bugs.
*   **Flexible Body**: Their body can contain multiple statements, including assignments, loops (`while`, `for`), conditional statements (`if`, `elif`, `else`), `try`/`except` blocks, and other complex logic.
*   **Parameters and Arguments**: They can accept a fixed or arbitrary number of arguments, which can be passed positionally or by keyword, and can have default values.
*   **Return Values**: They can return a single value, multiple values (as a tuple), or `None` (though raising exceptions for special situations is preferred over returning `None`).
*   **Docstrings**: They can have docstrings to provide documentation, accessible at runtime, making them easier to understand for other developers.
*   **Attributes**: Possess many attributes, including `__doc__` and `__name__`, allowing for introspection.

**Example of a normal function**:
```python
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

hello() # Calling the function
```
This function can be called multiple times, like `hello()`. Similarly, a function could accept arguments and return a value:
```python
def remainder(number, divisor): # Defines a function with two parameters
    return number % divisor # Returns a single value

assert remainder(20, 7) == 6 # Example call
```
Functions can also be used to organize larger tasks, like processing models.

### Lambda Functions (Anonymous Functions)

**Lambda functions** are **unnamed** (or anonymous) functions defined using the `lambda` keyword. They are typically used for creating **small, one-off functions**.

**Key characteristics of lambda functions**:
*   **Anonymous**: They do not have a name, which can make debugging and understanding stack traces more challenging.
*   **Single Expression Body**: The **syntax of Python limits the body of lambda functions to be pure expressions**. This means they **cannot contain assignments** or other Python **statements** like `while`, `try`, etc.. This is a "price to pay for Python's highly readable syntax".
*   **Concise Syntax**: They follow the general syntax: `lambda <PARAM>: <RETURN EXPRESSION>`.
*   **Contextual Use**: Their best use is in the context of an argument list, particularly with higher-order functions that expect a small function as an argument.

**Example of a lambda function for sorting**:
Instead of defining a separate `def` function for a simple operation, a `lambda` can be used directly as the `key` for sorting:
```python
items = [[0, 'a', 2], [5, 'b', 0], [2, 'c', 1]]

# Using a normal function as a key:
def second(item):
    return item
sorted_by_second = sorted(items, key=second)
# Expected output: [[0, 'a', 2], [5, 'b', 0], [2, 'c', 1]]

# Using a lambda function as a key:
sorted_by_second_lambda = sorted(items, key=lambda item: item)
# Expected output: [[0, 'a', 2], [5, 'b', 0], [2, 'c', 1]]

sorted_by_third_lambda = sorted(items, key=lambda item: item)
# Expected output: [[5, 'b', 0], [2, 'c', 1], [0, 'a', 2]]
```
Other examples of lambda functions used for sorting include sorting a list of `Tool` objects by their `name` or `weight` attributes.

### Similarities between Normal and Lambda Functions

Despite their differences, both normal and lambda functions are **first-class objects** in Python. This means they can be treated like any other data type (e.g., integers, strings, dictionaries) and possess the following capabilities:
*   They can be **created at runtime**.
*   They can be **assigned to a variable** or an element in a data structure. For example, `fact = factorial` assigns a function to a variable. You can put multiple functions into a list and iterate through it to invoke them.
*   They can be **passed as an argument to another function** (as seen with the `key` parameter in `sort()` or `sorted()`, and with `map()` or `filter()`).
*   They can be **returned as the result of a function**.

### Why and When to Use (and Not Use) Lambda Functions

Lambda functions are generally useful for situations where a function expects a small, simple function as an argument. Historically, they were motivated by functional programming tools like `map()` and `filter()`. For instance, `map(lambda x: x**2, a)` applies squaring to each element.

**Limitations and best practices**:
*   **Readability**: Overuse or creating non-trivial lambdas can lead to code that is **poorly documented and confusing to read**. The syntactic restrictions can make them unreadable or unworkable.
*   **Prefer Comprehensions**: **List comprehensions (and dictionary/set comprehensions)** are often **clearer than `map()` and `filter()` with `lambda` expressions**, achieving the same result without needing a `lambda`. The introduction of list comprehension syntax significantly diminished the need for `map`, `filter`, and `lambda`.
*   **Use `def` for Complexity**: For more complex logic or functions that will be reused, defining a named function with `def` is generally clearer and easier to maintain.
*   **`operator` Module**: The `operator` module provides function equivalents for many arithmetic operators (e.g., `operator.mul` instead of `lambda a, b: a*b`), further minimizing the need for simple lambdas in operations like `reduce()`.
*   **Lundh's Refactoring Recipe**: If a `lambda` makes code hard to understand, one recommended refactoring procedure is to comment what it does, think of a name, convert it to a `def` statement with that name, and then remove the comment.

While some services like **AWS Lambda** are referred to as "Lambda functions," it's important to distinguish them. These are serverless computing functions often implemented using regular Python `def` statements, not necessarily Python `lambda` expressions.