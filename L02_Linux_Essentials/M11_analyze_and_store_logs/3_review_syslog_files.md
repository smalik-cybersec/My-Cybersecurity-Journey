Perfect, Shahid! You're now entering a **hands-on, investigative topic** that every SOC analyst, system administrator, and cybersecurity student must master:

> **Topic:** Review Syslog Files
> **Page Ref:** \~346
> **Goal:** Learn how to read, interpret, and investigate Linux syslog files for auditing, security monitoring, and incident response.

---

# 📘 Review Syslog Files

## 📌 Chapter Overview

Syslog files are the **primary source of truth** for almost every activity on a Linux system. From SSH logins and sudo attempts to kernel errors and cron job failures — **it’s all in the logs**.

> 🎯 **Objective:** Learn how to locate, understand, search, and analyze important syslog files on a Linux system.

---

## 📚 Table of Contents

- [📘 Review Syslog Files](#-review-syslog-files)
  - [📌 Chapter Overview](#-chapter-overview)
  - [📚 Table of Contents](#-table-of-contents)
  - [🧩 What Is Syslog?](#-what-is-syslog)
  - [📁 Location and Format of Syslog Files](#-location-and-format-of-syslog-files)
  - [📁 Important Log Files in `/var/log/`](#-important-log-files-in-varlog)
  - [👀 Reading and Interpreting Logs](#-reading-and-interpreting-logs)
    - [1. Use `less`, `cat`, `tail`:](#1-use-less-cat-tail)
    - [2. Watch logs in real-time:](#2-watch-logs-in-real-time)
    - [3. Understand a sample entry:](#3-understand-a-sample-entry)
  - [🔎 Filtering Logs with Tools](#-filtering-logs-with-tools)
    - [🔍 Basic Search](#-basic-search)
    - [🔍 Show failed login attempts by IP](#-show-failed-login-attempts-by-ip)
    - [🔍 Filter SSH Logins](#-filter-ssh-logins)
  - [🚨 Common Events \& Signatures to Watch For](#-common-events--signatures-to-watch-for)
  - [🧪 Lab: Investigate Real Logs](#-lab-investigate-real-logs)
    - [🔬 Task 1: Find All Failed SSH Attempts](#-task-1-find-all-failed-ssh-attempts)
    - [🔬 Task 2: Find All Successful Logins for User `shahid`](#-task-2-find-all-successful-logins-for-user-shahid)
    - [🔬 Task 3: Monitor Live Cron Activity](#-task-3-monitor-live-cron-activity)
    - [🔬 Task 4: Find All Sudo Commands Used Today](#-task-4-find-all-sudo-commands-used-today)
  - [🧠 Quiz \& Knowledge Check](#-quiz--knowledge-check)
  - [📁 GitHub-Ready Project Layout](#-github-ready-project-layout)
  - [🎯 Summary](#-summary)

---

## 🧩 What Is Syslog?

**Syslog** is both:

* A **standardized format** for log messages
* A **protocol** used to forward logs to local/remote systems

Syslog messages are **structured with 3 parts**:

```
<Priority> Timestamp Hostname Process: Message
```

Example:

```
Jul 12 14:12:34 server01 sshd[1023]: Failed password for invalid user root from 192.168.1.55 port 50652
```

---

## 📁 Location and Format of Syslog Files

All syslog-managed logs are located in:

```
/var/log/
```

These files are plain text and readable with any terminal tool (like `cat`, `less`, `tail`).

---

## 📁 Important Log Files in `/var/log/`

| File                | Description                                        |
| ------------------- | -------------------------------------------------- |
| `/var/log/syslog`   | General system messages (Debian/Ubuntu)            |
| `/var/log/messages` | General logs (Red Hat/CentOS)                      |
| `/var/log/auth.log` | Login attempts, sudo, SSH activity                 |
| `/var/log/kern.log` | Kernel-level messages                              |
| `/var/log/boot.log` | Boot sequence messages                             |
| `/var/log/dmesg`    | Hardware detection messages during boot            |
| `/var/log/cron.log` | Scheduled task executions                          |
| `/var/log/faillog`  | Failed user login attempts                         |
| `/var/log/dpkg.log` | Package installations/removals (Debian-based)      |
| `/var/log/apache2/` | Apache web server logs (`access.log`, `error.log`) |
| `/var/log/ufw.log`  | UFW firewall activity log (if enabled)             |

---

## 👀 Reading and Interpreting Logs

### 1. Use `less`, `cat`, `tail`:

```bash
less /var/log/syslog
cat /var/log/auth.log
tail -f /var/log/auth.log
```

### 2. Watch logs in real-time:

```bash
sudo tail -f /var/log/syslog
```

### 3. Understand a sample entry:

```
Jul 12 13:10:22 ubuntu sshd[1433]: Accepted publickey for shahid from 192.168.1.12 port 52914 ssh2
```

Breakdown:

* `Jul 12 13:10:22`: Timestamp
* `ubuntu`: Hostname
* `sshd[1433]`: Process and PID
* `Accepted publickey for shahid`: Login success
* `from 192.168.1.12`: Source IP
* `ssh2`: Protocol

---

## 🔎 Filtering Logs with Tools

### 🔍 Basic Search

```bash
grep "Failed" /var/log/auth.log
```

### 🔍 Show failed login attempts by IP

```bash
grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr
```

### 🔍 Filter SSH Logins

```bash
grep "sshd" /var/log/auth.log
```

---

## 🚨 Common Events & Signatures to Watch For

| Event Type           | Log File            | What to Look For                  |
| -------------------- | ------------------- | --------------------------------- |
| Failed SSH login     | `/var/log/auth.log` | `Failed password for`             |
| Successful SSH login | `/var/log/auth.log` | `Accepted password/publickey for` |
| Sudo usage           | `/var/log/auth.log` | `sudo:` or `COMMAND=`             |
| Cron job execution   | `/var/log/cron.log` | Specific job command timestamps   |
| Kernel panic         | `/var/log/kern.log` | `panic:` or `stack trace`         |
| Firewall block (UFW) | `/var/log/ufw.log`  | `BLOCK IN` or `BLOCK OUT`         |

---

## 🧪 Lab: Investigate Real Logs

### 🔬 Task 1: Find All Failed SSH Attempts

```bash
grep "Failed password" /var/log/auth.log
```

### 🔬 Task 2: Find All Successful Logins for User `shahid`

```bash
grep "Accepted" /var/log/auth.log | grep "shahid"
```

### 🔬 Task 3: Monitor Live Cron Activity

```bash
sudo tail -f /var/log/cron.log
```

### 🔬 Task 4: Find All Sudo Commands Used Today

```bash
grep "sudo" /var/log/auth.log | grep "$(date '+%b %e')"
```

---

## 🧠 Quiz & Knowledge Check

**Q1.** Which file contains general system activity logs in Debian-based systems?
→ `/var/log/syslog`

**Q2.** What does this mean:
`Failed password for invalid user admin from 10.0.0.1 port 55923 ssh2`
→ Someone tried (and failed) to SSH into the system using the "admin" user.

**Q3.** How do you view real-time authentication logs?
→ `sudo tail -f /var/log/auth.log`

**Q4.** What tool helps you find unique IPs in brute-force logs?
→ `awk`, `uniq`, `sort`

**Q5.** What log file would show a successful use of `sudo`?
→ `/var/log/auth.log`

---

## 📁 GitHub-Ready Project Layout

```
/Syslog-Review/
├── README.md
├── commands/
│   └── log_queries.sh
├── examples/
│   ├── authlog_failed_entries.txt
│   ├── successful_ssh_sessions.txt
├── screenshots/
│   └── sudo_logins.png
├── tools/
│   └── log_parser.awk
```

---

## 🎯 Summary

You’ve learned how to:

* Locate and identify key log files
* Use command-line tools to read and filter logs
* Detect brute-force and login activity
* Investigate cron jobs, sudo usage, and system events

> 📌 **Log review is a key daily task in cybersecurity operations and forensics.**

---

Would you like to:

* 📦 Export this as Markdown or PDF?
* 💡 Get a **Red Team simulation** (e.g., attacker hides in logs)?
* 📊 Visual cheat sheet of log types?

I'm ready for the **next command**, Shahid.
