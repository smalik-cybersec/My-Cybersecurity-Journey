# 💻 Lesson 02: **Access the Command Line**

> *Module: Red Hat System Administration / Linux Essentials*
> *Craw Cyber Security – One-Year Cyber Security Diploma Course*
> *Page Reference: Page 14*

---

## 📚 Table of Contents

- [💻 Lesson 02: **Access the Command Line**](#-lesson-02-access-the-command-line)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 What Is the Command Line?](#-what-is-the-command-line)
  - [🧠 Why Learn the Command Line in Cybersecurity?](#-why-learn-the-command-line-in-cybersecurity)
  - [📦 Types of Command Line Interfaces (CLI)](#-types-of-command-line-interfaces-cli)
  - [🎛️ CLI vs GUI](#️-cli-vs-gui)
  - [🔑 Common CLI Environments in Linux](#-common-cli-environments-in-linux)
  - [🧰 Basic Commands You Must Know](#-basic-commands-you-must-know)
  - [🧪 Lab Practice](#-lab-practice)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 🎯 What Is the Command Line?

The **Command Line Interface (CLI)** is a text-based interface used to interact with the operating system. It allows users to issue commands to perform tasks such as:

- Navigating the file system
- Managing users and permissions
- Starting/stopping services
- Viewing logs, monitoring systems, and much more

> Unlike GUI (Graphical User Interface), the CLI is **lightweight, faster**, and gives **more control**.

---

## 🧠 Why Learn the Command Line in Cybersecurity?

| Reason                              | Explanation                                                                                  |
| ----------------------------------- | -------------------------------------------------------------------------------------------- |
| 🔍 **Deep System Access**           | Penetration testers, forensic analysts, and sysadmins often need access below the GUI layer. |
| 🧪 **Security Tools Depend on CLI** | Nmap, Nikto, Metasploit, Netcat, etc., are CLI-based.                                        |
| 📁 **Scriptability & Automation**   | Shell scripts automate tasks like log parsing, firewall configs, malware scans.              |
| 🌐 **Remote Access via SSH**        | Most servers (especially in the cloud) are accessed via CLI over SSH.                        |
| 🔐 **GUI might be disabled**        | In hardened systems or incidents, only CLI may be available.                                 |

---

## 📦 Types of Command Line Interfaces (CLI)

| CLI Tool              | Description                                                           |
| --------------------- | --------------------------------------------------------------------- |
| **Bash**              | Bourne Again Shell, default shell in most Linux distros               |
| **Sh**                | Original Bourne Shell                                                 |
| **Zsh**               | Extended Bash with more features                                      |
| **Fish**              | Friendly Interactive Shell                                            |
| **TTY**               | Terminal interface (text-mode interface on physical console)          |
| **Terminal Emulator** | GUI program to interact with CLI (like GNOME Terminal, Konsole, etc.) |

---

## 🎛️ CLI vs GUI

| Feature        | CLI                     | GUI             |
| -------------- | ----------------------- | --------------- |
| Speed          | Faster                  | Slower          |
| Resource Usage | Low (RAM/CPU efficient) | High            |
| Learning Curve | Steep                   | Easy            |
| Control        | Complete system control | Limited control |
| Automation     | Easy (shell scripting)  | Difficult       |

---

## 🔑 Common CLI Environments in Linux

| Environment                        | How to Access             | Description                           |
| ---------------------------------- | ------------------------- | ------------------------------------- |
| **Virtual Console (TTY)**          | `Ctrl + Alt + F1` to `F6` | Native text-mode interface            |
| **Terminal Emulator**              | Applications → Terminal   | Bash access inside GUI                |
| **SSH Remote Terminal**            | `ssh user@IP`             | Access CLI of remote server           |
| **Rescue Mode / Single User Mode** | Boot-time GRUB option     | CLI for system repair or forensic use |

---

## 🧰 Basic Commands You Must Know

| Command | Purpose                           |
| ------- | --------------------------------- |
| `pwd`   | Print current directory           |
| `ls`    | List files in a directory         |
| `cd`    | Change directory                  |
| `mkdir` | Make new directory                |
| `touch` | Create an empty file              |
| `echo`  | Display text or variable          |
| `cat`   | View file content                 |
| `man`   | Open manual pages for any command |
| `clear` | Clear the screen                  |
| `exit`  | Exit the terminal session         |

```bash
# Example: Navigate and create a file
cd /home/shahid
mkdir practice
cd practice
touch file.txt
```

---

## 🧪 Lab Practice

Try these exercises in a Linux terminal or VM:

1. 🔎 Open a terminal. Use `pwd`, `ls`, and `cd` to explore your system.
2. 📁 Create a new folder called `redhat_lab` in your home directory.
3. 📝 Inside it, create a file called `linux_notes.txt` using `touch`.
4. ✏️ Use `echo` to write your name into the file.
5. 📜 Display the content using `cat`.
6. 🔄 Use `man ls` to read the manual for the `ls` command.

---

## 🧠 Quiz Yourself

1. What is the full form of **CLI**?
2. Which Linux command prints the current working directory?
3. What command is used to create a new file?
4. How can you open the manual for any Linux command?
5. Name two advantages of using the command line over a GUI.

---

## 📎 Summary

- The **command line** is essential for professional Linux system use.
- Tools like `bash`, `tty`, and `ssh` give full access to system internals.
- Mastering commands like `cd`, `ls`, `touch`, and `man` forms the foundation of Linux proficiency.
- CLI is **indispensable** for cybersecurity, DevOps, administration, and scripting.
