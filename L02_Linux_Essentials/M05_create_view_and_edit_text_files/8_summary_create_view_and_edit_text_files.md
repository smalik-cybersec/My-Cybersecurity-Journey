# 📎 **Summary: Create, View, and Edit Text Files**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 144*

---

## 📖 Overview

In this lesson, you learned how to **create**, **view**, and **edit** text files directly from the Linux terminal — a fundamental skill for any Linux administrator, cybersecurity analyst, or DevOps engineer.

> Text files are used everywhere in Linux: configuration files, log files, scripts, and documentation. Mastering how to handle them efficiently is critical.

---

## 🛠️ Key Concepts and Tools

### 🗂️ File Creation

| Command                  | Purpose                           |
| ------------------------ | --------------------------------- |
| `touch file.txt`         | Create an empty text file         |
| `echo "text" > file.txt` | Create and write to file          |
| `cat > file.txt`         | Input multi-line content directly |

---

### 📄 File Viewing

| Command        | Purpose                       |
| -------------- | ----------------------------- |
| `cat`          | Print entire file to terminal |
| `more`, `less` | Scroll through large files    |
| `head`         | View the first few lines      |
| `tail`         | View the last few lines       |

---

### 📝 File Editing

| Editor | Description                    |
| ------ | ------------------------------ |
| `nano` | Beginner-friendly, easy to use |
| `vim`  | Advanced, fast, modal editor   |

#### 🔑 Key nano shortcuts

| Keys       | Action      |
| ---------- | ----------- |
| `Ctrl + O` | Save file   |
| `Ctrl + X` | Exit editor |
| `Ctrl + K` | Cut line    |
| `Ctrl + U` | Paste line  |

#### 🔑 Key vim commands

| Keys/Command | Action              |
| ------------ | ------------------- |
| `i`          | Insert mode         |
| `Esc`        | Exit to normal mode |
| `:w`         | Save                |
| `:q`         | Quit                |
| `:wq`        | Save and quit       |
| `:q!`        | Quit without saving |

---

## 🧪 Practical Examples

```bash
touch config.txt
echo "ServerName localhost" > config.txt
cat config.txt
nano config.txt      # Add or modify contents
vim config.txt       # Advanced editing
head config.txt
tail config.txt
```

---

## 🧠 Why This Matters in Cybersecurity & Administration

| Task              | Real-World Application                         |
| ----------------- | ---------------------------------------------- |
| Edit config files | Modify `/etc/ssh/sshd_config`, `/etc/fstab`    |
| Write scripts     | Automate tasks with `bash`, `python`, etc.     |
| Inspect log files | Analyze `/var/log/auth.log`, `/var/log/syslog` |
| Document findings | Store notes or findings in `.txt` format       |

---

## ✅ What You Should Be Able to Do Now

* ✅ Create new text files from the command line
* ✅ View file contents using `cat`, `less`, `head`, and `tail`
* ✅ Edit text files using `nano` and `vim`
* ✅ Use redirection operators (`>`, `>>`, `cat >>`) to write and append content
* ✅ Understand when and why to use terminal-based editing
