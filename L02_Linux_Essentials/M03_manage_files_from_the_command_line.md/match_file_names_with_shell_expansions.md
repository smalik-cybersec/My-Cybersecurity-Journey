Let’s explore how to **match file names with shell expansions** (also called “globbing”) in the Bash shell. This is a fundamental skill for efficient file management and command-line productivity.

## Plain-English Explanation

**Shell expansions** allow you to use special characters (wildcards) to match multiple files or patterns in a single command. The shell automatically expands these patterns to the list of matching filenames before running the command. This saves time and effort, especially when working with many files.

The most common shell expansion characters (wildcards) are:

- `*` — matches **zero or more characters** (any string)
- `?` — matches **exactly one character**
- `[abc]` — matches **any one character in the brackets**
- `[a-z]` — matches **any one character in the range**


## Real Linux Commands with Examples

Let’s create a test directory and files for practice:

```bash
mkdir ~/glob_lab
cd ~/glob_lab
touch file1.txt file2.txt fileA.txt fileB.log data1.csv data2.csv script.sh
```

- This sets up a directory with various file types and names.


### 1. **Using the `*` Wildcard**

```bash
ls *.txt
# Lists all files ending with .txt: file1.txt file2.txt fileA.txt

ls file*
# Lists all files starting with 'file': file1.txt file2.txt fileA.txt fileB.log

ls *
# Lists all files in the directory
```


### 2. **Using the `?` Wildcard**

```bash
ls file?.txt
# Matches files with 'file' + any one character + .txt: file1.txt file2.txt fileA.txt

ls data?.csv
# Matches data1.csv and data2.csv
```


### 3. **Using Bracket Expressions**

```bash
ls file[AB].txt
# Matches fileA.txt only (fileB.txt would match if it existed)

ls file[1-2].txt
# Matches file1.txt and file2.txt
```


### 4. **Combining Wildcards**

```bash
ls *.txt *.log
# Lists all .txt and .log files

ls file?.*
# Matches file1.txt, file2.txt, fileA.txt, fileB.log
```


## Tab Completion and Shell Expansion

- **Tab completion** helps you auto-complete file and directory names.
Type part of a filename and press `Tab` to complete it.
If there are multiple matches, pressing `Tab` twice lists all possibilities[^1].


## Output Examples

```bash
ls *.csv
# Output: data1.csv  data2.csv

ls file?.*
# Output: file1.txt  file2.txt  fileA.txt  fileB.log
```


## Common Errors

- If no files match, you may see:

```
ls: cannot access '*.pdf': No such file or directory
```

- Quoting the pattern disables expansion:

```bash
ls "*.txt"
# Output: *.txt (literal string, not expanded)
```


## Key Takeaways

- **Shell expansions** (globbing) let you match groups of files efficiently.
- `*` matches any string, `?` matches one character, `[ ]` matches a set or range.
- Use wildcards with commands like `ls`, `cp`, `mv`, and `rm` for batch operations.
- Tab completion helps you quickly find and complete file names[^1].


## Try These in Your Lab

1. **Create files with different extensions and use wildcards to list, copy, or remove them.**
2. **Experiment with bracket expressions to match specific file patterns.**



### Quiz: Match File Names with Shell Expansions

**1. Which shell pattern matches all files ending with `.conf` in the current directory?**
a) `ls *.conf`
b) `ls .conf*`
c) `ls *conf.`
d) `ls conf*.`

**2. Which pattern matches files named `file1.txt`, `file2.txt`, and `file3.txt` but not `file10.txt`?**
a) `ls file?.txt`
b) `ls file*.txt`
c) `ls file[1-3].txt`
d) Both a and c

**3. What does the pattern `ls data[AB].csv` match?**
a) Any file starting with `data` and ending with `.csv`
b) Only `dataA.csv` and `dataB.csv`
c) All CSV files
d) Only `data[AB].csv` (literally)

**4. Which command lists all files with a single character extension (e.g., `file.a`, `test.b`)?**
a) `ls *.?`
b) `ls *.?`
c) `ls *.*`
d) `ls ?.file`

**5. If you run `ls [a-z]*.sh`, which files will match?**
a) Files starting with any lowercase letter and ending with `.sh`
b) Files starting with any letter and ending with `.sh`
c) Files ending with `.sh`
d) Files starting with `[a-z]` and ending with `.sh`

**6. What happens if you run `ls *.pdf` and no PDF files exist?**
a) All files are listed
b) An error or “No such file or directory” message
c) The command hangs
d) The command lists directories only

**7. Which pattern matches both `script.sh` and `script.bash`?**
a) `ls script.*`
b) `ls script.???`
c) `ls script.[sb]ash`
d) a and b

**8. What does quoting a wildcard pattern (e.g., `ls "*.txt"`) do?**
a) Expands the pattern as usual
b) Prevents the shell from expanding the pattern
c) Lists all `.txt` files
d) Causes an error

### Answer Key

1. a) `ls *.conf`
2. d) Both a and c
3. b) Only `dataA.csv` and `dataB.csv`
4. b) `ls *.?`
5. a) Files starting with any lowercase letter and ending with `.sh`
6. b) An error or “No such file or directory” message
7. a) `ls script.*`
8. b) Prevents the shell from expanding the pattern

**Try these in your lab:**

- Create files with different names and extensions, then use the patterns above to see which files match.
- Experiment with quoting patterns to observe the difference in behavior.