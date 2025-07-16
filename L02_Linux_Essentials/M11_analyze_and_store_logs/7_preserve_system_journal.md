Perfect, Shahid. Here's your structured, publish-ready Markdown file for:

---

## 📄 `Lesson11.04-Preserve-System-Journal-RHEL.md`

# 🧠 Linux Essentials – Module 11: Analyze and Store Logs

## Lesson 04: Preserve the System Journal

🎯 Focused on **Red Hat Enterprise Linux (RHEL 8/9)**

---

## 🎓 Introduction

By default, `systemd-journald` logs are stored in **volatile memory** (`/run/log/journal`) and are lost after reboot unless explicitly preserved.

Preserving the **system journal** means:

* Writing logs to disk (`/var/log/journal/`)
* Controlling retention, size, and rotation
* Ensuring **log integrity** and **forensic readiness**

This lesson is **critical for SOC, IR, and hardening roles** where log retention is a regulatory and security requirement.

---

## 🔍 Core Concepts (Feynman + Visual)

### 🧠 Why are journals not preserved by default?

> Feynman Analogy: Think of journald as a whiteboard. If you **don’t save a snapshot**, all notes are erased when you reboot. Preserving journals is like taking **photocopies of the whiteboard regularly**.

In RHEL, if `/var/log/journal/` doesn't exist:

* Journals go to `/run/log/journal/` (RAM)
* Logs disappear after reboot

---

## 📁 Journal Paths in RHEL

| Location            | Description            | Volatile or Persistent |
| ------------------- | ---------------------- | ---------------------- |
| `/run/log/journal/` | Default, RAM-only logs | Volatile               |
| `/var/log/journal/` | Persistent log storage | Persistent             |

---

## 🛠️ Check Current Journal Status

```bash
sudo journalctl --disk-usage
```

If it reports very low or **0B**, persistent logging is likely **not enabled**.

---

## ✅ Enable Persistent Journal in RHEL

### 🔹 Step 1: Create the journal directory

```bash
sudo mkdir -p /var/log/journal
```

> Creates persistent storage directory for `journald`.

---

### 🔹 Step 2: Apply permissions and reload

```bash
sudo systemd-tmpfiles --create --prefix /var/log/journal
sudo systemctl restart systemd-journald
```

➡️ Journald now detects `/var/log/journal/` and writes persistent logs after reboot.

---

### 🔹 Step 3: Confirm it's working

```bash
ls -l /var/log/journal
```

Then reboot:

```bash
sudo reboot
```

After reboot:

```bash
sudo journalctl -b -1  # See logs from previous boot
```

✅ If this works, **you've successfully preserved the system journal**.

---

## ⚙️ Optional: Configure Retention Settings

Edit journald config:

```bash
sudo nano /etc/systemd/journald.conf
```

Relevant fields:

```ini
Storage=persistent
SystemMaxUse=200M
SystemMaxFileSize=50M
SystemKeepFree=100M
MaxRetentionSec=7day
```

Apply changes:

```bash
sudo systemctl restart systemd-journald
```

---

## 🔐 Bonus: Enable Journal Forwarding to Syslog (Optional)

Ensure `ForwardToSyslog=yes` in `/etc/systemd/journald.conf`
Then restart `journald` and `rsyslog`.

---

## 🧪 Guided Lab: Preserve + Verify Journal

```bash
# 1. Create persistent directory
sudo mkdir -p /var/log/journal

# 2. Apply tmpfiles
sudo systemd-tmpfiles --create --prefix /var/log/journal

# 3. Restart journald
sudo systemctl restart systemd-journald

# 4. Confirm new journal
ls /var/log/journal

# 5. Reboot and check previous boot
sudo reboot
sudo journalctl -b -1
```

---

## 🔴 Red Team Simulation: Clear Persistent Logs

```bash
# Dangerous! Clears ALL persistent logs
sudo journalctl --vacuum-time=1s
```

⚠️ May indicate attacker behavior if done outside of rotation policy.

---

## 🔵 Blue Team Detection: Monitor Journal Retention

| Behavior                | Detection Strategy                            |
| ----------------------- | --------------------------------------------- |
| `journalctl` purged     | Use `auditd` to monitor `--vacuum-*` usage    |
| Journal file deleted    | Monitor `/var/log/journal/` with FIM tools    |
| Storage reverted to RAM | Detect missing `/var/log/journal/` on startup |

---

## 📘 Quiz – Preserve System Journal

1. What is the purpose of `/var/log/journal/` in RHEL?
2. How would you verify that journald is writing persistent logs?
3. What happens if only `/run/log/journal/` exists?
4. How do you check how much space your journal logs are using?
5. What fields in `journald.conf` control log retention?
6. How would you detect if an attacker purged the journal logs?
7. After enabling persistence, how can you view logs from the previous boot?

---

## 📊 Summary Table + Checklist

| ✅ Task                                           | Done? |
| ------------------------------------------------ | ----- |
| Created `/var/log/journal/`                      | ☐     |
| Restarted `systemd-journald`                     | ☐     |
| Verified persistent logs after reboot            | ☐     |
| Configured retention settings in `journald.conf` | ☐     |
| Simulated red team log purge                     | ☐     |
| Mapped detection using FIM/auditd                | ☐     |

---

## 📘 Journaling + Reflection

* Why does RHEL use volatile journaling by default?
* What are the implications of not preserving journal logs in a SOC/IR role?
* What changes can I make to secure `/var/log/journal/` from attackers?

📈 **Confidence Rating (1–10)**: `___`
🧠 **Still unclear about**: `___`
📅 **Date completed**: `________`

---

## 💼 Job + Certification Mapping

| Job Role      | Application                            |
| ------------- | -------------------------------------- |
| SOC Analyst   | Ensuring logs survive reboot           |
| IR Specialist | Access logs for previous attack events |
| Linux Admin   | Log rotation & retention configuration |

| Certification  | Module Alignment        |
| -------------- | ----------------------- |
| RHCSA          | Journal configuration   |
| CompTIA Linux+ | Logging policies        |
| CEH/OSCP       | Log tampering detection |

---

## 📅 Spaced Revision Plan

| Day | Task                                              |
| --- | ------------------------------------------------- |
| 1   | Enable journal persistence and reboot check       |
| 3   | Edit retention settings in `journald.conf`        |
| 7   | Simulate tampering and review mitigation          |
| 30  | Script to alert if `/var/log/journal/` is missing |

---

Let me know if you'd like a **guided lab** or **incident response simulation** for persistent logs or to begin:

🔜 `Lesson11.05: Back Up and Restore Log Files`

Ready when you are, Shahid 🚀📂📈
