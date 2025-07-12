Absolutely, Shahid! Here's your complete, structured, hands-on **guided exercise** for:

---

# 🧪 **Guided Exercise: Read Manual Pages**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 104*

---

## 🎯 Objective

To practice using the `man` command and navigate Linux manual pages effectively. This exercise will help you understand **command usage**, **options**, **file formats**, and **admin-level tools** — all using built-in Linux documentation.

> This is one of the **most powerful skills** for becoming independent in Linux: reading and interpreting man pages like a pro.

---

## 🧰 Lab Requirements

* Linux system (Red Hat, Ubuntu, Kali, etc.)
* Terminal access (GUI or SSH)
* Basic knowledge of Linux commands (e.g., `ls`, `cp`, `mv`)

---

## 🧭 Step-by-Step Instructions

---

### 🔹 **Step 1: Open a Terminal**

Start your terminal and make sure you're in your home directory:

```bash
cd ~
```

---

### 🔹 **Step 2: View a Simple man Page**

```bash
man ls
```

* Scroll using `↑`, `↓`, or `Space`
* Quit with `q`

---

### 🔹 **Step 3: Navigate and Search Inside man Pages**

```bash
man cp
```

Try the following keys:

* `/recursive` → searches for the term “recursive”
* `n` → jump to next match
* `q` → exit the man page

---

### 🔹 **Step 4: Identify Structure of a man Page**

While viewing any man page (e.g. `man mv`), locate and write down:

| Section     | Example (from `mv`)              |
| ----------- | -------------------------------- |
| NAME        | mv - move (rename) files         |
| SYNOPSIS    | mv \[OPTION]... SOURCE DEST      |
| DESCRIPTION | What the command does            |
| OPTIONS     | List of available flags          |
| EXAMPLES    | Practical use cases (if present) |

---

### 🔹 **Step 5: View a Specific man Section**

```bash
man 5 passwd
```

This shows the **file format** of `/etc/passwd` instead of the command `passwd`.

---

### 🔹 **Step 6: Search for Related Commands Using man -k**

```bash
man -k ssh
```

This shows all man page entries that mention “ssh”. Pick one and open it:

```bash
man sshd_config
```

---

### 🔹 **Step 7: Practice with Administrative Command Sections**

```bash
man 8 fdisk
man 8 iptables
```

✅ Section 8 is used for **administration-level commands**.

---

### 🔹 **Step 8: Combine with Other man Tools (Bonus)**

```bash
whatis chmod         # Short description of command
apropos firewall     # All matching man entries
```

---

## 🧠 Reflection Questions

1. What is the difference between `man cp` and `man 1 cp`?
2. How do you search for a term inside a man page?
3. Which man section would you use to understand the structure of `/etc/shadow`?
4. What’s the benefit of using `man -k` or `apropos`?
5. How is reading a man page better than random web searches?

---

## ✅ Practice Completion Criteria

✔ Viewed at least 5 man pages
✔ Navigated with search (`/` and `n`)
✔ Identified `NAME`, `SYNOPSIS`, and `DESCRIPTION` sections
✔ Searched system-wide docs with `man -k`
✔ Opened a **section-specific** man page (e.g., section 5)

---

## 📎 Summary

You now know how to:

* Open and interpret `man` pages for any command
* Search **within man pages** and **across the system**
* Understand what options, arguments, and config files do
* Use section numbers to get the right documentation
* Use `man` as your **first resource** when learning or troubleshooting

---

✅ Would you like:

* 🧠 Answer key for the reflection quiz
* 📥 Markdown export of this lab
* ⏭️ Next topic: *Use `--help`, `whatis`, `info`, and `apropos`*

You’re now reading Linux like it was meant to be read — straight from the source. Great work, Shahid! 🧠📘🐧
