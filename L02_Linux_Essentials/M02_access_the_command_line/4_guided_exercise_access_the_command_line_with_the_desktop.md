The "Guided Exercise: Access the Command Line with the Desktop" is specifically designed to help users familiarise themselves with the **GNOME 40 desktop environment** in Red Hat Enterprise Linux 9, and to teach them how to **run commands from a shell prompt in a terminal program**. The exercise focuses on the process of logging in through the graphical display manager as a regular user.

**Outcomes of the Exercise:**
Upon completing this guided exercise, you should be able to:
*   **Log in to a Linux system using the GNOME 40 desktop environment**.
*   **Execute commands from a shell prompt in a terminal program**.

**Preparatory Steps:**
Before you begin the exercise, you must use the `lab` command as the student user on the workstation machine to ensure all necessary resources are available:
`[student@workstation ~]$ lab start cli-desktop`

**Instructions for the Exercise:**
1.  **Log in to the workstation as the student user** with "student" as the password. This involves clicking the student user account on the GNOME login screen, entering "student" when prompted for the password, and then pressing Enter.
2.  **Change the password for the student user** from "student" to "55TurnK3y". This step requires opening a Terminal window and using the `passwd` command at the shell prompt. It is important to note that a subsequent "finish" script will revert the password for the student user back to "student", and this script must be executed at the end of the exercise.
3.  **Learn how to shut down the workstation from the graphical interface, but then cancel the operation** before the system powers off. This is achieved by navigating to the system menu in the upper-right corner, selecting "Power Off/Log Out > Power Off", and then clicking "Cancel" in the dialog box that appears.

**Finishing the Exercise:**
To conclude the exercise and ensure that resources from previous exercises do not interfere with future ones, you must navigate to the student user's home directory on the workstation machine and execute the `lab` command:
`[student@workstation ~]$ lab finish cli-desktop`

---

**General Information on Accessing the Command Line with a Desktop:**

**1. Desktop Environments and the Shell:**
*   A **desktop environment** functions as the graphical user interface (GUI) on a Linux system. In Red Hat Enterprise Linux (RHEL) 9, the **GNOME 40 desktop environment** is the default. Other popular desktop environments include KDE, Xfce, and Unity.
*   The **command line** is a text-based interface used to input instructions to the computer. The Linux command line is primarily delivered by a program known as the **shell**.
*   The **GNU Bourne-Again Shell (bash)** is the default user shell in RHEL. Bash is an advanced version of the original Bourne Shell (sh). Red Hat advises using the default shell for system administration, though users can choose alternatives.

**2. Launching a Terminal Session:**
To gain access to the shell prompt within a graphical environment, you need to open a **terminal program** (also referred to as a terminal emulator or shell window). Common methods to launch a terminal include:
*   **Within the GNOME Desktop:**
    *   Clicking the **Terminal icon** from the Dash, or by using the "Show Applications" button from the Activities overview.
    *   Typing "terminal" into the search bar located at the top of the windows overview.
    *   Pressing the **Alt+F2** key combination to open the "Enter a Command" window, then typing `gnome-terminal`.
    *   Navigating through menus: `Applications` ➢ `System Tools` ➢ `Terminal`.
*   **Within the KDE Desktop:** The default terminal emulator is **Konsole Terminal**. It can be accessed via the `Kickoff Application Launcher` ➢ `Applications` ➢ `System` ➢ `Terminal (Konsole)`.
*   **General Methods:**
    *   Many Linux desktops allow you to **right-click the desktop** to find an option such as "Open in Terminal", "New Terminal", or "Terminal Window".
    *   You can **create a launcher icon** on your desktop for quick access to a terminal emulator like `gnome-terminal` or `konsole`.
    *   The keyboard shortcut **Ctrl+Alt+T** can also quickly launch the GNOME terminal in some distributions.

**3. Understanding the Shell Prompt:**
After opening a terminal window, a **shell prompt** will be displayed, indicating that the shell is ready to receive commands.
*   For a **normal user**, the prompt typically ends with a **dollar sign ($)**. It commonly includes your username, hostname, and current directory, for example, `[user@host ~]$` or `christine@server01:~$`.
*   For the **root user** (administrator), the prompt concludes with a **hash sign (#)**.

**4. Interacting with the Command Line (Bash Shell Features):**
*   Commands are typed at the cursor position and executed by pressing **Enter**.
*   Commands typically comprise a **command name**, **options** (often preceded by a hyphen `-` or double hyphen `--`), and **arguments** (the targets of the command).
*   **Command History**: Previous commands can be recalled using the **Up/Down arrow keys**. The `history` command provides a list of previously executed commands. Commands can also be recalled using `!number` (by their history number) or `!string` (the most recent command starting with that string).
*   **Command Completion (Tab Completion)**: Pressing the **Tab key** can auto-complete command names, filenames, or variables, which helps in saving typing time and preventing errors. Pressing Tab twice will display all possible completions if there are multiple options.
*   **Command-Line Editing Shortcuts**: Useful shortcuts include **Ctrl+A** (jump to the beginning of the line), **Ctrl+E** (jump to the end of the line), **Ctrl+U** (clear from cursor to beginning), **Ctrl+K** (clear from cursor to end), **Alt+f** (move right one word), **Alt+b** (move left one word), **Ctrl+LeftArrow** (jump to the beginning of the previous word), **Ctrl+RightArrow** (jump to the end of the next word), and **Ctrl+R** (search history).
*   **Clearing the Screen**: The `clear` command or **Ctrl+L** can be used to clear the terminal screen.
*   **Switching Users**: The `su` command (e.g., `su -` for a login session) enables switching to another user account, including the `root` user. Alternatively, the `sudo` command allows a normal user to execute commands with administrative privileges.
*   **Password Management**: The `passwd` command is used to set or change a user's password.

**5. Virtual Consoles:**
*   Linux systems typically offer **multiple virtual consoles (VTs)**, which are distinct text-based terminal sessions.
*   You can **switch between these virtual consoles** by holding **Ctrl+Alt** and pressing a **function key (F1 through F7)**.
*   In RHEL 9, the **graphical login screen generally operates on tty1** (Ctrl+Alt+F1). Text-based login prompts are typically available on tty2 through tty6 (Ctrl+Alt+F2 through F6).
*   **Console 2 (Ctrl+Alt+F2)** specifically provides a shell interface where commands can be run as the root user.
*   To return to the graphical desktop, you would typically press **Ctrl+Alt+F1** or **Ctrl+Alt+F7** (depending on the system's configuration).