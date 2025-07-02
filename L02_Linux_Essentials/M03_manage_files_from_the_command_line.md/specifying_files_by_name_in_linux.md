In Linux, **files are specified by their names and paths**. You can refer to a file using:

- **Absolute paths** (starting from the root `/`)
- **Relative paths** (starting from your current directory)
- **Special characters** like `.` (current directory) and `..` (parent directory)
- **Wildcards** for matching multiple files

**Filenames are case-sensitive** and can include letters, numbers, periods, dashes, and underscores. Avoid spaces and special characters unless you know how to escape or quote them.

#### Key Concepts

- **Absolute Path:**
Begins with `/`, e.g., `/home/alex/report.txt`. Always points to the same file, no matter your current directory.
- **Relative Path:**
Does not begin with `/`. It’s relative to your current working directory.
Example: If you’re in `/home/alex`, the file `report.txt` can be referred to as `report.txt` or `./report.txt`.
- **Special Directories:**
    - `.` = current directory
    - `..` = parent directory
- **Home Directory Shortcuts:**
    - `~` = your home directory
    - `~username` = another user’s home directory


#### Practical Linux Commands

**1. Print Working Directory**

```bash
pwd
# Shows your current directory, e.g., /home/alex
```

**2. List Files by Name**

```bash
ls report.txt
# Lists report.txt if it exists in the current directory

ls /etc/passwd
# Lists the file /etc/passwd using an absolute path

ls ../notes.txt
# Lists notes.txt in the parent directory
```

**3. Use Wildcards to Specify Multiple Files**

```bash
ls *.txt
# Lists all files ending in .txt in the current directory

ls ~/Documents/*.pdf
# Lists all PDF files in your Documents directory
```

**4. Referencing Home Directories**

```bash
ls ~
# Lists files in your home directory

ls ~alex
# Lists files in the home directory of user 'alex' (if you have permission)
```

**5. Using Special Characters**

```bash
ls .
# Lists contents of the current directory

ls ..
# Lists contents of the parent directory
```

**6. Quoting Filenames with Spaces or Special Characters**

```bash
touch "my file.txt"
ls "my file.txt"
# Use quotes if the filename contains spaces or special characters
```


#### Output Examples

```bash
ls /etc/passwd
# Output: /etc/passwd

ls *.txt
# Output: report.txt  notes.txt  summary.txt
```


#### Common Errors

- **No such file or directory:**
If you mistype the filename or path, e.g., `ls repot.txt`, you’ll see:

```
ls: cannot access 'repot.txt': No such file or directory
```

- **Permission denied:**
If you try to access a file you don’t have permission for.


#### Key Takeaways

- You can specify files by **absolute or relative paths**.
- Use `.` and `..` for current and parent directories.
- Use `~` for home directories.
- Filenames are **case-sensitive**.
- Use quotes for filenames with spaces or special characters.

Here’s a quiz to test your understanding of **specifying files by name** on Linux. Each question focuses on how to reference files using absolute/relative paths, wildcards, and special characters.

### Quiz: Specify Files by Name

**1. Which of the following is an absolute path to a file?**
a) `notes.txt`
b) `./notes.txt`
c) `/home/alex/notes.txt`
d) `../notes.txt`

**2. What does the `~` character represent in a file path?**
a) The root directory
b) The current directory
c) The parent directory
d) The user’s home directory

**3. Which command lists all files ending with `.log` in the current directory?**
a) `ls .log`
b) `ls *.log`
c) `ls /log`
d) `ls log*`

**4. If you are in `/home/alex` and want to specify the file `report.txt` inside `/home/alex/docs`, which relative path is correct?**
a) `docs/report.txt`
b) `/docs/report.txt`
c) `./docs/report.txt`
d) Both a and c

**5. What does the command `ls ../` do?**
a) Lists files in the current directory
b) Lists files in the parent directory
c) Lists hidden files
d) Lists files in the root directory

**6. How would you specify a file named `my file.txt` in a command?**
a) `my file.txt`
b) `my\ file.txt`
c) `"my file.txt"`
d) Both b and c

**7. What does the wildcard `*` match in a filename?**
a) Any single character
b) Any number of characters (including none)
c) Only files starting with `*`
d) Only hidden files

**8. If you want to reference the file `-data.txt`, which command works?**
a) `cat -data.txt`
b) `cat ./-data.txt`
c) `cat -- -data.txt`
d) Both b and c

### Answer Key

1. c) `/home/alex/notes.txt`
2. d) The user’s home directory
3. b) `ls *.log`
4. d) Both a and c
5. b) Lists files in the parent directory
6. d) Both b and c
7. b) Any number of characters (including none)
8. d) Both b and c