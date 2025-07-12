Here is your full **Guided Exercise** for:

---

# 🎯 Guided Exercise: **Manage Compressed tar Archives in Linux**

> 🧰 **Objective**: Learn how to create, compress, extract, list, and inspect `.tar`, `.tar.gz`, and `.tar.bz2` files using command-line tools.
> 🧠 **Skill Level**: Beginner → Intermediate
> 🔐 **Cybersecurity Relevance**: Compressed archives are common in malware delivery, forensic imaging, data exfiltration, and secure backups. This lab gives you the skills to handle them safely and effectively.

---

## 🧭 Table of Contents

- [🎯 Guided Exercise: **Manage Compressed tar Archives in Linux**](#-guided-exercise-manage-compressed-tar-archives-in-linux)
  - [🧭 Table of Contents](#-table-of-contents)
  - [📘 Learning Objectives](#-learning-objectives)
  - [🧰 Requirements](#-requirements)
  - [📦 Lab Environment](#-lab-environment)
  - [✅ Task 1: Create Test Files](#-task-1-create-test-files)
  - [✅ Task 2: Create tar Archives](#-task-2-create-tar-archives)
    - [🔧 Create `.tar` (no compression)](#-create-tar-no-compression)
    - [📦 Verify](#-verify)
  - [✅ Task 3: Compress Archives (gzip, bzip2)](#-task-3-compress-archives-gzip-bzip2)
    - [🔧 Create `.tar.gz`](#-create-targz)
    - [🔧 Create `.tar.bz2`](#-create-tarbz2)
    - [📦 List all archives:](#-list-all-archives)
  - [✅ Task 4: List Archive Contents (Safe Inspection)](#-task-4-list-archive-contents-safe-inspection)
  - [✅ Task 5: Extract tar Archives](#-task-5-extract-tar-archives)
    - [📂 Extract `.tar.gz`](#-extract-targz)
    - [📂 Extract `.tar.bz2`](#-extract-tarbz2)
    - [📂 Extract plain `.tar`](#-extract-plain-tar)
    - [🔍 Verify extraction](#-verify-extraction)
  - [🧪 Bonus Challenge: Inspect \& Extract Suspicious Archive](#-bonus-challenge-inspect--extract-suspicious-archive)
  - [📝 Lab Log Template](#-lab-log-template)

---

## 📘 Learning Objectives

By the end of this exercise, you will be able to:

* Create `.tar`, `.tar.gz`, and `.tar.bz2` files
* Compress and decompress files using `gzip` and `bzip2`
* Safely inspect archive contents before extraction
* Extract files to a specified directory
* Understand security considerations in archive handling

---

## 🧰 Requirements

| Tool                   | Purpose                    |
| ---------------------- | -------------------------- |
| `tar`                  | Archive and extract files  |
| `gzip` / `gunzip`      | Compress/decompress `.gz`  |
| `bzip2` / `bunzip2`    | Compress/decompress `.bz2` |
| `less`, `file`, `cat`  | View file details          |
| `mkdir`, `touch`, `ls` | Basic file management      |

---

## 📦 Lab Environment

Create a working directory:

```bash
mkdir -p ~/tar-lab/files
cd ~/tar-lab
```

Create test files:

```bash
touch files/report.txt files/log1.txt files/log2.txt
echo "Sample report data" > files/report.txt
```

---

## ✅ Task 1: Create Test Files

```bash
ls files/
```

You should see:

```
report.txt  log1.txt  log2.txt
```

> ✅ You now have 3 files inside a directory named `files/`.

---

## ✅ Task 2: Create tar Archives

### 🔧 Create `.tar` (no compression)

```bash
tar -cf archive.tar files/
```

### 📦 Verify

```bash
ls -lh archive.tar
```

---

## ✅ Task 3: Compress Archives (gzip, bzip2)

### 🔧 Create `.tar.gz`

```bash
tar -czf archive.tar.gz files/
```

### 🔧 Create `.tar.bz2`

```bash
tar -cjf archive.tar.bz2 files/
```

### 📦 List all archives:

```bash
ls -lh *.tar*
```

---

## ✅ Task 4: List Archive Contents (Safe Inspection)

> 🔐 Inspect before extracting — good practice in cybersecurity.

```bash
tar -tf archive.tar
tar -tzf archive.tar.gz
tar -tjf archive.tar.bz2
```

---

## ✅ Task 5: Extract tar Archives

### 📂 Extract `.tar.gz`

```bash
mkdir extract-gz
tar -xzf archive.tar.gz -C extract-gz/
```

### 📂 Extract `.tar.bz2`

```bash
mkdir extract-bz2
tar -xjf archive.tar.bz2 -C extract-bz2/
```

### 📂 Extract plain `.tar`

```bash
mkdir extract-tar
tar -xf archive.tar -C extract-tar/
```

### 🔍 Verify extraction

```bash
ls extract-gz/files/
ls extract-bz2/files/
```

---

## 🧪 Bonus Challenge: Inspect & Extract Suspicious Archive

1. Download or simulate a suspicious `.tar.gz` file.
2. List its contents without extracting:

   ```bash
   tar -tzf suspicious.tar.gz
   ```
3. Extract to a controlled location:

   ```bash
   mkdir ~/suspicious-sandbox
   tar -xzf suspicious.tar.gz -C ~/suspicious-sandbox/
   ```
4. Use `file` or `less` to inspect contents:

   ```bash
   file ~/suspicious-sandbox/*
   less ~/suspicious-sandbox/<filename>
   ```

> ⚠️ **Never extract suspicious archives as root**
> ⚠️ Always inspect archives before unpacking

---

## 📝 Lab Log Template

```text
👨‍💻 Directory: ~/tar-lab
📦 Files Archived: report.txt, log1.txt, log2.txt
🗜️ Created Archives:
  - archive.tar (uncompressed)
  - archive.tar.gz (gzip)
  - archive.tar.bz2 (bzip2)
🔍 Inspected with: tar -tf / -tzf / -tjf ✅
📂 Extracted to:
  - ./extract-tar
  - ./extract-gz
  - ./extract-bz2
🧪 Bonus Task: Suspicious archive reviewed & extracted in sandbox ✅
```

---

Would you like:

* 🧰 A **Bash script** to automate tar archiving tasks?
* 🔐 A **cybersecurity exercise** to detect hidden files in tar archives?
* 📜 A **comparison table** of tar/gzip/bzip2/xz compression speeds?

I'm ready for your next topic whenever you are!
