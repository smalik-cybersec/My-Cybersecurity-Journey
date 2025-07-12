Perfect timing, Shahid! Let’s turn the **theory of persistent journaling** into **practical experience** with this fully guided hands-on activity:

> **🧪 Guided Exercise:** Preserve the System Journal
> **Page Ref:** \~364
> **Objective:** Enable and verify persistent system logging using `systemd-journald` to ensure log availability across reboots — a critical feature for forensics and audit compliance.

---

# 🧪 Guided Exercise: Preserve the System Journal

---

## 🎯 Goals of This Exercise

✅ Configure your Linux system to retain system logs across reboots
✅ Verify that persistent logs are stored properly
✅ Apply journald configuration for log size and retention
✅ Simulate a reboot and confirm log recovery

---

## 🛠️ What You Need

| Resource                    | Required |
| --------------------------- | -------- |
| Linux with `systemd`        | ✅        |
| Terminal with `sudo`        | ✅        |
| Text editor (`nano`, `vim`) | ✅        |
| Ability to reboot system    | ✅        |

---

## 📋 Exercise Steps

---

### ✅ Step 1: Check if Journald Is Currently Persistent

Run the following to check if the persistent log directory exists:

```bash
ls -ld /var/log/journal
```

If you **see nothing**, journald is using **volatile (temporary)** logs stored in `/run/log/journal/`.

---

### ✅ Step 2: Check Current Log Disk Usage

```bash
sudo journalctl --disk-usage
```

> Output of 0B means logs are not persistent.

---

### ✅ Step 3: Enable Persistent Journaling

Run:

```bash
sudo mkdir -p /var/log/journal
sudo systemd-tmpfiles --create --prefix /var/log/journal
sudo systemctl restart systemd-journald
```

---

### ✅ Step 4: Verify It's Working

Now check again:

```bash
ls -l /var/log/journal
```

✔️ You should now see a directory with your system’s machine ID inside it.

---

### ✅ Step 5: Configure Log Retention and Storage Limits

Open the configuration file:

```bash
sudo nano /etc/systemd/journald.conf
```

Uncomment and update the following:

```ini
Storage=persistent
SystemMaxUse=300M
SystemKeepFree=50M
SystemMaxFileSize=100M
MaxRetentionSec=2w
```

💾 Save and exit.

Apply changes:

```bash
sudo systemctl restart systemd-journald
```

---

### ✅ Step 6: Simulate a Reboot

Reboot your system:

```bash
sudo reboot
```

---

### ✅ Step 7: Verify Log Preservation After Reboot

After the system reboots, log back in and check:

```bash
journalctl -b -1
```

✔️ This command shows **logs from the previous boot** — proving that journaling is persistent!

---

## ✅ Output Checklist

| Task                                                     | Status (✔/❌) |
| -------------------------------------------------------- | ------------ |
| Verified `/var/log/journal` exists                       |              |
| Enabled journald persistent storage                      |              |
| Set disk usage and retention policies in `journald.conf` |              |
| Rebooted the system                                      |              |
| Verified logs survived reboot with `-b -1`               |              |

---

## 🔧 Optional: View Logs Across Multiple Boots

```bash
journalctl --list-boots
```

This shows boot IDs and timestamps:

```
-1  d9b1d7b... Sat 2025-07-12
 0  3a27d45... Sun 2025-07-13
```

View older boots:

```bash
journalctl -b -1
journalctl -b -2
```

---

## 🔐 Security Tip

Protect `/var/log/journal` permissions:

```bash
sudo chmod 750 /var/log/journal
sudo chown root:systemd-journal /var/log/journal
```

Only authorized users (e.g., `root`, `journalctl` group) should be able to read persistent logs.

---

## 📁 GitHub-Style Structure

```
/Preserve-Journald-Lab/
├── README.md
├── screenshots/
│   └── journald-verified.png
├── config/
│   └── journald.conf
├── scripts/
│   └── enable-persistence.sh
├── logs/
│   └── journalctl-b-1-output.txt
```

---

## 🧠 Reflect & Review

1. Why is persistent journaling important for forensic investigations?
2. What would happen if `/var/log/journal` is deleted?
3. How do you check logs from two boots ago?

---

## ✅ You Have Achieved

✔️ Journald persistence across reboots
✔️ Log retention and disk management
✔️ Log verification with real-world tools

> 🎯 This is foundational in **blue team operations**, **SIEM integration**, and **compliance** audits.

---

Would you like to:

* 📤 Export this as Markdown or PDF for your GitHub notes?
* 🔁 Run a Red Team simulation to test log persistence?
* 🧠 Take a quiz or certification-style challenge on journald?

Let’s go to the next one when you're ready, Shahid!
