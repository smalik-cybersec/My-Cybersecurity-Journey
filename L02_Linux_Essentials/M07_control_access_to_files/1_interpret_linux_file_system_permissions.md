# 📂 **Lesson: Interpret Linux File System Permissions**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 200*

---

## 📚 Table of Contents

- [📂 **Lesson: Interpret Linux File System Permissions**](#-lesson-interpret-linux-file-system-permissions)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [📁 What Are File System Permissions?](#-what-are-file-system-permissions)
    - [Types of Permissions](#types-of-permissions)
  - [🧑 User, Group, and Others](#-user-group-and-others)
  - [🔠 Understanding Permission Strings](#-understanding-permission-strings)
    - [Breakdown of `-rwxr-xr--`](#breakdown-of--rwxr-xr--)
  - [🔢 Numeric (Octal) Representation](#-numeric-octal-representation)
    - [Examples](#examples)
    - [Putting it together](#putting-it-together)
  - [🧪 Practical Examples](#-practical-examples)
    - [View permissions](#view-permissions)
    - [Change permissions symbolically](#change-permissions-symbolically)
    - [Change permissions numerically](#change-permissions-numerically)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 🎯 Introduction

Linux is a **multi-user operating system**, and permissions are the foundation of its **security model**. Every file and directory in Linux has a set of permissions that defines **who can read, write, or execute** the object.

> Misconfigured permissions can lead to **data leaks, privilege escalation, and root access compromises**. Interpreting them accurately is the first step toward securing a Linux system.

---

## 📁 What Are File System Permissions?

Each file or directory has three types of permissions, applied to three categories of users:

### Types of Permissions

| Symbol | Permission | Description                     |
| ------ | ---------- | ------------------------------- |
| `r`    | Read       | View contents of file/directory |
| `w`    | Write      | Modify file or directory        |
| `x`    | Execute    | Run a file or enter a directory |

---

## 🧑 User, Group, and Others

Every file and directory is owned by:

- **User (u):** the file owner
- **Group (g):** a group associated with the file
- **Others (o):** everyone else on the system

Permissions are defined separately for each of these.

---

## 🔠 Understanding Permission Strings

Run:

```bash
ls -l
```

You’ll see output like:

```bash
-rwxr-xr-- 1 shahid devteam 1452 Jul 10 11:42 script.sh
```

### Breakdown of `-rwxr-xr--`

| Position | Meaning                                     |
| -------- | ------------------------------------------- |
| 1st char | File type (`-` for file, `d` for directory) |
| 2–4      | User permissions (`rwx`)                    |
| 5–7      | Group permissions (`r-x`)                   |
| 8–10     | Others permissions (`r--`)                  |

So `-rwxr-xr--` means:

- User (shahid) can read, write, and execute
- Group (devteam) can read and execute
- Others can only read

---

## 🔢 Numeric (Octal) Representation

Each permission triplet can be represented as a **number**:

| Permission | Binary | Value |
| ---------- | ------ | ----- |
| `r`        | 4      | 100   |
| `w`        | 2      | 010   |
| `x`        | 1      | 001   |

### Examples

| Symbolic | Octal | Meaning                |
| -------- | ----- | ---------------------- |
| `rw-`    | 6     | read + write           |
| `r--`    | 4     | read only              |
| `rwx`    | 7     | read + write + execute |
| `r-x`    | 5     | read + execute         |

### Putting it together

```bash
chmod 754 file.txt
```

Means:

- User: `7` → rwx
- Group: `5` → r-x
- Others: `4` → r--

---

## 🧪 Practical Examples

### View permissions

```bash
ls -l
```

### Change permissions symbolically

```bash
chmod u+x script.sh       # Add execute for user
chmod g-w file.txt        # Remove write for group
chmod o= file.txt         # Remove all for others
```

### Change permissions numerically

```bash
chmod 644 notes.txt       # rw-r--r--
chmod 755 script.sh       # rwxr-xr-x
chmod 700 private.txt     # rwx------
```

---

## 🧠 Quiz Yourself

1. What do the first 10 characters in `ls -l` output represent?
2. What permission is represented by `6` in octal?
3. What is the meaning of `chmod 755 file.sh`?
4. What’s the difference between symbolic and numeric mode in `chmod`?
5. How would you remove all permissions for "others" from a file?

---

## 📎 Summary

- Linux permissions consist of **read (r), write (w), and execute (x)**
- Permissions apply to **user**, **group**, and **others**
- You can represent permissions in **symbolic or numeric (octal)** form
- Use `ls -l` to view, and `chmod` to change permissions
- Understanding permissions helps you **secure files, scripts, and services**
