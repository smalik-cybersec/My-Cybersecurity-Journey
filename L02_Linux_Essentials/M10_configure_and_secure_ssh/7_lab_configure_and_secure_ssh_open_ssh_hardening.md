# 🧪 Lab: Configure and Secure SSH (OpenSSH Hardening)

## 🎯 Objective

By the end of this lab, you will:

* Set up secure SSH key-based access
* Harden the SSH server configuration (`sshd_config`)
* Restrict users, change default ports, apply security policies
* Validate all changes with live connection testing

This lab simulates a **real-world Linux server hardening** task.

---

## 🧱 Lab Environment

| Component    | Details                                    |
| ------------ | ------------------------------------------ |
| SSH Server   | Ubuntu Server (or Debian-based)            |
| Client       | Kali Linux, Parrot OS, or any Linux distro |
| Network      | Private network or bridged VM setup        |
| Server IP    | `192.168.1.20` (example)                   |
| Client IP    | `192.168.1.10` (example)                   |
| User Account | `shahid`                                   |

---

## 📦 Prerequisites

* OpenSSH server installed:

  ```bash
  sudo apt install openssh-server
  ```

* SSH service running:

  ```bash
  sudo systemctl status ssh
  ```

* At least one non-root sudo user on the server (`shahid`)

---

## 🛠️ Lab Tasks

---

### ✅ Task 1: Generate SSH Key Pair (on Client)

```bash
ssh-keygen -t rsa -b 4096 -C "shahid@lab"
```

> Accept default file location `~/.ssh/id_rsa` and optionally set a passphrase.

---

### ✅ Task 2: Configure Key-Based Authentication (Server)

Use:

```bash
ssh-copy-id shahid@192.168.1.20
```

Or manually:

```bash
cat ~/.ssh/id_rsa.pub | ssh shahid@192.168.1.20 "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

✅ Test key-only login:

```bash
ssh shahid@192.168.1.20
```

---

### ✅ Task 3: Backup SSH Configuration File

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
```

---

### ✅ Task 4: Edit and Harden sshd\_config

Edit:

```bash
sudo nano /etc/ssh/sshd_config
```

Update/Add the following:

```ini
Port 2222
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
AllowUsers shahid
LoginGraceTime 30
ClientAliveInterval 60
ClientAliveCountMax 2
Banner /etc/issue.net
LogLevel VERBOSE
```

---

### ✅ Task 5: Create Legal Warning Banner

```bash
sudo nano /etc/issue.net
```

Add:

```
⚠️ WARNING: Unauthorized access is strictly prohibited. Activity is monitored and logged.
```

---

### ✅ Task 6: Set Correct Permissions

On server:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

---

### ✅ Task 7: Restart SSH and Validate Config

```bash
sudo sshd -t      # Check for syntax errors
sudo systemctl restart ssh
```

✅ From client:

```bash
ssh -p 2222 shahid@192.168.1.20
```

> Confirm:
>
> * Passwordless login works
> * Banner is displayed
> * Login is successful
> * Root and unauthorized users are blocked

---

### ✅ Task 8: Monitor SSH Logs (Optional)

```bash
sudo tail -f /var/log/auth.log
```

---

## 🔐 Security Checklist

| Configuration Item                 | Verified ✔/❌ |
| ---------------------------------- | ------------ |
| SSH key-based login working        |              |
| Root login disabled                |              |
| Password authentication disabled   |              |
| Port changed from 22 to 2222       |              |
| Only `shahid` user allowed         |              |
| Banner displays before login       |              |
| Permissions correctly set          |              |
| SSH service restarted successfully |              |

---

## 🧠 Lab Questions

1. Why is it important to change the default SSH port?
2. What risks are associated with leaving `PasswordAuthentication` enabled?
3. How does `ClientAliveInterval` improve session security?
4. What should you do if you accidentally break `sshd_config`?

---

## 📁 GitHub-Ready Lab Structure

```
/SSH-Hardening-Lab/
├── README.md
├── sshd_config/
│   ├── original_sshd_config.bak
│   └── hardened_sshd_config
├── key_setup/
│   └── ssh_keygen_output.txt
├── banner/
│   └── issue.net
├── tests/
│   └── connection_test_results.txt
├── screenshots/
└── logs/
    └── auth.log
```

---

## 📝 Deliverables

* Hardened `sshd_config` (copy into GitHub or PDF)
* Screenshots of:

  * SSH key login
  * Connection with banner
  * Rejection of root login
* Optional: record session using `asciinema` or video

---

## ✅ Summary

This lab gave you hands-on practice with:

* SSH key authentication setup
* SSH daemon configuration and hardening
* Testing secure connections
* Using logging and banners for compliance
* Preventing brute-force and unauthorized access

> 🔒 This is a **must-have skill** for roles in system administration, red teaming, DevSecOps, and cloud security.
