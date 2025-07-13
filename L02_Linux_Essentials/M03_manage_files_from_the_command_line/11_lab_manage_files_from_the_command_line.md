# 🧪 **Lab: Manage Files from the Command Line**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 87*

---

## 🎯 Objective

To gain hands-on experience with creating, viewing, copying, moving, renaming, and deleting files and directories using Linux **command-line tools**. You will also practice using **wildcards**, **brace expansion**, and **safe deletion practices**.

> This lab reinforces core file operations essential for scripting, automation, system management, and cybersecurity investigations.

---

## 🧰 Lab Setup

1. Open your **terminal emulator** or SSH into your Linux system.
2. Navigate to your **home directory**:

   ```bash
   cd ~
   ```

3. Create a new working directory:

   ```bash
   mkdir cli_filelab && cd cli_filelab
   ```

---

## 🧭 Step-by-Step Lab Tasks

---

### 🔹 **Step 1: Create Files and Directories**

```bash
# Create files
touch file1.txt file2.txt file3.txt

# Create directories
mkdir archive logs reports
```

---

### 🔹 **Step 2: Use Brace Expansion to Create Files Quickly**

```bash
touch report_{jan,feb,mar}.csv
touch backup_{01..05}.sh
```

✅ This creates:

* `report_jan.csv`, `report_feb.csv`, `report_mar.csv`
* `backup_01.sh` through `backup_05.sh`

---

### 🔹 **Step 3: List Files Using Wildcards (Globbing)**

```bash
ls *.txt              # List all text files
ls report_*.csv       # List all reports
ls backup_0?.sh       # List numbered backup scripts
```

---

### 🔹 **Step 4: Copy and Move Files**

```bash
cp file1.txt archive/
cp backup_01.sh logs/
mv file2.txt file2_renamed.txt
mv report_feb.csv reports/
```

✅ You've:

* Copied `file1.txt` to `archive/`
* Copied `backup_01.sh` to `logs/`
* Renamed `file2.txt` to `file2_renamed.txt`
* Moved `report_feb.csv` to `reports/`

---

### 🔹 **Step 5: View and Edit File Contents**

```bash
echo "Cyber Lab Entry 01" > file3.txt
cat file3.txt
```

Optional: Open with a text editor

```bash
nano file3.txt   # or vim file3.txt
```

---

### 🔹 **Step 6: Remove Files and Folders Safely**

```bash
rm -i file3.txt               # Prompt before deleting
rm -r logs                    # Delete directory and contents
```

> ⚠️ Use `-i` for safe deletion and `-r` only for folders.

---

## 📂 Expected Directory Tree

```text
cli_filelab/
├── archive/
│   └── file1.txt
├── backup_01.sh
├── backup_02.sh
├── backup_03.sh
├── backup_04.sh
├── backup_05.sh
├── file1.txt
├── file2_renamed.txt
├── report_jan.csv
├── report_mar.csv
├── reports/
│   └── report_feb.csv
```

---

## 🧠 Reflection Questions

1. What’s the difference between `cp` and `mv`?
2. How does brace expansion help in file creation?
3. Why is `rm -i` safer than plain `rm`?
4. What command would copy all `.csv` files into the `reports/` folder?
5. What wildcard pattern matches any `.sh` file starting with “backup\_” followed by a single digit?

---

## 🔐 Cybersecurity Insight

| Task                  | Example Use                                   |
| --------------------- | --------------------------------------------- |
| 📦 Organize log files | `mv *.log /var/log/archive/`                  |
| 🔁 Rotate backups     | `cp config.yaml config_$(date +%F).yaml`      |
| 🔍 Investigate files  | `ls -ltr /etc/` to find recent config changes |

---

## ✅ Completion

Well done! You've now:

* Created and modified files/directories using CLI
* Used wildcards and brace expansion
* Practiced file movement and cleanup
* Built a foundation for automating file tasks in real-world systems
