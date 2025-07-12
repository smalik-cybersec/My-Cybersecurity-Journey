Here is your complete **Guided Exercise** for:

---

# 🎯 Guided Exercise: **Synchronize Files Between Systems Securely with rsync**

> 🔐 **Objective**: Practice using `rsync` over SSH to securely and efficiently synchronize files and directories between two Linux systems.
> 🧠 **Skill Level**: Beginner → Intermediate
> 🔒 **Cybersecurity Relevance**: Ensures **confidential**, **authenticated**, and **tamper-resistant** file transfers — critical in secure backups, log collection, configuration syncing, and forensic evidence handling.

---

## 🧭 Table of Contents

- [🎯 Guided Exercise: **Synchronize Files Between Systems Securely with rsync**](#-guided-exercise-synchronize-files-between-systems-securely-with-rsync)
  - [🧭 Table of Contents](#-table-of-contents)
  - [📘 Learning Objectives](#-learning-objectives)
  - [🧰 Requirements](#-requirements)
  - [📦 Lab Environment](#-lab-environment)
  - [✅ Task 1: Sync a Local Directory to Remote](#-task-1-sync-a-local-directory-to-remote)
    - [Step 1: Create local files](#step-1-create-local-files)
    - [Step 2: Use rsync to sync with remote](#step-2-use-rsync-to-sync-with-remote)
    - [Step 3: SSH into remote and verify](#step-3-ssh-into-remote-and-verify)
  - [✅ Task 2: Sync Files from Remote to Local](#-task-2-sync-files-from-remote-to-local)
    - [Step 1: Create a file on the remote system:](#step-1-create-a-file-on-the-remote-system)
    - [Step 2: Sync to local:](#step-2-sync-to-local)
  - [✅ Task 3: Use Exclude Patterns in rsync](#-task-3-use-exclude-patterns-in-rsync)
    - [Step 1: Add junk files locally](#step-1-add-junk-files-locally)
    - [Step 2: Sync excluding `.log` and `.bak`:](#step-2-sync-excluding-log-and-bak)
    - [Step 3: SSH into remote and confirm exclusions:](#step-3-ssh-into-remote-and-confirm-exclusions)
  - [✅ Task 4: Test rsync with `--delete` Option](#-task-4-test-rsync-with---delete-option)
    - [Step 1: Create a file only on remote:](#step-1-create-a-file-only-on-remote)
    - [Step 2: Sync from local to remote with `--delete`:](#step-2-sync-from-local-to-remote-with---delete)
    - [Step 3: Confirm file was deleted:](#step-3-confirm-file-was-deleted)
  - [🧪 Bonus Challenge: Automate Secure Backup with rsync](#-bonus-challenge-automate-secure-backup-with-rsync)
  - [📝 Lab Report Template](#-lab-report-template)

---

## 📘 Learning Objectives

By the end of this guided lab, you will be able to:

* Use `rsync` to securely transfer files over SSH
* Preserve file structure, permissions, and metadata
* Exclude unwanted files or patterns from syncing
* Test advanced flags like `--delete` and `--progress`
* Think critically about secure, scriptable file operations

---

## 🧰 Requirements

| Requirement | Description                                         |
| ----------- | --------------------------------------------------- |
| Systems     | Two Linux machines or VMs (one local, one remote)   |
| Access      | SSH access between the machines (`ssh user@remote`) |
| Tools       | `rsync`, `ssh`, and basic terminal utilities        |

---

## 📦 Lab Environment

Assume the following setup:

* **Local system**: `user@local`
* **Remote system**: `user@192.168.56.10`
* SSH access is available and working
* All commands run from the **local machine**

---

## ✅ Task 1: Sync a Local Directory to Remote

### Step 1: Create local files

```bash
mkdir ~/rsync-lab
echo "Hello from local machine" > ~/rsync-lab/welcome.txt
```

### Step 2: Use rsync to sync with remote

```bash
rsync -avz -e ssh ~/rsync-lab/ user@192.168.56.10:/home/user/rsync-lab/
```

### Step 3: SSH into remote and verify

```bash
ssh user@192.168.56.10
ls /home/user/rsync-lab
```

---

## ✅ Task 2: Sync Files from Remote to Local

### Step 1: Create a file on the remote system:

```bash
ssh user@192.168.56.10 "echo 'Synced from remote' > /home/user/rsync-lab/remote.txt"
```

### Step 2: Sync to local:

```bash
rsync -avz -e ssh user@192.168.56.10:/home/user/rsync-lab/ ~/rsync-pull/
```

---

## ✅ Task 3: Use Exclude Patterns in rsync

### Step 1: Add junk files locally

```bash
touch ~/rsync-lab/debug.log ~/rsync-lab/temp.bak
```

### Step 2: Sync excluding `.log` and `.bak`:

```bash
rsync -avz --exclude='*.log' --exclude='*.bak' -e ssh ~/rsync-lab/ user@192.168.56.10:/home/user/rsync-clean/
```

### Step 3: SSH into remote and confirm exclusions:

```bash
ssh user@192.168.56.10
ls /home/user/rsync-clean
```

---

## ✅ Task 4: Test rsync with `--delete` Option

> ⚠️ This removes files from the destination **not present in the source**

### Step 1: Create a file only on remote:

```bash
ssh user@192.168.56.10 "echo 'This will be deleted' > /home/user/rsync-lab/delete-me.txt"
```

### Step 2: Sync from local to remote with `--delete`:

```bash
rsync -avz --delete -e ssh ~/rsync-lab/ user@192.168.56.10:/home/user/rsync-lab/
```

### Step 3: Confirm file was deleted:

```bash
ssh user@192.168.56.10 "ls /home/user/rsync-lab"
```

---

## 🧪 Bonus Challenge: Automate Secure Backup with rsync

Create a simple backup script:

```bash
nano ~/backup-configs.sh
```

```bash
#!/bin/bash
rsync -az -e ssh /etc/ user@192.168.56.10:/home/user/system-backups/etc/
```

Make it executable:

```bash
chmod +x ~/backup-configs.sh
```

Run the script:

```bash
./backup-configs.sh
```

Optional: Add to `crontab` for daily automated sync.

---

## 📝 Lab Report Template

```text
🔁 rsync Source: ~/rsync-lab/
📡 Remote Target: user@192.168.56.10:/home/user/rsync-lab/

✅ Tasks Completed:
- [x] Local → Remote sync
- [x] Remote → Local sync
- [x] Used `--exclude` patterns
- [x] Used `--delete` safely
- [x] Created & ran rsync backup script

🗃️ Files Synced: welcome.txt, remote.txt
🚫 Files Excluded: debug.log, temp.bak
⚠️ Files Deleted on Remote: delete-me.txt (via `--delete`)
```

---

Would you like:

* 📜 A **template rsync script** with email alerts and logging?
* 🧪 A **forensic scenario** where evidence files must be securely mirrored?
* 📅 A **cron-based automation guide** with rotating backups?

Let me know — ready for your next topic!
