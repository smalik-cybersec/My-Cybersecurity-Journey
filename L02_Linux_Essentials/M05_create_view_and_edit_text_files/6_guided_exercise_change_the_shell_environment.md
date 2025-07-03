The "Guided Exercise: Change the Shell Environment" on page 141 of the student guide is designed to familiarise you with modifying your Bash shell environment. This exercise outlines how to personalise your shell prompt and configure your preferred text editor, ensuring these settings persist across different shell sessions.

### Key Objectives and Steps of the Exercise:

The exercise aims for the following outcomes:
*   **Edit a user profile**.
*   **Create a shell variable**.
*   **Create an environment variable**.

To begin, you initiate the lab environment using the command `lab start edit-bashconfig`.

1.  **Changing the `PS1` Shell Variable**:
    *   The exercise instructs you to modify the `student` user's `PS1` shell variable. This variable controls the appearance of your command prompt.
    *   You are to set the `PS1` value to `[\u@\h \t \w]$ `, which includes dynamic information such as the **username (`\u`)**, **hostname (`\h`)**, **current time (`\t`)**, and **current working directory (`\w`)**. It is recommended to enclose the value in quotation marks and include a trailing space for readability.
    *   To make this change persistent, you will edit the **`~/.bashrc` configuration file** using the `vim` editor after logging into a remote server (e.g., `servera`) via `ssh`. The `~/.bashrc` file is read each time an interactive Bash shell is opened, making it an ideal place for user-specific aliases and functions.
    *   After modifying the `~/.bashrc` file, you can either **exit the `ssh` session and re-login** to see the changes take effect, or immediately apply them in the current shell by executing `source ~/.bashrc`.

2.  **Assigning a Local Shell Variable**:
    *   The next step involves assigning a value to a local shell variable and then retrieving its value. **Shell variables** are temporary storage for data that are private to the current shell session. They are not automatically inherited by sub-shells or other programs.
    *   You define a variable using the format `variable=value`, ensuring there are no spaces around the equal sign. To view its value, you use the `echo $variable` command. Variable names can consist of uppercase or lowercase letters, digits, and the underscore character.

3.  **Assigning an Environment Variable**:
    *   You are then asked to assign a value to the `EDITOR` variable and simultaneously make it an environment variable using a single command, such as `export EDITOR=vim`. **Environment variables** (also known as global variables) are inherited by any sub-shells or programs launched from the current shell. This is particularly useful because many command-line programs respect the `EDITOR` or `VISUAL` environment variables to determine your preferred text editor. The `export` command explicitly makes a local shell variable available to child processes.

4.  **Completing the Exercise**:
    *   Finally, you will exit the remote `servera` session, return to your `workstation` system, and complete the exercise using `lab finish edit-bashconfig`.

### Broader Context of Shell Environment Changes:

*   The **shell environment** is a crucial component of Linux, providing a text-based interface and interpreter between the user and the kernel. The **GNU Bourne-Again Shell (Bash)** is the default user shell in Red Hat Enterprise Linux (RHEL).
*   To ensure that changes to your shell environment are permanent, they must be saved in **shell startup (or initialization) files**. For individual users, key files include `~/.bashrc` (for interactive shells) and `~/.bash_profile` (primarily for login shells). System-wide environment settings are typically configured in files within the `/etc` directory, such as `/etc/profile` and scripts located in `/etc/profile.d/`.
*   Understanding and customising the shell environment is a **fundamental skill for Linux administration**, enabling efficient system configuration, file editing, and task automation through shell scripts.
*   Beyond `echo` and `export`, other commands for managing variables include `unset` (to remove a variable) and `unalias` (to remove an alias). To view all currently set variables, the `set` command can be used, while `env` or `printenv` list only environment variables.