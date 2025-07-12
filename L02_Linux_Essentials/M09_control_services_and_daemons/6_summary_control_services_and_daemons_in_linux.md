Certainly, Shahid! Here's your clean, professional, and GitHub-ready **summary** for:

---

# 📎 **Summary: Control Services and Daemons in Linux**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 297*

---

## 📖 Overview

This lesson taught you how to **control system services and background daemons** in Linux using the `systemctl` command. These services run critical components such as networking, firewalls, SSH, scheduled tasks, and more.

Managing these services is essential for:

* 📦 System reliability
* 🔐 Security hardening
* 🚀 Performance optimization
* 🧩 Service availability and control

---

## 🧠 Key Concepts

### 🔸 What is a Daemon?

A **daemon** is a background service process (like `sshd`, `cron`, `firewalld`) started during system boot or manually by a user/admin.

### 🔸 systemd

Modern Linux systems use **`systemd`** to manage services through **unit files** stored in:

* `/etc/systemd/system/`
* `/lib/systemd/system/`
* `/usr/lib/systemd/system/`

---

## ⚙️ Common Service States

| State      | Meaning                                       |
| ---------- | --------------------------------------------- |
| `active`   | Service is running                            |
| `inactive` | Service is stopped                            |
| `enabled`  | Will auto-start on boot                       |
| `disabled` | Will not auto-start on boot                   |
| `masked`   | Cannot be started (manually or automatically) |

---

## 🛠️ Commands You Learned

| Task                             | Command Example                   |
| -------------------------------- | --------------------------------- |
| Start a service                  | `sudo systemctl start sshd`       |
| Stop a service                   | `sudo systemctl stop sshd`        |
| Restart a service                | `sudo systemctl restart sshd`     |
| Reload config without restarting | `sudo systemctl reload sshd`      |
| Enable a service at boot         | `sudo systemctl enable sshd`      |
| Disable a service at boot        | `sudo systemctl disable sshd`     |
| Check if enabled                 | `systemctl is-enabled sshd`       |
| Check status                     | `systemctl status sshd`           |
| Mask (block) a service           | `sudo systemctl mask bluetooth`   |
| Unmask a service                 | `sudo systemctl unmask bluetooth` |
| View logs for a service          | `journalctl -u sshd`              |
| Check boot-time service delays   | `systemd-analyze blame`           |

---

## 🔐 Security & Hardening Tips

* **Mask** unnecessary services like `telnet`, `bluetooth`, or `cups`
* Only **enable** essential services at boot
* Use `journalctl` to **audit logs** of services for troubleshooting or security analysis
* Use `systemd-analyze blame` to detect slow services at boot

---

## ✅ You Can Now

* ✅ View and manage running services
* ✅ Enable or disable daemons at boot
* ✅ Mask and unmask services to harden systems
* ✅ Analyze logs and performance impact of services
* ✅ Control your system's behavior with confidence

---

## 📥 For GitHub or Portfolio?

Let me know — I’ll export this as a Markdown document with styling and structure ideal for your GitHub repo or cybersecurity resume folder.

---

⏭️ **Next Topic:** *System Logging and Journal Analysis*

You now control the heartbeat of your Linux system—its services and daemons. Excellent work, Shahid 🧠⚙️🔥 Let’s continue!
