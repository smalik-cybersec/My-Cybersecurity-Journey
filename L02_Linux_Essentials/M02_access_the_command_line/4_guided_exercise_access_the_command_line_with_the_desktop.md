# 🎯 **Guided Exercise: Access the Command Line with the Desktop**

> *Lesson 03 Lab Practice – Linux Essentials (Red Hat System Administration)*
> *Craw Cyber Security Diploma – Page 28*

---

## 📋 Objective

> To gain confidence in **accessing**, **navigating**, and **using the Linux Command Line Interface (CLI)** via a **desktop environment** using Terminal Emulators.

This guided exercise helps you become **comfortable** with terminal navigation, launching commands, and verifying CLI usage in a GUI-based Linux system.

---

## 🧑‍💻 Prerequisites

✅ A system running Red Hat Enterprise Linux (RHEL), Fedora, CentOS, Ubuntu, or Kali
✅ GUI (Graphical Desktop Environment) installed
✅ User account with **sudo** privileges
✅ Terminal Emulator pre-installed (e.g., GNOME Terminal, Konsole, Xfce Terminal)

---

## 🧭 Step-by-Step Instructions

---

### 🔹 **Step 1: Log into the System with GUI**

* Start your Linux VM or local system.
* Ensure that you're using a **Graphical User Interface** like GNOME, KDE, or Xfce.
* Log in using your username and password.

---

### 🔹 **Step 2: Open the Terminal Emulator**

> Try each of these different access methods to develop muscle memory.

✅ **Option 1: Applications Menu**

```text
Menu → System Tools → Terminal
```

✅ **Option 2: Keyboard Shortcut**

```text
Ctrl + Alt + T
```

✅ **Option 3: Right-click Method**

* Right-click inside your desktop or folder
* Choose “Open Terminal Here”

✅ **Option 4: Run Command**

* Press `Alt + F2`
* Type: `gnome-terminal` or `konsole`

---

### 🔹 **Step 3: Identify the Shell and Environment**

Type the following commands to confirm:

```bash
whoami            # Shows current user
echo $SHELL       # Shows current shell, usually /bin/bash
echo $HOME        # Shows home directory
```

✔️ Make sure you're in your home directory (usually `/home/your-username`)

---

### 🔹 **Step 4: Practice Navigation and Basic Commands**

Type each command and observe the output:

```bash
pwd               # Show current path
ls -la            # List all files including hidden ones
cd Documents      # Navigate into Documents folder
mkdir CLI_Practice
cd CLI_Practice
touch linux.txt
echo "Hello, CLI!" > linux.txt
cat linux.txt
```

🔍 **Check understanding**:

* What did each command do?
* What does the `>` symbol mean in `echo`?

---

### 🔹 **Step 5: Use the Manual System**

Now learn how to read the **manual pages**:

```bash
man ls
```

* Use `arrow keys` to scroll
* Press `q` to quit

---

### 🔹 **Step 6: Open Multiple Terminal Tabs**

Try opening two tabs and use one to monitor, one to work:

* In GNOME Terminal: **Right-click → Open Tab**
* Run `top` in one tab
* Run other commands in the second tab

---

### 🔹 **Step 7: Optional Styling & Profiles**

Customize your terminal:

* Change font size or color scheme
* Set profile name to “Cyber CLI”
* Enable scrollbar if hidden

---

## ✅ Expected Results

| Action                      | Expected Output/Behavior                    |
| --------------------------- | ------------------------------------------- |
| Terminal opens successfully | CLI prompt appears (e.g., `shahid@host:~$`) |
| `pwd`                       | Shows path (e.g., `/home/shahid`)           |
| `echo $SHELL`               | Shows `/bin/bash` or `/bin/zsh`             |
| Create file & view content  | `cat` shows: `Hello, CLI!`                  |
| `man` opens help pages      | Full manual view with navigation            |
| `top` in another tab        | Real-time system monitor interface appears  |

---

## 📂 File Tree After Exercise

```text
/home/shahid
├── Documents
│   └── CLI_Practice
│       └── linux.txt
```

---

## 🧠 Reflection Questions

1. What’s the difference between using a terminal in TTY vs GUI?
2. Why does CLI remain important even in modern Linux desktops?
3. Can you perform everything via GUI that you just did in CLI?

---

## 🧪 Challenge Task (Optional)

1. Create a directory called `CyberProjects` in your Desktop
2. Create 3 text files inside it: `report.txt`, `notes.txt`, `checklist.txt`
3. Write different content in each file using `echo`
4. Display them using `cat`
5. List the directory in long format with hidden files: `ls -la`