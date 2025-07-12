Great follow-up, Shahid! Let's now **practice what you just learned** with a **hands-on Guided Exercise** on maintaining accurate system time.

> **🧪 Guided Exercise: Maintain Accurate Time**
> **Page Ref:** \~371
> **Objective:** Configure and verify time synchronization using `systemd-timesyncd` or another NTP tool to ensure your system clock remains accurate — a crucial skill in cybersecurity.

---

# 🧪 Guided Exercise: Maintain Accurate Time

---

## 🎯 Learning Objectives

By the end of this exercise, you will:

✅ Check your current system time status
✅ Enable and configure time synchronization
✅ Set the correct time zone
✅ Confirm that synchronization works, even after reboot

---

## 🛠️ Lab Requirements

| Requirement                            | Status |
| -------------------------------------- | ------ |
| Linux system (Ubuntu/Debian preferred) | ✅      |
| Internet connection                    | ✅      |
| `sudo` privileges                      | ✅      |

---

## 📋 Exercise Tasks

---

### ✅ Task 1: Check Current Time Settings

```bash
timedatectl status
```

🧠 **What to observe:**

* `Time zone` (Is it correct?)
* `NTP service` (active or inactive?)
* `System clock synchronized` (yes or no?)

---

### ✅ Task 2: Set Correct Time Zone

If you’re in India, run:

```bash
sudo timedatectl set-timezone Asia/Kolkata
```

To verify:

```bash
timedatectl
```

---

### ✅ Task 3: Enable and Start Time Synchronization

Start the NTP sync service:

```bash
sudo systemctl enable --now systemd-timesyncd
```

Check its status:

```bash
systemctl status systemd-timesyncd
```

---

### ✅ Task 4: Configure Custom NTP Servers (Optional)

Edit the config file:

```bash
sudo nano /etc/systemd/timesyncd.conf
```

Update/add this section:

```ini
[Time]
NTP=0.in.pool.ntp.org 1.in.pool.ntp.org
FallbackNTP=2.in.pool.ntp.org 3.in.pool.ntp.org
```

Restart the service:

```bash
sudo systemctl restart systemd-timesyncd
```

---

### ✅ Task 5: Confirm Synchronization

```bash
timedatectl status
```

✔ You should now see:

* `System clock synchronized: yes`
* `NTP service: active`

---

### ✅ Task 6: Reboot & Verify

```bash
sudo reboot
```

After reboot:

```bash
timedatectl
```

✔ Confirm that the clock is still correct and synchronization is still active.

---

## ✅ Output Checklist

| Task Completed                               | ✔ / ❌ |
| -------------------------------------------- | ----- |
| Checked time and NTP sync with `timedatectl` |       |
| Set correct time zone                        |       |
| Enabled `systemd-timesyncd`                  |       |
| (Optional) Configured custom NTP servers     |       |
| Verified sync before and after reboot        |       |

---

## 🧠 Reflection Questions

1. Why must logs from multiple servers have synchronized time?
2. What would happen if your system clock drifts by a few minutes?
3. What does `System clock synchronized: no` indicate?
4. What’s the difference between hardware clock and system clock?

---

## 🗂 GitHub-Style Directory Layout

```
/Guided-Maintain-Accurate-Time/
├── README.md
├── screenshots/
│   └── timedatectl-status.png
├── config/
│   └── timesyncd.conf
├── logs/
│   └── pre-and-post-reboot-time.txt
├── scripts/
│   └── sync_time.sh
```

---

## 🏁 End of Exercise Summary

You have now successfully:

* Verified and set your time zone
* Enabled reliable system time syncing
* Verified synchronization before and after reboot
* Configured optional custom NTP servers

> ⏰ Maintaining accurate time is vital for logs, security, authentication, and forensic accuracy. This makes you a reliable defender in a networked environment.

---

Would you like:

* 🧪 A challenge lab simulating a system with time drift?
* 📄 Markdown version for GitHub?
* 🧠 Quiz for revision?

Let me know when you're ready for the next chapter, Shahid! You're doing amazing, mashaAllah.
