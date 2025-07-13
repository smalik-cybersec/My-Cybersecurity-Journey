# 📝 **Lesson: Edit Text Files from the Shell Prompt**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 128*

---

## 📚 Table of Contents

- [📝 **Lesson: Edit Text Files from the Shell Prompt**](#-lesson-edit-text-files-from-the-shell-prompt)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [🧠 Why Shell-Based Editing Matters](#-why-shell-based-editing-matters)
  - [🛠️ Common Command-Line Text Editors](#️-common-command-line-text-editors)
  - [🧑‍💻 Editing with `nano`](#-editing-with-nano)
    - [📥 Launching nano](#-launching-nano)
    - [📚 Common nano Commands](#-common-nano-commands)
  - [⚡ Editing with `vim`](#-editing-with-vim)
    - [📥 Launching vim](#-launching-vim)
    - [🎮 Modes in vim](#-modes-in-vim)
    - [📚 Common vim Commands](#-common-vim-commands)
  - [📋 Other Useful Editors (Optional)](#-other-useful-editors-optional)
  - [🧪 Hands-On Practice](#-hands-on-practice)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 🎯 Introduction

On a headless Linux system (like a server), you often won’t have access to a GUI text editor like Notepad or gedit. Instead, you’ll use **terminal-based editors** to:

- View and edit configuration files
- Update logs or notes
- Write shell scripts
- Analyze system or network output

> In cybersecurity, forensics, DevOps, or sysadmin work, knowing terminal editors like `nano` or `vim` is non-negotiable.

---

## 🧠 Why Shell-Based Editing Matters

| Reason                  | Benefit                                                     |
| ----------------------- | ----------------------------------------------------------- |
| 🔒 Secure environments  | No GUI = no distractions or risks                           |
| 🧰 Default availability | Tools like `vim` and `nano` are pre-installed               |
| 🚀 Lightweight & fast   | Instant access to files with no loading time                |
| ⚙️ Script editing       | Needed for bash, Python, Ansible, etc.                      |
| 🛡️ Incident response   | Used during breaches to check/edit config/logs in real time |

---

## 🛠️ Common Command-Line Text Editors

| Editor | Use Case               | Ease of Use | Notes                                     |
| ------ | ---------------------- | ----------- | ----------------------------------------- |
| `nano` | Beginner-friendly      | ⭐⭐⭐⭐⭐       | Perfect for quick edits                   |
| `vim`  | Advanced editing       | ⭐⭐☆☆☆       | Extremely powerful but requires practice  |
| `vi`   | Older version of `vim` | ⭐⭐☆☆☆       | Always available, even on minimal systems |
| `ed`   | Very minimal           | ⭐☆☆☆☆       | Useful in limited rescue shells           |

---

## 🧑‍💻 Editing with `nano`

### 📥 Launching nano

```bash
nano filename.txt
```

### 📚 Common nano Commands

| Keys       | Action             |
| ---------- | ------------------ |
| `Ctrl + O` | Write/save changes |
| `Ctrl + X` | Exit nano          |
| `Ctrl + K` | Cut line           |
| `Ctrl + U` | Paste line         |
| `Ctrl + W` | Search in file     |

🧠 nano is ideal for quick config edits like `/etc/hostname`, crontabs, `.bashrc`, etc.

---

## ⚡ Editing with `vim`

### 📥 Launching vim

```bash
vim filename.txt
```

### 🎮 Modes in vim

| Mode         | Purpose                             |
| ------------ | ----------------------------------- |
| Normal Mode  | Default mode for navigation         |
| Insert Mode  | For typing text (`i`, `a`, etc.)    |
| Command Mode | For saving, quitting (`:wq`, `:q!`) |

### 📚 Common vim Commands

| Command | Description           |
| ------- | --------------------- |
| `i`     | Enter insert mode     |
| `Esc`   | Return to normal mode |
| `:w`    | Save the file         |
| `:q`    | Quit vim              |
| `:wq`   | Save and quit         |
| `:q!`   | Quit without saving   |
| `/text` | Search for "text"     |
| `dd`    | Delete current line   |
| `u`     | Undo last action      |

🧠 vim is essential when you're working on servers with no nano installed.

---

## 📋 Other Useful Editors (Optional)

| Editor  | Usage                                     |
| ------- | ----------------------------------------- |
| `micro` | Modern terminal editor with mouse support |
| `emacs` | Advanced programmable editor              |
| `sed`   | For stream-based editing (scripting)      |
| `ed`    | Used in constrained or rescue shells      |

---

## 🧪 Hands-On Practice

```bash
# Step 1: Create and edit a file with nano
nano testfile.txt
# Type: Hello from Shahid. Save and exit.

# Step 2: View it
cat testfile.txt

# Step 3: Edit with vim
vim testfile.txt
# Press 'i' to insert, make edits, then save with ':wq'

# Step 4: Try searching
vim /etc/passwd
# Type: /root → to find "root" entries
```

---

## 🧠 Quiz Yourself

1. What is the shortcut to save and exit in `nano`?
2. How do you switch to insert mode in `vim`?
3. What does `:q!` do in vim?
4. Which mode are you in when vim first opens?
5. What command opens a file called `info.txt` using nano?

---

## 📎 Summary

- Linux servers often rely on **text-mode editors** like `nano` and `vim` for all file operations.
- `nano` is **simple and beginner-friendly**, while `vim` is **powerful and fast** once learned.
- Mastering these tools is critical for tasks like:

  - Editing configs and crontabs
  - Writing bash or Python scripts
  - Fixing issues in `/etc` or `/var/log`
  - Working in recovery shells or SSH sessions