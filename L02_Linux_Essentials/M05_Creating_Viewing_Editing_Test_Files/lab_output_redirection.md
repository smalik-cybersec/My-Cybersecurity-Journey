# Lab: Redirecting Output in Linux

### 1. Objective
> To understand and practice redirecting command output to files and other commands using `>` (overwrite), `>>` (append), and `|` (pipe) operators. This is a fundamental skill for saving data, automating tasks, and processing information in a Linux environment for cybersecurity purposes.

### 2. Steps & Commands

**Step 1:** Use `>` to redirect `ls -l` output to a new file.
  `ls -l > my_directory_contents.txt`
  *Description: This command lists the detailed contents of your current directory and saves that list into a new file named `my_directory_contents.txt`. If the file existed before, it will be overwritten.*

**Step 2:** View the contents of the newly created file.
  `cat my_directory_contents.txt`
  *Description: Use the `cat` command to display the content of `my_directory_contents.txt` to confirm the output was redirected correctly.*

**Step 3:** Use `date` and `>>` to append the current date and time to the same file.
  `date >> my_directory_contents.txt`
  *Description: This command takes the current date and time and adds it to the end of `my_directory_contents.txt` without deleting the existing directory listing.*

**Step 4:** View the updated contents of the file to see the appended date.
  `cat my_directory_contents.txt`
  *Description: Verify that both the directory listing and the date are now in the file.*

**Step 5:** Use `|` (pipe) to send the output of `ls -l` to `grep` to find specific files.
  `ls -l | grep ".txt"`
  *Description: This command first lists all files with detailed information. Then, that entire list is passed (`|`) as input to the `grep` command, which filters for any lines containing ".txt", effectively showing only your text files.*

**Step 6:** Clean up the created file.
  `rm my_directory_contents.txt`
  *Description: Remove the file created during this lab to keep your working directory tidy.*

### 3. Key Takeaway
* Output redirection is a powerful Linux feature that allows you to control where the results of a command go, either to a file for saving/analysis (`>`, `>>`) or as input to another command for further processing (`|`). This is essential for data collection and automation in cybersecurity tasks.