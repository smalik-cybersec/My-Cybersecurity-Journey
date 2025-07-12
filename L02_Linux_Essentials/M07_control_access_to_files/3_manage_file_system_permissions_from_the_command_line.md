Here is your complete, professional, and GitHub-friendly documentation for:

---

# 🔐 **Lesson: Manage File System Permissions from the Command Line**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 208*

---

## 📚 Table of Contents

- [🔐 **Lesson: Manage File System Permissions from the Command Line**](#-lesson-manage-file-system-permissions-from-the-command-line)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [🔍 Understanding Permissions Recap](#-understanding-permissions-recap)
  - [⚙️ The `chmod` Command](#️-the-chmod-command)
    - [🔹 Symbolic Mode](#-symbolic-mode)
    - [🔹 Numeric (Octal) Mode](#-numeric-octal-mode)
  - [🧑 File Ownership: `chown` and `chgrp`](#-file-ownership-chown-and-chgrp)
    - [🔹 `chown` — Change file owner](#-chown--change-file-owner)
    - [🔹 `chgrp` — Change group ownership](#-chgrp--change-group-ownership)
    - [Combine both:](#combine-both)
  - [🔢 Symbolic vs Numeric Mode](#-symbolic-vs-numeric-mode)
  - [🧪 Practical Command Examples](#-practical-command-examples)
  - [🚫 Common Mistakes to Avoid](#-common-mistakes-to-avoid)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 🎯 Introduction

Linux file systems use permission flags to **control who can access files and directories**. These permissions can be changed or assigned directly from the **command line** using tools like `chmod`, `chown`, and `chgrp`.

> Properly managing file permissions is essential for protecting sensitive data, restricting unauthorized access, and preventing privilege escalation.

---

## 🔍 Understanding Permissions Recap

Each file or directory has:

* **User (u)** — owner
* **Group (g)** — group owner
* **Others (o)** — everyone else

Each of them can have:

* **Read (r)** — view file or list directory
* **Write (w)** — modify file or directory contents
* **Execute (x)** — run script / enter directory

Example:

```bash
-rwxr-xr-- 1 shahid devteam  892 Jul 12 13:10 scan.sh
```

---

## ⚙️ The `chmod` Command

Used to change permission **modes** on files and directories.

### 🔹 Symbolic Mode

```bash
chmod u+x script.sh     # Add execute to user
chmod g-w report.txt    # Remove write from group
chmod o=r file.txt      # Set read-only for others
chmod a+x tool.sh       # Add execute for all (u+g+o)
```

### 🔹 Numeric (Octal) Mode

```bash
chmod 644 file.txt      # rw-r--r--
chmod 755 run.sh        # rwxr-xr-x
chmod 700 secret.sh     # rwx------
```

| Value | Permission | Binary |
| ----- | ---------- | ------ |
| 7     | rwx        | 111    |
| 6     | rw-        | 110    |
| 5     | r-x        | 101    |
| 4     | r--        | 100    |
| 0     | ---        | 000    |

---

## 🧑 File Ownership: `chown` and `chgrp`

### 🔹 `chown` — Change file owner

```bash
sudo chown analyst file.txt
sudo chown root:root /etc/secure.conf
```

### 🔹 `chgrp` — Change group ownership

```bash
sudo chgrp devteam shared.txt
```

### Combine both:

```bash
sudo chown shahid:devteam project/
```

---

## 🔢 Symbolic vs Numeric Mode

| Mode     | Syntax      | Best Use Case               |
| -------- | ----------- | --------------------------- |
| Symbolic | `chmod u+x` | Readable, selective changes |
| Numeric  | `chmod 755` | Fast, full permission sets  |

---

## 🧪 Practical Command Examples

```bash
# Give owner full access, deny everyone else
chmod 700 confidential.txt

# Make script executable by all users
chmod a+x scan.sh

# Set directory permissions to rwx for user and group only
chmod 770 /opt/shared

# Change ownership to 'shahid'
sudo chown shahid notes.txt

# Change group to 'students'
sudo chgrp students homework.txt

# Combine both
sudo chown shahid:students homework.txt
```

---

## 🚫 Common Mistakes to Avoid

| Mistake                               | Consequence                          |
| ------------------------------------- | ------------------------------------ |
| `chmod 777` on sensitive files        | Anyone can read, write, or execute   |
| Forgetting `-R` for recursive changes | Only top directory gets changed      |
| Omitting `a+` or `o+` when needed     | Unintended access remains restricted |
| Misusing `chown` on system files      | Can break critical services          |

---

## 🧠 Quiz Yourself

1. What is the difference between `chmod` and `chown`?
2. How would you make a file executable only by its owner?
3. What does `chmod 644` mean in symbolic form?
4. How do you recursively apply permissions to a directory?
5. What command would you use to change both owner and group?

---

## 📎 Summary

* Use `chmod` to change file permissions (symbolic or numeric)
* Use `chown` to change the file owner and optionally the group
* Use `chgrp` to change the group only
* Understand numeric values (e.g., `755`, `644`) for quicker permission setting
* Always review permissions with `ls -l` and apply least privilege

---

✅ Let me know if you'd like:

* 🧪 Guided Lab to practice `chmod`, `chown`, and `chgrp`
* 🧠 Quiz with answers
* 📥 Export as Markdown or PDF for GitHub portfolio
* ⏭️ Next topic: *Use Access Control Lists (ACLs) for Advanced Permissions*

You’re now confidently controlling who can access what — a key cybersecurity and sysadmin skill, Shahid 🧑‍💻🔐
