# 📂 **Lesson: Specify Files by Name**

> *Module: Red Hat System Administration / Linux Essentials*
> *Craw Cyber Security One-Year Diploma – Page 54*

---

## 📚 Table of Contents

- [📂 **Lesson: Specify Files by Name**](#-lesson-specify-files-by-name)
  - [📚 Table of Contents](#-table-of-contents)
  - [🔍 Overview](#-overview)
  - [📁 Linux Filesystem Navigation Recap](#-linux-filesystem-navigation-recap)
  - [🔡 File Name Conventions](#-file-name-conventions)
  - [🧭 Specifying Files by Path](#-specifying-files-by-path)
    - [Absolute Path](#absolute-path)
    - [Relative Path](#relative-path)
  - [⭐ Wildcards (Globbing Patterns)](#-wildcards-globbing-patterns)
  - [🔎 File Search Techniques](#-file-search-techniques)
    - [1. `find` – Search files recursively](#1-find--search-files-recursively)
    - [2. `locate` – Fast indexed search (requires `updatedb`)](#2-locate--fast-indexed-search-requires-updatedb)
    - [3. `which` – Locate a command's executable](#3-which--locate-a-commands-executable)
    - [4. `type` – Check how a command is resolved](#4-type--check-how-a-command-is-resolved)
  - [🧪 Lab Activities](#-lab-activities)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 🔍 Overview

In Linux, **specifying files by name** is more than just typing their full name — it includes using **wildcards, relative or absolute paths**, and search tools to efficiently access files in scripts, commands, or automation.

> In cybersecurity and system administration, precision in file targeting can mean the difference between patching a vulnerability or breaking the system.

---

## 📁 Linux Filesystem Navigation Recap

| Command | Purpose                                 |
| ------- | --------------------------------------- |
| `pwd`   | Show current working directory          |
| `ls`    | List directory contents                 |
| `cd`    | Change directory                        |
| `tree`  | Show directory structure (if installed) |

---

## 🔡 File Name Conventions

Linux file names are:

| Rule                          | Explanation                                                  |                   |
| ----------------------------- | ------------------------------------------------------------ | ----------------- |
| **Case-sensitive**            | `Report.txt` ≠ `report.txt`                                  |                   |
| **No file extensions needed** | A file is executable or not based on permissions, not `.exe` |                   |
| **Special characters**        | Avoid spaces, quotes, special symbols (`*`, `&`, \`          | \`) unless quoted |
| **Hidden files**              | Files starting with a dot (e.g., `.bashrc`) are hidden       |                   |

> Use `ls -a` to show hidden files.

---

## 🧭 Specifying Files by Path

### Absolute Path

- Starts from root (`/`)

```bash
cat /etc/passwd
```

### Relative Path

- Starts from current directory

```bash
cat ./myfile.txt
cd ../ && ls
```

| Symbol | Meaning           |
| ------ | ----------------- |
| `.`    | Current directory |
| `..`   | Parent directory  |
| `~`    | Home directory    |

---

## ⭐ Wildcards (Globbing Patterns)

Wildcards allow flexible file name targeting:

| Wildcard | Meaning                                  | Example             | Result                         |
| -------- | ---------------------------------------- | ------------------- | ------------------------------ |
| `*`      | Matches **any number of characters**     | `ls *.txt`          | Lists all `.txt` files         |
| `?`      | Matches **exactly one character**        | `ls file?.sh`       | `file1.sh`, `fileA.sh`         |
| `[abc]`  | Matches **one of the listed characters** | `ls file[123].txt`  | `file1.txt`, `file2.txt`, etc. |
| `[a-z]`  | Range match                              | `ls file[a-z].txt`  | Matches files from a–z         |
| `[^x]`   | NOT match                                | `ls file[^0-9].txt` | Excludes digits                |

> 🔐 Globbing is powerful in scripts for log file cleanup, backups, or targeting malware.

---

## 🔎 File Search Techniques

### 1. `find` – Search files recursively

```bash
find /home/shahid -name "*.pdf"
```

### 2. `locate` – Fast indexed search (requires `updatedb`)

```bash
locate passwd
```

### 3. `which` – Locate a command's executable

```bash
which python3
```

### 4. `type` – Check how a command is resolved

```bash
type ls
```

---

## 🧪 Lab Activities

> Run these commands in your terminal for hands-on learning:

```bash
# 1. Create a practice directory
mkdir ~/lab_patterns && cd ~/lab_patterns

# 2. Create some sample files
touch log1.txt log2.txt log3.txt logX.log error.txt .hiddenfile config1.cfg config2.cfg

# 3. List only .txt files
ls *.txt

# 4. Match log files with a single-digit number
ls log?.txt

# 5. Match files starting with "config"
ls config*

# 6. Show hidden files
ls -a

# 7. Find all .cfg files recursively
find . -name "*.cfg"
```

---

## 🧠 Quiz Yourself

1. What’s the difference between `*` and `?` in file name matching?
2. Write a command to list all hidden files in your home directory.
3. How would you find all `.log` files inside `/var`?
4. What does the `~` symbol represent in file paths?
5. Explain the difference between absolute and relative paths.

---

## 📎 Summary

- Linux uses both **absolute** and **relative paths** to locate files.
- **Globbing patterns** like `*`, `?`, and `[]` are essential for flexible file targeting.
- Tools like `find`, `locate`, and `which` help in **automated file discovery**.
- Mastering file specification is critical for scripting, system analysis, and cybersecurity tasks like log analysis and malware cleanup.
