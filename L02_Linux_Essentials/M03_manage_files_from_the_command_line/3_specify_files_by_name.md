When you "Specify Files by Name" in Linux, you are essentially providing the system with a unique identifier or location for a particular file or directory within the file system hierarchy. This is a fundamental concept for interacting with files and directories from the command line.

Here are the key concepts and commands related to specifying files by name:

*   **Pathname**: A pathname is the route you take along the branches of the Linux file system hierarchy to get to the desired directory or file. It indicates the unique file-system location of a file or directory [RHCSA Red Hat Enterprise Linux 8.pdf, p. 55].

*   **Absolute Pathnames**:
    *   An **absolute path** (or fully qualified pathname) pinpoints the precise position of a file starting from the **root directory (`/`)** [RHCSA Red Hat Enterprise Linux 8.pdf, p. 55].
    *   It **always begins with a forward slash (`/`)** [RHCSA Red Hat Enterprise Linux 8.pdf, p. 55, 593].
    *   Example: `/home/joe/Documents/memos/memo1.doc` specifies the exact location of `memo1.doc` from the root.

*   **Relative Pathnames**:
    *   A **relative path** specifies the location of a file or directory **relative to the current working directory** [RHCSA Red Hat Enterprise Linux 8.pdf, p. 55].
    *   It **does not start with a forward slash (`/`)** [RHCSA Red Hat Enterprise Linux 8.pdf, p. 55].
    *   If your current directory is `/home/joe/Documents/memos`, you can refer to `memo1.doc` simply as `memo1.doc`.

*   **Current Working Directory**:
    *   This is the directory a user or process is currently "standing in".
    *   **`pwd` (print working directory)**: This command displays the **absolute pathname of the current working directory** for that shell. This helps you determine the syntax for relative path names.
    *   **`cd` (change directory)**: This command is used to move between directories in the file system.
        *   **`cd` or `cd ~`**: Typing `cd` alone or `cd ~` returns you to the current user's **home directory**. The tilde character (`~`) represents a user's home directory.
        *   **`cd ..`**: This command moves you up one level to the **parent directory**. The double dot (`..`) refers to the parent of the current working directory.
        *   **`cd .`**: The single dot (`.`) refers to the **current working directory** itself.
        *   **`cd -`**: This command returns you to the **previous working directory**.

*   **Listing Files and Directories (`ls`)** [RHCSA Red Hat Enterprise Linux 8.pdf, p. 54, 518]:
    *   The `ls` command (short for "list") displays the names of files and directories.
    *   If no directory is specified, it lists the contents of the **current working directory**.
    *   It can also list files in given directories or individually.
    *   **`-a` (all files)**: Normally, `ls` omits files whose names begin with a dot (`.`), known as hidden files or dot files. Adding `-a` displays all files, including these hidden files.
    *   **`-l` (long listing)**: This option displays detailed file information, including file type, permissions, link count, owner, group, size, date and time of last modification, and the name of the file.
    *   **`-d`**: When used with a directory name, it displays information *about* the directory itself rather than its contents.

*   **Filename Conventions and Case Sensitivity**:
    *   Linux allows files to be categorized by type without requiring file name extensions.
    *   Linux's native filesystems are **case-sensitive**. This means `afile.txt`, `Afile.txt`, and `AFILE.TXT` are distinct files. If you type a filename with incorrect case, the system will report that the file does not exist.
    *   While Linux supports long filenames that may contain embedded spaces and punctuation characters, it's recommended to **limit punctuation characters** to periods, dashes, and underscores, and **avoid embedding spaces** in filenames. For spaces, use underscores instead. If spaces are used, the filename needs to be encased in quotes when referenced from the command line.
    *   Files beginning with a period (`.`) are hidden by default from `ls` listings unless the `-a` option is used.

These concepts and commands form the basis for effective file navigation and management using the Linux command line.