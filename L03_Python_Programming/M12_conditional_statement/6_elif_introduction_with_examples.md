Module 12, Lesson 06 introduces the **`elif` statement**, which is an extension of the conditional logic you've learned with `if` and `if-else` statements. The `elif` (short for "else if") statement allows your program to test **more than two possible situations**.

### Purpose of `elif` Statements
While an `if-else` statement provides two paths—one if a condition is true, and one if it's false—many real-world scenarios involve more complex decision-making with multiple potential outcomes. The `if-elif-else` chain is designed for these situations. It allows Python to execute a specific block of code based on which of several conditions is met first.

### Structure of an `if-elif-else` Chain
An `if-elif-else` chain consists of:
1.  An initial **`if` statement** with its `conditional_test` and indented code block.
2.  One or more **`elif` statements**:
    *   The `elif` keyword.
    *   A **conditional test** (an expression that evaluates to `True` or `False`).
    *   A **colon (`:`)** marking the end of the `elif` line.
    *   An **indented block of code** (the `elif` clause), which contains instructions to be executed if its condition is `True`.
3.  An optional **`else` statement**:
    *   The `else` keyword, placed on a new line and unindented to match the `if` and `elif` statements.
    *   A **colon (`:`)** after the `else` keyword.
    *   An indented block of code (the `else` clause), which runs if none of the preceding `if` or `elif` conditions evaluate to `True`.

### Execution Flow
Python executes an `if-elif-else` chain by running each conditional test in order, from top to bottom.
*   When a test evaluates to **`True`**, the code block immediately following that `if` or `elif` statement is executed.
*   **Python then skips the rest of the tests** in that chain and moves on to any code that follows the entire `if-elif-else` structure.
*   If **all** `if` and `elif` conditions evaluate to `False`, and an `else` block is present, the code within the `else` block is executed.
*   If all conditions are `False` and **no `else` block is provided**, no code within the conditional chain will execute.

It is important to remember that **only one block of code will ever run in an `if-elif-else` chain**. This differs from a series of independent `if` statements, where multiple conditions might evaluate to `True` and thus execute their respective code blocks.

### Examples

Here are some examples of `if-elif-else` statements:

1.  **Amusement Park Admission Pricing**:
    This is a classic scenario where `if-elif-else` is highly effective.
    ```python
    age = 12 #

    if age < 4: # First condition: Is the person under 4 years old?
        price = 0 # If True, set price to $0
    elif age < 18: # Second condition: If not under 4, is the person under 18?
        price = 25 # If True, set price to $25
    else: # If neither of the above conditions were met (i.e., age is 18 or older)
        price = 40 # Set price to $40

    print(f"Your admission cost is ${price}.") #
    ```
    For `age = 12`, the `if age < 4` condition is `False`. Python then checks `elif age < 18`, which is `True`, so `price` is set to `25`. The program then skips the `else` block and prints "Your admission cost is $25.". You can add as many `elif` blocks as needed to handle more age groups or conditions, such as a senior discount.

2.  **Alien Colours #3 (Exercise 5-5)**:
    This exercise extends the "Alien Colors" scenario to include more than two outcomes.
    ```python
    alien_color = 'yellow' #

    if alien_color == 'green': # Check if alien is green
        print("You just earned 5 points!")
    elif alien_color == 'yellow': # If not green, check if yellow
        print("You just earned 10 points!")
    else: # If neither green nor yellow (e.g., red)
        print("You just earned 15 points!")
    ```
    If `alien_color` is `'yellow'`, the first `if` condition (`alien_color == 'green'`) is `False`. The `elif` condition (`alien_color == 'yellow'`) is `True`, so the player earns 10 points, and the `else` block is skipped.

3.  **Order of `elif` Statements**:
    The order of `elif` statements matters because Python executes tests sequentially and stops at the first `True` condition. Consider this example:
    ```python
    age = 3000

    if age < 12:
        print('You are a kiddo.')
    elif age > 100: # This condition comes before age > 2000
        print('You are a grannie.') # This will execute if age is 3000
    elif age > 2000:
        print('You are an undead, immortal vampire.')
    else:
        print('You are just a regular adult.')
    ```
    For `age = 3000`, the first `if` is `False`. The first `elif` (`age > 100`) is `True`, so "You are a grannie." is printed. The condition `age > 2000` is never checked because the previous `elif` condition was already met. If the order of the `elif` statements were swapped, the "undead, immortal vampire" message would print instead.

### Styling `if-elif-else` Statements
According to PEP 8, it is recommended to use a **single space around comparison operators** (e.g., `age < 4` is preferred over `age<4`). This spacing enhances code readability.

The `if-elif-else` structure provides a robust way to handle multiple mutually exclusive conditions in your programs, making your code more responsive and intelligent.