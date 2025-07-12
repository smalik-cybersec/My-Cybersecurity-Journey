Awesome, Shahid!
Now let’s turn theory into hands-on mastery with a **Guided Exercise** focused on:

> **Guided Exercise:** Review Syslog Files
> **Page Ref:** \~351
> **Objective:** Learn to search, filter, and interpret Linux system log files to identify system events, failed logins, and security-relevant activities.

This is designed as a **real-world analyst-style log review task**, like what you'd do in a SOC environment or during a forensic investigation.

---

# 🧪 Guided Exercise: Review Syslog Files

---

## 🎯 Objectives

* Locate and read Linux system log files
* Filter important security events (e.g., failed logins, sudo usage)
* Monitor logs in real-time
* Extract useful insights using commands like `grep`, `awk`, and `tail`

---

## 🛠️ Prerequisites

| Item                                              | Required   |
| ------------------------------------------------- | ---------- |
| Linux system (Debian/Ubuntu)                      | ✅          |
| SSH and sudo access                               | ✅          |
| Terminal utilities: `grep`, `tail`, `awk`, `less` | ✅ Built-in |

---

## 🧱 Scenario Setup

* **You are a SOC Tier 1 Analyst**
* A security alert flagged multiple failed login attempts from IP `192.168.1.55`
* You must investigate `auth.log`, `syslog`, and other files in `/var/log/`

---

## 📋 Exercise Steps

---

### ✅ Step 1: View All Files in `/var/log`

```bash
ls -lh /var/log
```

> Look for:
>
> * `auth.log`
> * `syslog`
> * `kern.log`
> * `ufw.log` (if firewall is enabled)

---

### ✅ Step 2: Review Authentication Logs

```bash
sudo less /var/log/auth.log
```

🔍 Look for entries like:

```
Failed password for invalid user admin from 192.168.1.55 port 50652
Accepted password for shahid from 192.168.1.12
sudo:   shahid : TTY=pts/0 ; PWD=/home/shahid ; COMMAND=/bin/apt update
```

---

### ✅ Step 3: Find All Failed SSH Logins

```bash
grep "Failed password" /var/log/auth.log
```

✔️ This helps detect brute-force or unauthorized login attempts.

---

### ✅ Step 4: Count Unique IPs in Failed Logins

```bash
grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr
```

✔️ Shows which IPs are attacking most frequently.

---

### ✅ Step 5: Review Sudo Command Usage

```bash
grep "sudo" /var/log/auth.log
```

> This shows commands executed with `sudo`—important for privilege abuse detection.

---

### ✅ Step 6: Monitor Live Log Activity

```bash
sudo tail -f /var/log/syslog
```

Then, in a second terminal, try:

```bash
ping google.com
```

✔️ Watch how your activity logs in real-time.

---

### ✅ Step 7: Search for Specific User Activity

```bash
grep "shahid" /var/log/auth.log
```

> Tracks login, sudo, and shell activity for the user `shahid`.

---

### ✅ Step 8: Review Kernel Logs (Optional)

```bash
less /var/log/kern.log
```

> Shows low-level kernel events like hardware errors or firewall module activity.

---

### ✅ Step 9: Search for Cron Job Execution

```bash
grep CRON /var/log/syslog
```

✔️ This helps detect scheduled task execution or malicious cron jobs.

---

## 📝 Optional Advanced Filters

| Command                                       | Purpose                          |                         |
| --------------------------------------------- | -------------------------------- | ----------------------- |
| `journalctl -xe`                              | View recent critical logs        |                         |
| `grep "Accepted publickey" /var/log/auth.log` | Find successful key-based logins |                         |
| `grep -i "segfault" /var/log/syslog`          | Detect crashes or program faults |                         |
| \`grep -E "(sshd                              | Failed)" /var/log/auth.log\`     | Multiple pattern search |

---

## 📂 Output Checklist

| Task                                    | Verified (✔/❌) |
| --------------------------------------- | -------------- |
| Found and opened `/var/log/auth.log`    |                |
| Detected failed logins via `grep`       |                |
| Identified top attacker IPs with `awk`  |                |
| Monitored real-time logs with `tail -f` |                |
| Checked sudo usage logs                 |                |
| Filtered logs by username               |                |

---

## 🧠 Reflective Questions

1. What patterns indicate a brute-force SSH attack?
2. How can you prove someone used `sudo` with malicious intent?
3. How can real-time monitoring help during an incident?

---

## 📁 GitHub-Style Folder (Optional)

```
/Review-Syslog-Files/
├── README.md
├── screenshots/
│   └── auth_log_analysis.png
├── logs/
│   └── filtered_authlog.txt
├── tools/
│   └── top_ips.sh
├── queries/
│   └── grep_filters.md
```

---

## ✅ Summary

You now know how to:

* Review and filter key Linux syslog files
* Detect brute-force and unauthorized access attempts
* Trace user actions like `sudo` or login
* Monitor logs in real-time during live incidents

> 🔍 **This skill is fundamental for SOC, incident response, and forensic analysis.**

---

Would you like:

* 📦 Markdown export?
* 💡 A mini Red Team scenario that hides its tracks in logs?
* 🎯 Next lesson or lab?

Let’s keep going, Shahid. You're doing great!
