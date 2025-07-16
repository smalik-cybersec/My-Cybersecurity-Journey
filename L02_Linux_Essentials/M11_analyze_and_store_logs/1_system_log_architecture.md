## 📁 `Lesson11.01-system_log_architecture.md`

# 🧠 Linux Essentials – Module 11: Analyze and Store Logs

## Lesson 01: Describe System Log Architecture

---

## 🎓 Introduction

In Linux, logs are the *eyes and ears* of the system administrator and cybersecurity professional. Understanding the **System Log Architecture** is essential for visibility, forensics, incident detection, and compliance.

This lesson covers how logging is handled in Linux — from **log producers (kernel, daemons)** to **log processors (rsyslog, journald)** and **log storage (plain text, structured logs)**.

---

## 🔍 Core Concepts (Feynman + Visual)

### 🧩 What is System Logging?

> **Feynman Analogy**: Think of logging as a digital diary where every action, warning, error, and success is automatically written down by your system so that a sysadmin or security analyst can "read the story" later.

### 🧱 Components of Linux Logging Architecture

| Layer              | Role                                       | Examples                            |
| ------------------ | ------------------------------------------ | ----------------------------------- |
| **Log Generators** | Produce logs                               | Kernel, systemd, applications, sshd |
| **Log Collectors** | Receive, format, filter logs               | `rsyslog`, `journald`               |
| **Log Storage**    | Save logs to disk or forward them remotely | `/var/log/`, Elasticsearch, SIEM    |
| **Log Viewers**    | Help users read logs                       | `journalctl`, `less`, `cat`         |

---

### 🗂️ Standard Log File Locations

| File                | Description                         |
| ------------------- | ----------------------------------- |
| `/var/log/messages` | Generic system logs (older distros) |
| `/var/log/syslog`   | System messages (Debian-based)      |
| `/var/log/auth.log` | Authentication logs                 |
| `/var/log/kern.log` | Kernel logs                         |
| `/var/log/secure`   | RHEL authentication logs            |
| `/var/log/dmesg`    | Boot-time kernel messages           |
| `/var/log/journal/` | Binary systemd journal logs         |

---

### 📊 Diagram: Linux System Log Architecture

```
[Kernel/Apps/Daemons] 
       ↓
 [systemd-journald] <--- system log buffer
       ↓
   ┌──────────────┐       ┌──────────────┐
   │   rsyslog    │─────► │ /var/log/*   │
   └──────────────┘       └──────────────┘
       ↓
   [Remote Syslog/SIEM]
```

---

## 🧪 Labs

### 🧑‍💻 Beginner Lab: View & Navigate Log Files

```bash
# See current system logs (Debian/Ubuntu)
cat /var/log/syslog

# View kernel messages
dmesg | less

# View journal logs (systemd)
journalctl

# Check SSH login logs
cat /var/log/auth.log | grep sshd
```

---

### ⚔️ Tactical Lab: Log Filtering with `journalctl`

```bash
# Show logs from today
journalctl --since today

# Show SSH login logs
journalctl _COMM=sshd

# Show logs for specific boot
journalctl -b -1
```

---

### 🔁 Simulation Lab: Inject + Monitor Log Events

1. **Generate a log**

   ```bash
   logger "Test log from Shahid's lab"
   ```

2. **Verify it was stored**

   ```bash
   grep 'Shahid' /var/log/syslog
   journalctl | grep 'Shahid'
   ```

---

## 🔴 Red Team Simulation: Log Evasion

| Tactic          | Technique                               | Command                                     |
| --------------- | --------------------------------------- | ------------------------------------------- |
| Clear logs      | `LogTampering [T1070.001]`              | `echo "" > /var/log/auth.log` *(🛑 Risky!)* |
| Hide commands   | Use `LD_PRELOAD`, Bash aliases          | `alias rm='echo safe'`                      |
| Run from memory | Fileless payloads (in-memory shellcode) | Advanced only                               |

---

## 🔵 Blue Team Detection: Log Tampering

| Indicator                    | Detection                      |
| ---------------------------- | ------------------------------ |
| Auth log suddenly empty      | SIEM alert: file size drop     |
| `logger` entries not present | journal audit comparison       |
| Missing historical boots     | `journalctl --list-boots` gaps |

Use file integrity monitoring (FIM) tools like:

* `aide`
* `osquery`
* `auditd`

---

## 📝 Quiz (MCQs)

1. **Which file stores authentication logs in Ubuntu?**
   A. `/var/log/messages`
   B. `/var/log/auth.log` ✅
   C. `/etc/logrotate.conf`
   D. `/var/journal/auth.log`

2. **What does the `journalctl -b` command do?**
   A. Clears journal logs
   B. Shows boot logs ✅
   C. Filters auth logs
   D. Shows only system crashes

3. **What is the default log directory on most Linux systems?**
   A. `/etc/logs/`
   B. `/usr/log/`
   C. `/var/log/` ✅
   D. `/log/`

---

## 📊 Summary Table + Checklist

| ✅ Task                                | Status |
| ------------------------------------- | ------ |
| Understood journald and rsyslog roles | ☐      |
| Navigated log files using journalctl  | ☐      |
| Generated test logs using `logger`    | ☐      |
| Simulated log tampering (safely)      | ☐      |
| Mapped MITRE techniques to log events | ☐      |

---

## 📘 Journaling + Confidence

* **What part of the system log pipeline do I feel most confident about today?**
* **Could I detect log deletion or tampering in a real system?**
* **Did I try both journald and syslog views of the logs?**

📈 **Confidence (1-10):** `___`
🕵️ **Today’s key takeaway:** `___`
🧠 **What I will revise next time:** `___`

---

## 💼 Job Role & Certification Mapping

| Role                 | Relevance                     |
| -------------------- | ----------------------------- |
| SOC Analyst (Tier 1) | Log review, incident triage   |
| System Administrator | Log rotation, uptime checking |
| Pentester (Red Team) | Evade/detect log traces       |

| Cert                   | Module Alignment          |
| ---------------------- | ------------------------- |
| **CompTIA Linux+**     | System log management     |
| **CEH**                | Log evasion, auditing     |
| **OSCP (buffer logs)** | Log analysis post-exploit |

---

## 🧠 Revision Plan (Spaced Repetition)

| Day        | Task                                                     |
| ---------- | -------------------------------------------------------- |
| **Day 1**  | Rewatch systemd-journald video, redo `journalctl` basics |
| **Day 3**  | Simulate tampering + test alerts                         |
| **Day 7**  | Read logs from `/var/log/` and `/var/log/journal/`       |
| **Day 30** | Create custom log parser shell script                    |

---

Shall we move on to **Lesson 02: Review Syslog Files** next, or would you like a deeper lab for this one first?

Let me know and I’ll generate the next Markdown module.
