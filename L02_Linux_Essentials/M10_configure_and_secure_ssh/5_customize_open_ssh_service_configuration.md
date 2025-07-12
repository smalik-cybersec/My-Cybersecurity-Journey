Excellent, Shahid.
You're now approaching a **critical administrative and security skill**:

> **Lesson:** Customize OpenSSH Service Configuration
> **Page Ref:** \~323
> **Context:** Part of securing and optimizing SSH access across production environments.

This lesson focuses on customizing the behavior of the **SSH daemon (`sshd`)**, which governs how your server handles remote access. These configurations are **vital for security, compliance, and operational control**.

---

# ⚙️ Customize OpenSSH Service Configuration

## 📌 Chapter Overview

OpenSSH allows fine-tuned control over remote access via its configuration file: `/etc/ssh/sshd_config`. This lesson explores how to **safely customize, secure, and optimize** the SSH service for your organization or personal server.

> 🎯 **Goal:** Learn how to configure OpenSSH server settings like port number, login permissions, authentication methods, banners, timeouts, and logging.

---

## 📚 Table of Contents

- [⚙️ Customize OpenSSH Service Configuration](#️-customize-openssh-service-configuration)
  - [📌 Chapter Overview](#-chapter-overview)
  - [📚 Table of Contents](#-table-of-contents)
  - [🔍 What is `sshd` and `sshd_config`?](#-what-is-sshd-and-sshd_config)
    - [🔑 File Path](#-file-path)
  - [📌 Default Configuration Location](#-default-configuration-location)
  - [🛠 Essential Customization Parameters](#-essential-customization-parameters)
  - [🔐 Security-Hardening Settings](#-security-hardening-settings)
  - [🔄 Restarting the SSH Service](#-restarting-the-ssh-service)
  - [🧪 Testing Before Lock-In (Important!)](#-testing-before-lock-in-important)
  - [🧪 Lab Exercises](#-lab-exercises)
    - [🔬 Lab 1: Change Default SSH Port](#-lab-1-change-default-ssh-port)
    - [🔬 Lab 2: Disable Root Login and Password Auth](#-lab-2-disable-root-login-and-password-auth)
    - [🔬 Lab 3: Add a Login Banner](#-lab-3-add-a-login-banner)
  - [🧠 Quiz and Knowledge Check](#-quiz-and-knowledge-check)
  - [📁 GitHub Sample Layout](#-github-sample-layout)
  - [✅ Summary](#-summary)

---

## 🔍 What is `sshd` and `sshd_config`?

* **`sshd`**: The **OpenSSH server daemon** that handles incoming SSH connections.
* **`sshd_config`**: The main **configuration file** for controlling SSH server behavior.

### 🔑 File Path

```bash
/etc/ssh/sshd_config
```

> Modifying this file directly affects **how clients connect**, authenticate, and interact with your server over SSH.

---

## 📌 Default Configuration Location

| Component     | Path                     | Purpose                              |
| ------------- | ------------------------ | ------------------------------------ |
| Main config   | `/etc/ssh/sshd_config`   | Daemon-level settings                |
| Client config | `~/.ssh/config`          | Per-user shortcuts and overrides     |
| Key storage   | `~/.ssh/authorized_keys` | List of public keys allowed per user |

---

## 🛠 Essential Customization Parameters

Here are **commonly customized parameters** in `/etc/ssh/sshd_config`:

| Directive                | Description                                      | Example                     |
| ------------------------ | ------------------------------------------------ | --------------------------- |
| `Port`                   | Change default port (22) to reduce bot scans     | `Port 2222`                 |
| `PermitRootLogin`        | Disable direct root login (recommended)          | `PermitRootLogin no`        |
| `PasswordAuthentication` | Enable/disable password login                    | `PasswordAuthentication no` |
| `PubkeyAuthentication`   | Enable key-based authentication                  | `PubkeyAuthentication yes`  |
| `AllowUsers`             | Whitelist allowed SSH users                      | `AllowUsers shahid admin`   |
| `MaxAuthTries`           | Limit failed attempts before disconnecting       | `MaxAuthTries 3`            |
| `LoginGraceTime`         | Set timeout before auto-disconnect               | `LoginGraceTime 30`         |
| `ClientAliveInterval`    | Server pings client every N seconds              | `ClientAliveInterval 60`    |
| `ClientAliveCountMax`    | Disconnect if no reply after N pings             | `ClientAliveCountMax 3`     |
| `Banner`                 | Show custom legal or warning banner before login | `Banner /etc/issue.net`     |
| `LogLevel`               | Set SSH logging detail level                     | `LogLevel VERBOSE`          |

---

## 🔐 Security-Hardening Settings

These settings are highly recommended for **production** and **cybersecurity environments**:

```ini
Port 2222
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
AllowUsers shahid
MaxAuthTries 3
LoginGraceTime 20
ClientAliveInterval 60
ClientAliveCountMax 2
LogLevel VERBOSE
```

---

## 🔄 Restarting the SSH Service

After making changes:

```bash
sudo systemctl restart ssh
```

> 🧠 To verify SSH is running and listening:

```bash
sudo systemctl status ssh
sudo netstat -tulnp | grep ssh
```

---

## 🧪 Testing Before Lock-In (Important!)

Always test new settings **in a separate SSH session** before closing the existing one.

```bash
ssh shahid@192.168.1.100 -p 2222
```

✅ This avoids being **locked out** if something breaks.

Use:

```bash
sudo sshd -t
```

✅ To **test syntax** of your changes before restarting the service.

---

## 🧪 Lab Exercises

> ⏱ Duration: \~45 minutes

---

### 🔬 Lab 1: Change Default SSH Port

1. Edit `/etc/ssh/sshd_config`:

   ```ini
   Port 2222
   ```
2. Restart service:

   ```bash
   sudo systemctl restart ssh
   ```
3. Connect using:

   ```bash
   ssh -p 2222 shahid@192.168.1.100
   ```

---

### 🔬 Lab 2: Disable Root Login and Password Auth

Edit `/etc/ssh/sshd_config`:

```ini
PermitRootLogin no
PasswordAuthentication no
```

Ensure key-based login is working, then restart SSH.

---

### 🔬 Lab 3: Add a Login Banner

1. Create banner message:

```bash
sudo nano /etc/issue.net
```

Example:

```
WARNING: Authorized Users Only. Unauthorized access is a criminal offense.
```

2. Edit SSH config:

```ini
Banner /etc/issue.net
```

3. Restart SSH and test by reconnecting.

---

## 🧠 Quiz and Knowledge Check

**Q1.** What is the default SSH configuration file path?
→ `/etc/ssh/sshd_config`

**Q2.** How do you prevent root user from logging in via SSH?
→ `PermitRootLogin no`

**Q3.** Which directive changes the default port for SSH?
→ `Port`

**Q4.** What does `ClientAliveInterval` control?
→ The time interval for server-to-client keep-alive messages.

**Q5.** True or False: You must restart SSH service after editing `sshd_config`.
→ ✅ True

---

## 📁 GitHub Sample Layout

```
/OpenSSH-Server-Config/
├── README.md
├── sshd_config_examples/
│   ├── hardened_config.txt
│   ├── custom_banner.txt
├── lab_instructions/
│   ├── change_port.md
│   ├── disable_passwords.md
│   └── set_banner.md
├── screenshots/
└── backup_configs/
    └── sshd_config_original.bak
```

---

## ✅ Summary

OpenSSH's configuration file is your **control center** for remote access. By customizing `sshd_config`, you:

* Harden your system against brute force and privilege escalation
* Control who logs in and how
* Set policies for timeout, logging, and authentication methods
* Prepare your system for production-grade deployments

> 🔐 This is a **core skill** for cybersecurity professionals, system administrators, red teamers, and cloud engineers.

---

Let me know if you'd like:

* 📦 Export as `.md` or `.pdf`
* 🧱 Add a mini-project (e.g., Harden an SSH jump box)
* ▶️ Visual diagrams of SSH workflow and config file mapping
* ✅ Move on to the next lesson

Ready for your next command, Shahid.
