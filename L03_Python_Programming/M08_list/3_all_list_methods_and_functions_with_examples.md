Lesson 03 of Module 08 covers **All List methods and Functions with examples**. Lists are a fundamental and versatile data type in Python, used for organising collections of items. They are a **mutable sequence type**, meaning their contents can be changed after creation.

Here's a detailed overview of list methods and functions:

### 1. List Declaration and Basic Concepts
*   **Declaration**: Lists are indicated by **square brackets (`[]`)**, with individual elements separated by commas. For example, `['trek', 'cannondale', 'redline', 'specialized']` is a list of bicycles.
*   **Creating Lists**:
    *   An **empty list** can be created using `[]`.
    *   The `list()` function can convert other iterable objects (like a `range` or a string) into a list, e.g., `list(range(10))`.
    *   Lists can contain items of **different data types**.
*   **Naming Convention**: It's good practice to use plural names for lists, such as `letters`, `digits`, or `names`.
*   **Indexing**: Python uses **zero-based indexing**, meaning the first item is at position 0.
    *   You can access individual elements using their index in square brackets, e.g., `bicycles`.
    *   **Negative indexes** access elements from the end of the list; `bicycles[-1]` would retrieve the last item.
    *   Trying to access an index that does not exist will result in an `IndexError`.
*   **Mutability and References**: Variables holding lists contain a **reference** to the list value, not the list itself. Modifying a list through one variable will affect any other variables referencing the same list object.

### 2. List Methods (Modifying and Interacting with Lists)
List methods are functions that are "called on" a list value using dot notation (e.g., `my_list.method()`).

*   **`append(item)`**: Adds an `item` to the **end** of the list. This is the most efficient way to add a single item.
    *   Example: `my_list.append('new_item')`.
*   **`insert(index, item)`**: Adds an `item` at a specific `index` in the list. Existing elements shift to the right to make space.
    *   Example: `motorcycles.insert(0, 'ducati')` inserts 'ducati' at the beginning.
*   **`del list_name[index]`**: A Python statement (not a method) used to **permanently remove an item** from the list at a specific `index`.
    *   Example: `del motorcycles`.
*   **`pop([index])`**: Removes an item from a list and **returns that item**. If no `index` is specified, `pop()` removes and returns the last item.
    *   Example: `popped_motorcycle = motorcycles.pop()`.
*   **`remove(value)`**: Removes the **first occurrence** of a specified `value` from the list. If the value appears multiple times, a loop is needed to remove all occurrences.
    *   Example: `motorcycles.remove('ducati')`.
*   **`sort(key=None, reverse=False)`**: **Permanently sorts** the list in alphabetical/numerical order. The `reverse=True` argument sorts in reverse order. The `key` parameter can be used to sort by complex criteria, such as the length of strings in a list.
    *   Example: `cars.sort()` or `names.sort(key=len)`.
*   **`reverse()`**: **Permanently reverses** the order of elements in the list.
    *   Example: `cars.reverse()`.
*   **`index(value, start=0, end=None)`**: Returns the **index of the first occurrence** of `value` in the list. Raises `ValueError` if the value is not found.
    *   Example: `my_list.index('hello')`.
*   **`count(value)`**: Returns the **number of times** a `value` appears in the list.
*   **`clear()`**: Removes **all items** from the list, making it empty.
*   **`extend(iterable)`**: Appends **all items from an iterable** (e.g., another list) to the end of the current list. This is similar to concatenation but modifies the list in place.
*   **`copy()`**: Returns a **shallow copy** of the list. This means changes to mutable nested objects in the copy will still affect the original. For a complete independent copy, `copy.deepcopy()` is used.

### 3. List-Related Functions and Operations
These are built-in functions or operators that operate on lists.

*   **`len(list)`**: Returns the **number of items** (length) in a list.
    *   Example: `len(guests)`.
*   **`sorted(list, key=None, reverse=False)`**: Returns a **new sorted list** from the given iterable, leaving the original list unchanged. It also supports `key` and `reverse` arguments similar to `sort()`.
    *   Example: `sorted(cars)`.
*   **`min(list)`, `max(list)`, `sum(list)`**: Return the minimum, maximum, and sum of numerical values in a list, respectively. These functions work efficiently even with large lists.
    *   Example: `min(digits)`, `max(digits)`, `sum(digits)`.
*   **Slicing (`list[start:end:step]`)**: Allows you to work with **parts of a list**.
    *   `list[start:end]`: Creates a new list containing elements from `start` up to (but not including) `end`.
    *   Omitting `start` or `end` implies the beginning or end of the list respectively.
    *   A `step` argument can be used to skip elements, e.g., `list[::2]` for every second element.
    *   `list[::-1]` is a common way to **reverse a list** without modifying the original.
    *   It's recommended to use **catch-all unpacking** over slicing for dividing a list into non-overlapping pieces, as it's less error-prone.
*   **`in` and `not in` operators**: Used to check for **membership** (presence or absence) of an item in a list. They return `True` or `False`.
    *   Example: `'mushrooms' in requested_toppings`.
*   **List Comprehensions**: Provide a concise way to create new lists based on existing sequences. They combine a `for` loop and the creation of new elements into a single line, automatically appending each new element. They are often preferred over `map()` and `filter()` for readability.
    *   Example: `squares = [value**2 for value in range(1,11)]`.
*   **`for` loops**: The most common way to iterate through and process every item in a list.
    *   Example: `for magician in magicians: print(magician)`.
*   **`enumerate()`**: Returns an iterable of (index, value) pairs, useful when you need both the index and the item during iteration.
*   **`random.choice(list)` and `random.shuffle(list)`**:
    *   `random.choice()` returns a random element from the list.
    *   `random.shuffle()` shuffles the items of the list in place.
*   **Augmented Assignment Operators**: Combine an operation with assignment, e.g., `list += other_list` (list concatenation) or `list *= n` (list replication).

### 4. Advanced Concepts
*   **Special Methods (Dunder Methods)**: Many built-in functions and operators used with lists internally call special methods (e.g., `__len__` for `len()`, `__getitem__` for indexing and slicing, `__contains__` for `in`). Implementing these methods in custom classes allows them to behave like standard Python sequences.
*   **`collections.abc`**: For custom container types that should behave like lists, it's recommended to inherit from `collections.abc.Sequence` or `collections.abc.MutableSequence` to ensure all expected methods are present or inherited. Python will provide missing methods like `index` and `count` for free if `__getitem__` is implemented and the class inherits from `Sequence`.
*   **Generators**: For working with very large datasets, using generators instead of returning full lists can provide better performance and reduced memory usage. The `itertools` module offers many functions for advanced iteration and working with generators.

Understanding these methods and functions enables efficient and Pythonic manipulation of data stored in lists.