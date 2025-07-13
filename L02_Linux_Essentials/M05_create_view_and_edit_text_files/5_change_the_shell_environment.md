# 🌍 **Lesson: Change the Shell Environment**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 134*

---

## 📚 Table of Contents

- [🌍 **Lesson: Change the Shell Environment**](#-lesson-change-the-shell-environment)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [⚙️ What Is the Shell Environment?](#️-what-is-the-shell-environment)
  - [🧬 Shell Environment Variables](#-shell-environment-variables)
  - [📦 Common Environment Variables](#-common-environment-variables)
  - [🔧 Modifying the Shell Environment](#-modifying-the-shell-environment)
    - [🧪 View all current variables](#-view-all-current-variables)
    - [🧪 Set a temporary environment variable](#-set-a-temporary-environment-variable)
    - [🧪 Remove a variable](#-remove-a-variable)
  - [🛠️ Persistent vs Temporary Changes](#️-persistent-vs-temporary-changes)
    - [Example: Make `EDITOR=nano` persistent for the user](#example-make-editornano-persistent-for-the-user)
  - [🧪 Practice Examples](#-practice-examples)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 🎯 Introduction

In Linux, the **shell environment** controls how commands behave, where the system looks for executables, how prompts appear, and much more. As a user or administrator, you can **customize your shell** to make your workflow more efficient and secure.

> Mastery of the shell environment helps in scripting, secure access, automation, and system performance.

---

## ⚙️ What Is the Shell Environment?

The **shell environment** is a set of variables and settings that define how your shell behaves. It is initialized when you open a terminal session or log into the system.

> The most common shell used in Linux is **Bash (Bourne Again Shell)**.

---

## 🧬 Shell Environment Variables

Environment variables are key-value pairs that control:

- User preferences
- Command behavior
- System paths
- Shell appearance

You can **view**, **create**, and **modify** them using:

```bash
echo $VARIABLE
export VARIABLE=value
unset VARIABLE
```

---

## 📦 Common Environment Variables

| Variable | Description                                   |
| -------- | --------------------------------------------- |
| `PATH`   | Directories the shell searches for commands   |
| `HOME`   | Current user's home directory                 |
| `USER`   | Username of the logged-in user                |
| `SHELL`  | Path to the default shell (e.g., `/bin/bash`) |
| `PWD`    | Current working directory                     |
| `EDITOR` | Default text editor used by CLI apps          |
| `PS1`    | Defines the shell prompt format               |

---

## 🔧 Modifying the Shell Environment

### 🧪 View all current variables

```bash
printenv
```

or

```bash
env
```

### 🧪 Set a temporary environment variable

```bash
export MYNAME=Shahid
echo $MYNAME
```

✅ This variable is active for the current shell session only.

### 🧪 Remove a variable

```bash
unset MYNAME
```

---

## 🛠️ Persistent vs Temporary Changes

| Change Type | Scope                  | Method                                             |
| ----------- | ---------------------- | -------------------------------------------------- |
| Temporary   | Current session only   | `export NAME=value`                                |
| Persistent  | Across logins/sessions | Edit `.bashrc`, `.bash_profile`, or `/etc/profile` |

### Example: Make `EDITOR=nano` persistent for the user

```bash
echo "export EDITOR=nano" >> ~/.bashrc
source ~/.bashrc
```

---

## 🧪 Practice Examples

```bash
# View the current PATH
echo $PATH

# Add a custom directory to PATH
export PATH=$PATH:/home/shahid/scripts

# Set a new prompt
export PS1="[\u@\h \W]\$ "

# Make a variable persist (nano used to edit .bashrc)
echo 'export PROJECT=CyberLab' >> ~/.bashrc
source ~/.bashrc
```

---

## 🧠 Quiz Yourself

1. What command lists all environment variables?
2. How do you make a variable available to child processes?
3. How do you permanently add a new directory to your PATH?
4. What does the `PS1` variable control?
5. What is the difference between `export` and `set`?

---

## 📎 Summary

- The **shell environment** defines your Linux session's behavior.
- You can use `export`, `printenv`, `unset`, and `echo` to interact with environment variables.
- Temporary changes affect the **current session only**.
- Persistent changes require editing `.bashrc`, `.bash_profile`, or global system files.
- Managing your shell environment is key to efficient, repeatable, and secure system usage.
