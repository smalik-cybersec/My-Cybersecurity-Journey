Absolutely, Shahid! Here's your **structured, hands-on guided exercise** for:

---

# 🧪 **Guided Exercise: Edit Text Files from the Shell Prompt**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 132*

---

## 🎯 Objective

To gain real-world practice editing text files directly from the **Linux shell prompt** using `nano` and `vim`, the two most common terminal-based editors. This exercise prepares you to confidently edit configuration files, scripts, and logs—skills essential in cybersecurity, DevOps, and system recovery.

---

## 🧰 Prerequisites

* A Linux terminal (local or SSH session)
* `nano` and `vim` installed (default on most Linux distros)
* Basic familiarity with CLI navigation

---

## 🧭 Step-by-Step Instructions

---

### 🔹 **Step 1: Create and Edit a File Using `nano`**

```bash
nano greetings.txt
```

**Do this inside nano:**

* Type the following:

  ```
  Hello, Shahid!
  Welcome to your Linux shell editing lab.
  This is a file created with nano.
  ```
* Press `Ctrl + O` → Save the file
* Press `Enter` to confirm filename
* Press `Ctrl + X` to exit nano

✅ Check your work:

```bash
cat greetings.txt
```

---

### 🔹 **Step 2: Edit an Existing File Using `vim`**

```bash
vim greetings.txt
```

**Inside vim:**

1. Press `i` → to enter insert mode
2. Add a new line:

   ```
   This line was added using vim.
   ```
3. Press `Esc` → to return to normal mode
4. Type `:wq` → Save and quit vim

✅ View changes:

```bash
cat greetings.txt
```

---

### 🔹 **Step 3: Use `nano` to Create a Simple Shell Script**

```bash
nano my_script.sh
```

Type:

```bash
#!/bin/bash
echo "This is Shahid's first shell script!"
```

**Save and exit** (`Ctrl + O`, `Enter`, then `Ctrl + X`)

Make it executable:

```bash
chmod +x my_script.sh
```

Run it:

```bash
./my_script.sh
```

✅ You should see the echo message in your terminal.

---

### 🔹 **Step 4: Use `vim` to Edit a System File (Simulated)**

> **Note:** We'll simulate editing a system file safely by copying it.

```bash
cp /etc/hostname ~/hostname_copy
vim ~/hostname_copy
```

* Press `i`, change the hostname (e.g., to `cyberhost`)
* Press `Esc`, then type `:wq` to save and exit

Check changes:

```bash
cat ~/hostname_copy
```

✅ This prepares you for real-world tasks like updating hostname or config files (with root access).

---

## 📂 Final Lab Structure (Your Home Directory)

```text
~/ 
├── greetings.txt
├── my_script.sh
├── hostname_copy
```

---

## 🧠 Reflection Questions

1. What are the key differences between `nano` and `vim`?
2. How do you save a file in `nano` vs. `vim`?
3. Why is `chmod +x` necessary before running a script?
4. What happens if you exit vim without saving?
5. Which editor do you feel more confident using right now—and why?

---

## ✅ Completion Criteria

| Task                          | Status |
| ----------------------------- | ------ |
| Created file with `nano`      | ✅      |
| Edited file with `vim`        | ✅      |
| Created and ran shell script  | ✅      |
| Simulated system file edit    | ✅      |
| Answered reflection questions | ✅      |

---

## 📎 Summary

* You now know how to create, edit, and manage files using **`nano` and `vim`** from the shell prompt.
* These skills are essential for editing config files, logs, and writing bash scripts directly in the terminal — even in emergency or recovery environments.

---

✅ Let me know if you'd like:

* 📥 Markdown or PDF export
* 🧠 Quiz based on this lab
* ⏭️ Next topic: *Understand and Modify Linux File Permissions*

You're editing files like a true Linux professional now, Shahid 🧑‍💻📝 Keep pushing forward!
