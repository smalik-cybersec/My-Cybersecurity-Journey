The guided exercise "Edit Text Files from the Shell Prompt" on page 132 of the `rh124-9.0-student-guide.pdf` is designed to familiarise users with the **`vim` editor**, a crucial skill for Linux system administration. This exercise leverages the interactive `vimtutor` program to provide hands-on practice.

### Why Editing Text Files from the Shell Prompt is Essential

Linux's fundamental design philosophy dictates that information and configuration settings are primarily stored in **text-based files**. These can include various formats such as lists of settings, INI-like structures, or structured XML/YAML. The advantage of this text-based approach is that these files can be easily edited with any simple text editor.

For a system administrator, proficiency with a text-mode editor is indispensable because:
*   You will frequently need to **create and edit configuration files and shell scripts**. Shell scripts, for instance, are simply text files containing a list of commands to be executed.
*   Many Linux systems, especially servers, **may not have a graphical desktop environment installed** or available. In such cases, command-line editors are the only option for editing files, including during emergency system rescue scenarios.
*   Command-line tools often provide **more power and flexibility** for experienced users compared to their graphical counterparts.

Linux offers several text editors that operate within the shell:
*   **`vim` (Vi Improved)**: This is the **default and most commonly installed text editor on Red Hat Enterprise Linux (RHEL) systems**. It is highly configurable and efficient for experienced users, offering features like split-screen editing, color formatting, and highlighting. Mastering `vim` is considered **essential for system administrators**. The `vimtutor` program is explicitly designed to help users gain this competency.
*   **`nano`**: Often recommended for beginners due to its simplicity and straightforward interface. It displays common commands at the bottom of its window.
*   **`emacs`**: Considered one of the most advanced and complex text editors, capable of operating in both text-mode and graphical environments.

### Guided Exercise: Edit Text Files from the Shell Prompt (Page 132)

This exercise focuses on using the `vimtutor` command to learn the fundamentals of `vim`'s **mode-based operation**. `Vim` has distinct modes that dictate how keystrokes are interpreted:
*   **Command Mode (Normal Mode)**: This is the **default mode when `vim` starts**. Keystrokes are interpreted as commands for navigation, deletion, copying, and pasting. To return to command mode from any other mode, **press the `Esc` key**. It is safe to press `Esc` repeatedly if you are unsure of the current mode.
*   **Insert Mode (Edit Mode / Entry Mode)**: In this mode, **anything you type is entered as text into the file**. You enter insert mode from command mode using commands like `i` (insert text before the current cursor position) or `a` (append text after the current cursor position).
*   **Extended Command Mode (Last Line Mode / Ex Mode)**: Entered by typing a colon (`:`) from command mode. The cursor moves to the bottom of the screen where you can type commands for tasks such as saving, quitting, or search/replace operations.

#### Objectives and Outcomes

*   **Objectives**: To create and edit text files from the command line with the `vim` editor.
*   **Outcomes**: To edit files with `Vim` and gain competency in `Vim` by using the `vimtutor` command.

#### Instructions for the Exercise

1.  **Before You Begin**:
    *   As the `student` user on the `workstation` machine, execute the preparation command: `lab start edit-editfile`. This command ensures all necessary resources are available for the exercise.

2.  **Start `vimtutor`**:
    *   Open a terminal and type `vimtutor`. This command launches the **interactive tutorial for `vim`**.

3.  **Lesson 1.1 - The First `vim` Commands**:
    *   Follow the tutorial's instructions to learn basic `vim` commands. This typically covers how to start `vim` (e.g., `vim filename` opens a file for editing, creating it if it doesn't exist).

4.  **Lesson 1.2 - Moving the Cursor**:
    *   Learn efficient cursor movement in **Command Mode**. This includes using the arrow keys, or `h` (left), `j` (down), `k` (up), `l` (right) if introduced, as well as `Ctrl+F` or `PageDown` to move forward one screen, `Ctrl+B` or `PageUp` to move backward one screen. You also learn to jump to specific lines using `G` (last line), `gg` (first line), or `numG` (specific line number).

5.  **Lesson 1.3 - Exiting `vim`**:
    *   Understand how to **exit `vim`** from **Command Mode**:
        *   `:wq`: Save the file and quit `vim`. (Alternatively, typing `ZZ` in command mode also saves and exits).
        *   `:q!`: Quit `vim` and discard all changes made since the last save.
        *   `:q`: Quit `vim` if no modifications have been made.

6.  **Lesson 1.4 - Deleting Text**:
    *   Practice deleting text while in **Command Mode**. This includes:
        *   `x`: Delete the character at the cursor position.
        *   `dd`: Delete the current line.
        *   `Vim` offers other efficient keystrokes for deleting specific numbers of words, lines, sentences, or paragraphs, such as `dw` (delete word).

7.  **Lesson 1.5 - Inserting Text**:
    *   Learn various ways to enter **Insert Mode** from Command Mode:
        *   `i`: Insert text before the current cursor position.
        *   Other commands like `a` (append after cursor), `o` (open a new line below the current line) are also introduced.
    *   Remember, in `Insert Mode`, **all typed text directly modifies the file content**.

8.  **Lesson 1.6 - Appending Text**:
    *   This lesson reinforces the concept of adding text, specifically focusing on commands like `a` to append text after the cursor, and `A` to append text to the end of the current line.

9.  **Read Lesson 1 Summary**:
    *   Review the concepts covered in the first section of the tutorial. The `vimtutor` includes six more multi-step lessons, which are not assigned as part of the course but are available for further exploration.

10. **Return to workstation**:
    *   Exit `servera` and return to the `workstation` system as the `student` user by typing `exit`.

11. **Finish**:
    *   Once back in the `student` user's home directory on the `workstation` machine, run the command `lab finish edit-editfile` to complete the exercise and reset the lab environment.