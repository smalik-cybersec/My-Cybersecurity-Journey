Perfect progression, Shahid.
You’re now entering the **hands-on practical application** of the SSH Key-Based Authentication lesson:

> **Guided Exercise:** Configure SSH Key-Based Authentication
> **Page Ref:** \~317
> **Context:** Practice generating, deploying, securing, and testing SSH keys in a real-world lab environment.

Here’s your **professional, GitHub-ready Guided Exercise chapter**, formatted cleanly for real-world documentation, labs, or a recruiter-facing project repo.

---

# 🧪 Guided Exercise: Configure SSH Key-Based Authentication

## 🎯 Objective

This guided exercise helps you **securely configure SSH Key-Based Authentication** between a client and a remote server. You will:

* Generate SSH key pairs
* Deploy public keys to a remote server
* Configure permissions
* Test secure passwordless login
* (Optional) Disable password-based login for maximum security

---

## 🧱 Lab Environment

| Component     | Role                 | Example IP   |
| ------------- | -------------------- | ------------ |
| **Client VM** | User’s local machine | 192.168.1.10 |
| **Server VM** | Remote Linux server  | 192.168.1.20 |

> 📌 You can use VirtualBox/VMware or cloud instances (AWS EC2, DigitalOcean, etc.)

---

## 📦 Prerequisites

* SSH server (`openssh-server`) installed and running on the remote server
* SSH client tools installed on your local system (default on most Linux distros)
* sudo privileges on both machines
* Basic networking connectivity (verify with `ping`)

---

## 🧰 Step-by-Step Instructions

---

### ✅ Step 1: Generate SSH Key Pair (On Client Machine)

```bash
ssh-keygen -t rsa -b 4096 -C "shahid@yourdomain.com"
```

* Press **Enter** to accept default file location: `~/.ssh/id_rsa`
* Set a **passphrase** for added security (optional but recommended)

✅ **Output:**

* Private key: `~/.ssh/id_rsa`
* Public key: `~/.ssh/id_rsa.pub`

---

### ✅ Step 2: Deploy Public Key to Remote Server

#### Option A: Using `ssh-copy-id` (Recommended)

```bash
ssh-copy-id shahid@192.168.1.20
```

> This securely appends your public key to the server’s `~/.ssh/authorized_keys` file.

#### Option B: Manual Method (if `ssh-copy-id` is not available)

```bash
cat ~/.ssh/id_rsa.pub | ssh shahid@192.168.1.20 "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

---

### ✅ Step 3: Set Correct Permissions (On Remote Server)

SSH will **refuse to authenticate** if these file permissions are too loose.

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

---

### ✅ Step 4: Test SSH Key-Based Authentication

From your client machine:

```bash
ssh shahid@192.168.1.20
```

✅ If everything is set correctly, you'll connect **without being prompted for a password**.

---

### ✅ Step 5 (Optional): Disable Password Authentication on SSH Server

> ⚠️ **Only do this once key-based login is fully working.**

#### Edit the SSH daemon configuration:

```bash
sudo nano /etc/ssh/sshd_config
```

Update the following lines:

```ini
PasswordAuthentication no
PubkeyAuthentication yes
PermitRootLogin no
```

#### Restart SSH to apply changes:

```bash
sudo systemctl restart ssh
```

---

## 🔒 Security Checklist

| Item                                    | Completed |
| --------------------------------------- | --------- |
| Key pair generated                      | ✔ / ❌     |
| Public key copied to server             | ✔ / ❌     |
| Correct file permissions set            | ✔ / ❌     |
| Passwordless SSH login verified         | ✔ / ❌     |
| Password login disabled on server (opt) | ✔ / ❌     |

---

## 💡 Optional SSH Config Shortcut (Client Side)

Add a shortcut profile in `~/.ssh/config`:

```ini
Host myserver
    HostName 192.168.1.20
    User shahid
    IdentityFile ~/.ssh/id_rsa
```

Connect using:

```bash
ssh myserver
```

---

## 🧠 Reflection Questions

1. Why is SSH key authentication considered more secure than passwords?
2. What happens if your private key is stolen?
3. Why must permissions on `~/.ssh` and `authorized_keys` be strict?

---

## 📂 GitHub-Ready Folder Structure (Sample)

```
/SSH-Key-Auth-Lab/
├── README.md
├── ssh_keygen_steps.md
├── server_config_checklist.md
├── screenshots/
│   ├── ssh_keygen.png
│   ├── ssh_copy_id.png
│   ├── successful_login.png
└── ssh_config_example
```

---

## ✅ Summary

This exercise taught you how to:

* Generate and manage SSH key pairs
* Authenticate to servers securely without passwords
* Lock down remote access using cryptographic credentials

> 🔐 This is **standard practice** in DevOps, cloud engineering, ethical hacking, and system administration.

---

Would you like me to:

* Export this as `.md` for your GitHub repo?
* Create a **real-world task challenge** (e.g., “Automate secure backup over SSH”)?
* Move on to the next topic from your syllabus?

I’m ready when you are, Shahid.
