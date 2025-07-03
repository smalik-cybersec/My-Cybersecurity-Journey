Accessing the command line in Red Hat Enterprise Linux (RHEL) is fundamental for system administration and is a key skill for certifications such as the Red Hat Certified Systems Administrator (RHCSA). The command line, often referred to as the **shell**, is a text-based interface that allows you to input instructions to a computer system.

### The Linux Shell

The Linux command line is provided by a program called the shell. Over the years, many shell program variants have been developed, but the default user shell in RHEL is the **GNU Bourne-Again Shell (Bash)**. Bash is an improved version of the original Bourne Shell (sh) on UNIX systems.

The shell indicates it is waiting for user input by displaying a **shell prompt**. The appearance of this prompt varies depending on the Linux distribution and whether you are logged in as a regular user or the superuser (root).
*   For a **regular user**, the prompt typically ends with a **dollar ($) character**. For example, `[user@host ~]$`.
*   For the **superuser (root)**, a **hash (#) character** replaces the dollar ($) character, serving as a visual cue to avoid mistakes that could affect the entire system. For example, `[root@host ~]#`.

### Methods to Access the Command Line

You can access the command line in several ways:

1.  **Text-Mode Consoles (Virtual Consoles)**: Linux systems support **virtual terminals (VTs)**, which are multiple logical consoles that can each support an independent login session.
    *   During RHEL 9 installation, six text-based virtual console screens are available to monitor the process and view diagnostic messages. For example, `Ctrl+Alt+F2` displays a shell interface to run commands as the root user.
    *   After installation, if you are in a graphical environment, you can switch to a text-mode console by pressing **`Ctrl+Alt+F1`**, `Ctrl+Alt+F2`, and so on, for up to six terminals by default. When switching between text-mode VTs, `Alt+Fn` is often sufficient.
    *   When you log in to a console terminal, nothing is displayed on the screen as you type your password.

2.  **Graphical Terminal Emulators**: From a graphical desktop environment (such as GNOME), you can open a terminal emulator program to access the command line interface.
    *   Common methods to open a terminal in GNOME include:
        *   Selecting **`Terminal`** from the dash in the Activities overview.
        *   Searching for "terminal" in the search field.
        *   Pressing **`Alt+F2`** to open the "Enter a Command" dialog and typing `gnome-terminal`.
    *   These terminal windows often support features like copy/paste and customisation of fonts and colours.

3.  **Remote Access**: You can log in to a Linux system remotely using protocols like Secure Shell (SSH). The `ssh` command allows secure login to a remote system or execution of a command without a full login.

### Basic Command Syntax and Execution

Commands entered at the shell prompt typically have three basic parts:
*   **Command**: The name of the program to run (e.g., `ls`, `date`).
*   **Options**: These adjust the behaviour of the command, often starting with one or two dashes (e.g., `-L`, `--help`).
*   **Arguments**: These specify the target that the command should operate on (e.g., a filename, username).

To execute a command, you **press the Enter key**. You can run multiple commands on a single line by separating them with a **semicolon (`;`)**. For long commands, you can use a **backslash (`\`)** at the end of a line to continue typing the command on the next line.

Common basic commands include:
*   `whoami`: Displays the current user's username.
*   `hostname`: Shows the computer's hostname.
*   `pwd`: Displays the **present working directory**.
*   `ls`: Lists the contents of a directory.
*   `date`: Displays the current date and time.
*   `cal`: Displays a calendar.
*   `head` and `tail`: Display the beginning and end of a file, respectively (by default, 10 lines, but can be specified with `-n`).

### Command Line Features

The Bash shell offers powerful features to enhance efficiency:

*   **Command History**: The `history` command displays a list of previously executed commands, each with a number.
    *   You can recall commands using the **`Up Arrow`** and **`Down Arrow`** keys.
    *   The **exclamation point (`!`)** metacharacter can expand previous commands: `!number` runs the command matching that number, and `!string` runs the most recent command starting with that string.
    *   The `!!` command runs the very last command again.
*   **Command Line Editing**: Bash uses the Readline library for command line editing, offering shortcuts for cursor movement and text modification.
    *   `Ctrl+A`: Jumps to the beginning of the line.
    *   `Ctrl+E`: Jumps to the end of the line.
    *   `Ctrl+U`: Clears from the cursor to the beginning of the line.
    *   `Ctrl+K`: Clears from the cursor to the end of the line.
    *   `Ctrl+LeftArrow` / `Ctrl+RightArrow`: Jumps to the beginning/end of the previous/next word.
*   **Command Completion (Tab Completion)**: Pressing the **`Tab`** key can automatically complete commands, filenames, or variables. Pressing `Tab` twice may show all possible completions.
*   **Input/Output Redirection**: Linux uses three basic data streams: standard input (`stdin`), standard output (`stdout`), and standard error (`stderr`). Commands can redirect these streams using operators like:
    *   `>`: Redirects standard output to a file, overwriting existing content.
    *   `>>`: Appends standard output to a file.
    *   `|` (pipe): Sends the standard output of one command as the standard input to another.
*   **Environment Variables**: The shell maintains variables that affect how commands operate, such as `PATH`, which is a list of directories the shell searches for executable commands. `PS1` and `PS2` define the primary and secondary shell prompts, respectively.
*   **Directory Navigation**: Commands like `cd` (change directory), `mkdir` (make directory), `rmdir` (remove directory), `mv` (move), `cp` (copy), and `rm` (remove) are used to manage files and directories. Special characters like `~` (home directory), `.` (current directory), and `..` (parent directory) simplify navigation.

### Superuser Access

For administrative tasks, you need **superuser privileges**.
*   You can log in directly as the `root` user.
*   The `su` command (switch user or substitute user) allows you to change your identity within a shell. Typing `su` (without a username) assumes root, and you'll be prompted for the root password. Using `su -` will also load the root user's environment.
*   The `sudo` command runs a single command with root privileges, requiring your own password (or root's password depending on configuration).

### Logging Out

To terminate a shell session, you can use the `exit` command, `logout` command, or simply press the key combination **`Ctrl+D`**.

### Web Console Terminal Session

The **web console** (Cockpit) provides a web-based management interface for RHEL, offering a fully functional interactive terminal session within your web browser. This allows you to run arbitrary commands to manage and troubleshoot the system.