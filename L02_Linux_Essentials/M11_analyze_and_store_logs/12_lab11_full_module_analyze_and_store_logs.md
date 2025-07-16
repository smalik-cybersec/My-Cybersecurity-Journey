Absolutely, Shahid. Below is your **Ultra Edition v4.0+ master lab** for:

---

## 📄 `Lab11-FullModule-Analyze-and-Store-Logs-RHEL.md`

# 🧪 Master Lab – Module 11: Analyze and Store Logs

🎯 **Distribution**: Red Hat Enterprise Linux (RHEL 8/9)
📦 **Covers**:

* System Log Architecture
* Syslog Review
* Journal Review
* Preserving Journals
* Maintaining Accurate Time

---

## 🎓 Lab Objective

You are working as a **SOC Tier 1 Analyst** managing several RHEL servers. Your job is to:

* Inspect how logs are structured and stored
* Monitor logs for authentication and system activity
* Preserve logs across reboots
* Detect log tampering
* Ensure all logs are timestamped accurately via NTP

---

## 🛠️ Pre-Lab Setup

Ensure the following:

* ✅ RHEL 8 or 9 installed (VM or bare metal)
* ✅ Root/sudo access
* ✅ Internet access for NTP sync
* ✅ SELinux enforcing mode (for realism)

---

## 🔁 PART 1: Understand and Navigate the Log Architecture

---

### 🧪 Task 1.1 – Identify Log Components

```bash
# Check systemd journal status
systemctl status systemd-journald

# Check if rsyslog is running
systemctl status rsyslog
```

✅ **Confirm**: Both `systemd-journald` and `rsyslog` are running.

---

### 🧪 Task 1.2 – Locate Key Log Files

```bash
ls -l /var/log/
ls -l /var/log/journal/
```

📌 Explore:

| File                | Purpose                     |
| ------------------- | --------------------------- |
| `/var/log/messages` | System-wide log events      |
| `/var/log/secure`   | Authentication events (SSH) |
| `/var/log/cron`     | Scheduled job logs          |
| `/var/log/dmesg`    | Boot & kernel ring buffer   |
| `/var/log/journal/` | Binary persistent logs      |

---

## 📂 PART 2: Analyze Syslog and Authentication Logs

---

### 🧪 Task 2.1 – Monitor Syslog in Real-Time

```bash
tail -f /var/log/messages
```

In another terminal, run:

```bash
logger "🧪 Syslog test by Shahid"
```

🔍 Verify your message appears.

---

### 🧪 Task 2.2 – Extract Failed SSH Logins

```bash
grep "Failed password" /var/log/secure
```

Filter by date or IP address.

---

### 🧪 Task 2.3 – Identify Successful `sudo` Events

```bash
grep "sudo:" /var/log/messages
```

Use `grep` and `cut` to format output.

---

## 🗃️ PART 3: Work with Journald Logs (Binary + Structured)

---

### 🧪 Task 3.1 – Filter by Boot, Unit, and Priority

```bash
# Last boot
journalctl -b

# Previous boot
journalctl -b -1

# View SSH service logs
journalctl -u sshd

# Show errors only
journalctl -p err..alert
```

---

### 🧪 Task 3.2 – Inject and Retrieve Custom Journal Entry

```bash
logger "🔒 Shahid's journald injection test"

# Retrieve
journalctl | grep "Shahid"
```

---

## 🧾 PART 4: Preserve Logs Across Reboots

---

### 🧪 Task 4.1 – Enable Persistent Journaling

```bash
sudo mkdir -p /var/log/journal
sudo systemd-tmpfiles --create --prefix /var/log/journal
sudo systemctl restart systemd-journald
```

Reboot:

```bash
sudo reboot
```

After reboot, run:

```bash
journalctl -b -1
```

✅ You should now see previous boot logs.

---

### 🧪 Task 4.2 – Simulate Red Team Log Wipe

```bash
# Danger: simulate log deletion
sudo journalctl --vacuum-time=1s
```

---

### 🧪 Task 4.3 – Detect the Wipe (Blue Team)

```bash
journalctl --list-boots
journalctl --disk-usage
```

✅ Look for missing boots or 0B usage.

---

## 🕰️ PART 5: Maintain Accurate Time (NTP)

---

### 🧪 Task 5.1 – Check NTP Configuration

```bash
timedatectl
systemctl status chronyd
chronyc tracking
```

Ensure:

* `NTP enabled: yes`
* `System clock synchronized: yes`

---

### 🧪 Task 5.2 – Simulate Time Tampering (Red Team)

```bash
sudo timedatectl set-time "2024-01-01 00:00:00"
```

Check logs:

```bash
timedatectl
journalctl -b
```

---

### 🧪 Task 5.3 – Restore Time Accuracy (Blue Team)

```bash
sudo timedatectl set-ntp true
sudo systemctl restart chronyd
chronyc tracking
```

---

## 🔐 Bonus: Audit Tampering Attempts

```bash
sudo auditctl -w /usr/bin/date -p x -k time_change
sudo ausearch -k time_change
```

✅ Detect if anyone manually sets the time or edits chrony configuration.

---

## ✅ Final Lab Checklist

| Task                                            | Status |
| ----------------------------------------------- | ------ |
| Verified log daemons (`journald`, `rsyslog`)    | ☐      |
| Analyzed `/var/log/messages`, `/var/log/secure` | ☐      |
| Used `journalctl` filters (`-b`, `-u`, `-p`)    | ☐      |
| Enabled and tested persistent journaling        | ☐      |
| Detected journald vacuum event                  | ☐      |
| Verified NTP and restored time drift            | ☐      |
| Injected and extracted custom log entries       | ☐      |
| Set up audit rule for `date` tampering          | ☐      |

---

## 🧠 Reflection & Journaling

* Which log source was easiest to navigate?
* Could you detect if logs were tampered or cleared?
* What are signs of time tampering in logs?

📘 **Date Completed:** `________`
📈 **Confidence Level (1–10):** `___`
🛠️ **Still Unclear On:** `________`

---

## 💼 Role & Cert Mapping

| Role        | Relevance                                  |
| ----------- | ------------------------------------------ |
| SOC Analyst | Log monitoring, log evasion detection      |
| IR Analyst  | Post-incident triage using timestamps      |
| SysAdmin    | Time, journal, log retention configuration |

| Certification | Mapped Domain                          |
| ------------- | -------------------------------------- |
| RHCSA         | `chronyd`, `journalctl`, `rsyslog`     |
| Linux+        | Time sync, log architecture            |
| CEH/OSCP      | Detecting and simulating log tampering |

---

## 📅 Revision Plan

| Day | Task                                       |
| --- | ------------------------------------------ |
| 1   | Run journal filters and syslog greps       |
| 3   | Simulate and detect journald vacuum        |
| 7   | Inject log → preserve across boot → detect |
| 30  | Automate journal + time audit script       |

---

Would you like a companion **quiz session** for this full lab? Or shall we proceed to **Module 12**?

Just say the word, Shahid. ⚔️🧠📘
