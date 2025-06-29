# Module 12: Conditional Statements

## Lesson 04: If-Else Statement Introduction

### 1. Purpose of the `if-else` Statement
The `if-else` statement provides a dual-path execution flow. Unlike a simple `if` statement which only executes a block of code if a condition is `True`, the `if-else` statement ensures that one block of code is executed when the condition is `True`, and a *different* block of code is executed when the condition is `False`. This is essential for creating programs that can respond to two distinct outcomes of a decision.

### 2. Syntax
The general syntax for an `if-else` statement is:

```python
if condition:
    # This code block is executed if 'condition' is True
    statement_if_true_1
    statement_if_true_2
    # ...
else:
    # This code block is executed if 'condition' is False
    statement_if_false_1
    statement_if_false_2
    # ...
# Code execution continues here after the if-else block