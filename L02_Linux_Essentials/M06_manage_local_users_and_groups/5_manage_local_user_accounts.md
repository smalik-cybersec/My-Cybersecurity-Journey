Here is your complete, professional, and GitHub-friendly documentation for:

---

# 👤 **Lesson: Manage Local User Accounts**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 171*

---

## 📚 Table of Contents

- [👤 **Lesson: Manage Local User Accounts**](#-lesson-manage-local-user-accounts)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [🔑 What Are Local User Accounts?](#-what-are-local-user-accounts)
  - [📦 Files That Store User Information](#-files-that-store-user-information)
  - [⚙️ Basic User Management Commands](#️-basic-user-management-commands)
  - [🔐 Password Management](#-password-management)
  - [🚫 Locking \& Expiring Accounts](#-locking--expiring-accounts)
  - [🧪 Practical Examples](#-practical-examples)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 🎯 Introduction

In Linux, **local user accounts** are used to authenticate people who access the system. Proper user management is crucial for **security**, **compliance**, and **resource control**—especially in multi-user or production environments.

---

## 🔑 What Are Local User Accounts?

A local user account consists of:

* A **username** (e.g., `shahid`)
* A unique **UID**
* A **home directory** (e.g., `/home/shahid`)
* A **login shell** (e.g., `/bin/bash`)
* A **password** (stored in hashed form)
* A **primary group**
* Optional **supplementary groups**

> Local users are created and managed **on that system only**, unlike LDAP or domain users.

---

## 📦 Files That Store User Information

| File           | Purpose                             |
| -------------- | ----------------------------------- |
| `/etc/passwd`  | Basic user info: username, UID, GID |
| `/etc/shadow`  | Password hashes, expiry data        |
| `/etc/group`   | Group definitions                   |
| `/etc/gshadow` | Secure group passwords (if used)    |

View users:

```bash
cat /etc/passwd
```

---

## ⚙️ Basic User Management Commands

| Task             | Command Example                              |
| ---------------- | -------------------------------------------- |
| Create user      | `sudo useradd -m username`                   |
| Add with comment | `sudo useradd -c "Full Name" username`       |
| Add with shell   | `sudo useradd -s /bin/bash username`         |
| Delete user      | `sudo userdel username`                      |
| Delete + home    | `sudo userdel -r username`                   |
| Modify username  | `sudo usermod -l newname oldname`            |
| Change shell     | `sudo usermod -s /bin/zsh username`          |
| Create home dir  | `sudo mkdir /home/username && sudo chown`... |

📝 New users get a default configuration from `/etc/skel`.

---

## 🔐 Password Management

| Task                   | Command                    |
| ---------------------- | -------------------------- |
| Set or change password | `sudo passwd username`     |
| Force password change  | `sudo chage -d 0 username` |
| View password status   | `sudo chage -l username`   |

---

## 🚫 Locking & Expiring Accounts

| Task                | Command                               |
| ------------------- | ------------------------------------- |
| Lock user account   | `sudo usermod -L username`            |
| Unlock user account | `sudo usermod -U username`            |
| Expire account now  | `sudo usermod -e 1970-01-01 username` |
| Set expiry date     | `sudo chage -E 2025-12-31 username`   |

> Locked accounts **cannot be logged into**, but files still remain intact.

---

## 🧪 Practical Examples

```bash
# Create a new user and set a password
sudo useradd -m analyst
sudo passwd analyst

# Lock the account temporarily
sudo usermod -L analyst

# Force analyst to change password on next login
sudo chage -d 0 analyst

# Delete user with their home directory
sudo userdel -r analyst
```

---

## 🧠 Quiz Yourself

1. What command would you use to create a new user named `cyberops`?
2. How do you force a user to change their password on next login?
3. What does the `-r` option do with `userdel`?
4. Where is the password hash stored?
5. What’s the difference between locking and deleting a user?

---

## 📎 Summary

* Linux stores all local user data in files like `/etc/passwd` and `/etc/shadow`.
* You can manage users with tools like `useradd`, `usermod`, `userdel`, and `passwd`.
* It’s critical to control **who can log in**, **how long**, and **under what permissions**.
* Use account locking and password expiry to enhance security.

---

✅ Let me know if you’d like:

* 🧪 Guided Lab: Create, lock, expire, and delete users
* 🧠 Quiz with answers
* 📥 Markdown export for GitHub
* ⏭️ Next topic: *Manage Local Group Accounts*

You're mastering access control, Shahid — a vital skill for secure Linux administration and cyber ops 🔐🧑‍💻
