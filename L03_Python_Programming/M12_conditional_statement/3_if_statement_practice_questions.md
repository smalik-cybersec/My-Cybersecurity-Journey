Building on our discussion of Module 12, Lesson 02, which introduced `if` statements with examples, Lesson 03 focuses on **practice questions** related to `if` statements. These exercises are designed to solidify your understanding of conditional tests and how to use `if`, `if-else`, and `if-elif-else` structures effectively in Python programs.

Here are some practice questions and concepts related to `if` statements, drawing from the sources:

*   **Conditional Tests**: At the heart of every `if` statement is a conditional test, which is an expression that evaluates to either `True` or `False`. Python uses these Boolean values to determine whether the code block associated with the `if` statement should be executed.
    *   **Exercise 5-1: Conditional Tests**: You should **write a series of conditional tests** and for each, print a statement describing the test and your prediction for its result, followed by the actual result. For instance:
        ```python
        car = 'subaru'
        print("Is car == 'subaru'? I predict True.")
        print(car == 'subaru') # Output: True
        print("\nIs car == 'audi'? I predict False.")
        print(car == 'audi')   # Output: False
        ```
        You should aim to create at least ten tests, with at least five evaluating to `True` and five to `False`.
    *   **Exercise 5-2: More Conditional Tests**: This exercise expands on conditional tests, asking you to include at least one `True` and one `False` result for each of the following types of comparisons:
        *   Equality (`==`) and inequality (`!=`) with strings.
        *   Tests using the `lower()` method (e.g., ignoring case when checking for equality).
        *   Numerical tests involving equality (`==`), inequality (`!=`), greater than (`>`), less than (`<`), greater than or equal to (`>=`), and less than or equal to (`<=`).
        *   Tests using the `and` keyword (where both conditions must be `True` for the overall expression to be `True`) and the `or` keyword (where at least one condition must be `True` for the overall expression to be `True`).
        *   Checking whether a value is **in a list** using the `in` keyword.
        *   Checking whether a value is **not in a list** using the `not in` keyword.

*   **Simple `if` Statements**: The simplest `if` statement includes one test and one action. If the conditional test is `True`, the indented code block (the `if` clause) is executed; otherwise, it is skipped.
    *   **Exercise 5-3: Alien Colors #1**: Create a variable `alien_color` and assign it a color ('green', 'yellow', or 'red'). Write an `if` statement to test if the `alien_color` is 'green'. If it is, print a message stating the player earned 5 points. Create two versions of this program: one that passes the `if` test and one that fails (producing no output).

*   **`if-else` Statements**: These statements provide an alternative path of execution. If the `if` condition is `True`, its block runs; if `False`, the `else` block is executed. An `else` statement does not have a condition.
    *   **Exercise 5-4: Alien Colors #2**: Choose an alien color and write an `if-else` chain. If the alien is green, print a message for 5 points. Otherwise (if it's not green), print a message for 10 points. Write one version to run the `if` block and another to run the `else` block.

*   **`if-elif-else` Chains**: This structure allows testing multiple conditions sequentially. Python executes the code block for the first condition that evaluates to `True` and then skips the rest of the chain. An `elif` statement provides another condition that is checked only if all previous conditions were `False`.
    *   **Exercise 5-5: Alien Colors #3**: Expand your `if-else` chain from Exercise 5-4 into an `if-elif-else` chain. Assign points based on color: 5 for green, 10 for yellow, and 15 for red. Create three versions of the program to ensure each message is printed for the appropriate alien color.
    *   **Exercise 5-6: Stages of Life**: Write an `if-elif-else` chain to determine a person's stage of life based on their age (e.g., baby, toddler, kid, teenager, adult, elder).
    *   **Question 9 (from Automate the Boring Stuff)**: Write code that prints "Hello" if 1 is stored in `spam`, "Howdy" if 2 is stored in `spam`, and "Greetings!" if anything else is stored in `spam`.

*   **Using `if` Statements with Lists**: `if` statements can be combined with lists to handle special values or changing conditions. An empty list evaluates to `False` in an `if` statement, while a list with at least one item evaluates to `True`.
    *   **Checking for Special Items**: This involves identifying specific elements in a list that need to be handled differently, as shown in the example with car names where 'bmw' is printed in uppercase while others are in title case.
    *   **Exercise 5-7: Favorite Fruit**: Make a list of three favorite fruits and then write five separate `if` statements, each checking if a certain fruit is in your list and printing a statement if `True`.
    *   **Exercise 5-8: Hello Admin**: This type of exercise involves iterating through a list of usernames and using `if` statements to greet them, with a special greeting for an 'admin' user.
    *   **Exercise 5-9: No Users**: Modifying the previous exercise to handle an empty list of users, printing a message like "We need to find some users!".
    *   **Exercise 5-10: Checking Usernames**: Comparing a list of new usernames against a list of current usernames to ensure uniqueness, using `if` statements and possibly string methods like `lower()` for case-insensitive comparison.
    *   **Exercise 5-11: Ordinal Numbers**: Store numbers 1 through 9 in a list. Loop through the list and use an `if-elif-else` chain *inside* the loop to print the correct ordinal ending (e.g., "1st", "2nd", "3rd") for each number.

*   **Styling `if` Statements**: For readability, PEP 8 (Python Enhancement Proposal 8) recommends using a **single space around comparison operators** (e.g., `if age < 4:` is preferred over `if age<4:`).
    *   **Exercise 5-12: Styling if statements**: Review and apply appropriate styling to your conditional tests.

These practice questions provide hands-on experience with `if` statements, conditional tests, and their application in various programming scenarios.