Here is your complete, professional, and GitHub-friendly documentation for:

---

# 🛡️ **Lesson: Manage Default Permissions and File Access**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 215*

---

## 📚 Table of Contents

- [🛡️ **Lesson: Manage Default Permissions and File Access**](#️-lesson-manage-default-permissions-and-file-access)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [🔍 What Are Default Permissions?](#-what-are-default-permissions)
  - [🧬 The `umask` Value](#-the-umask-value)
  - [📖 How umask Works](#-how-umask-works)
  - [🛠️ Viewing and Changing umask](#️-viewing-and-changing-umask)
    - [🔹 View Current umask](#-view-current-umask)
    - [🔹 Set umask Temporarily](#-set-umask-temporarily)
    - [🔹 Make umask Persistent](#-make-umask-persistent)
  - [📁 Examples with Files and Directories](#-examples-with-files-and-directories)
  - [🔐 Why umask Matters for Security](#-why-umask-matters-for-security)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 🎯 Introduction

Every time a new **file or directory** is created in Linux, it starts with a set of **default permissions**. These defaults are determined by a special setting called **`umask`** (user file-creation mode mask).

> Understanding and managing default permissions helps prevent accidental over-permissioning — a common cause of security breaches.

---

## 🔍 What Are Default Permissions?

By default:

* **Files** can have a maximum of `666` (rw-rw-rw-) permissions
* **Directories** can have a maximum of `777` (rwxrwxrwx) permissions

But these defaults are **filtered** through the **umask**, which subtracts permissions.

---

## 🧬 The `umask` Value

The `umask` is a **4-digit octal number** (typically `0022`, `0002`, or `0077`) that specifies what **permissions to remove** from new files and directories.

| Digit | Affects                             | Typical Meaning |
| ----- | ----------------------------------- | --------------- |
| 0     | No restriction (permission allowed) |                 |
| 2     | Remove write                        |                 |
| 7     | Remove all permissions              |                 |

Example:

* `umask 0022`

  * New files: `644` (rw-r--r--)
  * New dirs: `755` (rwxr-xr-x)

---

## 📖 How umask Works

To calculate **final permissions**:

```
Final permissions = Default permissions – umask
```

| Object Type | Default | umask 0022 | Resulting Permissions |
| ----------- | ------- | ---------- | --------------------- |
| File        | 666     | 022        | 644 (rw-r--r--)       |
| Directory   | 777     | 022        | 755 (rwxr-xr-x)       |

> ⚠️ Executable permission (`x`) is never set automatically for files.

---

## 🛠️ Viewing and Changing umask

### 🔹 View Current umask

```bash
umask
```

Output might be `0022`

### 🔹 Set umask Temporarily

```bash
umask 0077
```

Effect:

* New files: `600`
* New dirs: `700` (owner-only access)

### 🔹 Make umask Persistent

Edit user shell startup files:

```bash
nano ~/.bashrc
```

Add:

```bash
umask 027
```

Apply with:

```bash
source ~/.bashrc
```

---

## 📁 Examples with Files and Directories

```bash
umask 0022
touch public.txt
mkdir public_folder
ls -l
# => public.txt: rw-r--r-- | public_folder: rwxr-xr-x

umask 0077
touch private.txt
mkdir private_folder
ls -l
# => private.txt: rw------- | private_folder: rwx------
```

---

## 🔐 Why umask Matters for Security

| Risk                              | Mitigation with umask                    |
| --------------------------------- | ---------------------------------------- |
| World-readable confidential files | Use `umask 0077` for private work        |
| Shared team folder restriction    | Use `umask 0002` for group collaboration |
| Log files exposed to others       | Set stricter umask for cron/system users |

---

## 🧠 Quiz Yourself

1. What is the default maximum permission for a new file before umask is applied?
2. What does `umask 0022` translate to in final file permissions?
3. How can you make a `umask` value persistent?
4. Why doesn’t Linux set execute permission automatically for files?
5. What `umask` would you use to make files only accessible to the owner?

---

## 📎 Summary

* **umask** controls default permissions for newly created files and directories
* It **subtracts** permissions from a base value (`666` for files, `777` for directories)
* You can view it with `umask` and set it temporarily or permanently
* Lower umask = more permissions granted; higher umask = more restrictions
* Managing `umask` is a best practice in **system hardening**, **compliance**, and **data confidentiality**

---

✅ Let me know if you want:

* 🧪 A guided lab on `umask` settings
* 🧠 A quiz with answer key
* 📥 Export in Markdown for GitHub
* ⏭️ Next lesson: *Use Access Control Lists (ACLs) for Advanced Permissions*

You're mastering the default security behavior of Linux — excellent work, Shahid 🔐🧑‍💻
