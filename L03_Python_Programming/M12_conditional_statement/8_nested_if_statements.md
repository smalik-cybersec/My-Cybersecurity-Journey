Module 12, Lesson 08 introduces the concept of **nested `if` statements** [Source 494]. This builds upon your understanding of basic `if` statements, `if-else` statements, and `if-elif-else` chains [Source 65, 112, 115, 117, 493, 494].

### What are Nested `if` Statements?
A **nested `if` statement** occurs when one `if` statement (or an entire `if-elif-else` chain) is placed inside the code block of another `if`, `elif`, or `else` statement [Source 573]. This allows for **more granular control** over program flow by checking increasingly specific conditions only after broader conditions have already been met [Source 573].

### Structure and Execution Flow
The fundamental principle of nested `if` statements relies heavily on **indentation** [Source 69, 114, 216, 217, 571]. In Python, indentation defines code blocks [Source 216, 571], and a block can contain other blocks [Source 217].
*   An inner `if` statement's code block will **only execute if the condition of its outer `if` statement is `True`** [Source 113, 219, 573].
*   If the outer condition evaluates to `False`, the inner `if` statement and its associated blocks are entirely skipped [Source 113, 219].
*   An `else` block or `elif` block is associated with the **nearest preceding `if` or `elif` statement** at the same indentation level [Source 222, 228].

### Example
Consider a scenario where you want to check for a character within a string, and then based on that, perform another check on the string's specific value [Source 573, 574]:

```python
cat = 'spot' # Initial value for the 'cat' variable [Source 573]

if 's' in cat: # Outer if statement: Checks if 's' is in 'cat' [Source 573]
    print("Found an 's' in a cat") # This line executes if 's' is found [Source 574]
    if cat == 'Sheba': # Inner if statement: Only checked if 's' was found [Source 573]
        print("I found Sheba") # Executes if inner condition is True
    else: # Else for the inner if: Executes if inner condition is False [Source 574]
        print("Some other cat") # Executes if 's' is found but 'cat' is not 'Sheba'
else: # Else for the outer if: Executes if 's' is NOT found in 'cat' [Source 574]
    print("a cat without 's'") # Executes if outer condition is False

# Output for cat = 'spot':
# Found an 's' in a cat
# Some other cat
```
In this example:
*   The **outer `if` statement** `if 's' in cat:` is evaluated first. Since `'s'` is in `'spot'`, this condition is `True` [Source 573].
*   The code inside the outer `if` block, `print("Found an 's' in a cat")`, is executed [Source 574].
*   Then, the **nested `if` statement** `if cat == 'Sheba':` is evaluated. Since `'spot'` is not equal to `'Sheba'`, this condition is `False` [Source 573, 574].
*   Consequently, the `else` block associated with the *inner* `if` statement is executed, printing `"Some other cat"` [Source 574].

If `cat` were `'dog'`, the outer `if` condition `if 's' in cat:` would be `False`, and the `else` block of the *outer* `if` would execute, printing `"a cat without 's'"`. The inner `if-else` structure would not be checked at all.

### Considerations for Readability
While nesting provides powerful conditional logic, **deeply nested `if` statements can make code difficult to read and understand** [Source 34]. The sources advise avoiding comprehensions with more than two control subexpressions due to readability issues, suggesting "normal `if` and `for` statements and write a helper function" as an alternative [Source 35]. This general principle extends to complex `if-elif-else` structures; if your logic becomes too deeply nested, it might be an indication that you could refactor your code using functions to improve clarity [Source 9, 35].

Nested `if` statements are particularly useful when conditions are hierarchical and one condition's truth directly enables or necessitates the evaluation of a more specific condition. This differs from an `if-elif-else` chain, where only one block of code is executed, and each condition is tested sequentially as an alternative to the previous ones [Source 125, 128, 224]. It also differs from a series of independent `if` statements, where all conditions are evaluated regardless of whether previous ones were met [Source 125, 126].