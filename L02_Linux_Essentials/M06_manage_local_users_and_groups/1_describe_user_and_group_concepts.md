# 👥 **Lesson: Describe User and Group Concepts**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 154*

---

## 📚 Table of Contents

- [👥 **Lesson: Describe User and Group Concepts**](#-lesson-describe-user-and-group-concepts)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [🧑‍💻 What Are Users in Linux?](#-what-are-users-in-linux)
  - [👥 What Are Groups?](#-what-are-groups)
  - [🗂️ User Types](#️-user-types)
  - [🗃️ Essential User and Group Files](#️-essential-user-and-group-files)
  - [🔧 Managing Users and Groups (Basic)](#-managing-users-and-groups-basic)
    - [📋 Check Current User and Groups](#-check-current-user-and-groups)
    - [➕ Create a New User](#-create-a-new-user)
    - [➕ Create a New Group](#-create-a-new-group)
    - [➕ Add User to Group](#-add-user-to-group)
    - [❌ Delete User or Group](#-delete-user-or-group)
  - [🔐 Real-World Usage \& Cybersecurity Implications](#-real-world-usage--cybersecurity-implications)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 🎯 Introduction

In Linux, **users and groups** are the foundation of the system's **permissions**, **ownership**, and **access control**. Every file, process, or service runs under a user ID (UID), and often belongs to one or more groups.

> Understanding users and groups is critical for system security, resource management, and compliance.

---

## 🧑‍💻 What Are Users in Linux?

A **user** in Linux is any account that can log into or interact with the system.

Each user is identified by:

- **Username** (e.g., `shahid`)
- **UID** (User ID – a number)
- **Primary Group** (GID)
- **Home directory**
- **Default shell**

---

## 👥 What Are Groups?

A **group** is a collection of users. Groups make it easier to manage **permissions** on files and resources by assigning access to a group rather than individual users.

- A user can belong to:

  - **One primary group**
  - **Zero or more secondary (supplementary) groups**

---

## 🗂️ User Types

| User Type         | UID Range                         | Description                               |
| ----------------- | --------------------------------- | ----------------------------------------- |
| **Root user**     | 0                                 | Superuser with unrestricted system access |
| **System users**  | 1–999 (or 1–9999 on some systems) | Created by system/software, not for login |
| **Regular users** | 1000+                             | Human users created for login and work    |

---

## 🗃️ Essential User and Group Files

| File           | Purpose                                   |
| -------------- | ----------------------------------------- |
| `/etc/passwd`  | Stores basic user info (UID, home, shell) |
| `/etc/shadow`  | Stores hashed passwords (secured)         |
| `/etc/group`   | Lists groups and group memberships        |
| `/etc/gshadow` | Secure group password storage             |

You can inspect these files using `cat`, `less`, or `grep`.

---

## 🔧 Managing Users and Groups (Basic)

> These commands require root (or sudo) privileges.

### 📋 Check Current User and Groups

```bash
whoami
id
groups
```

### ➕ Create a New User

```bash
sudo useradd -m shahid
sudo passwd shahid
```

### ➕ Create a New Group

```bash
sudo groupadd redteam
```

### ➕ Add User to Group

```bash
sudo usermod -aG redteam shahid
```

### ❌ Delete User or Group

```bash
sudo userdel -r shahid
sudo groupdel redteam
```

---

## 🔐 Real-World Usage & Cybersecurity Implications

| Scenario                        | Why It's Important                      |
| ------------------------------- | --------------------------------------- |
| 🧑‍🏫 Role-based access control | Use groups like `developers`, `admins`  |
| 🔒 File system security         | File access is tied to user & group IDs |
| 🔍 Forensics & auditing         | Logs tie actions to UIDs                |
| 🛡️ Least privilege principle   | Avoid giving users root unnecessarily   |
| 🧪 Pentesting setups            | Create isolated test users/groups       |

---

## 🧠 Quiz Yourself

1. What is the UID of the root user?
2. What command shows the current user's group memberships?
3. What is the difference between primary and supplementary groups?
4. How do you assign a user to a new group without removing them from others?
5. Which file contains the list of all groups on the system?

---

## 📎 Summary

- Linux users and groups form the **foundation of access control**.
- Users are defined in `/etc/passwd`; groups in `/etc/group`.
- Each file and process is owned by a **user** and a **group**.
- You can manage users/groups with tools like `useradd`, `groupadd`, `usermod`, etc.
- Security in Linux heavily depends on proper user/group configurations.