# 🗃️ **Lesson: Manage Files with Command-line Tools**

> *Module: Red Hat System Administration / Linux Essentials*
> *Craw Cyber Security One-Year Diploma – Page 63*

---

## 📚 Table of Contents

- [🗃️ **Lesson: Manage Files with Command-line Tools**](#️-lesson-manage-files-with-command-line-tools)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [📂 Common File Management Commands](#-common-file-management-commands)
  - [📁 Directory Operations](#-directory-operations)
  - [📦 Copying, Moving, and Deleting Files](#-copying-moving-and-deleting-files)
    - [🟩 **Copying Files**](#-copying-files)
    - [🟨 **Moving Files (or Renaming)**](#-moving-files-or-renaming)
    - [🟥 **Deleting Files**](#-deleting-files)
  - [🔐 File Safety \& Overwriting](#-file-safety--overwriting)
  - [🧪 Hands-On Lab](#-hands-on-lab)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 🎯 Introduction

One of the most fundamental tasks in Linux administration is **managing files and directories** via the command line. Whether you're installing software, auditing logs, or preparing scripts, you'll rely on file manipulation commands daily.

> Knowing how to efficiently create, move, copy, and delete files is essential for both system admins and cybersecurity professionals.

---

## 📂 Common File Management Commands

| Command | Description                 | Example                       |
| ------- | --------------------------- | ----------------------------- |
| `touch` | Creates an empty file       | `touch file.txt`              |
| `cat`   | Displays file contents      | `cat notes.txt`               |
| `cp`    | Copies files or directories | `cp file.txt /tmp/`           |
| `mv`    | Moves or renames files      | `mv old.txt new.txt`          |
| `rm`    | Deletes files               | `rm unwanted.txt`             |
| `mkdir` | Creates a new directory     | `mkdir /home/shahid/logs`     |
| `rmdir` | Removes an empty directory  | `rmdir /home/shahid/old_logs` |

---

## 📁 Directory Operations

| Operation          | Command Example       | Description                           |
| ------------------ | --------------------- | ------------------------------------- |
| Create a directory | `mkdir myfolder`      | Makes a new folder                    |
| Nested folders     | `mkdir -p /tmp/a/b/c` | Creates parent folders recursively    |
| Remove directory   | `rm -r myfolder`      | Removes directory and contents        |
| List directory     | `ls -l`               | Detailed listing of files/directories |
| Navigate directory | `cd /var/log`         | Move into a folder                    |
| Go up              | `cd ..`               | Move one level up                     |

---

## 📦 Copying, Moving, and Deleting Files

### 🟩 **Copying Files**

```bash
cp file1.txt file2.txt              # Copy file
cp file.txt /home/shahid/           # Copy to another directory
cp -r folder1/ folder2/             # Copy directories recursively
```

### 🟨 **Moving Files (or Renaming)**

```bash
mv report.txt /tmp/                 # Move file to /tmp
mv notes.txt notes_backup.txt       # Rename file
```

### 🟥 **Deleting Files**

```bash
rm file.txt                         # Delete a file
rm -i file.txt                      # Confirm before deleting
rm -r foldername/                   # Delete directory and contents
rm -rf folder/                      # Force delete (Dangerous!)
```

> ⚠️ Always use `-i` (interactive) when deleting important files!

---

## 🔐 File Safety & Overwriting

| Scenario                        | Command Behavior                        |
| ------------------------------- | --------------------------------------- |
| Copy to same name               | Overwrites silently unless `-i` is used |
| Delete with `rm`                | Cannot be undone unless backed up       |
| Safer deletion                  | Use `rm -i` or `trash-cli` if installed |
| Accidental overwrite prevention | Use `cp -i`, `mv -i` for prompts        |

---

## 🧪 Hands-On Lab

Try these in a test folder like `~/lab_fileops/`:

```bash
# 1. Setup Lab Directory
mkdir -p ~/lab_fileops && cd ~/lab_fileops

# 2. Create files
touch a.txt b.txt c.txt

# 3. Copy file
cp a.txt copy_of_a.txt

# 4. Rename file
mv b.txt renamed_b.txt

# 5. Move file to new directory
mkdir new_folder
mv c.txt new_folder/

# 6. Delete file with confirmation
rm -i copy_of_a.txt

# 7. Create and delete nested folders
mkdir -p temp/logs/archive
rm -r temp
```

---

## 🧠 Quiz Yourself

1. What is the difference between `mv` and `cp`?
2. How can you create a directory structure like `/opt/scripts/backups/logs` in one command?
3. What does the `-i` flag do with `rm` or `cp`?
4. Which command deletes a directory and its contents?
5. How do you rename a file using the command line?

---

## 📎 Summary

- Linux provides powerful command-line tools for managing files and directories.
- Tools like `cp`, `mv`, `rm`, `mkdir`, and `touch` form the core of file operations.
- Understanding these commands is critical for **script automation**, **log analysis**, **file backups**, and **cybersecurity operations**.
- Always use caution when deleting or overwriting files — there's no recycle bin on most Linux systems!