## 📄 `Lesson11.03-Review-System-Journal-Entries-RHEL.md`

# 🧠 Linux Essentials – Module 11: Analyze and Store Logs

## Lesson 03: Review System Journal Entries

🎯 Focused on **Red Hat Enterprise Linux (RHEL)**

---

## 🎓 Introduction

Modern RHEL systems (7 and above) use **`systemd-journald`**, a binary-based logging system that captures all system logs in real-time and stores them in **structured journal entries**. Unlike plain-text syslog files, the journal allows powerful filtering and log correlation based on services, users, priorities, and time.

> 🧠 Think of `journald` as a time machine for logs: **queryable**, **filterable**, and **boot-aware**.

---

## 🔍 Core Concepts (Feynman + Visual)

### 📦 What is `systemd-journald`?

* It collects logs from:

  * The **kernel**
  * System **services**
  * **Standard output/error** of services
  * Syslog (via `/dev/log`)
* Stores logs in **binary format** in:

  ```bash
  /run/log/journal/  # volatile (RAM-based)
  /var/log/journal/  # persistent (if enabled)
  ```

---

### 🗂️ Key Features of Journal

| Feature               | Syslog | systemd-journald       |
| --------------------- | ------ | ---------------------- |
| Text-based logs       | ✅ Yes  | ❌ Binary (queryable)   |
| Per-service filtering | ❌ No   | ✅ Yes                  |
| Boot session tracking | ❌ No   | ✅ Yes (`--list-boots`) |
| Field-based search    | ❌ No   | ✅ Yes (`_PID`, `_UID`) |
| Retention management  | Manual | Automatic with limits  |

---

### 📊 Diagram: RHEL Logging Pipeline (Hybrid Logging)

```plaintext
[system services] → [systemd-journald] → 
      ↳ /run/log/journal/
      ↳ /var/log/journal/  (persistent)
      ↳ /dev/log → rsyslog → /var/log/messages, etc.
```

> 💡 RHEL systems run both `journald` and `rsyslog` together.

---

## 🧪 Guided Lab – Hands-On with Journal Logs (RHEL)

---

### ✅ Step 1: View Latest Journal Entries

```bash
# Show the most recent logs
sudo journalctl -n 50
```

---

### ✅ Step 2: View Boot Logs

```bash
# View logs from current boot
sudo journalctl -b

# Show boots and their IDs
sudo journalctl --list-boots

# View logs from a previous boot (index -1)
sudo journalctl -b -1
```

---

### ✅ Step 3: Filter Logs by Unit, PID, Priority

```bash
# View SSH logs only
sudo journalctl -u sshd

# View sudo-related logs
sudo journalctl _COMM=sudo

# Show kernel messages only
sudo journalctl -k

# Show only "error" level and above
sudo journalctl -p err..alert
```

🧠 `-p` levels:

```
0: emerg     🔥
1: alert
2: crit
3: err       ❗
4: warning
5: notice
6: info
7: debug
```

---

### ✅ Step 4: View Logs by Time

```bash
# Logs from today
sudo journalctl --since today

# Logs from last 2 hours
sudo journalctl --since "2 hours ago"

# Logs between a date range
sudo journalctl --since "2024-06-01" --until "2024-06-30"
```

---

### ✅ Step 5: Inject & Search Custom Journal Entry

```bash
# Inject a log entry
logger -p user.info "🧪 Shahid tested systemd-journal logging in RHEL."

# Search for it
sudo journalctl | grep "Shahid"
```

---

## 🔴 Red Team Simulation: Bypass Journald Logging

| Technique         | Example                                                        |
| ----------------- | -------------------------------------------------------------- |
| Run from memory   | Use in-memory shells (bypasses journald stdout)                |
| Clear journal     | `sudo journalctl --rotate && sudo journalctl --vacuum-time=1s` |
| Modify timestamps | Use `faketime` to mislead logging                              |
| Disable journald  | `systemctl stop systemd-journald` (🛑 dangerous)               |

---

## 🔵 Blue Team Defense: Detect Journal Evasion

| Event                      | Detection Strategy                                               |
| -------------------------- | ---------------------------------------------------------------- |
| Journal rotation or vacuum | Alert if `--vacuum-*` is triggered                               |
| Journal corruption         | SIEM alert + hash comparison                                     |
| Unexpected shutdowns       | Check boots with `--list-boots`                                  |
| Missing log gaps           | Correlate with `/var/log/messages` or `/var/log/audit/audit.log` |

---

## 📘 Quiz – System Journal

**Q1.** What command lists logs from the current boot session?
A. `cat /var/log/boot.log`
B. `journalctl -b` ✅
C. `journalctl -k`
D. `last`

---

**Q2.** Where does journald store persistent logs (RHEL)?
A. `/var/log/journal/` ✅
B. `/etc/systemd/journal/`
C. `/var/log/syslog/`
D. `/usr/lib/journal/`

---

**Q3.** Which command shows logs only from the `sshd` service?
A. `journalctl -u sshd` ✅
B. `grep sshd /var/log/messages`
C. `journalctl --sshd`
D. `systemctl logs sshd`

---

## 📊 Summary Table + Checklist

| ✅ Task                                  | Done? |
| --------------------------------------- | ----- |
| Explored journald vs syslog differences | ☐     |
| Viewed journal logs by boot & time      | ☐     |
| Filtered logs by service and priority   | ☐     |
| Simulated log injection                 | ☐     |
| Mapped Red/Blue detection logic         | ☐     |

---

## 📘 Journaling & Reflection

* What can `journald` do that `syslog` cannot?
* Why is journald useful in forensic triage?
* What happens if journald is disabled?

📈 **Confidence (1–10):** `___`
🧠 **Still unclear:** `___`
🛠️ **Next task to practice:** `___`

---

## 💼 Job & Cert Mapping

| Role        | Relevance                             |
| ----------- | ------------------------------------- |
| SOC Analyst | Real-time log triage & alert building |
| IR Analyst  | Boot tracking & session logging       |
| Linux Admin | Monitoring systemd failures           |

| Certification  | Module Link                       |
| -------------- | --------------------------------- |
| RHCSA/RHCE     | `journalctl`, `systemctl` logging |
| CompTIA Linux+ | Logging, uptime, and alerting     |
| CEH/OSCP       | Log tampering & detection         |

---

## ⏳ Revision Schedule

| Day | Focus                                        |
| --- | -------------------------------------------- |
| 1   | Practice `journalctl` filters                |
| 3   | Simulate service crash & review logs         |
| 7   | Investigate past boots with `-b`             |
| 30  | Write shell script to monitor journal errors |

---
