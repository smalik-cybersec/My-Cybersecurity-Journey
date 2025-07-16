## 📄 `Lab11.02-Guided-Exercise-Review-Syslog-Files-RHEL.md`

# 🧪 Guided Exercise – Review Syslog Files (RHEL Focused)

> 🎯 **Goal**: Gain hands-on experience with **system logs** in **RHEL**, using native tools like `rsyslog`, `logger`, and log files under `/var/log`.

---

## 🧭 Scenario

You're a **Junior SOC Analyst** at a company using **RHEL 9** systems. Your task is to:

* Understand how syslog works in RHEL
* Locate and review key system logs
* Monitor login activity and detect unauthorized attempts
* Inject and verify a test log message

---

## 🧱 Step-by-Step Lab Instructions

### ✅ Step 1: Confirm the Logging System

🔧 RHEL 7–9 uses both:

* `systemd-journald` (binary journal logs)
* `rsyslog` (writes plain text files in `/var/log`)

```bash
# Check if rsyslog is active
systemctl status rsyslog

# Check systemd journal service (always running)
systemctl status systemd-journald
```

➡️ Make sure `rsyslog` is active. If not:

```bash
sudo systemctl enable --now rsyslog
```

---

### ✅ Step 2: Explore Key Syslog Files on RHEL

```bash
# View general system activity
sudo less /var/log/messages

# View security/authentication logs (important for SOC work)
sudo less /var/log/secure

# View cron job logs
sudo less /var/log/cron

# View kernel messages
sudo less /var/log/dmesg
```

> 💡 **Note**: In **RHEL**, authentication logs go to `/var/log/secure`, not `/var/log/auth.log` (as on Debian/Ubuntu).

---

### ✅ Step 3: Watch Log Files in Real Time

```bash
# Watch system messages
sudo tail -f /var/log/messages

# Watch for authentication events
sudo tail -f /var/log/secure

# Watch logs from multiple files (optional)
sudo multitail /var/log/messages /var/log/secure
```

🔍 Use this live monitoring to detect brute-force or login attempts in real time.

---

### ✅ Step 4: Filter Specific Log Entries

```bash
# Find all failed SSH login attempts
sudo grep "Failed password" /var/log/secure

# Find successful root logins
sudo grep "Accepted password for root" /var/log/secure

# List sudo command executions
sudo grep "sudo:" /var/log/messages
```

> 🧠 These are often the first indicators of privilege escalation or brute force in a RHEL server.

---

### ✅ Step 5: Inject a Custom Log Entry Using `logger`

```bash
# Send a custom syslog message
logger -p user.notice "🔥 TEST: Shahid reviewed syslog in RHEL."

# Confirm it appears in the log
sudo tail -n 10 /var/log/messages
```

> ✅ This simulates how applications or scripts send logs to syslog.

---

### ✅ Step 6: Bonus - View Binary Journals (Optional)

Although you’re focusing on traditional syslog, RHEL also stores binary logs using `journald`.

```bash
# View recent logs from journal
sudo journalctl -n 20

# Filter logs by service (e.g., SSHD)
sudo journalctl -u sshd

# View logs from previous boot
sudo journalctl -b -1
```

---

## 🔐 Red Team Simulation (Safe Practice)

```bash
# Malicious log deletion attempt
sudo echo "" > /var/log/secure

# Verify it's now empty (🛑 Watch this in real environments)
ls -lh /var/log/secure
```

➡️ Now ask yourself: **Can your monitoring setup or SIEM catch this?**
Implement file integrity monitoring (`AIDE`, `auditd`, or `osquery`) for detection.

---

## 🧩 Reflection Questions

* What is the difference between `/var/log/messages` and `/var/log/secure` in RHEL?
* How would you script a daily check for failed SSH logins?
* What log file would you check to investigate a `cron` job failure?

---

## ✅ Checklist Summary

| Task                                   | Done? |
| -------------------------------------- | ----- |
| Verified rsyslog and journald services | ☐     |
| Reviewed core log files                | ☐     |
| Injected a custom log using `logger`   | ☐     |
| Monitored logs in real time            | ☐     |
| Searched for failed logins             | ☐     |
| Simulated log tampering (Red Team)     | ☐     |

---

## 💼 Job & Certification Mapping

| Role            | Why It's Relevant                            |
| --------------- | -------------------------------------------- |
| SOC Analyst     | Core skill: reviewing `/var/log/secure` logs |
| SysAdmin        | Log rotation and system troubleshooting      |
| IR Professional | Log forensics post-attack                    |

| Cert           | Relevance                                    |
| -------------- | -------------------------------------------- |
| CompTIA Linux+ | Covers `syslog`, `rsyslog`, and `journalctl` |
| CEH            | Log tampering and detection techniques       |
| OSCP           | Post-exploitation log analysis               |

---

Let me know when you're ready to move to:
🔜 `Lesson11.03-Review-System-Journal-Entries.md` (focused on `journald`)
or
📁 `Lab11.03-SSH-Incident-Investigation-RHEL.md` (based on real-world brute force hunting in `/var/log/secure`)

Shall we proceed?
