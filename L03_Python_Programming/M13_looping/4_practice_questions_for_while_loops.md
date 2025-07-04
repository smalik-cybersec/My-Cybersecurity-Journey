Module 13, Lesson 04 is dedicated to **practice questions for `while` loops**. These exercises are crucial for solidifying understanding and practical application of `while` loop concepts previously introduced in Lesson 02. The practice questions found in the sources cover various aspects of `while` loop control, user interaction, and data manipulation.

The primary goal of these practice questions is to help learners:
*   Understand and apply the fundamental mechanics of `while` loops, where a block of code executes repeatedly as long as a specified condition remains `True`.
*   Learn how to **control the flow of `while` loops** using conditional tests, flags, `break` statements, and `continue` statements.
*   Practise **avoiding infinite loops** by ensuring there is always a mechanism for the loop to terminate.
*   Integrate `while` loops with other Python constructs like **user input**, **lists**, and **dictionaries**.

Here are examples of `while` loop practice questions and scenarios drawn from the sources:

*   **Basic Counting and User Termination**
    *   **Exercise 7-4: Pizza Toppings**: This exercise requires writing a loop that repeatedly prompts the user for pizza toppings. The loop continues until the user enters a specific "quit" value, and for each valid topping, a confirmation message is printed. This reinforces handling user input and a clear exit condition.
    *   **Exercise 7-5: Movie Tickets**: This involves asking users for their age within a loop and then determining the cost of their movie ticket based on age ranges. The loop needs to continue prompting for ages, implying a mechanism for the user to quit.
    *   **Question 13 (Chapter 2 Practice Questions)**: This question asks to "Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop". This helps compare and contrast `for` and `while` loop structures for repetitive tasks where the number of iterations is known.

*   **Controlling Loop Flow with `break` and `continue`**
    *   **Exercise 7-6: Three Exits**: This builds on previous exercises by challenging the user to implement different ways to stop a `while` loop. Learners are asked to create versions that use:
        *   A **conditional test in the `while` statement** itself.
        *   An **`active` variable (flag)** to control the loop's running state. This is useful in complex programs like games where multiple events might need to stop the program.
        *   A **`break` statement** to exit the loop immediately upon a specific user input (e.g., 'quit'). The `break` statement can be used in any of Python's loops, including `for` loops.
    *   The `swordfish.py` example demonstrates how a `continue` statement can be used to skip the rest of the current iteration of a loop and return to the beginning based on a conditional test.

*   **Handling Infinite Loops**
    *   **Exercise 7-7: Infinity**: This exercise explicitly asks learners to "Write a loop that never ends, and run it". This is designed to teach how to handle (and avoid) accidental infinite loops, usually by pressing **`CTRL-C`** to terminate the program.

*   **Manipulating Data Structures with `while` Loops**
    *   **Exercise 7-8: Deli**: This involves two lists: `sandwich_orders` and `finished_sandwiches`. A `while` loop is used to process orders by moving items from one list to another.
    *   **Exercise 7-9: No Pastrami**: Building on the "Deli" exercise, this requires using a `while` loop to remove *all instances* of a specific value (e.g., 'pastrami') from a list, unlike the `remove()` method which only deletes the first occurrence.
    *   **Exercise 7-10: Dream Vacation**: This task uses a `while` loop to poll users for input and store their responses in a dictionary, demonstrating how to fill data structures dynamically.

*   **Integration with Other Concepts**
    *   `While` loops are frequently used with the `input()` function to make programs interactive, allowing them to accept and process user input until a specific condition is met.
    *   They are also used in conjunction with **functions**, for example, continuously asking for user names via a function within a `while True` loop that allows users to quit at any prompt.
    *   In the context of file handling, `while` loops can be used for tasks like collecting user input to write to a file (e.g., "Guest Book" and "Programming Poll" exercises).
    *   For **input validation**, `while` loops are essential for repeatedly prompting the user until a valid response is provided. Although the `PyInputPlus` module simplifies this, understanding the underlying `while` loop logic is still important.

These practice questions provide hands-on experience, reinforcing the theoretical knowledge of `while` loops, their various control mechanisms, and their common applications in interactive Python programs and data manipulation. They also emphasize the importance of writing robust code that handles user input and has clear termination conditions.