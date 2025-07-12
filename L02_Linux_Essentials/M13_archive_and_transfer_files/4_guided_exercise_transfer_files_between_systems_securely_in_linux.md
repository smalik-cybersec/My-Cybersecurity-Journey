Here is your complete **Guided Exercise** for:

---

# 🎯 Guided Exercise: **Transfer Files Between Systems Securely in Linux**

> 🔐 **Objective**: Gain hands-on experience using `scp`, `rsync`, and `sftp` to securely transfer files between Linux systems using SSH.
> 🧠 **Skill Level**: Beginner → Intermediate
> 🔒 **Cybersecurity Relevance**: Secure file transfer is essential for handling sensitive data, conducting audits, collecting evidence, and deploying configurations.

---

## 🧭 Table of Contents

- [🎯 Guided Exercise: **Transfer Files Between Systems Securely in Linux**](#-guided-exercise-transfer-files-between-systems-securely-in-linux)
  - [🧭 Table of Contents](#-table-of-contents)
  - [📘 Learning Outcomes](#-learning-outcomes)
  - [🧰 Requirements](#-requirements)
  - [📦 Lab Setup](#-lab-setup)
  - [✅ Task 1: Transfer a File Using `scp`](#-task-1-transfer-a-file-using-scp)
    - [🔹 On local system, create a test file:](#-on-local-system-create-a-test-file)
    - [📤 Copy file to remote:](#-copy-file-to-remote)
    - [📥 Copy file back to local (rename to avoid conflict):](#-copy-file-back-to-local-rename-to-avoid-conflict)
  - [✅ Task 2: Transfer a Directory Recursively](#-task-2-transfer-a-directory-recursively)
    - [📁 Create a test folder with files:](#-create-a-test-folder-with-files)
    - [📤 Transfer entire folder:](#-transfer-entire-folder)
    - [✅ Confirm on remote:](#-confirm-on-remote)
  - [✅ Task 3: Use `rsync` for Efficient Syncing](#-task-3-use-rsync-for-efficient-syncing)
    - [🔁 Sync reports folder to remote:](#-sync-reports-folder-to-remote)
    - [📥 Sync back to local:](#-sync-back-to-local)
  - [✅ Task 4: Use `sftp` for Interactive Transfers](#-task-4-use-sftp-for-interactive-transfers)
    - [🔐 Start secure FTP session:](#-start-secure-ftp-session)
    - [🔽 Download a file:](#-download-a-file)
    - [🔼 Upload a file:](#-upload-a-file)
    - [📂 Navigate:](#-navigate)
    - [❌ Exit:](#-exit)
  - [🧪 Optional Challenge: Backup \& Restore a Directory](#-optional-challenge-backup--restore-a-directory)
  - [📝 Lab Report Template](#-lab-report-template)

---

## 📘 Learning Outcomes

After completing this lab, you will be able to:

* Use `scp` to securely copy files and directories over SSH
* Use `rsync` to sync data efficiently between systems
* Use `sftp` to interactively upload/download files
* Validate and troubleshoot SSH-based file transfers
* Apply best practices for secure file handling in Linux

---

## 🧰 Requirements

| Requirement | Description                                                         |
| ----------- | ------------------------------------------------------------------- |
| Systems     | 2 Linux systems (VMs or physical), with SSH enabled                 |
| User Access | User accounts with password or key-based SSH access                 |
| Tools       | `scp`, `rsync`, `sftp`, `ssh` (pre-installed on most Linux distros) |

---

## 📦 Lab Setup

Assume the following:

* **Local system**: `user@local`
* **Remote system**: `user@192.168.56.10`
* Both systems are on the same network
* Remote system has SSH running:

  ```bash
  sudo systemctl status ssh
  ```

---

## ✅ Task 1: Transfer a File Using `scp`

### 🔹 On local system, create a test file:

```bash
echo "Confidential lab data" > secret.txt
```

### 📤 Copy file to remote:

```bash
scp secret.txt user@192.168.56.10:/home/user/
```

### 📥 Copy file back to local (rename to avoid conflict):

```bash
scp user@192.168.56.10:/home/user/secret.txt ./secret_copy.txt
```

---

## ✅ Task 2: Transfer a Directory Recursively

### 📁 Create a test folder with files:

```bash
mkdir reports && touch reports/report{1..3}.txt
```

### 📤 Transfer entire folder:

```bash
scp -r reports user@192.168.56.10:/home/user/
```

### ✅ Confirm on remote:

```bash
ssh user@192.168.56.10
ls ~/reports
```

---

## ✅ Task 3: Use `rsync` for Efficient Syncing

### 🔁 Sync reports folder to remote:

```bash
rsync -avz -e ssh reports/ user@192.168.56.10:/home/user/reports/
```

> `-a`: archive, `-v`: verbose, `-z`: compress during transfer, `-e ssh`: use SSH

### 📥 Sync back to local:

```bash
rsync -avz -e ssh user@192.168.56.10:/home/user/reports/ reports-copy/
```

---

## ✅ Task 4: Use `sftp` for Interactive Transfers

### 🔐 Start secure FTP session:

```bash
sftp user@192.168.56.10
```

### 🔽 Download a file:

```sftp
get /home/user/secret.txt
```

### 🔼 Upload a file:

```sftp
put secret_copy.txt
```

### 📂 Navigate:

```sftp
ls
cd /home/user
lcd ~/Documents
```

### ❌ Exit:

```sftp
bye
```

---

## 🧪 Optional Challenge: Backup & Restore a Directory

1. On local machine:

```bash
tar -czf configs.tar.gz /etc/
scp configs.tar.gz user@192.168.56.10:/home/user/
```

2. On remote:

```bash
tar -xzf configs.tar.gz -C /tmp/recovered-configs/
```

> ✅ This simulates a secure config backup and restore.

---

## 📝 Lab Report Template

```text
🖥️ Remote IP: 192.168.56.10
🔐 Authentication: Password / SSH Key

✅ Tasks Performed:
- [x] Transferred file using `scp`
- [x] Transferred folder using `scp -r`
- [x] Synced directory with `rsync`
- [x] Used `sftp` interactively
- [x] Verified files on both systems

📁 Test Files:
- secret.txt
- reports/report1.txt, report2.txt, report3.txt

🔁 Compression Used: ✅ (rsync -z)
📦 Optional Task: Config backup with tar ✅
```

---

Would you like:

* 🛠️ A **script to automate secure backups** with rsync?
* 🔐 A **guide for setting up passwordless SSH** using key pairs?
* 🧪 A **lab where a file transfer is intercepted over insecure FTP** for a real-world warning?

Let me know and I’ll build it! Ready for your next topic.
