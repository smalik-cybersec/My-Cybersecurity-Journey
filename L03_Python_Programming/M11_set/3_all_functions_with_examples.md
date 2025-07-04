For "Module 11: Set - Lesson 03: All Functions with examples", the curriculum delves into the various operations and methods available for Python's set types. Sets are powerful collection types primarily used for storing **unique items** and performing efficient membership tests and mathematical set operations.

As previously discussed, sets are defined by **curly braces `{}`**, similar to dictionaries, but they contain no key-value pairs. Unlike lists and dictionaries, **sets do not retain items in any specific order**. The `set` type is **mutable**, while its counterpart, `frozenset`, is **immutable**. Set elements **must be hashable**.

Here's a comprehensive overview of the functions and operations available for sets, categorised for clarity:

### 1. Set Creation and Basic Utility

*   **Direct Declaration (Literal Syntax)**:
    *   Sets can be declared using literal syntax with comma-separated elements inside curly braces, e.g., `my_set = {'python', 'ruby', 'c'}`. This method is generally **faster and more readable** than using the constructor because Python uses a specialised `BUILD_SET` bytecode.
    *   **Example**:
        ```python
        languages = {'python', 'ruby', 'python', 'c'}
        print(languages) # Output: {'ruby', 'python', 'c'} (order may vary, duplicates removed)
        ```
*   **Creating an Empty Set**:
    *   To declare an **empty set**, you **must use the `set()` constructor**, as `{}` creates an empty dictionary.
    *   **Example**:
        ```python
        empty_set = set()
        print(type(empty_set)) # Output: <class 'set'>
        ```
*   **`frozenset` Creation**:
    *   There is **no literal syntax for `frozenset`**; they must be created by calling their constructor.
    *   **Example**:
        ```python
        my_frozenset = frozenset(range(5))
        print(my_frozenset) # Output: frozenset({0, 1, 2, 3, 4})
        ```
*   **Set Comprehensions (Setcomps)**:
    *   Introduced in Python 2.7, these provide a concise way to build sets.
    *   **Example**:
        ```python
        from unicodedata import name
        # Build a set of Latin-1 characters that have "SIGN" in their Unicode names
        sign_chars = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')}
        print(sign_chars) # Output: {'§', '=', '¢', '#', '¤', '<', '¥', 'µ', '×', '$', '¶', '£', '©', '°', '+', '÷', '±', '>', '¬', '®', '%'}
        ```
*   **Removing Duplication**:
    *   A common use case for sets is to remove duplicates from other collections.
    *   **Example**:
        ```python
        my_list = ['spam', 'spam', 'eggs', 'spam']
        unique_items = set(my_list)
        print(unique_items) # Output: {'eggs', 'spam'}
        print(list(unique_items)) # Convert back to a list: ['eggs', 'spam'] (order may vary)
        ```
*   **Shallow Copy (`s.copy()`)**:
    *   Returns a shallow copy of the set. This works for both `set` and `frozenset`.
    *   **Example**:
        ```python
        original_set = {1, 2, 3}
        copied_set = original_set.copy()
        print(copied_set) # Output: {1, 2, 3}
        ```
*   **Length (`s.__len__()` or `len(s)`)**:
    *   Returns the number of elements in the set.
    *   **Example**:
        ```python
        my_set = {'apple', 'banana'}
        print(len(my_set)) # Output: 2
        ```
*   **Iteration (`s.__iter__()`)**:
    *   Returns an iterator over the elements in the set. Sets are iterable.
    *   **Example**:
        ```python
        my_set = {1, 2, 3}
        for item in my_set:
            print(item) # Prints each item (order not guaranteed)
        ```

### 2. Mathematical Set Operations

Sets in Python implement common mathematical set operations using both infix operators and methods. The infix operators typically require both operands to be sets, while the methods can often take any iterable as an argument.

*   **Union (Combining Sets)**:
    *   **Operator**: `|`
    *   **Method**: `s.union(iterable, ...)`
    *   **Description**: Returns a new set containing all unique elements from all sets/iterables.
    *   **Example**:
        ```python
        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        print(set1 | set2) # Output: {1, 2, 3, 4, 5}
        print(set1.union(set2, {5, 6})) # Output: {1, 2, 3, 4, 5, 6}
        ```
*   **Intersection (Common Elements)**:
    *   **Operator**: `&`
    *   **Method**: `s.intersection(iterable, ...)`
    *   **Description**: Returns a new set containing only the elements common to all sets/iterables. This is useful for **fast membership tests** or finding common items.
    *   **Example**:
        ```python
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        print(set1 & set2) # Output: {3, 4}
        # Counting occurrences of "needles" in a "haystack"
        needles = {1, 5, 8}
        haystack = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        found_count = len(needles & haystack)
        print(f"Found {found_count} needles in the haystack.") # Output: Found 3 needles in the haystack.
        ```
*   **Difference (Elements in One, Not Another)**:
    *   **Operator**: `-`
    *   **Method**: `s.difference(iterable, ...)`
    *   **Description**: Returns a new set containing elements in the first set that are not present in the other sets/iterables.
    *   **Example**:
        ```python
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        print(set1 - set2) # Output: {1, 2}
        ```
*   **Symmetric Difference (Elements in Either, But Not Both)**:
    *   **Operator**: `^`
    *   **Method**: `s.symmetric_difference(iterable)`
    *   **Description**: Returns a new set with elements that are in either set, but not in their intersection.
    *   **Example**:
        ```python
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        print(set1 ^ set2) # Output: {1, 2, 5, 6}
        ```

### 3. In-Place Operations (for Mutable Sets only)

These methods modify the set upon which they are called directly. They are not available for `frozenset`.

*   **Update Union (`s |= iterable` or `s.update(iterable, ...)`)**:
    *   Adds elements from an iterable to the set.
    *   **Example**:
        ```python
        my_set = {1, 2}
        my_set.update({3, 4},)
        print(my_set) # Output: {1, 2, 3, 4, 5}
        ```
*   **Update Intersection (`s &= iterable` or `s.intersection_update(iterable, ...)`)**:
    *   Removes elements from the set that are not present in the given iterables.
    *   **Example**:
        ```python
        my_set = {1, 2, 3, 4}
        my_set.intersection_update({3, 4, 5})
        print(my_set) # Output: {3, 4}
        ```
*   **Update Difference (`s -= iterable` or `s.difference_update(iterable, ...)`)**:
    *   Removes all elements found in the specified iterables from the set.
    *   **Example**:
        ```python
        my_set = {1, 2, 3, 4}
        my_set.difference_update({3, 5})
        print(my_set) # Output: {1, 2, 4}
        ```
*   **Update Symmetric Difference (`s ^= iterable` or `s.symmetric_difference_update(iterable)`)**:
    *   Updates the set with the symmetric difference of itself and another iterable.
    *   **Example**:
        ```python
        my_set = {1, 2, 3, 4}
        my_set.symmetric_difference_update({3, 4, 5, 6})
        print(my_set) # Output: {1, 2, 5, 6}
        ```
*   **Add Element (`s.add(element)`)**:
    *   Adds a single element to the set. If the element is already present, the set remains unchanged.
    *   **Example**:
        ```python
        my_set = {1, 2}
        my_set.add(3)
        my_set.add(2) # No change
        print(my_set) # Output: {1, 2, 3}
        ```
*   **Remove Element (`s.remove(element)`)**:
    *   Removes a specified element from the set. If the element is not found, a `KeyError` is raised.
    *   **Example**:
        ```python
        my_set = {1, 2, 3}
        my_set.remove(2)
        print(my_set) # Output: {1, 3}
        # my_set.remove(4) # This would raise KeyError
        ```
*   **Discard Element (`s.discard(element)`)**:
    *   Removes a specified element from the set if it is present. **No error is raised** if the element is not found.
    *   **Example**:
        ```python
        my_set = {1, 2, 3}
        my_set.discard(2)
        my_set.discard(4) # No error
        print(my_set) # Output: {1, 3}
        ```
*   **Pop Element (`s.pop()`)**:
    *   Removes and returns an **arbitrary** element from the set. Since sets are unordered, there's no way to predict which element will be removed. If the set is empty, a `KeyError` is raised.
    *   **Example**:
        ```python
        my_set = {1, 2, 3}
        popped_item = my_set.pop()
        print(f"Popped: {popped_item}, Remaining set: {my_set}")
        ```
*   **Clear Set (`s.clear()`)**:
    *   Removes all elements from the set, making it empty.
    *   **Example**:
        ```python
        my_set = {1, 2, 3}
        my_set.clear()
        print(my_set) # Output: set()
        ```

### 4. Set Predicates (Comparison Operations)

These operations return a **Boolean** value (True or False) and are used for comparing sets.

*   **Disjoint (`s.isdisjoint(iterable)`)**:
    *   Returns `True` if the set has no elements in common with the iterable, i.e., their intersection is empty.
    *   **Example**:
        ```python
        set1 = {1, 2}
        set2 = {3, 4}
        set3 = {2, 5}
        print(set1.isdisjoint(set2)) # Output: True
        print(set1.isdisjoint(set3)) # Output: False
        ```
*   **Subset (`s <= other_set` or `s.issubset(iterable)`)**:
    *   Returns `True` if every element in the set `s` is also in `other_set` (or `iterable`).
    *   **Example**:
        ```python
        set1 = {1, 2}
        set2 = {1, 2, 3}
        print(set1 <= set2) # Output: True
        print(set1.issubset()) # Output: True
        ```
*   **Proper Subset (`s < other_set`)**:
    *   Returns `True` if `s` is a subset of `other_set`, and `s` is not equal to `other_set`.
    *   **Example**:
        ```python
        set1 = {1, 2}
        set2 = {1, 2, 3}
        print(set1 < set2) # Output: True
        print(set2 < set2) # Output: False
        ```
*   **Superset (`s >= other_set` or `s.issuperset(iterable)`)**:
    *   Returns `True` if every element in `other_set` (or `iterable`) is also in set `s`.
    *   **Example**:
        ```python
        set1 = {1, 2, 3}
        set2 = {1, 2}
        print(set1 >= set2) # Output: True
        print(set1.issuperset()) # Output: False
        ```
*   **Proper Superset (`s > other_set`)**:
    *   Returns `True` if `s` is a superset of `other_set`, and `s` is not equal to `other_set`.
    *   **Example**:
        ```python
        set1 = {1, 2, 3}
        set2 = {1, 2}
        print(set1 > set2) # Output: True
        print(set1 > set1) # Output: False
        ```
*   **Membership Test (`element in s`)**:
    *   Checks if an element is present in the set. Sets provide an **extremely fast membership test** due to their underlying hash table implementation.
    *   **Example**:
        ```python
        my_set = {'apple', 'banana', 'cherry'}
        print('apple' in my_set) # Output: True
        print('grape' not in my_set) # Output: True
        ```

These functions and operators enable a wide range of data manipulation tasks, particularly when dealing with collections where uniqueness and efficient element look-up are important.