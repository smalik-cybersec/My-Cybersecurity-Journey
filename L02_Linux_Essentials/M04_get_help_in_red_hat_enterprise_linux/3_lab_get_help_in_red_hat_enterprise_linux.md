Here is your complete, structured, and professional **lab guide** for:

---

# 🧪 **Lab: Get Help in Red Hat Enterprise Linux**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 108*

---

## 🎯 Objective

To practice using various built-in help systems in **Red Hat Enterprise Linux (RHEL)** (or compatible systems like CentOS, AlmaLinux, Rocky, Fedora) including:

* `man`
* `--help`
* `whatis`
* `info`
* `apropos`

These tools provide **command reference**, **configuration guidance**, and **manuals** that are critical for self-sufficiency and Linux mastery.

---

## 🧰 Requirements

* Linux system with Bash shell (Red Hat or similar)
* Terminal access (GUI or remote SSH)
* Internet **not required** (all tools are local)

---

## 🧭 Step-by-Step Instructions

---

### 🔹 **Step 1: Use the `man` Command**

```bash
man mkdir
```

* Scroll using ↑/↓ or `Space`
* Quit using `q`
* Identify sections like **NAME**, **SYNOPSIS**, **DESCRIPTION**

📝 **Checkpoint:** What option allows you to create parent directories? (Answer: `-p`)

---

### 🔹 **Step 2: Use the `--help` Option**

Many commands support `--help` or `-h` to print quick reference usage.

```bash
mkdir --help
```

✅ Compare the output with the `man` page. Notice how:

* `--help` shows **brief syntax**
* `man` shows **detailed info**

---

### 🔹 **Step 3: Use the `whatis` Command**

This provides a **one-line summary** of a command’s purpose.

```bash
whatis passwd
whatis systemctl
```

> Output: `passwd (1) - change user password`

🧠 Good for: Quick refreshers and section identification.

---

### 🔹 **Step 4: Use the `apropos` or `man -k` Commands**

These show **all related commands** based on a keyword.

```bash
apropos user
man -k user
```

Try other keywords like `firewall`, `disk`, `ssh`, `password`

🧠 Good for: Discovering related tools and man sections.

---

### 🔹 **Step 5: Explore the `info` Pages**

```bash
info coreutils 'mkdir invocation'
```

Or for general info help navigation:

```bash
info mkdir
```

🔍 **`info`** is often more verbose than `man`. Use:

* Arrow keys to navigate
* Space to scroll
* `q` to quit

---

### 🔹 **Step 6: Compare All Help Methods**

| Tool      | Purpose                         | Usage Example     |
| --------- | ------------------------------- | ----------------- |
| `man`     | Full manual page                | `man cp`          |
| `--help`  | Quick summary of options        | `cp --help`       |
| `whatis`  | One-line command summary        | `whatis ls`       |
| `apropos` | Search man pages by keyword     | `apropos network` |
| `info`    | Detailed, often structured docs | `info mkdir`      |

---

### 🧪 Optional Bonus: Explore `tldr`

If installed, try:

```bash
tldr mkdir
```

🔎 `tldr` gives **examples-first help**. You can install it with:

```bash
sudo dnf install tldr
```

---

## 🧠 Reflection Questions

1. What’s the difference between `man` and `--help`?
2. Which command shows a one-line summary of another command?
3. How do you search for all documentation related to “disk”?
4. When would you prefer `info` over `man`?
5. What section number does `passwd (1)` represent?

---

## ✅ Success Criteria

| Task                                  | Status |
| ------------------------------------- | ------ |
| Used `man` to view help for a command | ✅      |
| Used `--help` to print quick help     | ✅      |
| Used `whatis` and `apropos`           | ✅      |
| Used `info` and compared content      | ✅      |
| Answered reflection questions         | ✅      |

---

## 📎 Summary

* Linux provides **built-in documentation systems** that don’t need an internet connection
* Tools like `man`, `--help`, `info`, `whatis`, and `apropos` help you:

  * Troubleshoot errors
  * Learn options
  * Explore related tools
  * Work efficiently without Google

> Mastering these help tools is a mark of a serious Linux or cybersecurity professional.

---

✅ Would you like:

* 🧠 Quiz based on this lab?
* 📥 Markdown version for GitHub?
* ⏭️ Proceed to: *File Permissions and Ownership in Linux*?

You're not just using Linux, Shahid — you're commanding it with clarity 📘⚙️
