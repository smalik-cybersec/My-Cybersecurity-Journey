Here is your full **Obsidian + GitHub-ready Ultra Edition v4.0+ Guided Exercise** for:

---

## 📄 `Lab11.05-Guided-Exercise-Maintain-Accurate-Time-RHEL.md`

# 🧪 Guided Exercise – Maintain Accurate Time

**Module 11 – Analyze and Store Logs**
🎯 Distribution: **RHEL 8/9**
🔍 Focus: Ensure system clock accuracy using `chronyd`, NTP, and monitoring tools
🧭 Aligned with: SOC, IR, SysAdmin job roles and RHCSA/CompTIA Linux+ exams

---

## 🧭 Scenario

You are a junior SOC analyst managing a fleet of RHEL servers. Your SIEM dashboard is showing **log time inconsistencies** between different systems. Your task:

* Verify current time settings
* Enable NTP and sync with trusted servers
* Use `chronyc` to troubleshoot drift
* Detect if a system’s clock was tampered with (Red Team simulation)

---

## 🧱 Environment Setup

* ✅ RHEL 8 or 9 (bare metal or VM)
* ✅ Internet connection for NTP
* ✅ Sudo/root access

---

## 🧪 Step-by-Step Guided Exercise

---

### 🔹 Step 1: View Current System Time & Time Zone

```bash
timedatectl
```

Expected output:

```
Local time:  Tue 2025-07-16 19:01:54 IST
Time zone:   Asia/Kolkata (IST, +0530)
NTP enabled: yes
System clock synchronized: yes
```

📌 Confirm:

* `NTP enabled` = **yes**
* `System clock synchronized` = **yes**

---

### 🔹 Step 2: Start and Enable the NTP Daemon (Chrony)

```bash
# Check status of chronyd
systemctl status chronyd

# Enable and start if not running
sudo systemctl enable --now chronyd
```

---

### 🔹 Step 3: Check NTP Synchronization

```bash
# Confirm NTP is syncing
timedatectl status
```

Enable NTP if needed:

```bash
sudo timedatectl set-ntp true
```

---

### 🔹 Step 4: Use `chronyc` to Analyze Sync Sources

```bash
# Show current NTP sources and status
chronyc sources

# Show detailed tracking information
chronyc tracking
```

Expected output fields:

* `Reference ID`
* `Last offset`
* `Frequency`
* `Root dispersion`

---

### 🔹 Step 5: Configure a Custom NTP Server (Optional)

```bash
# Edit NTP servers
sudo nano /etc/chrony.conf
```

Add or update:

```ini
server in.pool.ntp.org iburst
server time.cloudflare.com iburst
```

Apply changes:

```bash
sudo systemctl restart chronyd
```

Then re-check:

```bash
chronyc sources -v
```

---

### 🔹 Step 6: Manually Set the Time (Red Team Simulation)

```bash
# Simulate attacker setting time 2 days behind
sudo timedatectl set-time "2025-07-14 12:00:00"
```

Now check:

```bash
timedatectl
```

> 🛑 This breaks time consistency and log correlation!

---

### 🔹 Step 7: Detect and Correct Time Drift (Blue Team)

Check NTP sync:

```bash
chronyc tracking
```

Re-sync with NTP:

```bash
sudo timedatectl set-ntp true
sudo systemctl restart chronyd
```

Confirm correction:

```bash
timedatectl
```

---

## 📘 Optional: Monitor Time Drift with `auditd` or `osquery`

### Add an audit rule to track time change:

```bash
sudo auditctl -w /usr/bin/date -p x -k time_change
sudo auditctl -w /etc/chrony.conf -p wa -k chrony_config
```

View logs:

```bash
sudo ausearch -k time_change
```

---

## ✅ Checklist Summary

| Task                                           | Done? |
| ---------------------------------------------- | ----- |
| Verified system time and timezone              | ☐     |
| Confirmed NTP is enabled and chronyd is active | ☐     |
| Used `chronyc` to view tracking and sources    | ☐     |
| Simulated attacker time tampering              | ☐     |
| Re-synced with NTP after tampering             | ☐     |
| Monitored changes with `auditd`                | ☐     |

---

## 🧠 Reflection Prompts

* Why is NTP essential in distributed logging environments?
* What problems occur when time is inconsistent across systems?
* How would I write an alert for time skew over 5 seconds?

🧠 **Confidence Level (1–10):** `___`
📅 **Date Completed:** `__________`
🔍 **Still Unclear On:** `__________`

---

## 💼 Job & Cert Mapping

| Role               | Real-World Relevance               |
| ------------------ | ---------------------------------- |
| SOC Analyst        | Detect log skew, investigate drift |
| Incident Responder | Log sequence reconstruction        |
| SysAdmin           | Maintain NTP for compliance uptime |

| Certification  | Skill Coverage                      |
| -------------- | ----------------------------------- |
| RHCSA          | `chronyd`, `timedatectl`, drift fix |
| CompTIA Linux+ | Time sync & log integrity           |
| CEH/OSCP       | Time tampering for log evasion      |

---

## 📅 Spaced Revision Plan

| Day | Task                                        |
| --- | ------------------------------------------- |
| 1   | Practice `chronyc` and `timedatectl` basics |
| 3   | Simulate clock drift and correct with NTP   |
| 7   | Audit changes to `/etc/chrony.conf`         |
| 30  | Automate drift alerts with cron or osquery  |

---

Let me know if you'd like a:

* ✅ **Quiz + Answer Session** for this lesson
* 🔜 Move on to `Lesson11.06: Back Up and Restore Log Files`

Ready when you are, Shahid 🕰️📡🔍
