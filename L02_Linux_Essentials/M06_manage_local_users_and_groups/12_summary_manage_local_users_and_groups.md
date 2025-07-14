# 📎 **Summary: Manage Local Users and Groups**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 191*

---

## 📖 Overview

In Linux, **local users and groups** are essential components of the system’s **identity and access control model**. Every file, process, and command execution is tied to a user and a group. This module focused on how to **create**, **modify**, **lock**, **expire**, and **delete** user and group accounts securely from the command line.

---

## 👤 Local User Management

| Task                  | Command Example                           |
| --------------------- | ----------------------------------------- |
| Create user with home | `sudo useradd -m analyst`                 |
| Set password          | `sudo passwd analyst`                     |
| Force password reset  | `sudo chage -d 0 analyst`                 |
| Lock/unlock user      | `sudo usermod -L analyst` / `-U`          |
| Delete user           | `sudo userdel -r analyst`                 |
| Modify shell/comment  | `sudo usermod -s /bin/zsh -c "Role" user` |

---

## 👥 Local Group Management

| Task                   | Command Example                     |
| ---------------------- | ----------------------------------- |
| Create group           | `sudo groupadd devteam`             |
| Add user to group      | `sudo usermod -aG devteam analyst`  |
| Remove user from group | `sudo gpasswd -d analyst devteam`   |
| Rename group           | `sudo groupmod -n cyberops devteam` |
| Delete group           | `sudo groupdel devteam`             |

---

## 🔐 Password and Account Policies

| Policy Type           | Command Example                    |
| --------------------- | ---------------------------------- |
| Set max days (expire) | `sudo chage -M 60 analyst`         |
| Set min days          | `sudo chage -m 7 analyst`          |
| Set warning period    | `sudo chage -W 5 analyst`          |
| Set expiry date       | `sudo chage -E 2025-12-31 analyst` |
| View status           | `sudo chage -l analyst`            |

---

## 🛡️ Why This Matters in Cybersecurity

| Purpose                     | Why It’s Important                       |
| --------------------------- | ---------------------------------------- |
| Identity Management         | Ensures authorized user access           |
| Least Privilege Enforcement | Group roles reduce over-privileged users |
| Shared Access               | Group-based permissions improve control  |
| Auditability & Compliance   | Track and manage account lifecycle       |
| System Hardening            | Lock inactive accounts, expire passwords |

---

## ✅ What You Should Be Able to Do Now

* ✅ Create and delete users and groups
* ✅ Manage user group memberships
* ✅ Configure password expiration policies
* ✅ Lock, unlock, and expire user accounts
* ✅ Set up shared folders with group access control

---

## 📂 Key Files and Their Purpose

| File           | Purpose                                  |
| -------------- | ---------------------------------------- |
| `/etc/passwd`  | Stores basic user account information    |
| `/etc/shadow`  | Stores encrypted user passwords          |
| `/etc/group`   | Lists group names and memberships        |
| `/etc/gshadow` | Stores secure group password information |

---

## 🧠 Final Thought

> **"A secure Linux system starts with secure identity and access management."**
> Local users and groups form the **foundation** of all permissions and privilege controls. This lesson gave you the tools to structure users and groups in a way that is **secure**, **scalable**, and **compliant**.