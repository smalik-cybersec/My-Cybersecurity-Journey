# 🧩 **Lesson: Match File Names with Shell Expansions**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 78*

---

## 📚 Table of Contents

- [🧩 **Lesson: Match File Names with Shell Expansions**](#-lesson-match-file-names-with-shell-expansions)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 What is Shell Expansion?](#-what-is-shell-expansion)
  - [📂 Why Match Files Using Shell Patterns?](#-why-match-files-using-shell-patterns)
  - [✨ Globbing: The Power Behind File Matching](#-globbing-the-power-behind-file-matching)
    - [🔍 Examples](#-examples)
  - [🔢 Brace Expansion](#-brace-expansion)
    - [🧠 Syntax](#-syntax)
    - [🔍 Examples](#-examples-1)
  - [🧠 Practical Use Cases](#-practical-use-cases)
  - [🧪 Lab Exercises](#-lab-exercises)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 🎯 What is Shell Expansion?

**Shell expansion** in Bash refers to the process where the shell interprets **wildcards or special characters** to match **filenames, patterns, or generate arguments dynamically**.

This includes:

- **Filename expansion (globbing)**
- **Brace expansion**
- **Variable expansion**
- **Command substitution**

> This lesson focuses on **filename expansion (globbing)** and **brace expansion** for matching files.

---

## 📂 Why Match Files Using Shell Patterns?

Because:

- You can operate on **multiple files** using just one command.
- It allows automation of file-based tasks (backups, log cleanup, reports).
- Shell scripts depend on pattern matching to scale across environments.

---

## ✨ Globbing: The Power Behind File Matching

| Pattern | Matches                                     |
| ------- | ------------------------------------------- |
| `*`     | Any number of characters (zero or more)     |
| `?`     | Exactly one character                       |
| `[abc]` | Any one character listed (`a`, `b`, or `c`) |
| `[a-z]` | Any character in a range (lowercase a to z) |
| `[^x]`  | Any character except the listed one(s)      |

### 🔍 Examples

```bash
ls *.txt           # All files ending in .txt
ls file?.log       # file1.log, fileA.log (but NOT file12.log)
ls report[1-3].csv # report1.csv, report2.csv, report3.csv
ls data[!a-c].txt  # Excludes files with a, b, or c
```

> 🧠 Tip: Globbing patterns are expanded **before** the command is executed.

---

## 🔢 Brace Expansion

**Brace expansion** is used to generate multiple arguments or patterns.

```bash
echo file_{1..3}.txt
# Output: file_1.txt file_2.txt file_3.txt
```

### 🧠 Syntax

```bash
{item1,item2,...}
{start..end}
```

### 🔍 Examples

```bash
touch log_{mon,tue,wed}.txt
ls log_*.txt
# → Creates: log_mon.txt log_tue.txt log_wed.txt
```

```bash
touch test_{01..05}.sh
ls test_*.sh
```

---

## 🧠 Practical Use Cases

| Use Case                          | Example                       |
| --------------------------------- | ----------------------------- |
| 📁 **List all images**            | `ls *.jpg`                    |
| 🧹 **Remove old logs**            | `rm log*.gz`                  |
| 📦 **Bulk copy**                  | `cp file{1..3}.txt /backup/`  |
| 🧪 **Create test files**          | `touch test_{a,b,c}.txt`      |
| 🧬 **Target variable file names** | `ls config_20[2-4][0-9].json` |

---

## 🧪 Lab Exercises

Open a new terminal and try:

```bash
# Step 1: Create test files
mkdir ~/globbing_lab && cd ~/globbing_lab
touch file1.txt file2.txt fileA.txt fileB.log error.log report1.csv report2.csv

# Step 2: Pattern matching
ls *.txt
ls file?.*
ls report[1-2].csv
ls *.log
ls file[AB].*

# Step 3: Brace expansion
touch log_{jan,feb,mar}.txt
touch demo_{1..5}.sh
ls log_*.txt
ls demo_*.sh
```

---

## 🧠 Quiz Yourself

1. What does `*` match in a filename pattern?
2. How would you match `file1.txt`, `file2.txt`, and `file3.txt` only?
3. What is the result of `touch file_{a,b}.txt`?
4. What’s the difference between `?` and `*` in filename expansion?
5. Which expansion method allows you to create `demo1.sh` through `demo10.sh` quickly?

---

## 📎 Summary

- **Shell expansion** is essential for matching files dynamically in scripts and commands.
- **Globbing** uses wildcards like `*`, `?`, and `[]` to match filenames.
- **Brace expansion** is powerful for generating predictable sets of file names.
- These features enable **efficient file handling**, **automation**, and **flexibility** — especially in cybersecurity scripts, backup systems, and log parsers.