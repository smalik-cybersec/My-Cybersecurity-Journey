Here is your structured, GitHub/Obsidian-ready **Ultra Edition v4.0+ guided lab** for:

---

## 📄 `Lab11.04-Guided-Exercise-Preserve-System-Journal-RHEL.md`

# 🧪 Guided Exercise – Preserve the System Journal

**Module 11 – Analyze and Store Logs**
🎯 Focus: RHEL 8/9 | `systemd-journald` persistence, retention, and hardening
📂 Role: SOC Analyst • Incident Responder • Linux Admin

---

## 🧭 Scenario

You are part of a **blue team in a SOC**. The Red Team has simulated a system reboot followed by a **log tampering attempt**. You must ensure that **systemd journal logs persist across reboots** and are protected from unauthorized purging.

---

## 🛠️ Lab Objectives

1. ✅ Verify default journal behavior
2. ✅ Enable persistent journaling
3. ✅ Reboot and confirm previous logs exist
4. ✅ Configure retention limits
5. ✅ Simulate red team log purge
6. ✅ Detect the purge and harden the system

---

## 🧱 Prerequisites

* ✅ RHEL 8/9 VM (bare metal or virtualized)
* ✅ Root or `sudo` access
* ✅ `systemd` and `journald` (enabled by default)

---

## 🧪 Step-by-Step Instructions

---

### 🔹 Step 1: Check If Journald Is Using Volatile Storage

```bash
sudo journalctl --disk-usage
```

Check the log path:

```bash
sudo ls /run/log/journal/
sudo ls /var/log/journal/
```

➡️ If only `/run/log/journal/` exists, logs are stored in **RAM** and will be **lost on reboot**.

---

### 🔹 Step 2: Enable Persistent Journal Storage

```bash
# 1. Create the persistent storage directory
sudo mkdir -p /var/log/journal

# 2. Apply correct permissions and create tempfiles
sudo systemd-tmpfiles --create --prefix /var/log/journal

# 3. Restart journald
sudo systemctl restart systemd-journald
```

---

### 🔹 Step 3: Reboot and Verify

```bash
sudo reboot
```

After reboot:

```bash
# Check previous boot logs
sudo journalctl -b -1

# Confirm persistent journal is now active
sudo journalctl --disk-usage
```

✅ If logs from the **previous boot** are visible, journaling persistence is working.

---

### 🔹 Step 4: Configure Retention Policies

Edit the journald config:

```bash
sudo nano /etc/systemd/journald.conf
```

Update or uncomment:

```ini
Storage=persistent
SystemMaxUse=200M
SystemKeepFree=100M
SystemMaxFileSize=50M
MaxRetentionSec=7day
```

Apply changes:

```bash
sudo systemctl restart systemd-journald
```

---

### 🔹 Step 5: Simulate a Red Team Log Deletion Attempt

```bash
# Vacuum logs (Red Team style — wipes logs older than 1s)
sudo journalctl --rotate
sudo journalctl --vacuum-time=1s
```

➡️ All logs are now wiped. This simulates an attacker trying to cover their tracks.

---

### 🔹 Step 6: Detect the Purge (Blue Team)

Check boot history:

```bash
sudo journalctl --list-boots
```

Check disk usage:

```bash
sudo journalctl --disk-usage
```

➡️ If usage dropped significantly or logs disappeared from older boots, flag this in SIEM or incident response platform.

---

### 🛡️ Bonus: Harden Journald Against Tampering

**Use file integrity monitoring** (FIM):

* Monitor `/var/log/journal/`
* Detect unauthorized deletion or modification

**Example tools**:

* `auditd`
* `osquery`
* `tripwire`
* `AIDE`

---

## 📘 Guided Checklist

| Task                                                       | Done? |
| ---------------------------------------------------------- | ----- |
| Verified journald storage location (RAM/disk)              | ☐     |
| Created `/var/log/journal/`                                | ☐     |
| Restarted journald and rebooted system                     | ☐     |
| Verified previous boot logs with `-b -1`                   | ☐     |
| Set retention policies in `journald.conf`                  | ☐     |
| Simulated Red Team purge with `--vacuum-time`              | ☐     |
| Detected log purge using `--list-boots` and `--disk-usage` | ☐     |

---

## 🧠 Reflection Questions

* What happens if journald is misconfigured or not persistent?
* How can an attacker erase their tracks using journald?
* What defenses would you implement to alert on log tampering?

📈 **Confidence (1–10):** `___`
🛡️ **Key takeaway from this lab:** `___`
📅 **Date Completed:** `________`

---

## 💼 Job & Certification Mapping

| Role                | Skill Practiced                              |
| ------------------- | -------------------------------------------- |
| SOC Analyst         | Log preservation, tamper detection           |
| IR Analyst          | Post-attack forensic log triage              |
| Linux Administrator | Persistent logging configuration & hardening |

| Certification  | Alignment                                     |
| -------------- | --------------------------------------------- |
| RHCSA          | `journald` configuration & retention policies |
| CompTIA Linux+ | Log lifecycle management                      |
| CEH/OSCP       | Log tampering + blue team defense             |

---

## 📅 Spaced Revision Plan

| Day | Task                                        |
| --- | ------------------------------------------- |
| 1   | Practice enabling persistent journaling     |
| 3   | Simulate log purge and detect via `auditd`  |
| 7   | Test retention config via `MaxRetentionSec` |
| 30  | Monitor journald logs via custom FIM rules  |

---

Let me know if you'd like to move on to:

🔜 `Lesson11.05-Back-Up-and-Restore-Log-Files.md`
📁 or simulate a full Red/Blue log destruction hunt in:
`IncidentLab11.04-Forensic-Journal-Wipe-Recovery.md`

Ready when you are, Shahid. ⚙️🧠📘
