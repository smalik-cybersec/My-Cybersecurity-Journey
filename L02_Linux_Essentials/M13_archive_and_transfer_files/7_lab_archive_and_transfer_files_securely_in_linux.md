Here is your full, GitHub-ready, professional Markdown documentation for:

---

# 🧪 Lab: **Archive and Transfer Files Securely in Linux**

> 📦 **Objective**: Practice archiving files into `.tar.gz` format and transferring them securely between Linux systems using `scp` and `rsync`.
> 🧠 **Skill Level**: Beginner → Intermediate
> 🔐 **Cybersecurity Relevance**: Secure file packaging and transfer is essential in evidence handling, log shipping, forensic analysis, backups, and secure deployments.

---

## 🧭 Table of Contents

- [🧪 Lab: **Archive and Transfer Files Securely in Linux**](#-lab-archive-and-transfer-files-securely-in-linux)
  - [🧭 Table of Contents](#-table-of-contents)
  - [📘 Learning Objectives](#-learning-objectives)
  - [🧰 Tools Required](#-tools-required)
  - [📦 Lab Setup](#-lab-setup)
  - [✅ Task 1: Archive Files Using `tar`](#-task-1-archive-files-using-tar)
    - [Step 1: Create sample files](#step-1-create-sample-files)
    - [Step 2: Archive and compress](#step-2-archive-and-compress)
  - [✅ Task 2: Securely Transfer the Archive Using `scp`](#-task-2-securely-transfer-the-archive-using-scp)
    - [Verify on remote:](#verify-on-remote)
  - [✅ Task 3: Transfer Archive Using `rsync`](#-task-3-transfer-archive-using-rsync)
  - [✅ Task 4: Extract Archive on Remote System](#-task-4-extract-archive-on-remote-system)
    - [Step 1: SSH into remote](#step-1-ssh-into-remote)
    - [Step 2: Extract archive](#step-2-extract-archive)
    - [Step 3: Verify contents](#step-3-verify-contents)
  - [🧪 Bonus Challenge: Verify Archive Integrity](#-bonus-challenge-verify-archive-integrity)
    - [Step 1: Generate checksum before transfer](#step-1-generate-checksum-before-transfer)
    - [Step 2: Transfer both files:](#step-2-transfer-both-files)
    - [Step 3: On remote, verify:](#step-3-on-remote-verify)
  - [📝 Lab Report Template](#-lab-report-template)
  - [📌 Key Takeaways](#-key-takeaways)

---

## 📘 Learning Objectives

By the end of this lab, you will be able to:

* Archive multiple files/directories into a `.tar.gz` file
* Securely transfer files between Linux systems using `scp` and `rsync`
* Extract and verify archives after transfer
* Apply best practices in secure file packaging and transmission

---

## 🧰 Tools Required

| Tool    | Purpose                      |
| ------- | ---------------------------- |
| `tar`   | Archive and compress files   |
| `scp`   | Securely copy files over SSH |
| `rsync` | Efficient syncing over SSH   |
| `ssh`   | Remote shell access          |

---

## 📦 Lab Setup

Assume:

* Local system: `user@local`
* Remote system: `user@192.168.56.10`
* SSH access is available:

  ```bash
  ssh user@192.168.56.10
  ```

---

## ✅ Task 1: Archive Files Using `tar`

### Step 1: Create sample files

```bash
mkdir -p ~/lab-data/logs
echo "System Log 1" > ~/lab-data/logs/log1.txt
echo "System Log 2" > ~/lab-data/logs/log2.txt
```

### Step 2: Archive and compress

```bash
tar -czf logs-backup.tar.gz ~/lab-data/
```

> ✅ This creates a compressed archive `logs-backup.tar.gz`

---

## ✅ Task 2: Securely Transfer the Archive Using `scp`

```bash
scp logs-backup.tar.gz user@192.168.56.10:/home/user/
```

### Verify on remote:

```bash
ssh user@192.168.56.10
ls -lh /home/user/logs-backup.tar.gz
```

---

## ✅ Task 3: Transfer Archive Using `rsync`

(Alternative to `scp`, especially for large archives)

```bash
rsync -avz -e ssh logs-backup.tar.gz user@192.168.56.10:/home/user/backup/
```

> ✅ `rsync` is ideal for incremental syncs or automation

---

## ✅ Task 4: Extract Archive on Remote System

### Step 1: SSH into remote

```bash
ssh user@192.168.56.10
```

### Step 2: Extract archive

```bash
mkdir -p ~/extracted-data
tar -xzf logs-backup.tar.gz -C ~/extracted-data/
```

### Step 3: Verify contents

```bash
ls ~/extracted-data/lab-data/logs
```

---

## 🧪 Bonus Challenge: Verify Archive Integrity

### Step 1: Generate checksum before transfer

```bash
sha256sum logs-backup.tar.gz > logs-backup.tar.gz.sha256
```

### Step 2: Transfer both files:

```bash
scp logs-backup.tar.gz logs-backup.tar.gz.sha256 user@192.168.56.10:/home/user/
```

### Step 3: On remote, verify:

```bash
sha256sum -c logs-backup.tar.gz.sha256
```

> ✅ Output should be:

```text
logs-backup.tar.gz: OK
```

---

## 📝 Lab Report Template

```text
📁 Archive Created: logs-backup.tar.gz
📂 Archived Content: ~/lab-data/logs/log1.txt, log2.txt
🗜️ Compression: gzip via tar
📤 Transferred with:
  - [x] scp
  - [x] rsync (to /home/user/backup/)
📥 Archive Extracted: /home/user/extracted-data/
📋 Files Verified on Remote: ✅ Yes
🔒 SHA256 Integrity Check: ✅ Passed
```

---

## 📌 Key Takeaways

* Use `tar -czf` to archive and compress directories
* Use `scp` for simple transfers, and `rsync` for smarter syncing
* Always **verify transfer integrity** using checksums like SHA-256
* Archive before transfer to group files and reduce size
* Avoid transferring sensitive files in raw format — always encrypt or package securely

---

Would you like:

* 📜 A **Bash script** that automates archive, checksum, and transfer?
* 🧪 A **cybersecurity challenge** involving detecting tampered archives?
* 📅 A **cron-based backup + transfer task**?

Let me know — and I’m ready for your next topic!
