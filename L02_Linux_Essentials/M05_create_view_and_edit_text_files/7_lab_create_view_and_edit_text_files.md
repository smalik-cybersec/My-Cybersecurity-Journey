To create the lab session for "Lab: Create, View, and Edit Text Files", you will follow a series of steps designed to build proficiency in manipulating text files using command-line tools, particularly the **Vim editor**. This lab, found in Chapter 5 of the "Red Hat Enterprise Linux 9 Administration" student guide, aims to equip you with essential file management skills.

**Lab Goal and Objectives**
The primary **goal** of this lab is to enable you to **create, view, and edit text files** from command output or within a text editor. By completing this lab, you should achieve the following **objectives**:
*   **Save output or errors to a file with shell redirection**, and process command output through multiple command-line programs using **pipes**.
*   **Create and edit text files from the command line with the `vim` editor**.
*   Set shell variables to run commands, and edit Bash startup scripts to configure shell and environment variables to modify shell and program behaviour.
*   **Use Vim visual mode to simplify editing large files**.

**Technical Requirements and Preparation**
For this practical exercise, it is assumed you are operating as the `student` user on a `workstation` machine within a Red Hat Enterprise Linux 9 (RHEL 9) virtual machine environment, typically installed with the Minimal Install software selection. The lab environment is usually set up using virtualization software like VirtualBox or VMware Workstation Player.

**Before You Begin**
To prepare your system and ensure all required resources are available, open your terminal on the `workstation` machine as the `student` user and run the following command:
```bash
[student@workstation ~]$ lab start edit-review
```
This command initializes your lab environment for the specific exercise.

**Lab Instructions: Create, View, and Edit Text Files**

Here are the step-by-step instructions for the lab, focusing on editing a text file with the Vim editor, including the use of Vim's visual mode:

1.  **Create a Shell Variable and Redirect Command Output**:
    *   Create a shell variable named `lab_file` and assign it the value `editing_final_lab.txt`.
    *   List the contents of your student home directory, including hidden directories and files (`ls -al`).
    *   Redirect this output to the file specified by your `lab_file` shell variable (`editing_final_lab.txt`), overwriting any existing content.
    ```bash
    [student@workstation ~]$ lab_file=editing_final_lab.txt
    [student@workstation ~]$ ls -al > $lab_file
    ```
2.  **Edit the File with Vim**:
    *   Open the `editing_final_lab.txt` file using the `vim` editor, referencing the `lab_file` shell variable.
    ```bash
    [student@workstation ~]$ vim $lab_file
    ```
    *   *Note*: Vim is an interactive, full-screen visual text-editing tool widely available in Linux distributions and is considered essential for system administrators due to its efficiency and customisation capabilities, especially in text-only environments. The `vimtutor` command provides an excellent tutorial for learning its basics.

3.  **Remove First Three Lines using Line-Based Visual Mode**:
    *   Inside Vim, position your cursor on the first character of the first line.
    *   Enter **line-based visual mode** by pressing `Shift+V` (uppercase V). This selects the entire current line.
    *   Move the cursor down twice using the down arrow key to select the first three lines.
    *   Delete the selected lines by typing `x`.

4.  **Remove Characters from First Column using Visual Mode**:
    *   Enter **visual mode** by pressing `V` (lowercase v).
    *   Position your cursor at the last character of the first column on the first line.
    *   Select the last seven characters from the first column.
    *   Delete the selection by typing `x`. You should preserve only the first four characters of the first column.

5.  **Remove Characters from First Column (Multiple Lines) using Visual Block Mode**:
    *   Enter **visual block mode** by pressing `Ctrl+V`.
    *   Repeat the operation from the previous step (removing characters from the first column), but this time select from the second to the last line.
    *   Preserve only the first four characters of the first column.

6.  **Remove Fourth Column using Visual Block Mode**:
    *   Enter **visual block mode** (`Ctrl+V`) again.
    *   Select and remove the fourth column of the file.

7.  **Remove Time Column using Visual Block Mode**:
    *   Enter **visual block mode** (`Ctrl+V`) again.
    *   Select and remove the time column, leaving only the month and day columns on all lines.

8.  **Remove Specific Rows using Visual Line Mode**:
    *   Enter **visual line mode** (`Shift+V`).
    *   Position your cursor on any character of the row containing the "Desktop" string and type `x` to delete the entire line.
    *   Repeat this operation for the row containing the "Public" string.

9.  **Save Changes and Exit Vim**:
    *   Save your modifications and exit the file by entering the last-line command `:wq`. The `w` command writes the file, and `q` quits the editor.

10. **Backup the File with a Timestamp**:
    *   Back up the `editing_final_lab.txt` file.
    *   Append the current date (in seconds) to the end of the backup filename, preceded by an underscore (`_`) character. Use the `lab_file` shell variable for this.
    ```bash
    [student@workstation ~]$ cp $lab_file editing_final_lab_$(date +%s).txt
    ```

11. **Append a Dashed Line**:
    *   Append a dashed line (`------------`, exactly 12 dashes) to the `editing_final_lab.txt` file, using the `lab_file` shell variable.
    ```bash
    [student@workstation ~]$ echo "------------" >> $lab_file
    ```
    *   *Note*: The `>>` operator appends output to a file, unlike `>` which overwrites.

12. **Append Directory Content**:
    *   List the content of the `Documents` directory.
    *   Redirect this output to the `editing_final_lab.txt` file, using the `lab_file` shell variable. This step demonstrates how to pipe command output and then append it to a file using `tee -a`.
    ```bash
    [student@workstation ~]$ ls Documents/ | tee -a $lab_file
    ```

13. **Confirm File Content**:
    *   Confirm that the new directory listing is located at the bottom of your `editing_final_lab.txt` file by displaying its content using the `cat` command with the `lab_file` shell variable.
    ```bash
    [student@workstation ~]$ cat $lab_file
    ```

**Evaluation**
After completing all the instructions, evaluate your work by running the following command:
```bash
[student@workstation ~]$ lab grade edit-review
```
Correct any reported failures and rerun the command until all criteria show a `PASS` status.

**Finish**
To clean up the resources used during this exercise, navigate to your student user's home directory and run the command:
```bash
[student@workstation ~]$ lab finish edit-review
```
This ensures that resources from previous exercises do not impact subsequent ones.