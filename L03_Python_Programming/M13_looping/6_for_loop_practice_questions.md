Here are some practice questions to deepen your understanding of `for` loops in Python, drawing on the information in the sources.

### **Lesson 06: For Loop Practice Questions**

**Basic `for` Loop Iteration**

1.  **Iterating Through a List**:
    *   Create a list named `favorite_foods` containing at least five different food items.
    *   Write a **`for` loop** to print each food item in the list, along with a statement like "I really enjoy [food item]!". This demonstrates how a `for` loop repeats steps for each item in a list.
    *   After the loop has finished, add a line of code that prints a general concluding statement about your love for food. Note that this statement will execute only once after the loop has processed all items.

2.  **Iterating Through a String**:
    *   Define a string variable `my_word = "Python"`.
    *   Write a `for` loop that iterates through each **character** in `my_word` and prints each character on a new line. `For` loops can iterate over sequence types like strings.

**Using `range()` with `for` Loops**

3.  **Counting Up**:
    *   Use a `for` loop and the `range()` function to print the numbers from 1 to 10 (inclusive). The `range()` function is often used with `for` loops to generate a series of numbers, typically starting from 0 by default, and going up to, but not including, the `stop` value if one argument is provided.

4.  **Counting with a Step**:
    *   Use a `for` loop and the `range()` function to print all **even numbers** from 2 to 20 (inclusive). Remember that `range()` can take an optional third argument for the step size.

5.  **Counting Down**:
    *   Use a `for` loop and the `range()` function to print numbers from 5 down to 0 (inclusive). A negative step argument can be used to count down.

**`for` Loops with Collections**

6.  **Looping Through a Dictionary**:
    *   Create a dictionary called `capitals` that stores at least three country-capital pairs (e.g., `'USA': 'Washington D.C.'`).
    *   Write a `for` loop to **print each key-value pair** from the dictionary.
    *   Then, write another `for` loop to print only the **country names** (keys). Looping through keys is the default behavior when iterating over a dictionary.
    *   Finally, write a `for` loop to print only the **capital cities** (values).

7.  **Looping Through a Tuple**:
    *   Define a tuple `dimensions = (200, 50)`.
    *   Use a `for` loop to print each dimension.
    *   *Challenge:* Briefly explain why you might choose to use a tuple instead of a list for `dimensions` in this context. (Hint: Consider the mutability of these data types).

**Flow Control within `for` Loops (`break` and `continue`)**

8.  **Using `break`**:
    *   Create a list of numbers `nums =`.
    *   Write a `for` loop that iterates through `nums`. If the number is greater than 50, print "Number too large, stopping!" and **exit the loop** immediately using the `break` statement. Otherwise, print the current number. The `break` statement allows you to exit any Python loop (including `for` loops) prematurely.

9.  **Using `continue`**:
    *   Create a list of integers `numbers =`.
    *   Write a `for` loop that iterates through `numbers`. If a number is odd, print "Skipping odd number: [number]" and **skip the rest of the current iteration** using the `continue` statement, moving to the next number. If the number is even, print "Processing even number: [number]". The `continue` statement causes the program to skip the rest of the current loop iteration and move to the next item in the sequence.

**Advanced `for` Loop Concepts**

10. **`enumerate()` Function**:
    *   Create a list `fruits = ['apple', 'banana', 'cherry', 'date']`.
    *   Use a `for` loop with `enumerate()` to print each fruit along with its **index** (starting the count from 1 instead of 0). For example: "1: apple", "2: banana", etc. `enumerate()` provides both the index and the item during iteration and allows you to specify a starting count.

11. **`zip()` Function**:
    *   You have two lists: `names = ['Alice', 'Bob', 'Charlie']` and `ages =`.
    *   Use a `for` loop with `zip()` to iterate through both lists in parallel and print a message like "Alice is 30 years old." for each pair. `zip()` is used to process iterators in parallel.
    *   *Self-reflection:* What happens if one list is shorter than the other when using `zip()`?

12. **List Comprehensions**:
    *   **Simple Comprehension:** Create a new list called `cubes` that contains the cube of each integer from 1 to 10, using a single **list comprehension**. List comprehensions offer a concise way to create new lists from an existing sequence, often replacing multi-line `for` loops.
    *   **Comprehension with Condition:** Create a new list called `even_squares` that contains the square of only the even numbers from 0 to 9, using a single **list comprehension** with a conditional filter.
    *   *Challenge:* Convert the problem "Write a list comprehension that results in a list of every letter in the word smogtether capitalized." into code.

13. **Nested `for` Loops**:
    *   Print a simple multiplication table (e.g., up to 3x3) using **nested `for` loops**.
        *   Example output for 3x3:
            ```
            1 x 1 = 1
            1 x 2 = 2
            1 x 3 = 3
            2 x 1 = 2
            ...
            3 x 3 = 9
            ```

**Common Pitfalls and Best Practices**

14. **Indentation Errors**:
    *   Consider the following code snippet. Identify and describe the likely **indentation errors** if `print("Finished processing.")` was intended to run once after the loop, but was mistakenly indented.
        ```python
        for i in range(3):
            print(f"Number: {i}")
            print("Finished processing.")
        ```
    *   How would you correct this code to ensure "Finished processing." runs only once after the loop?

15. **`else` Block with `for` Loop**:
    *   Explain what the `else` block after a `for` loop does in Python. When does it execute, and when does it not? Provide a brief code example to illustrate. Python loops have an extra feature not found in most other languages: an `else` block immediately after the loop's repeated interior block. This `else` block executes **only if the loop completes without encountering a `break` statement**. It will also run if the loop iterates over an empty sequence.
    *   Based on the sources, what is the general recommendation regarding the use of `else` blocks after loops, and why? The sources advise **avoiding `else` blocks after loops** because their behavior is not intuitive and can be confusing.