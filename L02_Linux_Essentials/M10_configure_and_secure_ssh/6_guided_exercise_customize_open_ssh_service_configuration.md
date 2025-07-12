Excellent continuation, Shahid.
This **Guided Exercise** gives you hands-on experience in securing and customizing SSH via `sshd_config`.
Think of this as your **real-world practice in Linux server hardening**—something every cybersecurity and DevOps professional is expected to master.

---

# 🧪 Guided Exercise: Customize OpenSSH Service Configuration

## 🎯 Objective

This exercise guides you through **editing and securing the SSH daemon configuration (`sshd_config`)**. You’ll apply key security best practices, change the SSH port, restrict user access, and configure a legal banner—turning a default server into a hardened system.

---

## 🧱 Lab Setup

| Role       | Machine Type                       | Example IP   |
| ---------- | ---------------------------------- | ------------ |
| SSH Server | Ubuntu/Debian VM or Cloud Instance | 192.168.1.20 |
| SSH Client | Kali Linux / Ubuntu Desktop        | 192.168.1.10 |

✅ **SSH must already be installed and running** on the server.
Use: `sudo apt install openssh-server`

---

## ⚠️ Safety Notice

Always test new SSH settings in a **parallel SSH session** or **out-of-band console** to avoid getting locked out.

---

## 🛠️ Exercise Instructions

---

### ✅ Task 1: Backup the SSH Configuration

Always back up before making changes:

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
```

✅ If something goes wrong, you can restore it using:

```bash
sudo mv /etc/ssh/sshd_config.bak /etc/ssh/sshd_config
```

---

### ✅ Task 2: Change the SSH Port

1. Open the configuration file:

```bash
sudo nano /etc/ssh/sshd_config
```

2. Find and change:

```ini
#Port 22
Port 2222
```

3. Restart SSH:

```bash
sudo systemctl restart ssh
```

4. Test new connection:

```bash
ssh -p 2222 shahid@192.168.1.20
```

---

### ✅ Task 3: Disable Root Login

In `sshd_config`, set:

```ini
PermitRootLogin no
```

✔️ This prevents attackers from brute-forcing root access.

---

### ✅ Task 4: Enforce Key-Based Authentication

In `sshd_config`, ensure:

```ini
PasswordAuthentication no
PubkeyAuthentication yes
```

✔️ Only users with matching public/private key pairs will be allowed to connect.

---

### ✅ Task 5: Whitelist Allowed Users

Add:

```ini
AllowUsers shahid
```

✅ This blocks all other users from connecting via SSH.

---

### ✅ Task 6: Set Idle Timeout & Login Grace Period

In the config file, set:

```ini
LoginGraceTime 30
ClientAliveInterval 60
ClientAliveCountMax 2
```

✔️ These settings:

* Limit how long a user has to log in
* Automatically disconnect inactive sessions

---

### ✅ Task 7: Add a Legal Login Banner

1. Create banner file:

```bash
sudo nano /etc/issue.net
```

Add content:

```
WARNING: Unauthorized access is prohibited. All activity is logged.
```

2. In `sshd_config`:

```ini
Banner /etc/issue.net
```

3. Save, and restart SSH again:

```bash
sudo systemctl restart ssh
```

---

### ✅ Task 8: Verify Configuration Syntax

Run this to catch any typos:

```bash
sudo sshd -t
```

✅ If no output, config is valid.

---

## 🧪 Post-Configuration Test

Open a **new terminal** and try logging in with:

```bash
ssh -p 2222 shahid@192.168.1.20
```

> ✅ Confirm:
>
> * Password login is blocked
> * Root cannot log in
> * Banner message is displayed
> * You can still access using your key

---

## ✅ Completion Checklist

| Task                                       | Completed (✔/❌) |
| ------------------------------------------ | --------------- |
| SSH config backed up                       |                 |
| Port changed from 22 to 2222               |                 |
| Password login disabled                    |                 |
| Root login blocked                         |                 |
| User restriction applied                   |                 |
| Idle timeout + login grace time configured |                 |
| Custom banner created and shown            |                 |
| SSH service restarted and verified         |                 |

---

## 🧠 Reflective Questions

1. What could happen if you misconfigure SSH and restart without testing?
2. Why is disabling `root` login safer?
3. Why is changing the default SSH port not enough for full security?

---

## 📂 GitHub-Friendly Structure

```
/OpenSSH-Hardening-Lab/
├── README.md
├── backup/
│   └── sshd_config.bak
├── hardened_config/
│   └── sshd_config_hardened
├── banner/
│   └── issue.net
├── verification/
│   └── ssh_test_results.txt
└── screenshots/
```

---

## ✅ Summary

You’ve now **successfully hardened your OpenSSH service** using best practices. These changes help:

* Prevent brute-force and unauthorized access
* Control who can connect and how
* Add visibility through banners and logs
* Set your Linux systems up for **production-grade security**

> 🔐 This is an essential **Linux hardening and compliance skill**.

---

Let me know if you'd like:

* 📦 Export as `.md`
* 🎯 Add a **Red Team Simulation** (e.g., attacker tries to brute-force root)
* 🔁 Next lesson from the syllabus

I'm ready when you are, Shahid.
