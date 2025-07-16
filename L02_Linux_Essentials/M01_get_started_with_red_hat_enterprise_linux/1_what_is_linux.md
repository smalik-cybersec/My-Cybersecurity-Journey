Perfect, Shahid. Here's the clean, GitHub/Obsidian/MkDocs-ready Markdown file for:

> **`lesson-01-what-is-linux.md`**
> Location: `linux-essentials/module-01-get-started-with-rhel/`

---

````markdown
---
title: Lesson 01 - What Is Linux?
module: Module 01 - Get Started with Red Hat Enterprise Linux
course: Linux Essentials (Level 3)
author: Shahid
version: Ultra Edition v4.0+
tags: [linux, kernel, rhel, open-source, introduction]
certs: [RHCSA, Linux+, CEH, OSCP]
job_roles: [SOC Analyst, Penetration Tester, Linux SysAdmin, DevSecOps]
created: 2025-07-16
---

# 🧠 Lesson 01: What Is Linux?

## 🧭 Introduction

Linux is more than an operating system — it’s the backbone of modern computing: powering servers, mobile devices (Android), IoT, cybersecurity labs, and even supercomputers.

Understanding what Linux is — and what makes it open, modular, and secure — is your first step in becoming a professional in cybersecurity, DevOps, or system administration.

---

## 🔑 Core Concepts

| Concept | Explanation |
|--------|-------------|
| **Linux** | A Unix-like, open-source operating system based on the Linux kernel, first released by Linus Torvalds in 1991. |
| **Kernel** | The core of the operating system that manages hardware (CPU, RAM, I/O) and system processes. |
| **Distributions (Distros)** | Packaged OS versions built on top of the Linux kernel (e.g., RHEL, Ubuntu, Kali). |
| **GNU** | A project that provides essential command-line tools and libraries often combined with the Linux kernel to form a full OS. |
| **RHEL** | Red Hat Enterprise Linux — a commercial, enterprise-grade Linux distribution supported by Red Hat, widely used in production servers and cloud systems. |

---

## 💻 Key Features of Linux

| Feature | Description |
|--------|-------------|
| Open Source | Anyone can view, modify, and redistribute the source code. |
| Multitasking | Multiple programs can run at the same time. |
| Multiuser | Many users can work on the same system without interfering with each other. |
| Security | Fine-grained permissions, SELinux, firewalls (iptables/nftables). |
| CLI-Oriented | Command-line interface is powerful, scriptable, and remote-friendly. |
| Package Management | `rpm`, `yum`, `dnf`, `apt` systems for installing software. |

---

## 🧪 Hands-on Lab: Is Your OS Linux?

**Objective:** Check if your current environment is Linux-based and view its properties.

```bash
# View the kernel name
uname

# View detailed kernel info
uname -a

# Check OS release version
cat /etc/os-release

# Check logged-in user
whoami

# Check system uptime
uptime
````

📍 **Expected Output Example:**

```bash
$ uname -a
Linux rhel9 5.14.0-284.el9.x86_64 #1 SMP Mon Oct 3 14:50:00 UTC 2022 x86_64 GNU/Linux

$ cat /etc/os-release
NAME="Red Hat Enterprise Linux"
VERSION="9.2 (Plow)"
```

---

## ⚔️ Red vs Blue Team Simulation

| Role         | Action                                                                                  |
| ------------ | --------------------------------------------------------------------------------------- |
| 🟥 Red Team  | Identify OS to plan exploits (e.g., using `uname -a` to detect kernel vulnerabilities). |
| 🟦 Blue Team | Harden OS by limiting information leakage (e.g., banner hiding, kernel patching).       |

---

## 🧩 Quiz

1. What is the relationship between Linux and GNU?
2. Name two Linux distributions other than RHEL.
3. What command do you use to check the Linux kernel version?
4. True/False: Linux is a monolithic kernel.
5. What makes Linux attractive for enterprise environments?

---

## 🧠 Memory Hooks (Flashcards)

| Question              | Answer                                 |
| --------------------- | -------------------------------------- |
| Linux = ?             | Kernel only                            |
| Full OS = ?           | Linux Kernel + GNU tools               |
| RHEL = ?              | Commercial Linux distro for enterprise |
| `uname -a` = ?        | Full kernel and system info            |
| `/etc/os-release` = ? | OS version file                        |

---

## 🧳 Job Role Mapping

| Role                     | Relevance of Linux                                                |
| ------------------------ | ----------------------------------------------------------------- |
| **SOC Analyst**          | Understand logs, use CLI tools like `journalctl`, `netstat`, etc. |
| **Penetration Tester**   | Navigate Kali or Parrot OS, identify Linux vulnerabilities.       |
| **System Administrator** | Manage servers, patch systems, configure services on RHEL/CentOS. |
| **DevSecOps Engineer**   | Automate CI/CD, Docker, K8s — all Linux-based platforms.          |

---

## 🧼 Summary

Linux is a versatile, powerful, and secure operating system that forms the foundation of cybersecurity and server administration. Starting with Red Hat Enterprise Linux gives you an industry-aligned, stable platform to build your skills.

---

## 🔁 Spaced Revision Plan

| Day    | Activity                                     |
| ------ | -------------------------------------------- |
| Day 1  | Read & run all commands manually             |
| Day 3  | Recall concepts using flashcards             |
| Day 7  | Repeat lab and simulate CLI-only interaction |
| Day 14 | Take quiz again without notes                |
| Day 21 | Reflect on Red/Blue Team relevance           |
| Day 30 | Integrate this into GitHub knowledge base    |

---

## ➕ Next Lesson

[Lesson 02 → Linux History and Flavors](lesson-02-linux-history-and-flavors.md)

```

---

### ✅ Next Step:

You can now:
- 📥 Copy this into `linux-essentials/module-01-get-started-with-rhel/lesson-01-what-is-linux.md`
- 🧠 Start practicing the commands in your terminal (RHEL, Fedora, CentOS, or any Linux VM)
- 🔁 Schedule revisions as per the table
- 🧱 Begin building your **Linux knowledge base** from the ground up

Shall we move forward to **Lesson 02: Linux History and Flavors**?
```
