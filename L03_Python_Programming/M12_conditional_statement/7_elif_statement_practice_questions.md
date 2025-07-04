Module 12, Lesson 07 focuses on **practice questions for `elif` statements**, building upon the introduction provided in Lesson 06.

As a reminder from Lesson 06, the **`elif` statement**, which is short for "else if", allows your program to test **more than two possible situations** [Source 128]. While an `if-else` statement provides two paths, the `if-elif-else` chain handles scenarios with multiple potential outcomes [Source 128].

**Key points about `if-elif-else` chains:**
*   Python executes tests in order, from top to bottom [Source 128].
*   When a test evaluates to **`True`**, its corresponding code block is executed, and Python **skips the rest of the tests** in that chain, moving on to any code after the entire structure [Source 128].
*   If all `if` and `elif` conditions evaluate to `False`, and an `else` block is present, the code within the `else` block is executed [Source 128].
*   If all conditions are `False` and no `else` block is provided, no code within the conditional chain will execute [Source 264].
*   **Only one block of code will ever run in an `if-elif-else` chain** [Source 128, 137, 264]. This is a crucial distinction from a series of independent `if` statements, where multiple conditions could be true and their respective blocks executed [Source 135, 137].
*   The **order of `elif` statements matters** because Python stops at the first `True` condition [Source 132, 266]. If you swap conditions, it can lead to unexpected results (bugs) because a broader condition might be met and executed before a more specific one that was intended [Source 266, 267, 268].

Here are some practice questions to help you apply your understanding of `if-elif-else` statements:

***

### Practice Questions for `elif` Statements

**1. Stages of Life (Exercise 5-6)** [Source 140, 141]
Write an `if-elif-else` chain that determines a person’s stage of life based on their `age`.
*   Set a value for the variable `age`.
*   If the person is less than 2 years old, print: **"The person is a baby."**
*   If the person is at least 2 years old but less than 4, print: **"The person is a toddler."**
*   If the person is at least 4 years old but less than 13, print: **"The person is a kid."**
*   If the person is at least 13 years old but less than 20, print: **"The person is a teenager."**
*   If the person is at least 20 years old but less than 65, print: **"The person is an adult."**
*   If the person is age 65 or older, print: **"The person is an elder."**

Test your program with various ages: `1`, `3`, `10`, `16`, `30`, and `70`.

**2. Alien Colours #3 (Exercise 5-5)** [Source 139, 140]
Turn your `if-else` chain from Lesson 05, Exercise 2 into an `if-elif-else` chain.
*   Choose a colour for an alien (e.g., `'green'`, `'yellow'`, or `'red'`) and store it in a variable called `alien_color`.
*   If the `alien_color` is `'green'`, print: **"You just earned 5 points!"**
*   If the `alien_color` is `'yellow'`, print: **"You just earned 10 points!"**
*   If the `alien_color` is `'red'`, print: **"You just earned 15 points!"**

Write three versions of this program, making sure each message is printed for the appropriate colour alien.

**3. Movie Tickets (Exercise 7-5)** [Source 164]
A movie theatre charges different ticket prices depending on a person’s `age`.
*   If a person is under the age of 3, the ticket is free.
*   If they are between 3 and 12 (inclusive), the ticket is $10.
*   If they are over age 12, the ticket is $15.

Write a program that takes a person's `age` as input and tells them the cost of their movie ticket.

Test your program with ages: `2`, `8`, `12`, `13`, `25`.

**4. Grade Calculator**
Write a program that takes a student's numerical `score` (0-100) as input and prints their corresponding letter grade based on the following scale:
*   90-100: A
*   80-89: B
*   70-79: C
*   60-69: D
*   Below 60: F

Test your program with scores: `95`, `82`, `70`, `64`, `59`.

**5. Fruit Availability and Pricing**
You're building a simple fruit stand program. You have a few types of fruits with different prices, and some are out of stock.
*   Create a variable `requested_fruit` and assign it a value (e.g., `'apple'`, `'banana'`, `'orange'`, `'grape'`).
*   Use an `if-elif-else` chain to determine the price or availability message:
    *   If `requested_fruit` is `'apple'`, print: **"Apples are $1.50 per unit."**
    *   If `requested_fruit` is `'banana'`, print: **"Bananas are $0.75 per unit."**
    *   If `requested_fruit` is `'orange'`, print: **"Oranges are $1.20 per unit."**
    *   If `requested_fruit` is `'grape'`, print: **"Sorry, grapes are currently out of stock."**
    *   For any other `requested_fruit`, print: **"We don't sell that fruit."**

Test your program with `'apple'`, `'orange'`, `'grape'`, and `'kiwi'`.