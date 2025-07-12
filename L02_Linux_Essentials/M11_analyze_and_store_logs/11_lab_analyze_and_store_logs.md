Absolutely, Shahid! You're now stepping into a **real-world cybersecurity lab** that bridges theory and practice:

> **Lab:** Analyze and Store Logs
> **Page Ref:** \~375
> **Objective:** Learn how to view, filter, analyze, and store system logs using journal tools and prepare them for long-term storage, auditing, and security investigations.

This lab focuses on working with **system logs**, using tools like `journalctl`, and storing them securely — a crucial skill in **SIEM setup, digital forensics, SOC workflows**, and **log-based threat detection**.

---

# 🧪 Lab: Analyze and Store Logs

---

## 🎯 Lab Goals

By the end of this lab, you will:

✅ Analyze logs from system journal (`journald`)
✅ Filter logs by time, service, priority
✅ Search for suspicious events
✅ Export logs to a file for evidence or storage
✅ Understand where and how to store logs securely

---

## 🛠️ Lab Requirements

| Requirement                                | Status |
| ------------------------------------------ | ------ |
| Linux system with `systemd`                | ✅      |
| `sudo` access                              | ✅      |
| Tools: `journalctl`, `grep`, `awk`, `less` | ✅      |
| Optional: Remote backup or USB             | ✅      |

---

## 📋 Lab Steps

---

### ✅ Step 1: View Full System Journal

```bash
journalctl
```

🔍 Scroll and observe:

* Login activity
* Service start/stop messages
* Warnings or failures

Press `q` to exit.

---

### ✅ Step 2: Filter Logs by Service (e.g., SSH)

```bash
journalctl -u ssh
```

➡️ This shows logs only from the SSH service.

Add a time filter:

```bash
journalctl -u ssh --since "1 day ago"
```

---

### ✅ Step 3: Filter by Priority (e.g., Errors Only)

```bash
journalctl -p err
```

➡️ Helps you focus on critical system issues.

You can combine filters:

```bash
journalctl -u ssh -p err --since yesterday
```

---

### ✅ Step 4: Search for Suspicious Login Attempts

```bash
journalctl | grep "Failed password"
```

or

```bash
journalctl -u ssh | grep "authentication failure"
```

✅ This is useful in **incident response** and brute-force detection.

---

### ✅ Step 5: Export Logs to a File

```bash
journalctl -u ssh --since yesterday > ssh_log_2025-07-12.txt
```

➡️ You now have a portable, readable copy of logs for archiving or analysis.

---

### ✅ Step 6: Securely Store the Log

**Option 1:** Copy to external USB

```bash
sudo cp ssh_log_2025-07-12.txt /media/shahid/usb/
```

**Option 2:** Transfer to a remote server:

```bash
scp ssh_log_2025-07-12.txt shahid@192.168.1.100:/home/shahid/logs/
```

**Option 3:** Compress for long-term archival:

```bash
gzip ssh_log_2025-07-12.txt
```

---

### ✅ Step 7: Enable Persistent Logging (if not already done)

If logs disappear after reboot, ensure persistence:

```bash
sudo mkdir -p /var/log/journal
sudo systemctl restart systemd-journald
```

---

## ✅ Output Checklist

| Task Completed                                   | ✔ / ❌ |
| ------------------------------------------------ | ----- |
| Viewed full journal logs                         |       |
| Filtered by service and time                     |       |
| Searched for failed login or suspicious activity |       |
| Exported logs to a local file                    |       |
| Compressed or moved logs for long-term storage   |       |
| Verified persistent journaling is enabled        |       |

---

## 🔐 Security Tips

| Practice                         | Why It Matters                           |
| -------------------------------- | ---------------------------------------- |
| Enable `Storage=persistent`      | Avoid losing logs after reboot           |
| Set permissions on exported logs | Prevent tampering or unauthorized access |
| Compress logs (`gzip`, `xz`)     | Save space and maintain integrity        |
| Store logs off-site or on a USB  | Protect against attacker log-wiping      |

---

## 🧠 Reflection Questions

1. Why is exporting logs important in forensics?
2. How can filtering by priority help in monitoring critical events?
3. What risks are involved if logs are stored only in RAM?
4. Where should long-term logs be stored in a secure network?

---

## 📁 GitHub-Style Folder Structure

```
/Lab-Analyze-and-Store-Logs/
├── README.md
├── logs/
│   ├── ssh_log_2025-07-12.txt
│   └── ssh_log_2025-07-12.txt.gz
├── scripts/
│   └── export-ssh-logs.sh
├── screenshots/
│   └── journalctl-filter-output.png
├── archive/
│   └── 2025-ssh-log-bkp.zip
```

---

## 🏁 Lab Summary

In this lab, you:

✔️ Learned to extract and analyze logs using `journalctl`
✔️ Identified failed login attempts and filtered by severity
✔️ Exported logs for long-term investigation
✔️ Practiced secure storage of logs for compliance and auditing

> 🔍 This skill is **crucial for security analysts, blue team responders, and forensic investigators** in both enterprise and government cybersecurity.

---

Would you like:

* 🔁 A Red Team simulation that triggers log entries you have to investigate?
* 📄 Markdown version for your GitHub notes?
* 🧠 Quiz or challenge lab based on real incident logs?

Just say the word, Shahid. You’re leveling up fast — ma shaa Allah!
