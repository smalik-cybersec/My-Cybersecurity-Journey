# 🎯 **Guided Exercise: Manage Files with Command-line Tools**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 68*

---

## 🧑‍💻 Objective

To practice **creating, copying, moving, renaming, and deleting files and directories** using Linux command-line tools such as `touch`, `mkdir`, `cp`, `mv`, and `rm`.

By the end of this lab, you’ll be able to manipulate files like a pro from the command line — a must-have skill for any Linux system administrator or cybersecurity analyst.

---

## 📦 Setup Instructions

1. Open your **terminal emulator** in a GUI-based system, or connect via **SSH** in headless systems.
2. Navigate to your **home directory**:

   ```bash
   cd ~
   ```

3. Create a **dedicated lab folder**:

   ```bash
   mkdir fileops_lab && cd fileops_lab
   ```

---

## 🧭 Step-by-Step Exercise

---

### 🔹 **Step 1: Create Files and Directories**

```bash
touch report.txt summary.txt
mkdir backups
mkdir -p projects/python/web
```

✅ Creates:

* Two text files
* A folder called `backups`
* Nested folders under `projects`

---

### 🔹 **Step 2: Copy Files**

```bash
cp report.txt backups/
cp summary.txt projects/
```

📝 What happened?

* `report.txt` is copied to the `backups/` folder
* `summary.txt` is copied to the `projects/` folder

---

### 🔹 **Step 3: Rename Files and Move Them**

```bash
mv summary.txt final_summary.txt
mv final_summary.txt backups/
```

🧠 `mv` is used for both renaming and moving!

---

### 🔹 **Step 4: Use `cp -r` and `rm -r` on Directories**

```bash
cp -r projects/ projects_backup/
rm -r projects_backup/
```

📌 `cp -r` = copy recursively (needed for directories)
⚠️ `rm -r` = delete directory and everything in it

---

### 🔹 **Step 5: Try Safe Deletion**

```bash
rm -i report.txt
```

🔐 `-i` flag prompts before deleting — always use this in real-world systems to avoid accidents.

---

### 🔹 **Step 6: Clean Up Lab**

```bash
cd ~
rm -r fileops_lab
```

✅ Removes everything you created in this lab.

---

## 🔎 Directory Tree During the Lab

```text
fileops_lab/
├── backups/
│   └── report.txt
│   └── final_summary.txt
├── projects/
│   └── python/
│       └── web/
├── report.txt
```

---

## 💡 Real-World Application

| Task                       | Example Use Case                        |
| -------------------------- | --------------------------------------- |
| 🔄 Copying logs            | `cp /var/log/auth.log ~/investigation/` |
| 🔐 Removing malware traces | `rm -r ~/Downloads/suspicious_app/`     |
| 📦 Organizing recon data   | `mv nmap_results.txt reports/`          |
| 📂 Making backups          | `cp -r /etc /home/user/backups/`        |

---

## 🧠 Reflection Questions

1. What’s the difference between `rm -r` and `rm -i`?
2. Why do you need `-r` to copy or remove a directory?
3. How can you ensure you don’t accidentally delete an important file?
4. Which command can you use to copy everything inside a folder?
