Here’s your complete, structured, and practical **Guided Exercise** for:

---

# 🧪 **Guided Exercise: Change the Shell Environment**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 141*

---

## 🎯 Objective

In this guided exercise, you’ll learn to **view**, **set**, **modify**, and **persist** environment variables in the Linux shell using `export`, `unset`, and `.bashrc` edits. You'll also customize your shell prompt and expand your `PATH`.

> This is critical for scripting, automation, privilege management, and even security isolation.

---

## 🧰 Prerequisites

* Linux terminal (Bash shell)
* Access to your user account
* Basic file editing experience (`nano` or `vim`)

---

## 🧭 Step-by-Step Instructions

---

### 🔹 **Step 1: View Your Current Shell Environment**

```bash
printenv
```

Also try:

```bash
env
```

✅ This shows all current environment variables.

Now check individual variables:

```bash
echo $USER
echo $HOME
echo $SHELL
echo $PATH
```

---

### 🔹 **Step 2: Create and Export a Custom Variable**

```bash
export MYROLE="CyberStudent"
echo $MYROLE
```

✅ You’ve now created a **temporary environment variable** for the session.

---

### 🔹 **Step 3: Add a Custom Directory to Your PATH**

```bash
mkdir ~/scripts
export PATH=$PATH:~/scripts
echo $PATH
```

Now test it:

```bash
echo -e '#!/bin/bash\necho Hello Shahid!' > ~/scripts/hello
chmod +x ~/scripts/hello
hello
```

✅ You just ran a script from your custom `PATH`.

---

### 🔹 **Step 4: Modify Your Prompt (PS1)**

Change your shell prompt (temporary):

```bash
export PS1="[CyberShell \u@\h \W]$ "
```

Explanation:

* `\u` = username
* `\h` = hostname
* `\W` = current directory

---

### 🔹 **Step 5: Persist Your Changes**

Open `.bashrc` using nano:

```bash
nano ~/.bashrc
```

Add these lines at the bottom:

```bash
export MYROLE="CyberStudent"
export PATH=$PATH:~/scripts
export PS1="[CyberShell \u@\h \W]$ "
```

Save and exit: `Ctrl + O`, `Enter`, `Ctrl + X`

Then activate your changes:

```bash
source ~/.bashrc
```

✅ Now these changes will persist across logins!

---

### 🔹 **Step 6: Unset (Delete) an Environment Variable**

```bash
unset MYROLE
echo $MYROLE
```

✅ This removes the variable **only for the current session**.

---

## 📂 Final Setup Snapshot

```text
~/scripts/
└── hello   # A script you added to your PATH

~/.bashrc
└── Modified to persist environment variables and shell prompt
```

---

## 🧠 Reflection Questions

1. What is the difference between `export` and `set`?
2. Why would you want to modify your `PATH`?
3. Where should you save environment changes to make them persistent?
4. What does the `PS1` variable control?
5. How can shell environment variables help in automation or security?

---

## ✅ Completion Checklist

| Task                                     | Done |
| ---------------------------------------- | ---- |
| Viewed current environment variables     | ✅    |
| Created a temporary environment variable | ✅    |
| Modified your `PATH`                     | ✅    |
| Customized your shell prompt             | ✅    |
| Persisted changes via `.bashrc`          | ✅    |
| Tested and unset a variable              | ✅    |

---

## 📎 Summary

In this exercise, you’ve learned how to:

* Read and modify environment variables
* Extend your system’s PATH for scripts
* Customize your shell’s appearance
* Make all of the above **persist** across sessions

These are core skills for **secure scripting**, **automated workflows**, and **personalized administration**.

---

✅ Let me know if you’d like:

* 📥 Markdown export for GitHub
* 🧠 Quiz based on this lab
* ⏭️ Next lesson: *Set Shell Aliases and Startup Files*

You're in full control of your shell environment now, Shahid — that’s the mark of a true Linux pro 🧑‍💻🔧🐚
