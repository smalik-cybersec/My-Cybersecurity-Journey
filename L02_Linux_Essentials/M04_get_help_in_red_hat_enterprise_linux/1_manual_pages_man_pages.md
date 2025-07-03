The **manual pages (man pages)** are a fundamental documentation resource in Red Hat Enterprise Linux (RHEL). They are typically available on the local system to provide users and system administrators with information about commands, configuration files, and system calls. Man pages are included as documentation within software packages and are one of the oldest help systems in Linux.

### Accessing Man Pages
You can view man pages directly from the command line using the **`man` command**. For example, to get help on the `ls` command, you would type `man ls`. When executed, the `man` command typically displays the command's name, the manual section it's documented in, its type, a short description, usage syntax, and a longer description.

Man pages are stored in subdirectories of the `/usr/share/man` directory.

### Man Page Structure and Headings
Each man page organises its information under various standard headings. Common headings include:
*   **NAME**: States the subject (command or file) and provides a brief description.
*   **SYNOPSIS**: Offers a concise summary of the command's syntax. Optional parameters are usually enclosed in square brackets `[]`.
*   **DESCRIPTION**: Provides a basic understanding of the topic.
*   **OPTIONS**: Explains the command-line options available.
*   **EXAMPLES**: Shows practical examples of how to use the command.
*   **FILES**: Lists related files and directories.
*   **SEE ALSO**: Directs you to other relevant man pages or topics, often with section numbers.
*   **BUGS**: Documents any known issues or limitations of the software.
*   **AUTHOR**: Provides information about the contributor(s) to the topic's development.

Not all man pages will feature every heading, as their relevance varies by topic.

### Manual Sections
Man pages are categorised into nine numbered sections to organise different types of information:
*   **Section 1**: User commands and shell programs (e.g., `ls(1)` or `passwd(1)`).
*   **Section 2**: System calls (kernel routines).
*   **Section 3**: Library functions (programming libraries).
*   **Section 4**: Special files, typically device files (e.g., in `/dev`).
*   **Section 5**: File formats, for various system configuration files (e.g., `passwd(5)` for `/etc/passwd`).
*   **Section 6**: Games and screensavers.
*   **Section 7**: Miscellaneous topics, conventions, and standards.
*   **Section 8**: System administration and privileged commands.
*   **Section 9**: Linux kernel API or internal kernel calls.

The `man` command typically searches sections in alphanumeric order. If a topic exists in multiple sections (e.g., `passwd` for both a command and a file format), the lowest-numbered section is displayed by default. To view a specific section, you must include the section number, for example, `man 5 passwd`. For the Red Hat Certified System Administrator (RHCSA) exam, sections 1, 5, and 8 are particularly important.

### Navigating Man Pages
When a man page is displayed, you can navigate its content using specific keyboard shortcuts, as the `man` command uses a pager program (usually `less`) to show the content:
*   **Spacebar**, **Page Down (PgDn)**, `f`, `Ctrl+V`, or `Ctrl+F`: Scroll **forward** one screen.
*   **Page Up (PgUp)**, `b`, `Ctrl+B`, or `Esc+V`: Scroll **backward** one screen.
*   **Enter** or **Down Arrow**: Move **forward** one line.
*   **Up Arrow**: Move **backward** one line.
*   `D` or `U`: Move down/up half a page.
*   `g` (lowercase G): Go to the **beginning** of the man page.
*   `G` (uppercase G, or `Shift+G`): Go to the **end** of the man page.
*   `q` or `Q`: **Quit** the man page and return to the command prompt.
*   `/string`: Search **forward** for the specified text string.
*   `?string`: Search **backward** for the specified text string.
*   `n`: Find the **next** occurrence of the search pattern.
*   `N`: Find the **previous** occurrence of the search pattern.
*   `h`: Displays help on navigation keys.

### Searching Man Pages by Keyword
If you don't know the exact name of a command or file, you can search for man pages using keywords:
*   The **`apropos` command** (or `man -k` option) searches for keywords in the names and short descriptions of all man pages and lists matching entries.
*   The **`whatis` command** provides a short, one-line description for a specified command or file from the man page database.
*   For a full-text search within man pages, the **`man -K` (uppercase)** option can be used, though it consumes more system resources and time. This command displays the first page with a match; you can then quit (`Q`) to view the next match or skip (`Ctrl+D`) to subsequent matches.
*   For new Linux installations, it might be necessary to run the **`mandb` command** (as root) to build an indexed database for keyword searches. The `man-db-cache-update` service typically performs this automatically when packages with man pages are installed.
*   Some commands also offer a quick help summary when executed with `--help` or `-?` options, providing a brief list of options without opening the full man page.

### Importance for RHCSA
Man pages are a **critical resource for the RHCSA exam**. During the exam, candidates have access to the local system's documentation, including man and info pages, and files in `/usr/share/doc`, but generally **no internet access**. Therefore, it is highly recommended that you review man pages for all commands covered in study materials and practice using them to find information to complete tasks.