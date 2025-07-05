Module 15: File Handling, Lesson 01 provides an introduction to how Python programs interact with files.

### Introduction to File Handling

File handling is a crucial aspect of programming that allows your programs to interact with data stored persistently on a computer's hard drive. Instead of just displaying data to the terminal, which is hard to manipulate later, file handling enables programs to **read information from files and save information to files**.

This capability is essential for various applications, such as:
*   **Saving user data** so it is not lost when the program stops running.
*   **Analysing large datasets** quickly.
*   **Consolidating and generating reports** from textual data like log files or configuration files.
*   **Reusing functions** and **libraries** that other programmers have written.
*   **Sharing files** with other programmers without needing to share the entire program.

### Basic Concepts of Files

When working with files in Python, it's important to understand fundamental concepts:

*   **File Properties**: A file typically has a **filename** and a **path**. The path specifies the file's location on the computer, and the **file's extension** (the part after the last period in the filename) often tells you its type (e.g., `.txt`, `.py`, `.pdf`, `.jpg`).
*   **Folders (Directories)**: Files are organized within folders, which can also contain other folders, creating a hierarchical structure.
*   **File Paths**:
    *   An **absolute path** always begins with the **root folder** (e.g., `C:\` on Windows or `/` on macOS and Linux).
    *   A **relative path** is specified relative to the program's current working directory.
    *   Special names like a single period (`.`) refer to "this directory," and two periods (`..`) refer to "the parent folder".
*   **Types of Files**:
    *   **Plaintext files** contain only basic text characters and do not include font, size, or colour information (e.g., `.txt` files or Python script files ending in `.py`).
    *   **Binary files** encompass all other file types, such as word processing documents, PDFs, images, spreadsheets, and executable programs. These appear as scrambled nonsense if opened in a plain text editor. The only difference between various file types like text, video, or image files is how their underlying 0s and 1s are interpreted.
*   **File Objects**: When you open a file in Python, the `open()` function returns a **File object**, which is a Python value used to interact with the file on your computer.

### Core File Operations

Python provides built-in functions and methods for essential file operations:

*   **Opening Files**:
    *   The `open()` function is used to open a file. It requires a string path to the file and an optional **mode** argument.
    *   Common modes include:
        *   `'r'` (read mode): This is the **default mode** and allows you to only read data from the file.
        *   `'w'` (write mode): Allows writing to a file. **If the file already exists, it will be erased and completely overwritten**.
        *   `'a'` (append mode): Allows adding new content to the end of an existing file without overwriting its previous contents.
        *   `'b'` (binary mode): Can be combined with other modes (e.g., `'rb'`, `'wb'`) to handle binary files.
    *   It is generally recommended to use the `with` statement when opening files. This ensures that the file is **automatically closed** even if errors occur.

*   **Reading Files**: Once a file is opened in read mode, you can use several methods to access its contents:
    *   `read()`: Reads the **entire contents of the file** as a single string value.
    *   `readline()`: Reads **one line** from the file at a time.
    *   `readlines()`: Returns a **list of strings**, where each string represents a line from the file's contents.

*   **Writing to Files**: When a file is opened in write or append mode, you can use methods like:
    *   `write()`: Writes a string to the file.
    *   You can write multiple lines by providing new line characters within the string or by calling `write()` multiple times.

### Related Modules for File Handling

Python's standard library provides modules that extend file handling capabilities:
*   **`os` module**: Provides a portable interface for interacting with the operating system, including functions for **managing files and directories**, checking paths, and listing folder contents (e.g., `os.makedirs()` to create directories, `os.getcwd()` to get the current working directory, `os.listdir()` to list contents).
*   **`shutil` module**: Offers higher-level operations for **copying, moving, renaming, and deleting** entire file trees.
*   **`json` module**: Useful for **saving user data** in JSON format, which can be easily reloaded later.
*   **`csv` module**: Specifically designed to work with **comma-separated values (CSV) files**, simplifying parsing and writing spreadsheet-like data.
*   **`shelve` module**: Allows you to **save Python variables** to a file, functioning like a dictionary that persists data.
*   **`pathlib` module**: Provides an object-oriented approach to handling file system paths, making path manipulation more intuitive.
*   **`PyPDF2` and `Python-Docx`**: These modules enable programmatic interaction with binary files like **PDFs and Word documents**, allowing text extraction and manipulation.