Perfect, Shahid.
You’re now studying one of the **most secure and job-critical skills** for remote access:

> **Lesson:** Configure SSH Key-based Authentication
> **Page Ref:** \~311
> **Context:** Deep-dive into replacing insecure password authentication with **cryptographic key pairs**, a best practice in DevOps, cloud, and cybersecurity.

---

Below is the **professional, comprehensive, and GitHub-ready documentation** for this lesson.

---

# 🔐 Configure SSH Key-Based Authentication

## 📌 Chapter Overview

SSH Key-Based Authentication replaces traditional password login with **public-private key cryptography**. It drastically increases security, enables automation, and is considered a **best practice** across cybersecurity, Linux administration, cloud engineering, and DevOps roles.

> 🎯 **Objective:** Learn to generate SSH key pairs, configure key-based login, enforce key-only authentication, and secure SSH access like a pro.

---

## 📚 Table of Contents

- [🔐 Configure SSH Key-Based Authentication](#-configure-ssh-key-based-authentication)
  - [📌 Chapter Overview](#-chapter-overview)
  - [📚 Table of Contents](#-table-of-contents)
  - [🔐 What is Key-Based Authentication?](#-what-is-key-based-authentication)
  - [⚙️ How It Works](#️-how-it-works)
  - [🪜 Step-by-Step Setup](#-step-by-step-setup)
  - [💻 Client-Side Configuration](#-client-side-configuration)
    - [✅ Step 1: Generate SSH Key Pair](#-step-1-generate-ssh-key-pair)
    - [✅ Step 2: Copy Public Key to Server](#-step-2-copy-public-key-to-server)
      - [Option 1: Using `ssh-copy-id` (Recommended)](#option-1-using-ssh-copy-id-recommended)
      - [Option 2: Manual Method](#option-2-manual-method)
  - [🖥️ Server-Side Configuration](#️-server-side-configuration)
    - [✅ Step 3: Set Correct Permissions](#-step-3-set-correct-permissions)
    - [✅ Step 4: Test Key-Based SSH Login](#-step-4-test-key-based-ssh-login)
  - [🚫 Optional: Lock Down Password Access](#-optional-lock-down-password-access)
  - [🔐 Best Practices](#-best-practices)
  - [🧪 Lab Exercises](#-lab-exercises)
    - [🔬 Lab 1: Generate and Deploy SSH Key Pair](#-lab-1-generate-and-deploy-ssh-key-pair)
    - [🔬 Lab 2: Enforce Key-Only Authentication](#-lab-2-enforce-key-only-authentication)
    - [🔬 Lab 3: SSH Profile in `.ssh/config`](#-lab-3-ssh-profile-in-sshconfig)
  - [🛠️ Troubleshooting Common Issues](#️-troubleshooting-common-issues)
  - [🧠 Quiz \& Knowledge Check](#-quiz--knowledge-check)
  - [🎯 Real-World Security Applications](#-real-world-security-applications)
  - [📁 GitHub-Ready Sample Layout](#-github-ready-sample-layout)
  - [✅ Summary](#-summary)

---

## 🔐 What is Key-Based Authentication?

Instead of typing a password, the client proves its identity using a **cryptographic key pair**.

* **Private Key** → Kept secret on the client machine
* **Public Key** → Uploaded to the server (`authorized_keys`)

✅ Authentication happens automatically if the keys match.

| Feature         | Password-Based            | Key-Based                        |
| --------------- | ------------------------- | -------------------------------- |
| Security        | Vulnerable to brute-force | Strong, cryptographically secure |
| Automation      | Difficult                 | Easy and scriptable              |
| User Experience | Manual input required     | One-click or no-interaction      |
| Common In       | Legacy systems            | Cloud, DevOps, secure systems    |

---

## ⚙️ How It Works

1. Client connects to server over SSH.
2. Server checks if the client has a valid **private key** matching one in its `authorized_keys` file.
3. If yes, connection is granted **without asking for a password**.
4. If not, access is denied.

💡 This is called **asymmetric encryption**, where the private key never leaves the client.

---

## 🪜 Step-by-Step Setup

> These steps apply to **Linux/macOS systems**. For Windows, see [PuTTY + Pageant](#windows-users-note).

---

## 💻 Client-Side Configuration

### ✅ Step 1: Generate SSH Key Pair

```bash
ssh-keygen -t rsa -b 4096 -C "shahid@domain.com"
```

* When prompted:

  * **File location?** Press Enter to use default (`~/.ssh/id_rsa`)
  * **Passphrase?** Optional (adds extra security)

**Result:**

* `~/.ssh/id_rsa` → Your private key (keep safe!)
* `~/.ssh/id_rsa.pub` → Your public key

---

### ✅ Step 2: Copy Public Key to Server

#### Option 1: Using `ssh-copy-id` (Recommended)

```bash
ssh-copy-id shahid@192.168.1.100
```

* This appends your public key to `~/.ssh/authorized_keys` on the server.

#### Option 2: Manual Method

```bash
cat ~/.ssh/id_rsa.pub | ssh shahid@192.168.1.100 "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

---

## 🖥️ Server-Side Configuration

### ✅ Step 3: Set Correct Permissions

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

🔒 SSH will **refuse to connect** if these permissions are too open.

---

### ✅ Step 4: Test Key-Based SSH Login

From the client machine:

```bash
ssh shahid@192.168.1.100
```

✅ You should now connect **without typing a password**.

---

## 🚫 Optional: Lock Down Password Access

To **enforce key-only login** (after key-based access is confirmed):

1. Open the SSH server config:

```bash
sudo nano /etc/ssh/sshd_config
```

2. Modify/add the following:

```ini
PasswordAuthentication no
PermitRootLogin no
PubkeyAuthentication yes
```

3. Restart SSH service:

```bash
sudo systemctl restart ssh
```

⚠️ **Important:** Only do this **after** verifying that key-based login works. Otherwise, you may lock yourself out.

---

## 🔐 Best Practices

| Practice                            | Why It Matters                           |
| ----------------------------------- | ---------------------------------------- |
| Use strong key size (e.g. 4096-bit) | Harder to crack                          |
| Protect private key with passphrase | Adds layer in case the key is stolen     |
| Rotate keys periodically            | Prevent long-term key compromise         |
| Never share private key             | Even internally—always generate new keys |
| Use `.ssh/config` for profiles      | Manage multiple SSH servers easily       |
| Store private keys securely         | Use encrypted disk or tools like `gpg`   |

---

## 🧪 Lab Exercises

> ⏱ Estimated Time: 30–45 minutes

### 🔬 Lab 1: Generate and Deploy SSH Key Pair

* Generate key on client
* Use `ssh-copy-id` to upload
* Verify login without password

### 🔬 Lab 2: Enforce Key-Only Authentication

* Edit `sshd_config` on server
* Disable password authentication
* Restart SSH and test access

### 🔬 Lab 3: SSH Profile in `.ssh/config`

Example:

```ini
Host bastion
    HostName 192.168.1.100
    User shahid
    IdentityFile ~/.ssh/id_rsa
```

Then connect using:

```bash
ssh bastion
```

---

## 🛠️ Troubleshooting Common Issues

| Issue                           | Solution                                           |
| ------------------------------- | -------------------------------------------------- |
| `Permission denied (publickey)` | Check key permissions and user ownership           |
| Server ignores key              | Check `sshd_config` has `PubkeyAuthentication yes` |
| Key file has wrong permissions  | Set `chmod 600 ~/.ssh/id_rsa`                      |
| Wrong username or IP            | Double-check `ssh username@host` format            |
| Firewall/port blocking          | Ensure port 22 (or custom) is open                 |

---

## 🧠 Quiz & Knowledge Check

**Q1.** Which file holds the public key on the client?
→ `~/.ssh/id_rsa.pub`

**Q2.** Where is the server’s list of authorized keys stored?
→ `~/.ssh/authorized_keys`

**Q3.** How do you generate a key with a custom comment/email?
→ `ssh-keygen -t rsa -b 4096 -C "comment"`

**Q4.** What permissions should `authorized_keys` have?
→ `600`

**Q5.** True or False: It's safe to share your public key.
→ ✅ True

---

## 🎯 Real-World Security Applications

* 🔐 **Cloud Infrastructure:** AWS EC2, Azure VMs use key-based login by default
* ⚙️ **CI/CD pipelines:** Automate Git/GitHub/remote deployments securely
* 🛡️ **Red Teaming:** Persist on compromised systems with dropped public keys
* 🚫 **Root Hardening:** Allow admin login only via secured keys
* 🔗 **SSH Tunnels:** Use keys to authenticate jump boxes / bastion hosts

---

## 📁 GitHub-Ready Sample Layout

```
/SSH-Key-Authentication/
├── README.md
├── setup_instructions.md
├── lab_solutions/
│   ├── generate_key.md
│   ├── ssh_copy_id.md
│   └── lock_down_passwords.md
├── screenshots/
│   └── ssh-success.png
├── ssh_config_example
```

---

## ✅ Summary

SSH key-based authentication is:

* **Secure** (cryptographically stronger than passwords)
* **Scriptable** (great for automation)
* **Standard** for professionals

As a cybersecurity practitioner, this skill will serve you in:

* Cloud
* Linux admin
* Automation
* DevSecOps
* Pentesting

---

Let me know if you'd like:

* 📦 Export as `.md` or `.pdf`
* 🧱 Mini-project (e.g. Build your own Bastion Host with SSH keys)
* Next topic from the syllabus

Ready for the next one when you are, Shahid.
