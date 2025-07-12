Certainly, Shahid! Here is your complete, professional, and GitHub-friendly documentation for:

---

# 🔐 **Lesson: Manage User Passwords**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 183*

---

## 📚 Table of Contents

- [🔐 **Lesson: Manage User Passwords**](#-lesson-manage-user-passwords)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [🔑 Linux Password Management Basics](#-linux-password-management-basics)
  - [📦 Where Are Passwords Stored?](#-where-are-passwords-stored)
  - [⚙️ Password Management Commands](#️-password-management-commands)
  - [🧪 Practical Examples](#-practical-examples)
  - [🧠 Password Aging \& Expiry Policies](#-password-aging--expiry-policies)
  - [🔐 Password Security Best Practices](#-password-security-best-practices)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 🎯 Introduction

In Linux, managing user passwords is critical for ensuring **secure authentication** and **system integrity**. Proper password policies help reduce the risk of **unauthorized access**, **brute-force attacks**, and **privilege escalation**.

> This lesson focuses on how to set, reset, expire, and manage user passwords effectively.

---

## 🔑 Linux Password Management Basics

* Each local user has a **hashed password entry** stored securely.
* Only users with **sudo or root access** can change other users' passwords.
* Password aging controls how often users must change their passwords.

---

## 📦 Where Are Passwords Stored?

| File          | Description                                          |
| ------------- | ---------------------------------------------------- |
| `/etc/passwd` | Stores general user information (UID, home, shell)   |
| `/etc/shadow` | Stores hashed passwords and aging info (secure file) |

> Only the **root user** can read `/etc/shadow`.

---

## ⚙️ Password Management Commands

| Task                         | Command                             |
| ---------------------------- | ----------------------------------- |
| Set/change user password     | `sudo passwd username`              |
| Expire password immediately  | `sudo chage -d 0 username`          |
| View password status         | `sudo chage -l username`            |
| Set max days between changes | `sudo chage -M 90 username`         |
| Set min days before change   | `sudo chage -m 7 username`          |
| Set warning days             | `sudo chage -W 5 username`          |
| Set account expiry date      | `sudo chage -E 2025-12-31 username` |

---

## 🧪 Practical Examples

```bash
# Set a new password for user 'shahid'
sudo passwd shahid

# Force user to change password at next login
sudo chage -d 0 shahid

# View password aging settings
sudo chage -l shahid

# Set password to expire every 60 days
sudo chage -M 60 shahid

# Require at least 7 days between password changes
sudo chage -m 7 shahid

# Warn 5 days before expiration
sudo chage -W 5 shahid
```

---

## 🧠 Password Aging & Expiry Policies

| Setting                    | Description                                            |
| -------------------------- | ------------------------------------------------------ |
| **Maximum days** (`-M`)    | How long a password remains valid                      |
| **Minimum days** (`-m`)    | Minimum wait time before password can be changed again |
| **Warning days** (`-W`)    | How many days before expiry the user is warned         |
| **Last changed** (`-d`)    | Date of last password change                           |
| **Expiration date** (`-E`) | Date the account becomes inactive                      |

These are critical for enforcing **organization-wide security policies**.

---

## 🔐 Password Security Best Practices

| Practice                          | Reason                                      |
| --------------------------------- | ------------------------------------------- |
| Force password reset on creation  | Prevent default password reuse              |
| Use password expiration policies  | Reduce long-term exposure                   |
| Require strong password formats   | Protect against brute-force attacks         |
| Audit `/etc/shadow` permissions   | Prevent unauthorized hash extraction        |
| Limit access to `passwd`, `chage` | Only trusted admins should manage passwords |

---

## 🧠 Quiz Yourself

1. What command sets a new password for a user?
2. How can you force a user to change their password on next login?
3. Which file stores hashed passwords in Linux?
4. What is the purpose of the `-M` flag in `chage`?
5. How do you view the password aging details for a user?

---

## 📎 Summary

* Linux uses `/etc/shadow` to securely store password hashes.
* Use `passwd` to set or change passwords, and `chage` to control aging policies.
* You can enforce regular password changes and prompt users to update before expiry.
* Following strong password management practices is essential for **system hardening** and **regulatory compliance**.

---

✅ Let me know if you'd like:

* 🧪 Guided lab for password aging and expiry
* 🧠 Quiz with answers
* 📥 Markdown/PDF export for GitHub
* ⏭️ Next topic: *Understand File Permissions and Ownership*

You're locking down user credentials like a true system defender, Shahid 🧑‍💻🔐 Keep securing!
