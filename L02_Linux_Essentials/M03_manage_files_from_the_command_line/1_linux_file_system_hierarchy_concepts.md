Absolutely, Shahid! Here's your **structured, professional documentation** for:

---

# 🗂️ **Linux File System Hierarchy Concepts**

> *Module: Red Hat System Administration / Linux Essentials*
> *Craw Cyber Security One-Year Diploma – Page 48*

---

## 📚 Table of Contents

- [🗂️ **Linux File System Hierarchy Concepts**](#️-linux-file-system-hierarchy-concepts)
  - [📚 Table of Contents](#-table-of-contents)
  - [📖 Introduction to Linux File System](#-introduction-to-linux-file-system)
  - [🗺️ Understanding the FHS (Filesystem Hierarchy Standard)](#️-understanding-the-fhs-filesystem-hierarchy-standard)
  - [📂 Key Directories and Their Purpose](#-key-directories-and-their-purpose)
  - [📑 Special Files and Concepts](#-special-files-and-concepts)
  - [📌 Absolute vs Relative Paths](#-absolute-vs-relative-paths)
  - [🧪 Guided Lab Activity](#-guided-lab-activity)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 📖 Introduction to Linux File System

The **Linux file system** is organized as a **single-rooted inverted tree**, where the top is the **root directory (`/`)**. All files, directories, devices, and user spaces stem from this root — unlike Windows which uses drive letters like `C:\`.

> Everything in Linux is treated as a **file** — even hardware devices.

---

## 🗺️ Understanding the FHS (Filesystem Hierarchy Standard)

The **Filesystem Hierarchy Standard (FHS)** defines a consistent structure for Linux distributions, making systems easier to manage, automate, and secure.

| Term            | Description                                                                           |
| --------------- | ------------------------------------------------------------------------------------- |
| **FHS**         | Filesystem Hierarchy Standard – defines what each directory means and where things go |
| **Root (`/`)**  | The top-most directory; everything starts from here                                   |
| **Mount Point** | A directory where another file system is attached (e.g., USB, HDD partition)          |

---

## 📂 Key Directories and Their Purpose

| Directory | Description                                                   |
| --------- | ------------------------------------------------------------- |
| `/`       | Root of the file system                                       |
| `/bin`    | Essential binaries (e.g., `ls`, `cp`, `rm`) used by all users |
| `/sbin`   | System binaries (e.g., `fsck`, `reboot`) for admin use        |
| `/etc`    | Configuration files for system and services                   |
| `/home`   | User home directories (`/home/shahid`)                        |
| `/root`   | Home directory for root user                                  |
| `/tmp`    | Temporary files (cleared on reboot)                           |
| `/var`    | Variable data like logs (`/var/log/`), mail, cache            |
| `/usr`    | User applications and files (binaries, libraries)             |
| `/lib`    | Essential shared libraries used by `/bin` and `/sbin`         |
| `/media`  | Mount point for removable media like USBs                     |
| `/mnt`    | Temporary mount point for manual mounts                       |
| `/opt`    | Optional software installed by the user or 3rd party          |
| `/dev`    | Device files (e.g., `/dev/sda`, `/dev/tty`)                   |
| `/proc`   | Virtual file system with runtime kernel info                  |
| `/sys`    | Exposes kernel, process, device info                          |
| `/boot`   | Boot loader files and kernel images                           |
| `/run`    | Temporary runtime data for system processes                   |

---

## 📑 Special Files and Concepts

| Concept                 | Description                                                                |
| ----------------------- | -------------------------------------------------------------------------- |
| **Hidden Files**        | Files starting with `.` (e.g., `.bashrc`) are hidden                       |
| **Symbolic Links**      | Shortcuts (like Windows shortcuts) → created with `ln -s`                  |
| **Hard Links**          | Actual references to file data blocks                                      |
| **Device Files**        | Files in `/dev` used to interact with hardware                             |
| **Mount Points**        | Attach another file system (e.g., USB) to a directory                      |
| **Pseudo File Systems** | `/proc` and `/sys` contain kernel and system information, not actual files |

---

## 📌 Absolute vs Relative Paths

| Path Type    | Example                 | Meaning                         |
| ------------ | ----------------------- | ------------------------------- |
| **Absolute** | `/home/shahid/doc.txt`  | Full path from root (`/`)       |
| **Relative** | `../Downloads/file.txt` | Path based on current directory |

> Use `pwd` to see your current working directory.

---

## 🧪 Guided Lab Activity

Try these in your terminal:

```bash
# List the contents of root
ls /

# Explore key directories
ls /bin /etc /home /var

# Print your current directory
pwd

# Create a directory in your home
mkdir ~/CyberPractice

# Create a symbolic link
ln -s /etc/passwd ~/CyberPractice/passwd_link

# Check filesystem usage
df -h

# View device list
ls /dev

# Explore pseudo-filesystem
ls /proc
cat /proc/cpuinfo
```

---

## 🧠 Quiz Yourself

1. What does the `/etc` directory contain?
2. What is the purpose of `/var/log/`?
3. What's the difference between `/bin` and `/sbin`?
4. Which directory holds temporary files that are deleted on reboot?
5. What command lists the current working directory?

---

## 📎 Summary

* The Linux file system is **hierarchical**, **rooted at `/`**, and follows the **FHS standard**
* Directories like `/bin`, `/etc`, `/home`, `/var`, and `/usr` each serve a specific purpose
* Concepts like **mount points**, **device files**, and **pseudo-filesystems** make Linux extremely powerful and flexible
* Understanding the file system is **critical for cybersecurity tasks**, including log analysis, system forensics, and privilege escalation detection

---

✅ Let me know if you'd like:

* 📥 Markdown or GitHub README export
* 🧪 Deep-dive lab with file permission practice
* 🧠 Answer key for quiz
* ⏭️ Move to the next lesson: *Work with Files in Linux*

Always ready, Shahid — your Linux mastery is growing fast! 💪🐧
