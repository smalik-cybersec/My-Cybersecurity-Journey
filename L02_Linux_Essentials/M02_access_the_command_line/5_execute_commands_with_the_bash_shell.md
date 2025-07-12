Fantastic, Shahid! Here’s your **complete, professional-grade documentation** for:

---

# 🖥️ **Lesson 04: Execute Commands with the Bash Shell**

> *Module: Red Hat System Administration / Linux Essentials*
> *Craw Cyber Security One-Year Diploma – Page 30*

---

## 📚 Table of Contents

- [🖥️ **Lesson 04: Execute Commands with the Bash Shell**](#️-lesson-04-execute-commands-with-the-bash-shell)
  - [📚 Table of Contents](#-table-of-contents)
  - [📖 What is Bash?](#-what-is-bash)
  - [⚙️ How Bash Executes Commands](#️-how-bash-executes-commands)
  - [🗂️ Command Syntax \& Structure](#️-command-syntax--structure)
  - [🧪 Execution Examples (with Explanation)](#-execution-examples-with-explanation)
  - [🎛️ Variables, Quoting, and Expansion](#️-variables-quoting-and-expansion)
    - [✅ Environment \& Custom Variables](#-environment--custom-variables)
    - [✅ Quoting](#-quoting)
  - [🔗 Command Chaining \& Redirection](#-command-chaining--redirection)
    - [🔁 **Chaining Operators**](#-chaining-operators)
    - [➡️ **Input/Output Redirection**](#️-inputoutput-redirection)
  - [🧪 Guided Lab Practice](#-guided-lab-practice)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 📖 What is Bash?

**Bash (Bourne Again SHell)** is the default command-line shell used in most Linux distributions, including Red Hat. It allows users to interact with the system by executing commands, running scripts, and automating tasks.

> Bash is both a command interpreter and a scripting language.

---

## ⚙️ How Bash Executes Commands

When you type a command in the terminal and press Enter, Bash:

1. **Parses** the input
2. **Expands** any variables or wildcards
3. **Searches** for the command in the `PATH`
4. **Executes** it using a process ID (PID)

---

## 🗂️ Command Syntax & Structure

```bash
command [options] [arguments]
```

| Part        | Description                        | Example                  |
| ----------- | ---------------------------------- | ------------------------ |
| `command`   | The action or tool you want to run | `ls`                     |
| `options`   | Modify how the command works       | `-l`, `--help`           |
| `arguments` | Specify what the command acts upon | `/home/shahid/Downloads` |

Example:

```bash
ls -l /etc
```

This lists files in the `/etc` directory in long format.

---

## 🧪 Execution Examples (with Explanation)

```bash
date
```

➡️ Displays the current system date and time.

```bash
whoami
```

➡️ Shows the current logged-in user.

```bash
uptime
```

➡️ Tells how long the system has been running.

```bash
df -h
```

➡️ Shows disk usage in human-readable format.

```bash
uname -r
```

➡️ Displays the kernel version.

---

## 🎛️ Variables, Quoting, and Expansion

### ✅ Environment & Custom Variables

```bash
echo $USER       # Built-in environment variable
MYNAME="Shahid"
echo $MYNAME     # Custom variable
```

### ✅ Quoting

| Type                  | Syntax                          | Behavior                                           |
| --------------------- | ------------------------------- | -------------------------------------------------- |
| **Double Quotes**     | `" "`                           | Allows variable expansion and command substitution |
| **Single Quotes**     | `' '`                           | Treats everything literally                        |
| **Backticks or \$()** | `` `command` `` or `$(command)` | Executes a command and substitutes its output      |

```bash
echo "Today is $(date)"
```

---

## 🔗 Command Chaining & Redirection

### 🔁 **Chaining Operators**

| Operator | Purpose                           | Example                 |                                |           |   |                 |
| -------- | --------------------------------- | ----------------------- | ------------------------------ | --------- | - | --------------- |
| `;`      | Run commands sequentially         | `echo A; echo B`        |                                |           |   |                 |
| `&&`     | Run second only if first succeeds | `mkdir test && cd test` |                                |           |   |                 |
| \`       |                                   | \`                      | Run second only if first fails | \`cd /abc |   | echo "Failed"\` |

### ➡️ **Input/Output Redirection**

| Symbol | Description                  | Example                     |
| ------ | ---------------------------- | --------------------------- |
| `>`    | Redirects output (overwrite) | `echo "Hello" > file.txt`   |
| `>>`   | Appends output               | `echo "Line 2" >> file.txt` |
| `<`    | Takes input from a file      | `sort < file.txt`           |
| `2>`   | Redirects errors             | `command 2> error.log`      |

---

## 🧪 Guided Lab Practice

Try these in a terminal:

1. 🔍 View system uptime and log it:

   ```bash
   uptime > uptime_log.txt
   ```

2. ✏️ Set and display a custom variable:

   ```bash
   MYSECURITY="CyberSafe"
   echo $MYSECURITY
   ```

3. 🔁 Combine commands to create folder and switch into it:

   ```bash
   mkdir redhat_lab && cd redhat_lab
   ```

4. ⛔ Test error redirection:

   ```bash
   cat not_a_file 2> error.txt
   ```

5. 🧠 Use command substitution:

   ```bash
   echo "Today is $(date)"
   ```

---

## 🧠 Quiz Yourself

1. What is the role of the Bash shell in Linux?
2. What’s the difference between `>` and `>>`?
3. What does `echo $PATH` do?
4. How do you chain two commands so the second only runs if the first fails?
5. Write a command to create a variable and print it.

---

## 📎 Summary

* Bash is the **default Linux shell** used to run commands and automate tasks.
* Commands follow the syntax: `command [options] [arguments]`
* You can define **variables**, use **command substitution**, and handle **input/output redirection**
* **Chaining operators** make Bash powerful for scripting and automation.
* Mastery of Bash is a **core skill for cybersecurity pros** — especially in penetration testing, server admin, and automation roles.

---

✅ **Up Next:**
Would you like to move to:

> **Lesson 05: Use the `man` Pages and `--help` for Help**

Or should I generate a:

* 🧪 Lab workbook
* ✍️ Quiz for this Bash lesson
* 📦 Markdown export for GitHub?

Let me know your next command, brother Shahid ⚡
