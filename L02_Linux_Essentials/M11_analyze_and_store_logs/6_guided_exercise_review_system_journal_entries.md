Excellent, Shahid! Now let's make this knowledge **practical** with a structured, step-by-step:

> **🧪 Guided Exercise: Review System Journal Entries**
> **Page Ref:** \~358
> **Objective:** Learn to navigate and filter Linux system journal entries using `journalctl` — the default tool for viewing `systemd-journald` logs on modern Linux systems.

---

# 🧪 Guided Exercise: Review System Journal Entries

---

## 🎯 Learning Objectives

By the end of this exercise, you will be able to:

* View and filter system logs using `journalctl`
* Identify system events, boot issues, and service-related messages
* Extract logs by priority, service, time, and user
* Troubleshoot real-world incidents using journal entries

---

## 🛠️ Lab Environment Requirements

| Requirement                             | Status     |
| --------------------------------------- | ---------- |
| Linux system with `systemd`             | ✅ Required |
| sudo access                             | ✅ Required |
| Tools used: `journalctl`, `grep`, `awk` | ✅ Built-in |

---

## 📋 Exercise Steps

---

### ✅ Step 1: View All Journal Entries

```bash
journalctl
```

> This displays logs collected by `systemd-journald`.
> Scroll with arrow keys or press `q` to quit.

---

### ✅ Step 2: Show Logs Since Last Boot

```bash
journalctl -b
```

> Useful to troubleshoot services or errors that happened during the current session.

---

### ✅ Step 3: Monitor Real-Time Logs

```bash
journalctl -f
```

> Keeps printing logs as they happen (like `tail -f` for systemd).

🔁 In another terminal, trigger a simple action:

```bash
ping -c 3 google.com
```

Watch journal update in real-time.

---

### ✅ Step 4: Filter Logs by Specific Service (e.g., SSH)

```bash
journalctl -u ssh
```

> View all logs related to the `sshd` daemon.

For better time context:

```bash
journalctl -u ssh --since today
```

---

### ✅ Step 5: Filter Logs by Priority Level

Show only errors:

```bash
journalctl -p err
```

Show only warnings and above:

```bash
journalctl -p warning -b
```

| Priority  | Use Case Example            |
| --------- | --------------------------- |
| `err`     | Crashed service             |
| `warning` | Misconfigurations, warnings |
| `info`    | Normal operational logs     |

---

### ✅ Step 6: Filter Logs by Time

```bash
journalctl --since "2025-07-11 10:00" --until "2025-07-11 14:00"
```

> Can be combined with `-u` to filter a specific service during that time:

```bash
journalctl -u ssh --since "2 hours ago"
```

---

### ✅ Step 7: Find Logs Related to a Specific User

```bash
journalctl _UID=$(id -u shahid)
```

> Replace `shahid` with the actual username if needed.

---

### ✅ Step 8: Export Logs for Reporting

```bash
journalctl -u ssh --since yesterday > ssh_yesterday_logs.txt
```

> Useful for log audits, incident response documentation, or case studies.

---

### ✅ Step 9: Search for Specific Patterns in Logs

Use `grep`:

```bash
journalctl | grep "Failed password"
```

Combine with date/time filter:

```bash
journalctl --since today | grep "sudo"
```

---

## 🔁 Optional Bonus Tasks

### 🔧 Bonus A: Show Kernel Boot Logs

```bash
journalctl -k
```

> Great for debugging hardware or low-level driver issues.

---

### 🔧 Bonus B: Check for Crashes or Segfaults

```bash
journalctl | grep -i segfault
```

> Useful for identifying broken binaries or malware behavior.

---

### 🔧 Bonus C: Enable Persistent Logging (if not enabled)

```bash
sudo mkdir -p /var/log/journal
sudo systemd-tmpfiles --create --prefix /var/log/journal
sudo systemctl restart systemd-journald
```

---

## ✅ Output Checklist

| Task                                 | Completed? (✔/❌) |
| ------------------------------------ | ---------------- |
| Viewed full journal entries          |                  |
| Filtered logs by boot session        |                  |
| Watched logs live with `-f`          |                  |
| Filtered logs by SSH service         |                  |
| Filtered logs by time window         |                  |
| Exported logs to a file              |                  |
| Searched for errors or failed logins |                  |

---

## 📁 GitHub-Style Folder Structure

```
/System-Journal-Exercise/
├── README.md
├── logs/
│   └── ssh_yesterday_logs.txt
├── scripts/
│   └── journal_filters.sh
├── screenshots/
│   └── journalctl_demo.png
└── report/
    └── log_analysis_notes.md
```

---

## 🧠 Reflection Questions

1. What’s the difference between `journalctl -b` and `journalctl`?
2. How can you investigate a failed login attempt using journal logs?
3. Why is `journalctl -u <service>` useful during troubleshooting?
4. When should you export logs to a file?

---

## ✅ Summary

You've now practiced:

* **Live log monitoring**
* **Time-based and service-based filtering**
* **Searching and exporting logs**
* **Using systemd's modern logging tools**

> 📌 **`journalctl` is your go-to tool for modern Linux log analysis.**
> It's used in **forensics, security monitoring, DevOps**, and **incident response**.

---

Would you like:

* 📄 This in Markdown or PDF?
* 🧠 A mini-quiz for this lab?
* 🚨 A Red Team attack scenario to investigate using `journalctl`?

Let me know the next step, Shahid. You're building rock-solid Linux log analysis skills!
