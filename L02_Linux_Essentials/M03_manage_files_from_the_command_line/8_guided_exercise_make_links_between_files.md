Absolutely, Shahid! Here's your fully structured, hands-on **guided exercise** for:

---

# 🧪 **Guided Exercise: Make Links Between Files**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 76*

---

## 🎯 Objective

To learn how to create and manage both **hard links** and **symbolic (soft) links** in Linux using the `ln` command. You’ll test link behavior by modifying and deleting source files to observe how links react — a crucial skill in system administration, scripting, backups, and cybersecurity investigations.

---

## 🧰 Lab Requirements

* A Linux system with Bash shell
* A terminal session (GUI or CLI)
* Basic familiarity with commands like `touch`, `ls`, `cat`, and `echo`

---

## 🧭 Step-by-Step Exercise

---

### 🔹 **Step 1: Create a Lab Directory**

```bash
cd ~
mkdir link_lab && cd link_lab
```

---

### 🔹 **Step 2: Create an Original File**

```bash
echo "Linux Link Lab by Shahid" > original.txt
```

Check file contents:

```bash
cat original.txt
```

---

### 🔹 **Step 3: Create a Hard Link**

```bash
ln original.txt hardlink.txt
```

✅ This creates a second file pointing to the **same inode**.

---

### 🔹 **Step 4: Create a Symbolic Link**

```bash
ln -s original.txt symlink.txt
```

✅ This creates a shortcut (pointer) to the file path.

---

### 🔹 **Step 5: Check File Metadata and Structure**

```bash
ls -li
```

🧠 Questions to consider:

* Do `original.txt` and `hardlink.txt` share the same inode?
* Does `symlink.txt` point to a path or to an inode?

---

### 🔹 **Step 6: Test File Behavior**

#### 6.1 Modify the original file:

```bash
echo "Appended line" >> original.txt
```

Then check:

```bash
cat hardlink.txt
cat symlink.txt
```

🧠 Both should reflect the same changes.

---

#### 6.2 Delete the original file:

```bash
rm original.txt
```

Now test:

```bash
cat hardlink.txt   # Still works!
cat symlink.txt    # Broken (file not found)
```

✅ **Hard link remains functional**
❌ **Symlink is broken**

---

### 🔹 **Step 7: Create a Symbolic Link to a Directory**

```bash
mkdir -p project/configs
ln -s ~/link_lab/project project_link
```

Then list files inside the linked directory:

```bash
ls -l project_link
```

✅ You can use symlinks to access entire folders from different locations — very useful for organizing configs, logs, scripts, etc.

---

## 📂 Expected Directory Tree (Before Deletion)

```text
link_lab/
├── original.txt
├── hardlink.txt
├── symlink.txt -> original.txt
├── project/
│   └── configs/
└── project_link -> project/
```

---

## 🧠 Reflection Questions

1. What’s the main technical difference between a hard link and a symlink?
2. Why is a hard link not broken when the original file is deleted?
3. Can you create a hard link to a directory? Why or why not?
4. When would you use a symbolic link in cybersecurity or DevOps?

---

## ✅ Summary of Key Commands

```bash
ln source.txt hardlink.txt         # Create hard link
ln -s source.txt symlink.txt       # Create symbolic link
ls -li                             # Show inode numbers
readlink symlink.txt               # Show symlink target
```

---

✅ Let me know if you want:

* 📥 Export this as a Markdown lab file
* 🧠 Quiz answer key from the previous lesson
* ⏭️ Next topic: *Use `vim` or `nano` to Edit Files*

You’re mastering system-level file management like a pro, Shahid 🔧📁 Keep up the momentum!
