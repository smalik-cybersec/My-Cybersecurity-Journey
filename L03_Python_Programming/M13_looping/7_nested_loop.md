**Module 13: Looping - Lesson 07: Nested Loop**

Nested loops involve placing one loop inside another, allowing for iteration over multi-dimensional data structures or complex, related collections. The inner loop will complete all of its iterations for each single iteration of the outer loop.

Here's a breakdown of nested loops based on the provided sources:

*   **Definition and Purpose**
    *   A **`for` loop** repeats a block of code once for each item in a sequence. When one `for` loop is placed inside another, it forms a nested loop.
    *   This structure is particularly useful for working with data that has multiple levels or dimensions, such as **matrices** (lists of lists).
    *   Python uses **indentation** to define which lines of code belong to the inner loop. The inner loop's code block must be indented further than the outer loop's code.

*   **How Nested Loops Iterate**
    *   For every single item processed by the outer loop, the inner loop will execute completely through all of its items.
    *   For example, when iterating over a 2D grid, the outer loop might iterate over rows, and the inner loop would iterate over columns within that row.
    *   Choosing meaningful variable names (e.g., `for cat in cats:`) is helpful for readability, especially in nested loops, to distinguish between a single element and the entire list.

*   **Practical Applications and Examples**
    *   **Processing 2D Data**: Nested `for` loops are commonly used to traverse and manipulate elements in two-dimensional structures like spreadsheets or game boards. For instance, in Conway's Game of Life, nested loops can print or calculate the state of each cell in a grid.
    *   **Generating Combinations**: They can be used to generate combinations or pairs of items from different sequences. For example, generating multiple-choice options for a quiz might involve a third `for` loop nested inside to create those options. Similarly, to duplicate an image by tiling it, nested `for` loops can iterate over `left` and `top` coordinates.
    *   **Web Scraping**: In web scraping, nested loops can control the order of requests, such as looping through all topics before moving to the next website to distribute the load more evenly on web servers.
    *   **Templating Engines**: In frameworks like Django, template tags such as `{% for ... %}` can effectively create nested iteration when displaying structured data.

*   **List Comprehensions with Nested Loops**
    *   Python provides a concise syntax called **list comprehensions** that can replace multi-line `for` loops, including nested ones.
    *   When using multiple `for` subexpressions in a list comprehension, they run in the order provided, from left to right.
    *   For example, flattening a matrix (a list containing other list instances) into one flat list can be done with a list comprehension like `flat = [x for row in matrix for x in row]`.
    *   **Important Consideration**: It is advised to **avoid using more than two control subexpressions** (e.g., two `for` loops, two `if` conditions, or one of each) in a single comprehension. Comprehensions that are more complex than this become very difficult to read, and it is recommended to use normal `if` and `for` statements instead, potentially with a helper function.

*   **Flow Control within Nested Loops**
    *   The **`break` statement** can be used to immediately exit the innermost loop it is contained within.
    *   The **`continue` statement** skips the rest of the current iteration of the innermost loop and moves to the next item or increment of that loop's counter. These statements can only be used inside `while` or `for` loops.

*   **Indentation Errors**
    *   Python relies heavily on indentation to define code blocks.
    *   An **indentation error** can lead to **logical errors**, where code meant to be part of a loop (or an inner loop) runs only once after the loop finishes because it is improperly unindented. If you expect an action to repeat for each item but it runs only once, check your indentation.