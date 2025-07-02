Certainly, here is a detailed guide for the "Lab: Access the Command Line" from page 40 of the sources, outlining the steps and expected actions.

This lab focuses on helping you become proficient with the Bash shell, specifically in executing commands, identifying file types, displaying portions of text files, and using command history shortcuts.

---

### Lab: Access the Command Line

**Outcomes**
Upon successful completion of this lab, you should be able to:
*   Successfully **run simple programs from the Bash shell command line**.
*   **Execute commands to identify file types and display parts of text files**.
*   Practice using some **Bash command history shortcuts to more efficiently repeat commands or parts of commands**.

**Before You Begin**
As the `student` user on the `workstation` machine, you will need to prepare your system for this exercise. To do this, execute the following command in your terminal:
`[student@workstation ~]$ lab start cli-review`
This command will prepare your environment and ensure that all required resources are available for the lab.

**Instructions (Step-by-Step)**

1.  **Use the `date` command to display the current time and date.**
    *   **Action:** Type `date` and press Enter.
    *   **Expected Output:** You should see the current day, month, date, time (in HH:MM:SS format with AM/PM and time zone), and year. For example:
        `[student@workstation ~]$ date`
        `Mon Feb 28 01:57:25 PM PDT 2022`

2.  **Display the current time in 24-hour clock time (for example, 13:57). Hint: The format string that displays that output is `%R`.**
    *   **Action:** Use the `+%R` argument with the `date` command.
    *   **Command:** `date +%R`
    *   **Expected Output:** You should see the time in 24-hour format:
        `[student@workstation ~]$ date +%R`
        `13:58`

3.  **What kind of file is `/home/student/zcat`? Is it readable by humans?**
    *   **Action:** Use the `file` command to determine its type.
    *   **Command:** `file zcat`
    *   **Expected Output:** The output should tell you it's a shell script and ASCII text, indicating it's human-readable:
        `[student@workstation ~]$ file zcat`
        `zcat: a /usr/bin/sh script, ASCII text executable`

4.  **Use the `wc` command and Bash shortcuts to display the size of `zcat`.**
    *   **Action:** You can use the `wc` command (word count, which also shows lines and bytes). To use a Bash history shortcut instead of retyping the filename, type `wc ` (with a space) and then press `Esc+.` (Escape key followed by a period). This shortcut inserts the last argument of the previous command into the current command line.
    *   **Command:** `wc` followed by `Esc+.` (which expands to `zcat`)
    *   **Expected Output:** The command will display the number of lines, words, and bytes in the `zcat` file.

5.  **Display the first 10 lines of the `zcat` file.**
    *   **Action:** Use the `head` command. Since `zcat` was the last argument in the previous step, you can again use `Esc+.` to quickly insert its name.
    *   **Command:** `head zcat` (or `head ` followed by `Esc+.`)
    *   **Expected Output:** The first 10 lines of the `/home/student/zcat` file will be displayed.

6.  **Display the last 10 lines of the `zcat` file.**
    *   **Action:** Use the `tail` command. Similar to the previous steps, you can use `Esc+.`
    *   **Command:** `tail zcat` (or `tail ` followed by `Esc+.`)
    *   **Expected Output:** The last 10 lines of the `/home/student/zcat` file will be displayed.

7.  **Display the usage message for the `zcat` command without executing the command, by using a command history shortcut.**
    *   **Note:** The provided solution in the source material for this specific instruction is incomplete, as it only demonstrates re-executing a previous `date +%R` command using `!2`. It does not explicitly show how to get the usage message for `zcat` using a history shortcut in this context.
    *   **Common methods (outside the precise solution provided for *this step's output*):**
        *   To generally get a usage message for a command, you would typically use `man zcat` (for the manual page) or `zcat --help`.
        *   If `zcat --help` was a *previous* command in your history (e.g., it was command number 5), you could use `!5` or `!zcat` to re-execute it.
    *   **As per the provided solution's example for `!number` for history recall:** You can inspect your command history by typing `history`. For instance, if `date +%R` was command number `2` in your history, you would re-execute it as follows:
        `[student@workstation ~]$ history`
        `(lists your command history)`
        `[student@workstation ~]$ !2`
        `date +%R`
        `14:02`
    *   **For the purpose of the original instruction to get `zcat`'s usage:** If you recall a command that showed `zcat`'s usage (e.g., `man zcat`), and it was, say, history number 6, you would type `!6`. If you just ran `zcat` itself with an error, it might print a usage message automatically.

8.  **Use the `tail` command with the `-n 20` option to display the last 20 lines in the file, using command-line editing to achieve this with minimal keystrokes.**
    *   **Action:** You can recall the previous `tail zcat` command from your history. A quick way is to type `tail` and then use an Up Arrow key to cycle through previous `tail` commands until you find `tail zcat`. Then, you can use the Left Arrow key to navigate to the beginning of `zcat` and insert `-n 20 ` (including the space) before `zcat`.
    *   **Command:** (After recalling and editing) `tail -n 20 zcat`
    *   **Expected Output:** The last 20 lines of the `zcat` file will be displayed.

9.  **Use the shell history to run the `date +%R` command again.**
    *   **Action:** As demonstrated in step 7, use the `!number` shortcut to re-execute the specific command from your history list. First, type `history` to identify the number corresponding to your `date +%R` command.
    *   **Command:** `!number` (replace `number` with the actual history number for `date +%R` from your `history` output).
    *   **Expected Output:** The command `date +%R` will be re-executed, displaying the current time in 24-hour format.

**Evaluation**
Once you have completed all the instructions, you can grade your work. As the `student` user on the `workstation` machine, use the `lab grade` command:
`[student@workstation ~]$ lab grade cli-review`
The system will evaluate your work and show a `PASS` or `FAIL` status for each grading criterion. If any failures are reported, correct them and rerun the `lab grade` command until all criteria show `PASS`.

**Finish**
Finally, to complete the exercise and clean up resources, change to the `student` user's home directory on the `workstation` machine and execute the `lab finish` command:
`[student@workstation ~]$ lab finish cli-review`
This step is important to ensure that resources from previous exercises do not impact upcoming exercises.

---