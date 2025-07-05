Building upon our previous discussion on the introduction to functions, Lesson 02 delves into the practical aspects of **declaring and calling functions** in Python. Functions are essential for structuring code, making it more readable, reusable, and easier to manage and debug.

### Declaring a Function

A function definition, or declaration, tells Python how to create a reusable block of code that performs a specific task.

*   **Syntax**:
    *   Function definitions **begin with the `def` keyword**.
    *   This is followed by the **function name**, then **parentheses `()`** that may contain parameters, and finally a **colon `:`**. For example, `def greet_user():`. The parentheses are required even if the function takes no information.
    *   The **body of the function** consists of all the **indented lines** that follow the `def` statement. The code within this indented block is executed only when the function is *called*, not when it is first defined.

*   **Parameters**:
    *   The variables listed inside the parentheses in the function's definition are called **parameters**. These are placeholders for the information the function needs to perform its job.
    *   You can define your own functions that accept arguments, which are stored in these parameters.

*   **Docstrings**:
    *   It is considered **best practice** to include a **docstring** immediately after the `def` statement.
    *   A docstring is a multiline string (enclosed in triple quotes `"""Docstring goes here"""`) that concisely describes what the function does, its parameters, and what it returns. Python uses docstrings when generating documentation for your functions. They are invaluable for communicating with future users of your code, as programmers can often use a function by reading only its docstring.

### Calling a Function

Once a function is defined, you can **call** it to execute the code within its body.

*   **Basic Call Syntax**:
    *   To call a function, you write its **name followed by parentheses `()`**. Any information the function needs is provided inside these parentheses. For example, `greet_user()`.
    *   When a function is called, the program execution jumps to the beginning of the function's code block, executes it, and then returns to the line that called the function.

*   **Arguments**:
    *   The values passed to a function call are known as **arguments**. These arguments are assigned to the parameters defined in the function's signature.
    *   **Positional Arguments**: Arguments can be passed by position, meaning the order in which they are provided matches the order of parameters in the function definition. For instance, `describe_pet('hamster', 'harry')` would assign 'hamster' to `animal_type` and 'harry' to `pet_name`.
    *   **Keyword Arguments**: Arguments can also be specified by keyword, explicitly naming the parameter to which each argument should be assigned (e.g., `describe_pet(pet_name='harry', animal_type='hamster')`). The order of keyword arguments does not matter. Using keyword arguments can improve clarity, especially for optional arguments or when positional arguments could be confusing.
    *   **Arbitrary Number of Positional Arguments (`*args`)**: Functions can be defined to accept a variable number of positional arguments by prefixing a parameter with an asterisk (`*`). This collects all remaining positional arguments into a tuple. For example, `def log(message, *values):` allows `log('My numbers are', 1, 2)` and `log('Hi there')`.
    *   **Arbitrary Number of Keyword Arguments (`**kwargs`)**: Similarly, two asterisks (`**`) before a parameter name (e.g., `**kwargs`) allow a function to accept any number of keyword arguments, which are collected into a dictionary.
    *   **Positional-Only and Keyword-Only Arguments**:
        *   **Keyword-only arguments** are defined after a single asterisk (`*`) in the argument list (e.g., `def func(a, *, b):`). These arguments *must* be supplied by keyword, which enhances clarity.
        *   **Positional-only arguments** are defined before a single forward slash (`/`) in the argument list (e.g., `def func(a, /, b):`). These arguments *cannot* be supplied using keywords, helping to reduce coupling by allowing parameter names to change without affecting callers. Parameters between the `/` and `*` can be supplied by either position or keyword, which is the default behavior.

*   **Return Values**:
    *   Functions can **return values** to the caller using the `return` statement.
    *   If a function does not have an explicit `return` statement, it implicitly returns `None`.
    *   Functions can return **multiple values**. These values are returned together in a tuple, which the calling code can then unpack into multiple variables. For example, `minimum, maximum = get_stats(lengths)`.

*   **Functions as First-Class Objects**:
    *   In Python, **functions are first-class objects**. This means they can be:
        *   Created at runtime.
        *   Assigned to variables or elements in data structures.
        *   Passed as arguments to other functions (known as **higher-order functions** when a function takes another function as an argument or returns one).
        *   Returned as the result of a function.
    *   This capability enables flexible programming styles, including functional programming paradigms. For example, you can put functions in a list and then iterate through the list to invoke them.

Functions provide a powerful way to organize and reuse code, making programs shorter, more manageable, and easier to update.