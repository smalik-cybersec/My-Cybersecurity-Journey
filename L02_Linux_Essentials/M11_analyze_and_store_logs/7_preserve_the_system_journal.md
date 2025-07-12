Great move, Shahid! You’re now focusing on an essential logging configuration step:

> **Topic:** Preserve the System Journal
> **Page Ref:** \~361
> **Goal:** Enable **persistent logging** for systemd-journald, so logs are not lost after a reboot — a critical step for auditing, forensic investigations, and long-term monitoring.

---

# 📘 Preserve the System Journal

---

## 📌 Chapter Overview

By default, `systemd-journald` stores logs in **volatile memory** (`/run/log/journal/`) which is **cleared on every reboot**. This is dangerous in security operations, where **evidence and audit trails are critical**.

> 🎯 **Objective:** Configure your Linux system to persist journal logs across reboots using `systemd-journald`.

---

## 📚 Table of Contents

- [📘 Preserve the System Journal](#-preserve-the-system-journal)
  - [📌 Chapter Overview](#-chapter-overview)
  - [📚 Table of Contents](#-table-of-contents)
  - [1️⃣ Understanding Volatile vs Persistent Journals](#1️⃣-understanding-volatile-vs-persistent-journals)
  - [2️⃣ Why Persistent Journals Matter in Cybersecurity](#2️⃣-why-persistent-journals-matter-in-cybersecurity)
  - [3️⃣ Check Current Logging Status](#3️⃣-check-current-logging-status)
  - [4️⃣ Enable Persistent Logging](#4️⃣-enable-persistent-logging)
    - [✅ Verify](#-verify)
  - [5️⃣ Configure Log Retention Policies](#5️⃣-configure-log-retention-policies)
  - [6️⃣ 🧪 Lab: Configure Persistent Journal](#6️⃣--lab-configure-persistent-journal)
    - [🎯 Task](#-task)
    - [🔧 Steps](#-steps)
  - [7️⃣ 🔐 Best Practices \& Security Considerations](#7️⃣--best-practices--security-considerations)
  - [8️⃣ 🧠 Quiz \& Reflection](#8️⃣--quiz--reflection)
    - [✅ True or False](#-true-or-false)
    - [✅ Short Answer](#-short-answer)
  - [9️⃣ ✅ Summary](#9️⃣--summary)
  - [📁 GitHub-Ready Folder Structure](#-github-ready-folder-structure)

---

## 1️⃣ Understanding Volatile vs Persistent Journals

| Property                | Volatile Journals   | Persistent Journals |
| ----------------------- | ------------------- | ------------------- |
| Stored in               | `/run/log/journal/` | `/var/log/journal/` |
| Deleted on reboot?      | ✅ Yes               | ❌ No                |
| Default on most systems | ✅ Yes               | ❌ No                |
| Forensics-friendly?     | ❌ No                | ✅ Yes               |

---

## 2️⃣ Why Persistent Journals Matter in Cybersecurity

🔒 Persistent logs are crucial for:

* **Incident response** (review what happened before a crash)
* **Digital forensics** (track user and system activity)
* **Audit trails** (required for compliance: SOC 2, ISO 27001)
* **Post-exploitation analysis** (what did the attacker do?)

---

## 3️⃣ Check Current Logging Status

Run this command:

```bash
ls -ld /var/log/journal
```

If this directory **does not exist**, journald is only writing volatile logs.

You can also verify with:

```bash
sudo journalctl --disk-usage
```

> If output is empty or small (0B), persistent logging is not enabled.

---

## 4️⃣ Enable Persistent Logging

Run the following steps:

```bash
sudo mkdir -p /var/log/journal
sudo systemd-tmpfiles --create --prefix /var/log/journal
sudo systemctl restart systemd-journald
```

> This forces journald to store logs in the persistent path.

### ✅ Verify

```bash
ls /var/log/journal
```

You should now see a subdirectory with a machine ID like:

```
/var/log/journal/f354c3088a4e4adfbfd48bba54efda67
```

And disk usage:

```bash
sudo journalctl --disk-usage
```

---

## 5️⃣ Configure Log Retention Policies

Edit the journald config file:

```bash
sudo nano /etc/systemd/journald.conf
```

Update/add these fields as needed:

```ini
Storage=persistent
SystemMaxUse=500M
SystemKeepFree=50M
SystemMaxFileSize=100M
MaxRetentionSec=2w
```

Then restart:

```bash
sudo systemctl restart systemd-journald
```

📌 **Fields explained:**

* `SystemMaxUse`: max disk journald may use
* `SystemKeepFree`: disk space to leave untouched
* `MaxRetentionSec`: how long to keep logs

---

## 6️⃣ 🧪 Lab: Configure Persistent Journal

### 🎯 Task

✅ Enable journald persistence
✅ Limit journal disk usage
✅ Confirm logs survive reboot

### 🔧 Steps

```bash
sudo mkdir -p /var/log/journal
sudo nano /etc/systemd/journald.conf
```

Set:

```ini
Storage=persistent
SystemMaxUse=300M
```

Save and restart:

```bash
sudo systemctl restart systemd-journald
```

Reboot system:

```bash
sudo reboot
```

After reboot:

```bash
journalctl -b -1
```

✔️ Shows logs from **previous boot** — confirms persistence.

---

## 7️⃣ 🔐 Best Practices & Security Considerations

| Practice                                           | Benefit                       |
| -------------------------------------------------- | ----------------------------- |
| Use `Storage=persistent`                           | Saves logs across reboots     |
| Set retention (`SystemMaxUse`)                     | Avoid disk exhaustion attacks |
| Combine with log forwarding (e.g., rsyslog → SIEM) | Centralized analysis          |
| Set permissions on `/var/log/journal`              | Prevent unauthorized access   |
| Monitor journald for suspicious clearing           | Detect log tampering attempts |

---

## 8️⃣ 🧠 Quiz & Reflection

### ✅ True or False

**Q1.** Journald logs are always persistent by default.
→ ❌ False

**Q2.** `/var/log/journal` must exist to enable persistent logging.
→ ✅ True

**Q3.** `journalctl -b -1` shows logs from the previous boot.
→ ✅ True

---

### ✅ Short Answer

**Q4.** What config option enables journald persistence?
→ `Storage=persistent`

**Q5.** Why is log retention size (`SystemMaxUse`) important in security?
→ Prevents disk fill attacks and ensures logs aren't deleted too early.

---

## 9️⃣ ✅ Summary

You've now learned how to:

* Detect if your journal logs are persistent or volatile
* Configure journald to preserve logs across reboots
* Set storage and retention policies
* Test your changes and ensure logs survive reboots

> 💡 This configuration is a **must** for real-world security monitoring, auditing, and digital forensics.

---

## 📁 GitHub-Ready Folder Structure

```
/Preserve-System-Journal/
├── README.md
├── config/
│   └── journald.conf (with comments)
├── screenshots/
│   └── disk_usage_before_after.png
├── verification/
│   └── journalctl-boot-logs.txt
└── scripts/
    └── enable_journald_persistence.sh
```

---

Would you like:

* 🧪 A guided simulation of detecting an incident after reboot using persistent logs?
* 📄 Markdown or PDF version for your GitHub repo?
* 💬 Help integrating journald with a remote SIEM like ELK or Graylog?

Just say the word, Shahid!
