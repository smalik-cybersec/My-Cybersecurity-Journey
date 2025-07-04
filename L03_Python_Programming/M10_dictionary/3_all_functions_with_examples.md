Dictionaries in Python are versatile data structures that allow you to store and manage information using **key-value pairs** [L01, 6, 33, 63, 135]. As a mutable collection [L01, L02, 135], dictionaries support a variety of operations for accessing, adding, modifying, and removing their contents. Modern Python versions (3.7+) also maintain the **insertion order of keys**, a significant change from historical behavior where dictionaries were unordered [L01, L02, 198].

Here are the key functions and methods associated with Python dictionaries, along with examples:

*   **Accessing Values**
    *   **Direct Key Access** `my_dict[key]` [L01, L02, 33]:
        You can access a value by referring to its key inside square brackets. If the key does not exist, this will raise a `KeyError`.
        *   Example:
            ```python
            alien_0 = {'color': 'green', 'points': 5} [L02, 33]
            print(alien_0['color']) # Output: green
            ```
    *   **`get()` Method** `my_dict.get(key, default_value)` [L01, 3, 20, 33, 46, 64, 116, 158, 220, 221]:
        The `get()` method is a safer way to retrieve a value, as it allows you to specify a **default value to return if the key doesn't exist**. If the key is not found and no default value is provided, it returns `None`. This prevents a `KeyError`.
        *   Example:
            ```python
            alien_0 = {'color': 'green', 'points': 5}
            print(alien_0.get('color'))        # Output: green
            print(alien_0.get('speed', 'slow')) # Output: slow (default value)
            print(alien_0.get('speed'))         # Output: None (no default, key not found)
            ```
            The sources suggest preferring `get()` over `in` and `KeyError` for handling missing keys.

*   **Adding and Modifying Elements**
    *   **Adding New Key-Value Pairs**:
        You can add new key-value pairs by assigning a value to a new key.
        *   Example:
            ```python
            alien_0 = {'color': 'green'}
            alien_0['points'] = 5
            print(alien_0) # Output: {'color': 'green', 'points': 5}
            ```
    *   **Modifying Values**:
        To change a value, you assign a new value to the existing key.
        *   Example:
            ```python
            alien_0 = {'color': 'green', 'points': 5}
            alien_0['color'] = 'yellow'
            print(alien_0) # Output: {'color': 'yellow', 'points': 5}
            ```
    *   **`update()` Method** `my_dict.update(other_dict_or_iterable)`:
        This method updates the dictionary with key-value pairs from another dictionary or from an iterable of key-value pairs. Existing keys are updated, new keys are added.
        *   Example:
            ```python
            my_dict = {'a': 1, 'b': 2}
            my_dict.update({'c': 3, 'a': 10})
            print(my_dict) # Output: {'a': 10, 'b': 2, 'c': 3}
            ```
    *   **`setdefault()` Method** `my_dict.setdefault(key, default_value)`:
        This method offers a convenient way to get a value associated with a key, and if the key doesn't exist, it **inserts the key with a `default_value` and returns that value**. It is a shortcut for an `if` statement check and assignment.
        *   Example:
            ```python
            spam = {'size': 'fat'}
            spam.setdefault('color', 'black') # 'color' not in spam, so it's added with 'black'
            print(spam) # Output: {'size': 'fat', 'color': 'black'}
            ```
            The sources suggest preferring `defaultdict` over `setdefault` for handling missing items in internal state.

*   **Removing Elements**
    *   **`del` Statement** `del my_dict[key]`:
        The `del` statement allows you to remove a key-value pair based on the key. If the key doesn't exist, it raises a `KeyError`.
        *   Example:
            ```python
            alien_0 = {'color': 'green', 'points': 5}
            del alien_0['points']
            print(alien_0) # Output: {'color': 'green'}
            ```
    *   **`pop()` Method** `my_dict.pop(key, default_value)`:
        Removes the specified `key` and returns its `value`. If the key is not found, it can return a default value or raise a `KeyError` if no default is provided.
        *   Example:
            ```python
            my_dict = {'a': 1, 'b': 2}
            value = my_dict.pop('a')
            print(value)      # Output: 1
            print(my_dict)    # Output: {'b': 2}
            print(my_dict.pop('c', 'Key not found')) # Output: Key not found
            ```
    *   **`popitem()` Method** `my_dict.popitem()`:
        Removes and returns a **(key, value)** pair from the dictionary. For `OrderedDict`, it removes the first item inserted (FIFO) or the last if `last=True` is specified.
        *   Example (behavior may vary slightly in older Python versions due to order):
            ```python
            my_dict = {'a': 1, 'b': 2, 'c': 3}
            item = my_dict.popitem()
            print(item)    # Output: ('c', 3) (in modern Python, typically last inserted)
            print(my_dict) # Output: {'a': 1, 'b': 2}
            ```
    *   **`clear()` Method** `my_dict.clear()`:
        Removes all items from the dictionary.
        *   Example:
            ```python
            my_dict = {'a': 1, 'b': 2}
            my_dict.clear()
            print(my_dict) # Output: {}
            ```

*   **Iterating Through Dictionaries**
    Dictionaries can be efficiently looped through.
    *   **Looping Through All Key-Value Pairs** `for key, value in my_dict.items():`:
        The `items()` method returns a view object that displays a list of a dictionary's key-value tuple pairs.
        *   Example:
            ```python
            user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
            for key, value in user_0.items():
                print(f"Key: {key}, Value: {value}")
            # Output:
            # Key: username, Value: efermi
            # Key: first, Value: enrico
            # Key: last, Value: fermi
            ```
    *   **Looping Through All the Keys** `for key in my_dict.keys():` or `for key in my_dict:`:
        The `keys()` method returns a view object that displays a list of all the keys in the dictionary. Iterating directly over a dictionary also iterates through its keys.
        *   Example:
            ```python
            favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby'}
            for name in favorite_languages.keys():
                print(name.title())
            # Output:
            # Jen
            # Sarah
            # Edward
            ```
    *   **Looping Through All Values** `for value in my_dict.values():`:
        The `values()` method returns a view object that displays a list of all the values in the dictionary.
        *   Example:
            ```python
            favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby'}
            for language in favorite_languages.values():
                print(language.title())
            # Output:
            # Python
            # C
            # Ruby
            ```
    *   **Looping Through a Dictionary's Keys in a Particular Order**:
        While dictionaries themselves are not inherently ordered (historically, though modern Python preserves insertion order), you can iterate through keys in a specific order by using the `sorted()` function.
        *   Example:
            ```python
            favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby'}
            for name in sorted(favorite_languages.keys()):
                print(f"{name.title()}, thank you for taking the poll.")
            # Output (alphabetical by key):
            # Edward, thank you for taking the poll.
            # Jen, thank you for taking the poll.
            # Sarah, thank you for taking the poll.
            ```
            Sorting by complex criteria can be done using the `key` parameter of the `sort` method (though this applies to lists being sorted, rather than directly to dictionaries). Example `dict(sorted(DIAL_CODES, key=lambda x:x))` demonstrates sorting a list of tuples then converting to a dict, which preserves the sorted order of keys for creation.

*   **Checking for Keys**
    *   **`in` Operator** `'key' in my_dict`:
        You can use the `in` operator to check if a key exists in a dictionary. `'key' in my_dict` and `'key' in my_dict.keys()` behave identically.
        *   Example:
            ```python
            alien_0 = {'color': 'green', 'points': 5}
            print('color' in alien_0) # Output: True
            print('speed' in alien_0) # Output: False
            ```
    *   **`not in` Operator**:
        Similarly, `not in` checks for the absence of a key.
        *   Example:
            ```python
            alien_0 = {'color': 'green', 'points': 5}
            print('speed' not in alien_0) # Output: True
            ```

*   **Other Utility Functions/Concepts**
    *   **`len()` Function** `len(my_dict)` [L01]:
        Returns the number of key-value pairs in a dictionary.
        *   Example:
            ```python
            my_dict = {'a': 1, 'b': 2, 'c': 3}
            print(len(my_dict)) # Output: 3
            ```
    *   **`copy()` Method** `my_dict.copy()`:
        Returns a shallow copy of the dictionary.
        *   Example:
            ```python
            original_dict = {'a': 1, 'b': 2}
            copied_dict = original_dict.copy()
            print(copied_dict) # Output: {'a': 1, 'b': 2}
            ```
    *   **`fromkeys()` Method** `dict.fromkeys(iterable, value)`:
        A class method that creates a new dictionary with keys from `iterable` and values set to `value` (defaults to `None` if not provided).
        *   Example:
            ```python
            keys = ['a', 'b', 'c']
            new_dict = dict.fromkeys(keys, 0)
            print(new_dict) # Output: {'a': 0, 'b': 0, 'c': 0}
            ```
    *   **Dictionary Comprehensions**:
        A concise way to create dictionaries based on existing sequences or other dictionaries.
        *   Example:
            ```python
            a =
            even_squares_dict = {x: x**2 for x in a if x % 2 == 0}
            print(even_squares_dict) # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
            ```
            Another example for mapping letters to their uppercase representations: `cap_map = {x: x.upper() for x in letters}`.
    *   **`__missing__` Method**:
        This special method can be implemented in custom dictionary subclasses to define behavior when a requested key is not found. It allows for the construction of key-dependent default values.
    *   **Nesting**:
        Dictionaries can store lists, and lists can store dictionaries, allowing for complex data structures. You can also nest a dictionary inside another dictionary.
        *   Example:
            ```python
            # A list of dictionaries
            aliens = [{'color': 'green'}, {'color': 'yellow'}]
            # A list in a dictionary
            pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}
            # A dictionary in a dictionary
            users = {'aeinstein': {'first': 'albert', 'last': 'einstein'}}
            ```
    *   **`pprint.pprint()`**:
        For pretty-printing dictionary values, especially for large or nested dictionaries, the `pprint` module's `pprint()` function can be used.
    *   **`all()` and `any()` Built-in Functions**:
        These functions can be used with dictionary views (like `keys()`, `values()`, `items()`) because they operate on any iterable. `all(iterable)` returns `True` if all elements are truthy; `any(iterable)` returns `True` if any element is truthy.
        *   Example:
            ```python
            my_dict = {'a': 1, 'b': 0, 'c': 3}
            print(all(my_dict.values())) # Output: False (because 0 is falsey)
            print(any(my_dict.values())) # Output: True (because 1 and 3 are truthy)
            ```
    *   **Returning a Dictionary from a Function**:
        Functions can construct and return dictionaries, which is a common pattern for organizing related data.
        *   Example:
            ```python
            def make_album(artist, title):
                album_dict = {'artist': artist, 'title': title}
                return album_dict
            album = make_album('Metallica', 'Master of Puppets')
            print(album) # Output: {'artist': 'Metallica', 'title': 'Master of Puppets'}
            ```

Dictionaries are a powerful tool for organizing information, connecting related data through keys and values, and are a fundamental part of the Python language itself [L01, 6, 219].