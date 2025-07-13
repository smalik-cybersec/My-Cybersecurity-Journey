# 🧪 **Guided Exercise: Gain Superuser Access**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 166*

---

## 🎯 Objective

To practice how to **safely and correctly gain superuser (root) access** in a Linux system using both `sudo` and `su`, and understand how to manage superuser permissions through the `sudoers` file.

> This skill is **critical** for administrative tasks, secure system operations, and cyber incident handling.

---

## 🧰 Prerequisites

* A Linux system (with Bash)
* A user account with `sudo` privileges (or access to root)
* A text editor (like `nano`, `vim`, or `visudo`)
* Basic CLI experience

---

## 🧭 Step-by-Step Instructions

---

### 🔹 **Step 1: Check Current Privileges**

```bash
whoami
id
groups
```

✅ This confirms your username, UID, and whether you’re in a group like `sudo` or `wheel`.

---

### 🔹 **Step 2: Attempt a Root-Level Command Without `sudo`**

Try running a restricted command (e.g., viewing system logs):

```bash
cat /etc/shadow
```

❌ You should get a **"Permission denied"** error if not root.

---

### 🔹 **Step 3: Run the Same Command Using `sudo`**

```bash
sudo cat /etc/shadow
```

✅ You will be prompted for **your own password**, and if successful, see the contents.

---

### 🔹 **Step 4: Switch to Root Shell Using `su -`**

```bash
su -
```

* Enter the **root password** (if you know it).
* If successful, your prompt should change to indicate you are now root (`#`).

Exit root shell:

```bash
exit
```

---

### 🔹 **Step 5: See What You Can Do with `sudo`**

```bash
sudo -l
```

✅ This lists all commands you're allowed to run as `sudo`.

---

### 🔹 **Step 6: Add a User to the `sudo` Group (as root)**

If you're root or using `sudo`, run:

```bash
usermod -aG sudo shahid
```

Then verify:

```bash
groups shahid
```

✅ User `shahid` now has sudo privileges.

---

### 🔹 **Step 7: Safely Edit the `sudoers` File Using `visudo`**

```bash
sudo visudo
```

Inside the editor, find or add:

```bash
shahid ALL=(ALL) ALL
```

Save and exit (`Ctrl + X`, `Y`, `Enter` in nano).

> ✅ This allows full sudo access to user `shahid`.

---

### 🔹 **Step 8: Create a Passwordless Sudo Rule (Advanced)**

Inside `visudo`:

```bash
shahid ALL=(ALL) NOPASSWD: /sbin/reboot
```

✅ Now `shahid` can reboot the system without being asked for a password.

Test:

```bash
sudo /sbin/reboot   # (Use with caution or comment it out!)
```

---

## 📂 Real-World Example Scenario

| Task                | Command                                |
| ------------------- | -------------------------------------- |
| Install updates     | `sudo dnf update` or `sudo apt update` |
| Edit network config | `sudo nano /etc/hosts`                 |
| Add new user        | `sudo useradd analyst`                 |
| Restart a service   | `sudo systemctl restart sshd`          |

---

## 🧠 Reflection Questions

1. What is the difference between `sudo` and `su`?
2. How does `sudo -l` help you understand your privileges?
3. Why is it dangerous to work as root full-time?
4. Why should `visudo` be used instead of editing `/etc/sudoers` directly?
5. What is the benefit of using `NOPASSWD:` in a command-specific rule?

---

## ✅ Completion Checklist

| Task Performed                              | Status |
| ------------------------------------------- | ------ |
| Attempted privileged command without `sudo` | ✅      |
| Gained root access with `sudo`              | ✅      |
| Used `su -` to become root                  | ✅      |
| Checked `sudo` permissions with `sudo -l`   | ✅      |
| Modified `sudoers` safely with `visudo`     | ✅      |
| Tested real-world root-level tasks          | ✅      |

---

## 📎 Summary

You now know how to:

* Gain root access responsibly using `sudo` or `su`
* Check and manage `sudo` rights
* Edit the `sudoers` file using `visudo`
* Securely control system permissions without compromising auditability

> Superuser access gives you **total control**—but must be used with caution to maintain **system integrity and security**.
