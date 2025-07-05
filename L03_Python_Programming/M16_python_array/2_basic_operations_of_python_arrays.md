Module 16, Lesson 02 focuses on the **Basic Operations of Python Arrays**, specifically the `array.array` type from the `array` module. As previously discussed, `array.array` is a memory-efficient sequence designed to store items of a single, uniform C data type, particularly useful for large numerical datasets [Conversation, 252, 253].

Here are the basic operations you can perform on `array.array` objects:

*   **Creation and Typecode Specification**: When creating an array, you must specify a `typecode`, which is a single character string dictating the underlying C data type for its elements. This typecode ensures that the array only stores numbers matching the specified type.
    *   Example: `floats = array('d', (random() for i in range(10**7)))` creates an array of double-precision floats.

*   **Accessing Elements (Indexing)**: Arrays are ordered collections, and individual elements can be accessed using zero-based indexing, similar to Python lists. Negative indices can be used to access elements from the end of the array, with -1 referring to the last element.
    *   The `__getitem__` special method handles this operation.
    *   Example: `floats[-1]` would access the last element of the `floats` array.

*   **Slicing**: You can extract subsets of an array using slicing, which returns a *new* array of the same type. Slices are specified using `[start:end]` or `[start:end:stride]` syntax.
    *   Slicing an `array.array` results in another `array.array` instance, which is generally desired behavior.
    *   The `memoryview` built-in type provides a way to handle slices of arrays without copying the underlying bytes, offering a "zero-copy interface" for efficient reading and writing.
    *   Example: `my_array[1:4]` would return a new array containing elements from index 1 up to (but not including) index 4.

*   **Modifying Elements**: Arrays are mutable sequences, meaning their contents can be changed after creation [Conversation, 218]. You can modify an element by assigning a new value to a specific index.
    *   Example: `my_array = 0x79`.

*   **Adding Elements**: Arrays support methods like `append()` and `insert()` to add new values.
    *   `append(e)` adds a single element `e` to the end of the array.
    *   `insert(p, e)` inserts element `e` before the item at position `p`.
    *   `extend(it)` appends items from an iterable `it`.

*   **Removing Elements**: Elements can be removed using `pop()` or `remove()` methods, or the `del` statement.
    *   `pop([p])` removes and returns the item at an optional position `p` (defaulting to the last item).
    *   `remove(e)` removes the first occurrence of element `e` by value.
    *   `del s[p]` removes the item at position `p`.

*   **Length (`len()`)**: The built-in `len()` function returns the number of items in the array.

*   **Membership Testing**: The `in` and `not in` operators can be used to check if an item exists within the array.

*   **Concatenation (`+`) and Replication (`*`)**: Arrays support the `+` operator for concatenation and the `*` operator for replication, creating a new array result.
    *   Augmented assignment operators like `+=` and `*=` are also supported; for mutable sequences like `array.array`, these operations typically occur in place.

*   **File I/O**: `array.array` provides specialized methods for efficient loading and saving of data directly to and from binary files.
    *   `tofile(f)` saves array items as packed machine values to a binary file `f`.
    *   `fromfile(f, n)` appends `n` items from a binary file `f`, interpreting them as packed machine values.
    *   These methods are significantly faster and more memory-efficient than reading/writing numbers to text files.

*   **Sorting**: Unlike Python lists, `array.array` does not have an in-place sort method (`sort()`). To sort an array, you typically use the built-in `sorted()` function to create a new sorted array. To maintain a sorted order when adding items, the `bisect.insort` function (from the `bisect` module) is used.

These operations allow for efficient handling and manipulation of large numerical datasets using Python's `array.array` type.