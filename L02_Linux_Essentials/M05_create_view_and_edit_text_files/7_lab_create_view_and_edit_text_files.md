Absolutely, Shahid! Here's your complete, hands-on **lab guide** for:

---

# 🧪 **Lab: Create, View, and Edit Text Files**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 144*

---

## 🎯 Objective

To practice the essential tasks of:

* Creating text files
* Viewing their contents
* Editing them using shell-based tools like `nano` and `vim`

> These are core tasks for configuring systems, writing scripts, handling logs, and performing forensic or remediation work on Linux machines.

---

## 🧰 Requirements

* Access to a Linux system (RHEL-based or similar)
* A terminal window
* Basic familiarity with shell commands (`cd`, `ls`, `touch`)

---

## 🧭 Step-by-Step Lab Instructions

---

### 🔹 **Step 1: Navigate to Your Working Directory**

Start by moving into your home directory or lab folder:

```bash
cd ~
mkdir textlab && cd textlab
```

✅ You are now inside a clean workspace.

---

### 🔹 **Step 2: Create Empty Text Files**

```bash
touch notes.txt todo.txt welcome.txt
```

Check:

```bash
ls -l
```

✅ This shows the newly created files with timestamps.

---

### 🔹 **Step 3: Add Content to a File Using `echo` and Redirection**

```bash
echo "My first Linux file" > notes.txt
echo "1. Learn Bash" > todo.txt
echo "2. Practice commands" >> todo.txt
```

Now view contents:

```bash
cat notes.txt
cat todo.txt
```

✅ You’ve written and appended data using redirection operators `>` and `>>`.

---

### 🔹 **Step 4: Use `nano` to Edit Files**

```bash
nano welcome.txt
```

Inside nano:

* Type:

  ```
  Welcome, Shahid!
  You are mastering Linux text file management.
  ```
* Save with `Ctrl + O`, press `Enter`
* Exit with `Ctrl + X`

✅ Check result:

```bash
cat welcome.txt
```

---

### 🔹 **Step 5: Use `vim` to Edit an Existing File**

```bash
vim notes.txt
```

Inside `vim`:

* Press `i` to enter insert mode
* Add a new line:

  ```
  Edited with vim.
  ```
* Press `Esc`, then type `:wq` to save and quit

✅ Confirm change:

```bash
cat notes.txt
```

---

### 🔹 **Step 6: Append Multiple Lines Using `cat` and Input Redirection**

```bash
cat >> welcome.txt
```

Type:

```
This is an extra line.
This is another one.
```

Press `Ctrl + D` to end.

✅ View:

```bash
cat welcome.txt
```

---

### 🔹 **Step 7: View File Contents with `less`, `more`, `head`, and `tail`**

```bash
head todo.txt
tail welcome.txt
more welcome.txt
less notes.txt
```

Use `q` to exit `less` or `more`.

---

## 📂 Lab File Structure (Expected Output)

```text
~/textlab/
├── notes.txt       # Created, edited with vim
├── todo.txt        # Appended with redirection
├── welcome.txt     # Edited with nano and `cat >>`
```

---

## 🧠 Reflection Questions

1. What’s the difference between `>` and `>>` when writing to a file?
2. What’s the purpose of `cat >> filename`?
3. How do you save and exit a file in `nano`? What about `vim`?
4. When would you use `head` or `tail` to read a file?
5. Why is text editing from the terminal critical for system administrators and cybersecurity professionals?

---

## ✅ Completion Checklist

| Task                                       | Done |
| ------------------------------------------ | ---- |
| Created text files using `touch`           | ✅    |
| Added content using `echo` and redirection | ✅    |
| Edited files with `nano`                   | ✅    |
| Edited files with `vim`                    | ✅    |
| Appended with `cat >>`                     | ✅    |
| Viewed files using `cat`, `less`, `head`   | ✅    |

---

## 📎 Summary

In this lab, you’ve gained hands-on practice in:

* Creating and modifying text files from the terminal
* Using both **redirection** and **interactive editors** (`nano`, `vim`)
* Reading files using `cat`, `head`, `tail`, and `less`

> This is foundational for working with **configs**, **logs**, **scripts**, and **incident data** — core skills in cybersecurity and Linux administration.

---

✅ Would you like:

* 📥 Export in Markdown for GitHub
* 🧠 Quiz based on this lab
* ⏭️ Next lesson: *Set Shell Aliases and Startup Files*

You're not just reading Linux files now, Shahid — you're writing your own configuration future ✍️🐧
