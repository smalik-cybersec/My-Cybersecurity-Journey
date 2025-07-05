Module 15, Lesson 02 focuses specifically on **Text file handling** in Python. This lesson builds upon the introduction to file handling by detailing how Python programs interact with files that contain only plain text characters [conversation].

### What are Text Files?
**Plaintext files** are distinct from binary files in that they contain only basic text characters, without any embedded formatting information such as font, size, or color [conversation, 118]. Common examples include `.txt` files or Python script files ending in `.py` [conversation, 118]. These files can be opened and read in simple text editors like Windows' Notepad or macOS's TextEdit, appearing as readable text. This contrasts with **binary files** (e.g., Word documents, PDFs, images, executables), which, if opened in a plain text editor, would appear as scrambled or nonsensical data [conversation, 119]. Programs can easily read the contents of plaintext files and treat them as ordinary string values.

### Opening Text Files

To interact with a text file, the first step is to **open** it, which returns a **File object** [conversation, 121]. This File object is a Python value that your program uses to read from or write to the file on your computer [conversation, 123].

The `open()` built-in function is used for this purpose and typically takes two main arguments:
1.  The **path to the file** (as a string) [conversation, 121]. This can be an **absolute path** (starting from the root directory, like `C:\` on Windows or `/` on macOS/Linux) or a **relative path** (relative to the program's current working directory) [conversation, 114, 121].
2.  An **optional `mode` argument**, which specifies how the file will be opened [conversation, 419, 460]. If omitted, the default is read mode (`'r'`) [conversation, 65, 122, 419, 460].

Here are the most common modes for text file handling:
*   **`'r'` (read mode)**: This is the **default** [conversation, 65, 122, 460]. It allows you to **only read data** from the file; you cannot write or modify it.
*   **`'w'` (write mode)**: This mode allows you to **write to a file** [conversation, 65, 460]. A crucial point to remember is that if the file already exists, **its contents will be completely erased and overwritten** when opened in `'w'` mode [conversation, 65, 125, 167]. If the file does not exist, `open()` will automatically create a new, blank file.
*   **`'a'` (append mode)**: This mode allows you to **add new content to the end of an existing file** [conversation, 65, 460]. Unlike write mode, it **does not overwrite** the file's previous contents [conversation, 66]. If the file does not exist, it will be created.
*   **`'r+'` (read and write mode)**: This mode allows both reading and writing to the file.

**Using the `with` Statement for Robustness:**
It is highly recommended to use the **`with` statement** when opening files [conversation, 62, 65, 185, 272, 431, 462]. The `with` statement acts as a **context manager**, ensuring that the file is **automatically closed** once the block of code is exited, even if errors occur [conversation, 272, 431]. This prevents common bugs where file handles might accidentally remain open.

**Encoding Considerations:**
When working with text files, **character encoding** is vital. Python 3 differentiates clearly between **Unicode strings (`str`)** and **sequences of 8-bit values (`bytes`)**. While `str` objects handle Unicode code points, `bytes` objects handle raw binary data. When you open a file in text mode, `open()` performs the necessary decoding when reading and encoding when writing.

It is a best practice to **always pass an explicit `encoding=` argument** when opening text files. This is because the default encoding can vary between different machines or Python versions, leading to unexpected errors or corrupted data. For example, `encoding='utf-8'` is a widely used and recommended choice. If you don't specify an encoding, the system's default locale encoding might be used, which can cause issues if the file was created with a different encoding. Conversely, opening a text file in binary mode (`'rb'` or `'wb'`) for standard text operations is generally discouraged unless you specifically need to analyze the file's bytes to determine its encoding, or if you are dealing with binary-specific data like images.

### Reading Text Files

Once a file is opened in read mode, you can use several methods on the File object to access its content:
*   **`read()`**: This method reads the **entire contents of the file** as a single string value [conversation, 27, 63, 124, 168, 419, 463]. You can optionally pass a `bytes` parameter to specify the number of bytes to read. If no number is specified, it reads until the end of the file.
    *   Example: `file_contents = file_object.read()`.
*   **`readline()`**: This method reads **one line** from the file at a time, including the newline character `\n` [conversation, 419, 464]. It also accepts an optional `size` parameter to limit the number of bytes read from the line.
*   **`readlines()`**: This method returns a **list of strings**, where each string represents a line from the file's contents, including the newline characters [conversation, 27, 124, 168, 432, 465]. This method can be memory-efficient for large files if used in conjunction with generator expressions, as it can lazily evaluate lines.

When reading text files, Python automatically handles the conversion of line endings (e.g., `\r\n` on Windows or `\n` on Unix) to a single `\n` character in the string returned.

### Writing to Text Files

When a file is opened in write mode (`'w'`) or append mode (`'a'`), you can use the `write()` method:
*   **`write(string)`**: This method writes the given `string` to the file [conversation, 65, 192, 431, 466]. To write multiple lines, you can include newline characters (`\n`) within the string or call `write()` multiple times [conversation, 192]. The `write()` method typically returns the number of characters (Unicode code points) written.
    *   Example using `with` statement:
        ```python
        with open("my_notes.txt", "w") as f:
            f.write("This is the first line.\n")
            f.write("This is the second line.\n")
        # File is automatically closed here
        ```
As previously mentioned, be extremely cautious with **`'w'` mode**, as it will erase any existing content in the file [conversation, 65, 125, 167]. For adding content without deletion, the **`'a'` (append) mode** is the correct choice [conversation, 66, 125].

After reading or writing to a file, it's crucial to explicitly call the `close()` method on the File object if you are not using a `with` statement, especially before attempting to open the same file again. However, the `with` statement makes this manual `close()` unnecessary, promoting safer and cleaner code.

### Related Modules and Advanced Concepts for Text Files

Several modules in Python's standard library enhance text file handling capabilities:
*   **`pathlib` module**: Offers an object-oriented approach to file paths, providing convenient methods like `read_text()` and `write_text()` for simplified text file operations.
*   **`os` module**: Provides functions for interacting with the operating system, including managing files and directories, checking path validity (e.g., `os.path.exists()`, `os.path.isfile()`), and constructing paths (e.g., `os.path.join()`) [conversation, 88, 116, 176, 433]. Note that `os` module functions can sometimes be dual-mode, accepting either `str` or `bytes` arguments, with different return types accordingly.
*   **`sys` module**: Provides access to standard input (`sys.stdin`) and standard output (`sys.stdout`) as **file-like objects**. These can be treated much like regular readable or writable file objects, supporting methods like `readline()` and `write()`.
*   **`io.StringIO`**: This class allows you to treat a **string in memory as if it were a file**. This is particularly useful when you have data as a string but need to pass it to a function that expects a file object (e.g., for testing or intermediate processing).
*   **`csv` and `json` modules**: While these are for structured data, they typically work with plaintext files (`.csv` and `.json` extensions) and simplify parsing and writing data in their respective formats [conversation, 93, 161].
*   **Docstrings**: When creating Python modules (which are essentially text files ending in `.py`), it's good practice to include a **module docstring** as the first line. This docstring should briefly describe the module's purpose and can detail available functions and classes.

Understanding these concepts and practices for text file handling is fundamental for developing robust Python programs that can persistently store, retrieve, and process textual data.