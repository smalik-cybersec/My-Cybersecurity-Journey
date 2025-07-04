Module 12, Lesson 05 focuses on **practice questions for `if-else` statements**, building upon the introduction and examples covered in Lesson 04. An `if-else` statement is a control flow structure that enables your program to choose between two distinct actions: one if a condition is `True`, and another if the condition is `False`. One of these two actions will always be executed.

The `if-else` structure consists of an `if` statement with its conditional test, followed by an `else` statement. If the `if` condition evaluates to `True`, the code block under the `if` is executed. If it evaluates to `False`, the code block under the `else` statement is executed. The `else` statement itself does not have a condition.

Here are some practice questions to help you solidify your understanding of `if-else` statements:

***

### Practice Questions for `if-else` Statements

**1. Voting Eligibility (Revisited)**
Recall the example of checking voting eligibility.
Write a program that takes a person's `age` as input.
*   If the `age` is 18 or greater, print: **"You are old enough to vote!"** and **"Have you registered to vote yet?"**
*   Otherwise (if the `age` is less than 18), print: **"Sorry, you are too young to vote."** and **"Please register to vote as soon as you turn 18!"**

Test your program with an age of `19` and then with an age of `17`.

**Concept Highlight**: This exercise directly reinforces the core purpose of `if-else`: providing two mutually exclusive paths based on a single condition.

**2. Alien Colours #2 (Exercise 5-4 Revisited)**
This is a direct practice exercise from the sources.
*   Choose a colour for an alien (e.g., `'green'`, `'yellow'`, or `'red'`) and store it in a variable called `alien_color`.
*   Write an `if-else` chain:
    *   If the `alien_color` is `'green'`, print a message that the player just earned **5 points** for shooting the alien.
    *   If the `alien_color` isn't `'green'`, print a message that the player just earned **10 points**.
*   Write two versions of this program: one that makes the `if` block run (e.g., `alien_color = 'green'`) and one that makes the `else` block run (e.g., `alien_color = 'red'` or `alien_color = 'yellow'`).

**Concept Highlight**: This exercise demonstrates how `if-else` handles two outcomes based on whether a specific condition (`alien_color` is 'green') is met or not.

**3. Pizza Topping Check**
Imagine a pizza order system. You want to check if a `requested_topping` is anything other than 'anchovies'.
*   Create a variable `requested_topping` and assign it a value like `'mushrooms'`.
*   Use an `if-else` statement:
    *   If the `requested_topping` is **not equal to** `'anchovies'`, print: **"Hold the anchovies!"**
    *   Otherwise, print: **"Adding anchovies to your pizza."**

Test your program with `requested_topping = 'mushrooms'` and then with `requested_topping = 'anchovies'`.

**Concept Highlight**: This uses the inequality operator (`!=`) in an `if-else` context, which is a common conditional test.

**4. Number Check: Even or Odd**
Write a program that determines if a given number is even or odd.
*   Take an integer `number` (e.g., `10`).
*   Use the **modulo operator (`%`)** to check if the number is divisible by 2.
*   Write an `if-else` statement:
    *   If the `number` is even, print: **"The number is even."**
    *   Otherwise, print: **"The number is odd."**

Test with `number = 10` and `number = 7`.

**Concept Highlight**: This showcases a numerical comparison using an `if-else` structure, specifically using the modulo operator.

**5. List Contains Item**
You have a list of available items, and a customer requests one. You need to tell the customer if the item is available or not.
*   Create a list called `available_items` (e.g., `['apple', 'banana', 'orange']`).
*   Choose a `requested_item` (e.g., `'banana'`).
*   Use the `in` operator with an `if-else` statement:
    *   If the `requested_item` is **in** `available_items`, print: **"Your item is available!"**
    *   Otherwise, print: **"Sorry, that item is currently unavailable."**

Test with `requested_item = 'banana'` and `requested_item = 'grape'`.

**Concept Highlight**: This demonstrates checking for membership in a list using the `in` operator within an `if-else` statement.

***

Remember to use proper **indentation** to define the code blocks within your `if-else` statements. Also, adhere to styling guidelines by using a **single space around comparison operators** (e.g., `age >= 18` instead of `age>=18`).