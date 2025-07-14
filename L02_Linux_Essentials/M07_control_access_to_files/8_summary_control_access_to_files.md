# 📎 **Summary: Control Access to Files**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 224*

---

## 📖 Overview

This lesson focused on how to **control access to files and directories** in Linux using:

* **Standard file permissions** (`r`, `w`, `x`)
* **Ownership management** (`user`, `group`)
* Tools like `chmod`, `chown`, `chgrp`, and `umask`

Understanding and applying these concepts is essential for **file-level security**, **collaboration control**, and **preventing unauthorized access**.

---

## 🔐 Key Concepts

### 1. **File Permissions**

Each file/directory has:

* **User (u)** — file owner
* **Group (g)** — associated group
* **Others (o)** — all other users

Permission types:

| Symbol | Meaning                |
| ------ | ---------------------- |
| `r`    | Read                   |
| `w`    | Write                  |
| `x`    | Execute (or enter dir) |

---

### 2. **Permission Management Tools**

| Command | Use Case                                   |
| ------- | ------------------------------------------ |
| `chmod` | Change permissions (numeric/symbolic)      |
| `chown` | Change file owner and group                |
| `chgrp` | Change group ownership only                |
| `umask` | Set default permissions for new files/dirs |

---

### 3. **Common Permission Scenarios**

| Use Case                | Command              | Resulting Permission |
| ----------------------- | -------------------- | -------------------- |
| Private file            | `chmod 600 filename` | rw-------            |
| Group-collab file       | `chmod 660 filename` | rw-rw----            |
| Public read-only file   | `chmod 644 filename` | rw-r--r--            |
| Shared team directory   | `chmod 770 folder/`  | rwxrwx---            |
| Personal/private folder | `chmod 700 folder/`  | rwx------            |

---

## 🛡️ Best Practices

* Always apply the **Principle of Least Privilege** (PoLP)
* Use **group ownership** for team-based projects
* Set proper `umask` values to enforce secure defaults
* Avoid `chmod 777` — it gives full access to everyone
* Regularly **audit file permissions** for sensitive content

---

## ✅ What You Can Now Do

* Interpret `ls -l` permission strings
* Modify permissions using `chmod` (symbolic or numeric)
* Assign user and group ownership using `chown` and `chgrp`
* Configure default permissions with `umask`
* Secure directories and files for various access models

---

## 🧠 Quick Review Table

| Tool    | Description                                   |
| ------- | --------------------------------------------- |
| `chmod` | Grants/revokes permissions (`+`, `-`, `=`)    |
| `chown` | Changes file owner (user\:group)              |
| `chgrp` | Changes group only                            |
| `umask` | Controls default permissions at creation time |

---

## 🔐 Why This Matters

> Misconfigured permissions are a **top cause of security breaches** in Linux environments.
> With proper access controls, you prevent:

* **Unauthorized viewing**
* **Accidental overwriting**
* **Privilege escalation**