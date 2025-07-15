# 🧪 Guided Exercise: Access the Remote Command Line using SSH

## 🎯 Exercise Objective

By the end of this exercise, you will:

* Establish a secure SSH connection to a remote Linux machine.
* Use both password-based and key-based authentication.
* Execute remote commands securely.
* Gain practical experience in using SSH for administration and security tasks.

---

## 🧠 Prerequisites

| Requirement                       | Notes                                             |
| --------------------------------- | ------------------------------------------------- |
| Two Linux machines (VMs or Cloud) | One as **Client**, one as **SSH Server**          |
| SSH installed on both             | Usually pre-installed. Can check with `which ssh` |
| Network access between machines   | Use `ping <IP>` to test connectivity              |
| sudo privileges on both machines  | Needed to install/start `sshd` or edit configs    |

---

## ⚙️ Environment Setup

Assume:

* **Client Machine (Kali or Ubuntu Desktop):**

  * IP: `192.168.1.10`
* **Server Machine (Ubuntu Server):**

  * IP: `192.168.1.20`
  * SSH installed and enabled

### Step 1: Install/OpenSSH Server (on remote/server)

```bash
sudo apt update
sudo apt install openssh-server -y
sudo systemctl enable ssh
sudo systemctl start ssh
```

### Step 2: Check SSH Status

```bash
sudo systemctl status ssh
```

You should see: `Active (running)`

---

## 🔐 Step-by-Step Exercise Tasks

---

### ✅ Task 1: Connect Remotely via Password-Based SSH

**From the client machine:**

```bash
ssh username@192.168.1.20
```

Example:

```bash
ssh shahid@192.168.1.20
```

🔒 You'll be prompted to enter the password for the user.

✅ Once connected, try a few commands:

```bash
hostname
whoami
uptime
```

---

### ✅ Task 2: Enable Key-Based Authentication (More Secure)

#### 1. Generate an SSH Key Pair (Client Side)

```bash
ssh-keygen -t rsa -b 4096 -C "shahid@yourdomain.com"
```

✅ Keep pressing **Enter** to accept defaults. The key is saved in `~/.ssh/id_rsa` (private) and `~/.ssh/id_rsa.pub` (public).

---

#### 2. Copy Public Key to Server

```bash
ssh-copy-id shahid@192.168.1.20
```

✅ This command adds your public key to the server’s `~/.ssh/authorized_keys`.

---

#### 3. Log in Again (Now Key-Based, No Password)

```bash
ssh shahid@192.168.1.20
```

⚡ You should be logged in **without password**.

---

### ✅ Task 3: Execute a Remote Command Without Logging In

```bash
ssh shahid@192.168.1.20 "uname -a"
ssh shahid@192.168.1.20 "uptime"
```

✅ Output should appear directly in your client terminal.

---

## 🛡️ Optional: Secure Your SSH Server

> If time allows, perform one or more of these actions on the **remote server**:

* Edit SSH config:

  ```bash
  sudo nano /etc/ssh/sshd_config
  ```

  * Disable root login:

    ```ini
    PermitRootLogin no
    ```

  * Change default port:

    ```ini
    Port 2222
    ```

* Restart SSH:

  ```bash
  sudo systemctl restart ssh
  ```

---

## 🚀 Challenge Task (Advanced)

Set up a **custom SSH config file** on the client machine to simplify repeated connections.

Edit `~/.ssh/config`:

```ini
Host webserver
    HostName 192.168.1.20
    User shahid
    Port 22
    IdentityFile ~/.ssh/id_rsa
```

Now you can simply run:

```bash
ssh webserver
```

---

## ✅ Verification Checklist

| Task                                           | Completed (✔/❌) |
| ---------------------------------------------- | --------------- |
| Installed SSH server and started the service   |                 |
| Connected using password-based SSH             |                 |
| Generated SSH key pair on client               |                 |
| Set up key-based authentication                |                 |
| Logged in without password                     |                 |
| Ran remote commands from client                |                 |
| (Optional) Hardened the SSH server             |                 |
| (Optional) Created an SSH config for shortcuts |                 |

---

## 📌 Notes & Tips

* Never share your **private key** (`id_rsa`).
* Always set proper file permissions:

  ```bash
  chmod 600 ~/.ssh/id_rsa
  chmod 700 ~/.ssh
  ```

* In cloud environments (like AWS), SSH access is often done using `.pem` files (we’ll cover this separately).

---

## 🧠 Reflection Questions

* Why is key-based SSH more secure than password-based login?
* What risks are associated with leaving the root account SSH-accessible?
* What would happen if your private key is leaked?

---
