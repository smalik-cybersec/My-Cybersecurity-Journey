Perfect, Shahid.
Here is the **Cybersecurity Documentation Protocol Ultra v5.0 — Master Grade Edition** documentation for:

# 🧪 **Guided Exercise: Transfer Files Between Systems Securely**

## *Module 13 – Archive and Transfer Files*

## 🔰 Introduction

This hands-on guided exercise strengthens your **practical command over secure file transfer tools** like `scp`, `rsync`, and `sftp` on **RHEL systems**. You'll simulate:

* Admin-to-server backup transfers
* Peer-to-peer file copying
* Detection logic and Red/Blue scenarios using MITRE ATT\&CK

> 🎯 *Goal*: Gain confidence in using secure file transfer tools in real-world administrative and adversarial scenarios.

---

## 🧠 Core Recap (Quick Reference Table)

| Tool    | Key Use       | Protocol | Resume Support | Recursive |
| ------- | ------------- | -------- | -------------- | --------- |
| `scp`   | Fast transfer | SSH      | ❌              | ✅         |
| `rsync` | Smart sync    | SSH      | ✅              | ✅         |
| `sftp`  | Interactive   | SSH      | ✅              | ✅         |

---

## 🧪 Guided Lab Steps (Real-World Workflow, RHEL Verified)

### 🖥️ Prerequisites (on both systems)

* SSH service running:

  ```bash
  sudo systemctl enable --now sshd
  ```
* Firewall rule open for port 22 (if needed):

  ```bash
  sudo firewall-cmd --add-service=ssh --permanent && sudo firewall-cmd --reload
  ```

---

### 🔹 **Step 1: Use `scp` to Copy a File to a Remote System**

**On system A (your local RHEL box):**

```bash
echo "confidential test data" > ~/secret.txt
scp ~/secret.txt user@192.168.1.100:/tmp/
```

✅ **Verify** on remote (system B):

```bash
ssh user@192.168.1.100 "ls -l /tmp/secret.txt"
```

---

### 🔹 **Step 2: Use `scp` to Download a Directory from a Remote System**

**From system A:**

```bash
scp -r user@192.168.1.100:/etc/ssh ~/ssh_backup
```

✅ Inspect folder:

```bash
ls ~/ssh_backup
```

---

### 🔹 **Step 3: Use `rsync` for Efficient Directory Sync**

```bash
mkdir -p ~/backup_data/
rsync -avz ~/ssh_backup/ user@192.168.1.110:/mnt/backups/ssh/
```

✅ Output will show each file transferred.

---

### 🔹 **Step 4: Use `sftp` for Interactive Transfer**

```bash
sftp user@192.168.1.100
```

Inside session:

```sftp
cd /tmp
put ~/secret.txt
ls
get secret.txt
exit
```

✅ Confirm both upload and download succeeded.

---

### 🔹 **Step 5: Automate Daily rsync with Cron**

Create a script:

```bash
nano ~/scripts/daily_rsync.sh
```

```bash
#!/bin/bash
rsync -az /var/www/ user@192.168.1.110:/mnt/web_backup/
```

Make executable:

```bash
chmod +x ~/scripts/daily_rsync.sh
```

Schedule:

```bash
crontab -e
0 1 * * * ~/scripts/daily_rsync.sh
```

---

### 🔹 **Step 6: Simulate Red Team File Drop (MITRE T1105)**

```bash
scp exploit.tar.gz reduser@192.168.1.222:/tmp/
```

✅ This simulates an adversary transferring a payload to a compromised host.

---

### 🔹 **Step 7: Simulate Blue Team Detection (Auditd)**

```bash
sudo auditctl -w /usr/bin/scp -p x -k scp-monitor
```

Trigger an `scp` transfer and check logs:

```bash
ausearch -k scp-monitor
```

✅ Blue team can now detect file movement via `scp`.

---

## 🛡 Red/Blue Team Reflection Table

| Team    | Tool Used         | MITRE ID                      | Defensive Idea                         |
| ------- | ----------------- | ----------------------------- | -------------------------------------- |
| 🔴 Red  | `scp`, `rsync`    | T1105 (Ingress Tool Transfer) | Auditd + SIEM alert                    |
| 🔵 Blue | Auditd, cron logs | N/A                           | File integrity + behavioral monitoring |

---

## 🧠 Quiz Checkpoint

1. How would you recursively copy a directory using `scp`?
2. What flag ensures `rsync` compresses data during transfer?
3. What is the MITRE technique ID for tool transfer via `scp`?
4. How do you detect secure file transfers on a Linux system?

---

## 📓 Journaling + Reflection

* 🗓️ *Date Completed*: `__________`
* ✅ *Did you use all 3 tools?* Yes / No
* ❓ *What surprised or confused you?*
  `_________________________________________`
* 🔐 *Red/Blue simulation notes*:
  `_________________________________________`
* 🎯 *Confidence Level (1–5)*: `__`

---

## 🗂 Summary Checklist

| Task                   | Command                          |
| ---------------------- | -------------------------------- |
| Transfer file (scp)    | `scp file user@ip:/path/`        |
| Sync directory (rsync) | `rsync -avz src/ user@ip:/dest/` |
| Upload file (sftp)     | `sftp > put file`                |
| Detect transfer        | `auditctl -w /usr/bin/scp ...`   |
| Automate rsync         | `cron + bash`                    |

---

## 🧭 Job Role & Certification Mapping

| Role        | Real-World Task                          | Certification |
| ----------- | ---------------------------------------- | ------------- |
| SOC Analyst | Detect SCP exfiltration attempts         | CEH, CySA+    |
| Linux Admin | Set up secure backup jobs                | RHCSA         |
| Pentester   | Deliver payloads to test systems         | OSCP          |
| IR Analyst  | Review `scp`, `rsync` logs for anomalies | GCFA          |

---

## 🧠 Spaced Repetition Plan

* **Day 1**: Run all commands (`scp`, `rsync`, `sftp`) manually
* **Day 3**: Automate daily `rsync` backups
* **Day 7**: Simulate Red/Blue scenario with logging
* **Day 30**: Teach it to a peer, or document detection rules in SOP

---

✅ **Completed: Guided Exercise — Transfer Files Between Systems Securely**

Let me know the **next lesson** in Module 13 and I’ll continue with the same v5.0 structure.
