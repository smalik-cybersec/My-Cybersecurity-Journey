Great, Shahid! You're now moving into the **modern Linux logging system** used by most current distributions like Ubuntu, Fedora, and Arch:

> **Lesson:** Review System Journal Entries
> **Page Ref:** \~353
> **Goal:** Learn how to use `journalctl` to review system logs managed by `systemd-journald` — essential for real-time log analysis, troubleshooting, and incident response.

---

# 📘 Review System Journal Entries

## 📌 Chapter Overview

Linux systems that use **`systemd`** rely on `journald` to collect and store logs in a binary format. The **`journalctl`** command lets you filter, review, and analyze these logs for system activity, authentication, service failures, kernel messages, and more.

> 🎯 **Objective:** Understand how to query, filter, and analyze system journal logs using `journalctl`.

---

## 📚 Table of Contents

- [📘 Review System Journal Entries](#-review-system-journal-entries)
  - [📌 Chapter Overview](#-chapter-overview)
  - [📚 Table of Contents](#-table-of-contents)
  - [1️⃣ What Is `systemd-journald`?](#1️⃣-what-is-systemd-journald)
  - [2️⃣ Where Journal Logs Are Stored](#2️⃣-where-journal-logs-are-stored)
  - [3️⃣ Basic `journalctl` Commands](#3️⃣-basic-journalctl-commands)
  - [4️⃣ Filtering Journal Logs](#4️⃣-filtering-journal-logs)
    - [🔍 By Time](#-by-time)
    - [🔍 By Service](#-by-service)
    - [🔍 By Priority Level](#-by-priority-level)
    - [🔍 Grep-like Search](#-grep-like-search)
  - [5️⃣ Persistent vs Volatile Logs](#5️⃣-persistent-vs-volatile-logs)
  - [6️⃣ 🧪 Guided Practice Exercises](#6️⃣--guided-practice-exercises)
    - [🧪 Exercise 1: View Boot Logs](#-exercise-1-view-boot-logs)
    - [🧪 Exercise 2: View SSH Logs Only](#-exercise-2-view-ssh-logs-only)
    - [🧪 Exercise 3: Find Kernel Boot Errors](#-exercise-3-find-kernel-boot-errors)
    - [🧪 Exercise 4: Monitor Live System Logs](#-exercise-4-monitor-live-system-logs)
    - [🧪 Exercise 5: View Logs from Yesterday](#-exercise-5-view-logs-from-yesterday)
  - [7️⃣ 📁 GitHub Documentation Layout](#7️⃣--github-documentation-layout)
  - [8️⃣ 🧠 Quiz \& Knowledge Check](#8️⃣--quiz--knowledge-check)
  - [9️⃣ ✅ Summary](#9️⃣--summary)

---

## 1️⃣ What Is `systemd-journald`?

* **`journald`** is the system logging component of `systemd`.
* It **collects logs** from:

  * Kernel
  * System services (via stdout/stderr)
  * Syslog
  * Init processes
* Logs are **stored in binary format** (not plain text like `/var/log/syslog`).

---

## 2️⃣ Where Journal Logs Are Stored

| Type       | Path                | Volatile/Persistent          |
| ---------- | ------------------- | ---------------------------- |
| Runtime    | `/run/log/journal/` | Volatile (cleared on reboot) |
| Persistent | `/var/log/journal/` | Stored across reboots        |

🔧 To enable persistent logging:

```bash
sudo mkdir -p /var/log/journal
sudo systemd-tmpfiles --create --prefix /var/log/journal
sudo systemctl restart systemd-journald
```

---

## 3️⃣ Basic `journalctl` Commands

| Task                     | Command                 |
| ------------------------ | ----------------------- |
| View all logs            | `journalctl`            |
| Newest logs first        | `journalctl -r`         |
| Follow logs live         | `journalctl -f`         |
| View logs since boot     | `journalctl -b`         |
| View logs from a service | `journalctl -u ssh`     |
| View kernel logs         | `journalctl -k`         |
| Filter by user (`UID`)   | `journalctl _UID=1000`  |
| Export logs to text file | `journalctl > logs.txt` |

---

## 4️⃣ Filtering Journal Logs

### 🔍 By Time

```bash
journalctl --since "1 hour ago"
journalctl --since "2025-07-12 10:00" --until "2025-07-12 13:00"
```

---

### 🔍 By Service

```bash
journalctl -u ssh.service
journalctl -u apache2.service --since today
```

---

### 🔍 By Priority Level

| Priority Name | Number | Description             |
| ------------- | ------ | ----------------------- |
| emerg         | 0      | System unusable         |
| alert         | 1      | Immediate action needed |
| crit          | 2      | Critical condition      |
| err           | 3      | Error condition         |
| warning       | 4      | Warning condition       |
| notice        | 5      | Normal but significant  |
| info          | 6      | Informational messages  |
| debug         | 7      | Debugging messages      |

```bash
journalctl -p err
journalctl -p warning -b
```

---

### 🔍 Grep-like Search

```bash
journalctl | grep sshd
```

---

## 5️⃣ Persistent vs Volatile Logs

| Feature                | Volatile Logs             | Persistent Logs              |
| ---------------------- | ------------------------- | ---------------------------- |
| Stored in              | `/run/log/journal/`       | `/var/log/journal/`          |
| Retained after reboot? | ❌ No                      | ✅ Yes                        |
| Use case               | Debugging current session | Long-term monitoring, audits |

---

## 6️⃣ 🧪 Guided Practice Exercises

---

### 🧪 Exercise 1: View Boot Logs

```bash
journalctl -b
```

✔️ Shows logs from the current boot session.

---

### 🧪 Exercise 2: View SSH Logs Only

```bash
journalctl -u ssh
```

✔️ Great for spotting failed login attempts, key logins, restarts.

---

### 🧪 Exercise 3: Find Kernel Boot Errors

```bash
journalctl -k -p err
```

✔️ Filters only critical kernel errors.

---

### 🧪 Exercise 4: Monitor Live System Logs

```bash
journalctl -f
```

> Then open another terminal and trigger activity (e.g., login, restart ssh).

---

### 🧪 Exercise 5: View Logs from Yesterday

```bash
journalctl --since "yesterday" --until "today"
```

---

## 7️⃣ 📁 GitHub Documentation Layout

```
/Review-Journal-Entries/
├── README.md
├── commands/
│   └── journalctl_filters.sh
├── examples/
│   ├── ssh_logins.txt
│   └── boot_errors.txt
├── screenshots/
├── logs/
│   └── full_journal_export.txt
```

---

## 8️⃣ 🧠 Quiz & Knowledge Check

**Q1.** Which command shows all logs from the most recent boot?
→ `journalctl -b`

**Q2.** Where are persistent journal logs stored?
→ `/var/log/journal/`

**Q3.** What does `journalctl -u ssh` show?
→ Logs related to the SSH service only

**Q4.** How do you follow the live stream of logs?
→ `journalctl -f`

**Q5.** How do you view only error-level messages?
→ `journalctl -p err`

---

## 9️⃣ ✅ Summary

You’ve now learned how to:

* Understand and work with `systemd-journald` logs
* Use `journalctl` for filtering and analysis
* Monitor services, sessions, and errors
* Enable persistent logging for forensic use

> 🔍 **Mastering `journalctl` is critical for system health monitoring, incident detection, and audit trail analysis.**

---

Would you like a:

* 📄 Markdown or PDF export?
* 🧪 Guided lab scenario simulating log analysis?
* 🧠 Quiz for this topic?

Let’s keep building your cybersecurity expertise, Shahid — just give the word for the next lesson.
