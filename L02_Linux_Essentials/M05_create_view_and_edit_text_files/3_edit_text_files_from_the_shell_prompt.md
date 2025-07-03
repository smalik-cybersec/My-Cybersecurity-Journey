The section "Edit Text Files from the Shell Prompt" focuses on the crucial skill of manipulating text files directly from the Linux command line, particularly using the `vim` editor. Understanding this is fundamental for Linux administration, as many system settings and programs are stored in text-based configuration files.

### Why Edit Text Files from the Shell Prompt?

*   **Linux's Design Philosophy:** The fundamental design principle of Linux dictates that information and configuration settings are primarily stored in text-based files. These files can follow various structures, such as lists of settings, INI-like formats, or structured XML or YAML.
*   **Ease of Editing:** A major advantage of this text-based structure is that these files can be easily edited with any simple text editor.
*   **System Administration Necessity:** As a system administrator, you will frequently need to run a series of commands, and creating shell scripts (which are just text files containing commands) is an efficient way to automate these tasks.
*   **Remote and Emergency Access:** You must be proficient with at least one text-mode editor because, often, a graphical desktop environment may not be available (e.g., when accessing a remote server via `ssh` or during emergency system rescue scenarios). Text-mode tools also generally offer more power and flexibility compared to their graphical counterparts.

### Key Text Editors for the Command Line

Linux offers several text editors that operate within the shell:

*   **Vim (Vi Improved):** This is the **default and most commonly installed text editor on Red Hat Enterprise Linux (RHEL) systems**. It's an enhanced version of the traditional Unix `vi` editor. `Vim` is highly configurable and efficient for experienced users, offering features like split-screen editing, color formatting, and highlighting. Mastering `vim` skills is considered essential for system administrators. A tutorial program, `vimtutor`, is available to help users gain competency.
*   **Nano:** Often recommended for beginners due to its simplicity and straightforward interface. It's a lean editor popular in limited-space environments. Common commands are displayed at the bottom of its window.
*   **Emacs:** Considered one of the most advanced and complex text editors. It can operate in both text-mode and graphical environments and offers extensive features, including multiple windows and buffers for editing several files simultaneously.
*   **Graphical Editors (Gedit, KWrite, Kate):** These are user-friendly editors available within graphical desktop environments. While convenient, they may not be installed on all servers, especially those without a GUI, making command-line editors indispensable.

### Working with the `Vim` Editor

`Vim` is a **mode-based editor**, which is a key concept to understand:

1.  **Command Mode (Normal Mode):**
    *   This is the **default mode when `vim` starts**.
    *   Keystrokes are interpreted as commands for navigation, deletion, copying, and pasting.
    *   To return to command mode from any other mode, **press the `Esc` key**. If unsure of the current mode, pressing `Esc` a few times will safely bring you back to command mode.

2.  **Insert Mode (Edit Mode / Entry Mode):**
    *   In this mode, **anything you type is entered as text into the file**.
    *   To enter insert mode from command mode, use commands such as:
        *   `i`: Insert text before the current cursor position.
        *   `I`: Insert text at the beginning of the current line.
        *   `a`: Append text after the current cursor position.
        *   `A`: Append text to the end of the current line.
        *   `o`: Open a new line below the current line and enter insert mode.
        *   `O`: Open a new line above the current line and enter insert mode.

3.  **Extended Command Mode (Last Line Mode / Ex Mode):**
    *   Entered by **typing a colon (`:`) from command mode**. The cursor moves to the bottom of the screen where you can type commands.
    *   Used for tasks like:
        *   `:w filename`: Save the buffer to a file (can be a different filename).
        *   `:wq`: Save the buffer data to the file and quit `vim`. (Alternatively, `ZZ` also saves and exits).
        *   `:q`: Quit `vim` if no modifications have been made.
        *   `:q!`: Quit `vim` and discard all changes made since the last save.
        *   `:s/old/new/`: Substitute `old` text with `new` text. Add `g` for global replacement on a line (`:s/old/new/g`), or `%s/old/new/g` for the entire file.
        *   `:n,ms/old/new/g`: Replace text between line numbers `n` and `m`.
        *   `:help`: Access the online help.

4.  **Visual Mode:**
    *   Entered by pressing `v` (character-by-character), `Shift+V` (line-by-line), or `Ctrl+V` (block selection) from command mode.
    *   Allows you to select text for manipulation, such as copying or deleting.

### Common `Vim` Editing Operations

Once in command mode, you can perform various actions:

*   **Navigation:**
    *   Arrow keys: Move cursor.
    *   `Ctrl+F` / `PageDown`: Move forward one screen.
    *   `Ctrl+B` / `PageUp`: Move backward one screen.
    *   `G`: Move to the last line in the buffer.
    *   `numG`: Move to line number `num` in the buffer.
    *   `gg`: Move to the first line in the buffer.
*   **Deletion:**
    *   `x`: Delete the character at the cursor position.
    *   `dd`: Delete the current line.
    *   `dw`: Delete the word or part of the word to the right of the cursor.
*   **Copying (Yanking) and Pasting (Putting):**
    *   `yy`: Yank (copy) the current line into a buffer.
    *   `p`: Put (paste) the contents of the buffer after the cursor (or below the current line).
    *   `P`: Put (paste) the contents of the buffer before the cursor (or above the current line).
*   **Changing Text:**
    *   `r`: Replace the character at the cursor position with the next character typed.
    *   `R`: Overwrite or replace text on the current line.
    *   `cw`: Change (delete and enter insert mode) the word at the cursor position.
    *   `cc`: Change the entire line.
    *   `~`: Change the letter case (uppercase to lowercase, and vice versa) at the cursor location.
*   **Undo:**
    *   `u`: Undo the last change made. `vim` supports multiple levels of undo, unlike older `vi` versions.
*   **Multiple Files:** `vim` allows editing multiple files in the same session and switching between them using commands like `:bn` (buffer next) and `:bp` (buffer previous) or `:buffer num`.

### Best Practices for Editing Text Files

*   **Backup Configuration Files:** It is always a good idea to create a backup copy of important configuration files before editing them to protect against mistakes.
*   **Permissions:** For sensitive files like `/etc/passwd`, it's safer to use dedicated tools like `vipw` instead of directly editing the file, as `vipw` provides backup and locking mechanisms. Setting execute permissions on shell scripts is done with `chmod +x filename`.
*   **Environment Variables:** You can set environment variables like `EDITOR` or `VISUAL` to define your preferred default text editor for command-line programs.