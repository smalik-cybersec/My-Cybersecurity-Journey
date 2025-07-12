# 🧪 **Lab: Access the Command Line**

> *Lesson 04 Hands-On Lab – Linux Essentials (Red Hat System Administration)*
> *Craw Cyber Security One-Year Diploma – Page 40*

---

## 🎯 Objective

This lab will guide you through **executing commands using the Bash shell**, learning how Bash processes input, how to use variables, redirection, chaining, and basic command construction. This is foundational for scripting, automation, and cybersecurity tool usage.

---

## 🧰 Prerequisites

* ✅ Linux OS with Bash shell (Red Hat / CentOS / Fedora / Ubuntu / Kali)
* ✅ A terminal emulator (GNOME Terminal, Konsole, etc.)
* ✅ A non-root user with sudo access

---

## 🧭 Exercise 1: Basic Bash Command Execution

### 🔹 Goal: Run simple system commands and observe output

```bash
# 1. Display the current user
whoami

# 2. Show the current working directory
pwd

# 3. List all files in long format
ls -l

# 4. Display system uptime
uptime

# 5. Show disk usage in human-readable format
df -h
```

🔍 **Checkpoint**: Make sure you understand what each command is displaying.

---

## 🧭 Exercise 2: Variables & Substitution

### 🔹 Goal: Learn to declare, use, and expand variables in Bash

```bash
# 1. Set a variable
MYNAME="Shahid"

# 2. Print the value
echo $MYNAME

# 3. Combine with a message
echo "Hello, $MYNAME! Welcome to Linux."

# 4. Use command substitution
echo "Today is: $(date)"
```

---

## 🧭 Exercise 3: Redirection and Output Control

### 🔹 Goal: Redirect outputs and handle errors

```bash
# 1. Create a new file and write into it
echo "Linux Lab Output" > output.txt

# 2. Append more lines
echo "Second line" >> output.txt

# 3. View the file
cat output.txt

# 4. Redirect error output to a file
cat nonexistent.txt 2> error.log

# 5. View error log
cat error.log
```

---

## 🧭 Exercise 4: Command Chaining

### 🔹 Goal: Execute multiple commands conditionally

```bash
# 1. Create directory and enter it
mkdir reports && cd reports

# 2. Try to enter a non-existent folder or echo an error
cd /doesnotexist || echo "Directory not found"

# 3. Run two commands sequentially
echo "Start"; echo "End"
```

---

## 🧠 Reflection Questions

1. What happens when you use `>` vs `>>`?
2. How does `&&` differ from `;` in command chaining?
3. What is the benefit of `$(command)` in a Bash command?
4. How does Bash handle errors by default?

---

## 📂 Directory Snapshot After Completion

```bash
~/LinuxLabs
├── output.txt
├── error.log
└── reports/
```

---

## 🧪 Bonus Task (Optional)

> Create a Bash one-liner that:

1. Creates a file named `sysinfo.txt`
2. Adds your username, current date, and system uptime
3. Displays the contents of the file

```bash
echo "User: $(whoami), Date: $(date), Uptime: $(uptime)" > sysinfo.txt && cat sysinfo.txt
```

---

## ✅ What You Learned

* Basic Bash command structure and syntax
* Using environment and custom variables
* Input/output redirection and error handling
* Conditional command execution
* Real-world Bash command-line usage skills