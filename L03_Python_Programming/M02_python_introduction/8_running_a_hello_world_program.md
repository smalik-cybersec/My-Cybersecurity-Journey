For Lesson 08, the focus is on **Running a "Hello World" program**, which is a foundational step in setting up your Python programming environment. This simple program serves as a crucial test: if it runs correctly, it indicates that your Python installation is working properly, and any other Python program you write should function as well.

Here's a comprehensive guide to running your first "Hello World" program:

### 1. Setting Up Your Programming Environment

Before writing and running code, you need a Python installation and a **text editor** or an **Integrated Development Environment (IDE)**. While IDEs offer a comprehensive suite of tools, simple text editors are often recommended for beginners to focus on coding rather than the editor itself [Lesson 07].

**Recommended Tools from the sources:**
*   **Sublime Text:** A simple text editor that can run most programs directly from within the editor, displaying output in an embedded terminal session.
*   **Mu:** Another editor that includes an interactive shell.
*   **IDLE (Integrated Development and Learning Environment):** Installs alongside Python and can serve as an editor and interactive shell.
*   **PyCharm / Visual Studio Code (VS Code):** While PyCharm is specifically built for Python and VS Code functions more like an IDE, both offer robust features like linters, debuggers, and version control support [Lesson 07]. PyCharm includes a linter for code style adherence and an integrated debugger, while VS Code has debugger support, integrated version control, and code completion [Lesson 07].

It's crucial to ensure you are using **Python 3.6 or a later version**, as many examples and modern practices are written for these versions, and Python 2.x differs significantly [50, 53, 55, Lesson 07]. You can check your Python version by opening a terminal and typing `python --version` or `python3 --version`.

### 2. Writing the "Hello World" Code

**Open your chosen text editor or IDE** (e.g., Sublime Text, Mu).

**Save an empty Python file** with a `.py` extension. For instance, save it as `hello_world.py` in a new folder, such as `python_work`. Using lowercase letters and underscores for file and folder names is a standard Python convention.

**Enter the following single line of code** into the file:
```python
print("Hello Python world!")
```

This simple line uses the `print()` function, which displays the string value inside its parentheses on the screen. When the Python interpreter sees `print()` followed by parentheses, it understands to display whatever is enclosed within them.

### 3. Running Your Program

There are several ways to execute your Python program:

*   **From a Text Editor/IDE:**
    *   **Configure for Python 3:** If you're using Sublime Text, you may need to configure it to use your system's `python3` command. This involves creating a new build system file (e.g., `Python3.sublime-build`) with the content: `{"cmd": ["python3", "-u", "$file"]}`.
    *   **Build/Run:** Once configured, you can run your program by selecting **Tools > Build** from the menu or by pressing **CTRL-B** (or `⌘-B` on macOS).
    *   **Output:** A terminal screen should appear at the bottom of your editor window, displaying: `Hello Python world!`. Mu also has a "Run" button or F5 key for execution, which opens an interactive shell pane at the bottom.

*   **From the Interactive Shell (REPL):**
    *   You can run Python instructions one at a time and see immediate results using an interactive shell.
    *   **Open a terminal/command prompt** (e.g., Command Prompt on Windows, Terminal on macOS/Linux).
    *   **Start the Python interactive session** by typing `python` (on Windows) or `python3` (on macOS/Linux) and pressing Enter. You should see a `>>>` prompt.
    *   **Type the code directly:**
        ```python
        >>> print("Hello Python interpreter!")
        Hello Python interpreter!
        ```
    *   To exit the interactive session, press **CTRL-Z** then Enter (Windows) or **CTRL-D** (macOS/Linux), or type `exit()`.

*   **From the Terminal/Command Line:**
    *   This method is useful for running existing programs without opening an editor.
    *   **Open a new terminal/command prompt**.
    *   **Navigate to your `python_work` folder** using the `cd` (change directory) command. For example:
        *   **Windows:** `C:\> cd Desktop\python_work`
        *   **macOS/Linux:** `~/Desktop/python_work$ cd Desktop/python_work/`
    *   **Verify the file is present** using `dir` (Windows) or `ls` (macOS/Linux).
    *   **Run the program:**
        *   **Windows:** `C:\Desktop\python_work> python hello_world.py`
        *   **macOS/Linux:** `~/Desktop/python_work$ python3 hello_world.py` (ensure you use `python3` if `python` defaults to Python 2).
    *   The output will appear directly in the terminal.

### 4. Understanding What Happens

When you run `hello_world.py`, the `.py` extension tells your editor to pass the file to the Python interpreter. The **Python interpreter** reads your code line by line, determining the meaning of each word. For instance, `print()` is recognized as a function name, and the text within the parentheses is then displayed on the screen. Many editors also offer **syntax highlighting**, which colors different parts of your code (like function names and strings) to make the structure clearer and help you spot errors.

### 5. Troubleshooting Common Issues

Early setup issues can be frustrating, but they are common and resolvable.

*   **Tracebacks (Error Reports):** If your program contains a significant error, the Python interpreter will display a traceback, which is an error report. This report tells you where the problem occurred (filename, line number) and the type of error. For example, a `NameError` often means a variable name was misspelled or not defined.
*   **Syntax Errors:** Programming languages require very specific syntax. Even small mistakes like a missing colon, mismatched quotation marks, or incorrect parentheses can prevent a program from running. Your editor's syntax highlighting can often help you spot these.
*   **Indentation Errors:** Python uses indentation to define blocks of code. Incorrect indentation (e.g., indenting a line unnecessarily) can lead to an `IndentationError: unexpected indent`. Only indent when there is a specific reason, such as within a `for` loop.
*   **Python Version Conflicts:** If you encounter issues, ensure you are running Python 3.x, as recommended. Many resources are written for Python 3, and using Python 2.x can lead to problems [Lesson 07, 53]. If `python` command defaults to version 2, explicitly use `python3`.
*   **General Troubleshooting Steps:**
    *   **Check the traceback** for clues.
    *   **Take a break** and re-examine your code carefully.
    *   **Start over:** Consider deleting the file and re-creating it from scratch.
    *   **Seek help:** Ask someone knowledgeable in Python to review your setup, or consult online resources like Stack Overflow, official Python documentation, or community forums.

Once you successfully run your `hello_world.py` program, you've established a working environment and are ready to delve deeper into Python programming.