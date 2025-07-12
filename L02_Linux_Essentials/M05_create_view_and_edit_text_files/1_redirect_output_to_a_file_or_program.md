Here is your complete, professional, and GitHub-ready documentation for:

---

# 🔀 **Lesson: Redirect Output to a File or Program**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 118*

---

## 📚 Table of Contents

- [🔀 **Lesson: Redirect Output to a File or Program**](#-lesson-redirect-output-to-a-file-or-program)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [🧠 What Is Redirection in Linux?](#-what-is-redirection-in-linux)
  - [➡️ Output Redirection Operators](#️-output-redirection-operators)
    - [Examples:](#examples)
  - [⬅️ Input Redirection](#️-input-redirection)
  - [❌ Error Redirection](#-error-redirection)
    - [Redirect both STDOUT and STDERR:](#redirect-both-stdout-and-stderr)
  - [🔗 Combine Redirections](#-combine-redirections)
  - [🧪 Practical Examples](#-practical-examples)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 🎯 Introduction

In Linux, you can **redirect the output of a command** to a **file**, another **command**, or even a **log system**, instead of just displaying it in the terminal.

> This is essential for automation, scripting, and handling large or sensitive output—especially in cybersecurity tasks like logging, scanning, or data collection.

---

## 🧠 What Is Redirection in Linux?

**Redirection** allows you to change where input comes from or where output goes.

Linux handles three **standard I/O streams**:

| Stream | Name            | Abbreviation | File Descriptor |
| ------ | --------------- | ------------ | --------------- |
| STDIN  | Standard Input  | input        | 0               |
| STDOUT | Standard Output | output       | 1               |
| STDERR | Standard Error  | error output | 2               |

---

## ➡️ Output Redirection Operators

| Operator | Description                      | Example                        |
| -------- | -------------------------------- | ------------------------------ |
| `>`      | Redirect STDOUT (overwrite file) | `ls > list.txt`                |
| `>>`     | Redirect STDOUT (append to file) | `echo "log entry" >> logs.txt` |

### Examples:

```bash
echo "This is a report" > report.txt        # Creates/overwrites
echo "Another line" >> report.txt           # Appends to existing file
```

---

## ⬅️ Input Redirection

| Operator | Description            | Example               |
| -------- | ---------------------- | --------------------- |
| `<`      | Take input from a file | `sort < unsorted.txt` |

---

## ❌ Error Redirection

| Operator | Description             | Example                        |
| -------- | ----------------------- | ------------------------------ |
| `2>`     | Redirect STDERR         | `cat missing.txt 2> error.log` |
| `2>>`    | Append STDERR to a file | `command 2>> error.log`        |

### Redirect both STDOUT and STDERR:

```bash
command > all.log 2>&1
```

---

## 🔗 Combine Redirections

```bash
# Redirect output to out.txt, errors to err.txt
some_command > out.txt 2> err.txt

# Redirect both to a single file
some_command &> combined.txt
```

You can also pipe output to another **command** using `|` (see next lesson for pipes).

---

## 🧪 Practical Examples

```bash
# Save disk usage to a file
df -h > disk_report.txt

# Try to open a non-existent file, save error
cat notafile.txt 2> error.txt

# Redirect output and error to the same log
ls /root /tmp > output.txt 2>&1

# Sort a file using input redirection
sort < names.txt > sorted_names.txt
```

---

## 🧠 Quiz Yourself

1. What is the difference between `>` and `>>`?
2. What does `2>` redirect?
3. How can you redirect both output and error to the same file?
4. What file descriptor number is assigned to STDERR?
5. Write a command that reads input from `input.txt` and writes the sorted result to `output.txt`.

---

## 📎 Summary

* Linux allows **redirecting output and input** to and from files and commands.
* Operators like `>`, `>>`, `<`, `2>`, and `2>&1` control **standard streams**.
* These tools are powerful in **scripting**, **log handling**, and **incident response**.
* Always test your redirection in scripts to avoid overwriting critical data.

---

✅ Would you like:

* 🧪 Guided Lab: Redirection + Error Logging
* 🧠 Quiz + Answer Key
* 📥 Markdown version for GitHub
* ⏭️ Next topic: *Use Pipes to Connect Commands*

You’ve just unlocked the foundation of Linux automation, Shahid. Let’s keep going 🔁📁🧑‍💻
