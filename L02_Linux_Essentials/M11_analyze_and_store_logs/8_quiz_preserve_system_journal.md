Absolutely, Shahid. Here's your fully structured **Obsidian/GitHub-ready quiz + answer session** for:

---

## 📄 `QuizSession11.04-Preserve-System-Journal.md`

# 🧠 Quiz + Answer Session – Lesson 11.04

## Module 11: Analyze and Store Logs

🎯 Topic: **Preserve the System Journal (RHEL)**
🛠️ Format: Question ➜ Answer (inline)
🧭 Goal: Deepen understanding of how to enable, verify, and defend persistent `systemd-journald` logs in **RHEL 8/9**

---

### ❓Q1. What is the purpose of preserving the system journal in RHEL?

**✅ Answer:**
Preserving the system journal ensures that logs are **not lost after reboot**. Without this, logs are stored in **volatile memory** (`/run/log/journal`) and disappear when the system restarts. Persistent storage in `/var/log/journal/` allows **forensic analysis**, **audit trails**, and **incident investigation** across reboots.

---

### ❓Q2. Where does `journald` store logs by default if no configuration is changed?

**✅ Answer:**
In volatile memory under:

```bash
/run/log/journal/
```

These logs are **temporary** and will be **erased on reboot**.

---

### ❓Q3. How do you enable persistent journal storage in RHEL?

**✅ Answer:**

1. Create the persistent directory:

   ```bash
   sudo mkdir -p /var/log/journal
   ```

2. Apply tmpfiles policy:

   ```bash
   sudo systemd-tmpfiles --create --prefix /var/log/journal
   ```

3. Restart journald:

   ```bash
   sudo systemctl restart systemd-journald
   ```

After reboot, logs will now persist in `/var/log/journal/`.

---

### ❓Q4. How do you verify that journald is storing persistent logs?

**✅ Answer:**

1. Check disk usage:

   ```bash
   sudo journalctl --disk-usage
   ```

2. Confirm that the `/var/log/journal/` directory exists and contains boot subfolders.

3. Reboot the system and run:

   ```bash
   sudo journalctl -b -1
   ```

   If you see logs from the **previous boot**, persistence is working.

---

### ❓Q5. What command shows how many boots journald has logs for?

**✅ Answer:**

```bash
sudo journalctl --list-boots
```

This shows boot index numbers, boot IDs, and timestamps — useful for forensic timeline reconstruction.

---

### ❓Q6. What is the difference between `/run/log/journal/` and `/var/log/journal/`?

**✅ Answer:**

| Directory           | Type       | Behavior                         |
| ------------------- | ---------- | -------------------------------- |
| `/run/log/journal/` | Volatile   | Stored in RAM, lost after reboot |
| `/var/log/journal/` | Persistent | Stored on disk, survives reboots |

---

### ❓Q7. Which configuration file controls journald's storage behavior?

**✅ Answer:**

```bash
/etc/systemd/journald.conf
```

The key setting is:

```ini
Storage=persistent
```

You can also configure size, retention, and compression options here.

---

### ❓Q8. What does this command do?

```bash
journalctl --vacuum-time=1s
```

**✅ Answer:**
This **deletes all journal entries older than 1 second**, effectively wiping the journal.

⚠️ **Can be abused by attackers to destroy forensic evidence.**

---

### ❓Q9. How can a SOC analyst detect if journald logs have been purged?

**✅ Answer:**

* Use `journalctl --list-boots` to look for missing boot logs
* Monitor disk usage with:

  ```bash
  journalctl --disk-usage
  ```

  → Sudden drop to `0B` can indicate tampering.
* Use `auditd` or FIM tools like `osquery` to detect:

  * Deletion of files in `/var/log/journal/`
  * Usage of `--vacuum-*` options

---

### ❓Q10. After setting up journald persistence, how would you view logs from the previous boot?

**✅ Answer:**

```bash
sudo journalctl -b -1
```

This displays logs from the **previous boot session**.

---

### ❓Q11. How do you limit journal size on disk to avoid filling up `/var`?

**✅ Answer:**

Edit `/etc/systemd/journald.conf`:

```ini
SystemMaxUse=200M
SystemKeepFree=100M
SystemMaxFileSize=50M
MaxRetentionSec=7day
```

Then reload journald:

```bash
sudo systemctl restart systemd-journald
```

---

### ❓Q12. Why is persistent logging important for SOC and IR job roles?

**✅ Answer:**

* Allows tracking of **reboot-time attacks**
* Supports **timeline reconstruction**
* Enables **alert correlation** across reboots
* Ensures **log retention compliance** (e.g., PCI-DSS, HIPAA)
* Helps catch **Red Team log-clearing tactics**

---

## 🧾 Summary Table – Quick Review

| Topic                              | ✅ Understood |
| ---------------------------------- | ------------ |
| Enabling journal persistence       | ☐            |
| Difference: volatile vs persistent | ☐            |
| Verifying previous boot logs       | ☐            |
| Detecting log tampering            | ☐            |
| Setting retention policies         | ☐            |

---

## 🧠 Journaling Prompts

* Did I practice enabling and verifying journald persistence?
* Can I detect if logs have been tampered with or deleted?
* How would I respond to a vacuuming attempt by an attacker?

---

Let me know when you're ready to:
🔜 Proceed to `Lesson11.05-Back-Up-and-Restore-Log-Files.md`
📁 Or simulate a Red Team attack involving journal deletion with `Lab11.04-LogTamperSimulation-Journald.md`

I'm ready when you are, Shahid. 🧠📘⚙️
