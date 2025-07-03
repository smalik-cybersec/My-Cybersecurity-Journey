The "Custom Guided Exercise: Read Manual Pages" you're referring to is a practical activity detailed in the `rh124-9.0-student-guide.pdf`, specifically found on **page 104**. This exercise is designed to help you become proficient in using Red Hat Enterprise Linux (RHEL)'s local help systems, particularly its system manual pages.

**Objectives of the Exercise**
Upon successful completion of this guided exercise, you are expected to be able to:
*   **Locate relevant information for commands by searching manual pages**.
*   **Learn new options for common documentation commands**.
*   **Use appropriate tools to view and print documentation and other non-text formatted files**.

**Prerequisites and Setup**
To begin this exercise, you must be logged in as the **`student` user on the `workstation` machine**. The necessary lab environment is prepared by executing the command **`lab start help-manual`**.

**Detailed Steps of the Exercise**
The exercise guides you through a series of practical tasks using man pages:

1.  **View the `gedit` man page and explore options**:
    *   You will start by viewing the `gedit` man page using the command **`man gedit`**.
    *   Within the `gedit` man page, you will identify options for editing a specific file from the command line, such as specifying the file with `FILE` or moving the cursor to a particular line with `+LINE[:COLUMN]`.
    *   You will then use a relevant option, such as **`gedit + manual`**, to open the `/home/student/manual` file, ensuring the cursor is positioned at the end of the last line, and then close the application.

2.  **Read the `su(1)` man page**: This step involves reviewing the manual page for the `su` command. A note highlights that options like `-`, `-l`, and `--login` (when comma-separated on a single line) all produce the same behaviour.

3.  **Open the `man(1)` manual page**: You will view the man page that describes the `man` command itself, understanding its purpose as the system's manual pager.

4.  **Locate `passwd` utility man pages**: Use the **`whereis passwd`** command to find the binary, source, and manual pages associated with the `passwd` utility, verifying their presence in the `/usr/share/man` directory.

5.  **Search for ZIP archive information**: Employ **`man -k zip`** to search for man pages related to ZIP archives, such as `zipinfo(1)`.

6.  **Search for kernel boot parameters**: Use **`man -k boot`** to locate man pages that list parameters that can be passed to the kernel during boot, including `bootparam(7)` and `bootup(7)`.

7.  **Search for `ext4` filesystem tuning commands**: Utilize **`man -k ext4`** to identify commands used for tuning `ext4` filesystem parameters, for example, `tune2fs(8)` and `resize2fs(8)`.

After completing these steps, you are instructed to run **`lab finish help-manual`** to conclude the exercise.

**Understanding Manual Pages (Man Pages)**

Manual pages are a **primary and highly common source of documentation in RHEL**, typically available directly on the local system. They are fundamental for RHEL administration skills and are considered the **main information resource in the system**. Man pages are included as documentation within software packages and can be viewed from the command line using the **`man` command**. The actual files are stored in subdirectories of `/usr/share/man`.

**Man Page Structure and Sections**
Each man page organizes its information under various standard headings, although not all headings apply to every topic. Common headings include:
*   **NAME**: States the subject and a brief description.
*   **SYNOPSIS**: Offers a concise summary of the command's syntax.
*   **DESCRIPTION**: Provides a basic understanding of the topic.
*   **OPTIONS**: Explains the command-line options available.
*   **EXAMPLES**: Shows practical examples of how to use the command.
*   **FILES**: Lists related files and directories.
*   **SEE ALSO**: Directs you to other relevant man pages or topics, often with section numbers.

Man pages are structured as **quick references**, not in-depth tutorials. They are split into **nine numbered sections** for organization and clarity, depending on the type of information:
*   **Section 1**: User commands and shell programs (e.g., `ls(1)`, `passwd(1)`).
*   **Section 5**: File formats, for various system configuration files (e.g., `passwd(5)` for `/etc/passwd`).
*   **Section 8**: System administration and privileged commands.

When a topic exists in multiple sections (e.g., `passwd` for both a command and a file format), the `man` command typically searches sections in alphanumeric order, displaying the lowest-numbered section by default. To view a specific section, you must include the section number, for example, `man 5 passwd`. For the **RHCSA exam, sections 1, 5, and 8 are particularly important**.

**Navigating and Searching Man Pages**
When a man page is displayed, you can navigate its content using specific keyboard shortcuts, as the `man` command uses a pager program (usually `less`):
*   **Spacebar**, **Page Down (PgDn)**, `f`, `Ctrl+V`, or `Ctrl+F`: Scroll **forward** one screen.
*   **Page Up (PgUp)**, `b`, `Ctrl+B`, or `Esc+V`: Scroll **backward** one screen.
*   **Enter** or **Down Arrow**: Move **forward** one line.
*   **Up Arrow**: Move **backward** one line.
*   **`q`** or **`Q`**: **Quit** the man page and return to the command prompt.
*   **`/string`**: Search **forward** for the specified text string.
*   **`?string`**: Search **backward** for the specified text string.
*   **`n`**: Find the **next** occurrence of the search pattern.
*   **`N`**: Find the **previous** occurrence of the search pattern.

If you don't know the exact name of a command or file, you can search for man pages using keywords:
*   The **`apropos` command** (or **`man -k` option**) searches for keywords in the names and short descriptions of all man pages.
*   The **`whatis` command** provides a short, one-line description for a specified command or file from the man page database.
*   For new Linux installations, it might be necessary to run the **`mandb` command** (as root) to build an indexed database for keyword searches. The `man-db-cache-update` service typically performs this automatically when packages with man pages are installed.
*   Some commands also offer a quick help summary when executed with **`--help`** or **`-?`** options, providing a brief list of options without opening the full man page.

**Importance for RHCSA**
Man pages are a **critical resource for the RHCSA exam**. During the exam, candidates have access to the local system's documentation, including man and info pages, and files in `/usr/share/doc`, but generally **no internet access**. Therefore, it is highly recommended that you **review man pages for all commands covered in study materials and practice using them to find information to complete tasks**. The RHCSA exams are entirely "hands-on," and candidates are evaluated on whether their system is configured to meet requirements, not on the specific tools or methods used to achieve the results.