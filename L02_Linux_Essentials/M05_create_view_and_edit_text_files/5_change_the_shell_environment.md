To comprehensively address your query about "Change the Shell Environment" on page 134 of the student guide, we need to understand what the shell environment is, why it's important, and how to modify it for both temporary and persistent changes.

### Understanding the Shell Environment

The **shell environment** is a **text-based interface** that acts as an **interpreter** between the user and the Linux kernel. It provides a **customizable setting** for users and programs. In Red Hat Enterprise Linux (RHEL), the **GNU Bourne-Again Shell (Bash)** is the **default user shell**.

The shell environment is critical for system administrators as it allows them to **configure the system**, **create and edit configuration files**, and **automate tasks** through shell scripts [Page 132 Guided Exercise context, 119].

Within the shell environment, there are two primary types of variables that store data:

*   **Shell Variables (Local Variables)**: These are **private to the specific shell session** in which they are created. Their values are only available in the current shell and **cannot be used by programs or sub-shells** that are not started in that exact shell.
*   **Environment Variables (Global Variables)**: These variables are **inherited from the current shell to any sub-shells or programs** that it spawns. By convention, environment variable names are typically in **all uppercase characters**.

### Key Ways to Change the Shell Environment

You can define and modify various aspects of your shell environment to tailor it to your needs.

1.  **Setting and Unsetting Variables**:
    *   **Defining a Variable**: To assign a value to a variable, use the format `variable=value`. It is crucial **not to include any spaces around the equal sign (`=`)**. By default, the shell treats all variable values as strings, but you can explicitly define integer variables using `declare -i`.
    *   **Making a Variable Global**: To make a local shell variable accessible to sub-shells and other programs (i.e., make it an environment variable), use the `export` command. You can do this in two ways: `export VARIABLE` (after it's defined) or `export VARIABLE=value` (defining and exporting in one step). Note that a child shell **cannot permanently change or unset** a global environment variable's value in its parent shell.
    *   **Removing a Variable**: Use the `unset` command followed by the variable name (without the `$` symbol) to remove it from the shell environment.

2.  **Viewing Variable Values**:
    *   **Specific Variable**: To display the value of a particular variable, use `echo $VARIABLE`.
    *   **All Variables**: The `set` command lists **all currently set local and environment variables** (and shell functions).
    *   **Environment Variables Only**: The `env` or `printenv` commands display **only the environment variables**.

3.  **Customizing the Command Prompt (`PS1`)**:
    *   The appearance of your shell prompt is controlled by the **`PS1` environment variable**.
    *   You can customize it using **special character expansions** (e.g., `\u` for username, `\h` for hostname, `\w` for current working directory, `\t` for time, `\!` for history number).
    *   The prompt value **must be enclosed in quotation marks** (single or double) and Red Hat recommends ending it with a **trailing space**. The `PS2` variable controls the secondary prompt, used for multi-line commands.

4.  **Setting the Default Text Editor**:
    *   Many command-line programs use the **`EDITOR` or `VISUAL` environment variables** to determine your preferred text editor.
    *   You can set it, for example, by running `export EDITOR=vim` or `export EDITOR=nano`. Traditional systems often default to `vi` or `emacs`, but `nano` is considered easier for beginners.

5.  **Modifying the Command Search Path (`PATH`)**:
    *   The `PATH` environment variable tells the shell which directories to search for executable commands when you type a command without specifying its full path.
    *   You can add new directories to your `PATH` by appending them (e.g., `PATH=$PATH:/opt/mysystem/bin`). Changes made directly at the command line are **not persistent** across sessions.

6.  **Adjusting Default File Permissions (`umask`)**:
    *   The `umask` command sets the **default permissions for newly created files and directories**.
    *   Common `umask` values include `022` (gives other users read access to new files) and `077` (most restrictive, gives no access to others).

7.  **Creating Command Shortcuts (Aliases)**:
    *   **Aliases** are convenient shorthands for longer commands.
    *   They are defined using the `alias` command (e.g., `alias ll='ls -l --color=auto'`).
    *   Aliases defined on the command line are **not persistent** and vanish when the shell session ends.

### Making Changes Persistent with Shell Startup Files

To make environment changes permanent, they must be placed in **shell startup (or initialization) files**. These plain-text files contain shell commands and are **sourced by the shell upon user login or when a new shell is opened**.

There are two categories of startup files:

*   **System-Wide Startup Files**:
    *   Located in the `/etc` directory, these files **apply to all users** on the system and are maintained by the Linux administrator.
    *   **`/etc/profile`**: Executed once when a user **logs in** (for interactive login shells). It sets general environment variables like `PATH` and **sources any scripts in `/etc/profile.d/`**.
    *   **`/etc/bashrc`**: Executed **each time any Bash shell is opened** (for both interactive login and non-login shells). It typically sets the default prompt and may add aliases.
    *   **`/etc/profile.d/`**: A directory where administrators can place custom `.sh` scripts. This is the **recommended place for system-wide additions** to avoid conflicts during system upgrades.

*   **Per-User Startup Files**:
    *   Located in each user's home directory (often called **dot files** because their names start with a period, making them hidden by default).
    *   New user accounts typically get skeleton versions of these files copied from the `/etc/skel` directory by `useradd`.
    *   **`~/.bash_profile`**: Executed only once when a user **logs in** (for interactive login shells). It's the appropriate place to define **environment variables** that should be set on login and usually **sources `~/.bashrc`**.
    *   **`~/.bashrc`**: Executed **each time an interactive Bash shell is opened**, including when a user logs in (if sourced by `~/.bash_profile`) and when a new terminal window is launched. This is the **best location to add user-specific aliases and functions**.
    *   **`~/.bash_login`**: An alternative to `~/.bash_profile` if `~/.bash_profile` is not found.
    *   **`~/.profile`**: Used by some distributions (e.g., Ubuntu) for login shell configuration, similar to `~/.bash_profile`.
    *   **`~/.bash_logout`**: Executed each time a Bash shell is exited.

### Applying Changes

After modifying a startup file, the changes won't take effect immediately in the current shell. To apply them, you can:
*   **Re-login**: Log out and then log back in to start a new shell session that sources the modified files.
*   **`source` the file**: Use `source FILENAME` or `. FILENAME` (note the space before the dot) to force the current shell to re-read and execute the commands in the specified file.

### Relevance to the Guided Exercise

The "Guided Exercise: Edit Text Files from the Shell Prompt" on page 132 and the subsequent "Change the Shell Environment" on page 134 of `rh124-9.0-student-guide.pdf` are designed to teach these core concepts. The exercise specifically walks you through using the `vim` editor to modify the `~/.bashrc` file to **change the `PS1` shell variable** and **set the `EDITOR` environment variable**. This hands-on practice helps solidify the understanding of how to customize and persist shell environment settings crucial for effective Linux administration.