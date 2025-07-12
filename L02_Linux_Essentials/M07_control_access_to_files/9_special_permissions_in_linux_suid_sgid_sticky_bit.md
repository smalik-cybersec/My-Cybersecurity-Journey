Certainly, Shahid! Here's your complete, professional, and GitHub-ready documentation for:

---

# 🛡️ **Lesson: Special Permissions in Linux (SUID, SGID, Sticky Bit)**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Advanced Permissions Section*

---

## 📚 Table of Contents

- [🛡️ **Lesson: Special Permissions in Linux (SUID, SGID, Sticky Bit)**](#️-lesson-special-permissions-in-linux-suid-sgid-sticky-bit)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [🔐 What Are Special Permissions?](#-what-are-special-permissions)
  - [🔑 SUID (Set User ID)](#-suid-set-user-id)
    - [🔍 Use Case:](#-use-case)
  - [👥 SGID (Set Group ID)](#-sgid-set-group-id)
    - [🔍 Use Case:](#-use-case-1)
  - [📌 Sticky Bit](#-sticky-bit)
    - [🔍 Use Case:](#-use-case-2)
  - [⚙️ Applying and Viewing Special Permissions](#️-applying-and-viewing-special-permissions)
    - [🛠️ Symbolic Mode](#️-symbolic-mode)
    - [🔢 Numeric Mode](#-numeric-mode)
    - [👁️ Viewing Special Bits](#️-viewing-special-bits)
  - [🧪 Practical Examples](#-practical-examples)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 🎯 Introduction

In addition to regular permissions (`r`, `w`, `x`), Linux provides **three special permission bits** to support advanced access control use cases:

* **SUID (Set User ID)**
* **SGID (Set Group ID)**
* **Sticky Bit**

These permissions are particularly important for **secure script execution**, **collaborative directories**, and **file ownership control**.

---

## 🔐 What Are Special Permissions?

| Permission | Applies To  | Purpose                                                |
| ---------- | ----------- | ------------------------------------------------------ |
| **SUID**   | Files       | Run a program with file owner's privileges             |
| **SGID**   | Files/Dirs  | Inherit group ownership or run with group’s privileges |
| **Sticky** | Directories | Restrict delete access to owner only (e.g. `/tmp`)     |

---

## 🔑 SUID (Set User ID)

* When a file with **SUID** is executed, it runs with the **file owner’s UID**, not the current user's.
* Symbol: `s` in the **user execute** field (`-rwsr-xr-x`)
* Numeric mode: Add `4` in front (e.g., `4755`)

### 🔍 Use Case:

* `passwd` command (owned by root, run by regular users)

```bash
ls -l /usr/bin/passwd
# -rwsr-xr-x 1 root root ...
```

---

## 👥 SGID (Set Group ID)

* On files: runs with the **file group’s GID**
* On directories: files created inside inherit the **directory's group**
* Symbol: `s` in the **group execute** field (`-rwxr-sr-x` or `drwxr-sr-x`)
* Numeric mode: Add `2` in front (e.g., `2755`)

### 🔍 Use Case:

* Shared project folders with consistent group ownership

---

## 📌 Sticky Bit

* Used only on **directories**
* Allows only **file owners or root** to delete or rename files, even if others have write access
* Symbol: `t` in the **others execute** field (`drwxrwxrwt`)
* Numeric mode: Add `1` in front (e.g., `1777`)

### 🔍 Use Case:

* `/tmp` directory — world-writable but deletion restricted

```bash
ls -ld /tmp
# drwxrwxrwt 10 root root ...
```

---

## ⚙️ Applying and Viewing Special Permissions

### 🛠️ Symbolic Mode

```bash
chmod u+s file.sh   # Set SUID
chmod g+s dir/      # Set SGID
chmod +t dir/       # Set sticky bit
```

### 🔢 Numeric Mode

```bash
chmod 4755 secure_exec.sh
chmod 2755 shared_folder/
chmod 1777 /custom/tmp
```

### 👁️ Viewing Special Bits

```bash
ls -l file.sh
# Look for: s (setuid/setgid) or t (sticky) in the permission string
```

---

## 🧪 Practical Examples

```bash
# 1. Create a file with SUID
sudo cp /bin/cat /usr/local/bin/cat_suid
sudo chmod u+s /usr/local/bin/cat_suid

# 2. Create a group-shared folder with SGID
sudo mkdir /srv/devshare
sudo chgrp devteam /srv/devshare
sudo chmod 2775 /srv/devshare

# 3. Create a custom temporary directory with sticky bit
sudo mkdir /customtmp
sudo chmod 1777 /customtmp
```

---

## 🧠 Quiz Yourself

1. What does the `s` in the user or group position of `ls -l` mean?
2. How does SUID differ from regular execute permission?
3. What happens when you enable SGID on a directory?
4. What problem does the sticky bit solve in shared folders?
5. What numeric mode sets all three special bits?

---

## 📎 Summary

| Special Bit | Numeric | Symbolic | Applies To  | Purpose                    |
| ----------- | ------- | -------- | ----------- | -------------------------- |
| **SUID**    | 4       | `u+s`    | Files       | Run as file owner's UID    |
| **SGID**    | 2       | `g+s`    | Files/Dirs  | Run/inherit group          |
| **Sticky**  | 1       | `+t`     | Directories | Only file owner can delete |

* Use `chmod` to apply special bits (numeric or symbolic)
* Use `ls -l` to view special permissions
* Combine with normal `rwx` permissions to enforce advanced access rules

---

✅ Let me know if you'd like:

* 🧪 Guided Lab: Practice SUID, SGID, Sticky Bit
* 🧠 Quiz with answers
* 📥 Export in Markdown for GitHub
* ⏭️ Next lesson: *Use Access Control Lists (ACLs) for Fine-Grained Permissions*

You're entering the **advanced layer** of Linux file security, Shahid 🔐🧠 Keep building!
