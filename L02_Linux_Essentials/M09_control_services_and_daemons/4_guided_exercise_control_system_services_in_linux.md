# 🧪 **Guided Exercise: Control System Services in Linux**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 293*

---

## 🎯 Objective

In this lab, you will:

* Start, stop, enable, disable, restart, and reload services using `systemctl`
* Understand how to mask and unmask services
* Check and interpret service status
* Practice managing real system services (like `sshd`, `cron`, `firewalld`, etc.)

> This exercise helps you master **Linux service control**—a critical skill for securing, optimizing, and maintaining Linux systems.

---

## 🧰 Requirements

* A Linux system (VM or bare metal)
* A sudo-enabled user (e.g., `shahid`)
* Services like `sshd`, `cron`, and `firewalld` installed
* Terminal access

---

## 🧭 Step-by-Step Lab Instructions

---

### 🔹 **Step 1: List All Currently Running Services**

```bash
systemctl list-units --type=service --state=running
```

✅ This gives you a view of **active services** on the system.

---

### 🔹 **Step 2: Check the Status of a Service**

Let’s check the `sshd` service (replace with `cron` or `network` if not installed):

```bash
systemctl status sshd
```

Look for:

* Active/inactive state
* Main PID
* Last log entries

---

### 🔹 **Step 3: Stop and Start a Service**

```bash
sudo systemctl stop sshd
sudo systemctl start sshd
```

Check status after each command to confirm:

```bash
systemctl status sshd
```

---

### 🔹 **Step 4: Restart and Reload a Service**

```bash
sudo systemctl restart sshd      # Full restart
sudo systemctl reload sshd       # Reload config without restarting (if supported)
```

> Reload is safer for live systems if you only changed config.

---

### 🔹 **Step 5: Enable and Disable Services**

```bash
sudo systemctl enable sshd       # Enable at boot
sudo systemctl disable sshd      # Disable from boot
```

✅ Check if it worked:

```bash
systemctl is-enabled sshd
```

---

### 🔹 **Step 6: Mask and Unmask a Service**

**Masking** prevents all forms of starting (even manually):

```bash
sudo systemctl mask sshd
```

Try to start it:

```bash
sudo systemctl start sshd
# Should fail with "masked" message
```

Now unmask it:

```bash
sudo systemctl unmask sshd
sudo systemctl start sshd        # Now it should start
```

---

### 🔹 **Step 7: View Logs for a Service (Bonus)**

```bash
journalctl -u sshd
```

✅ Scroll with arrow keys or use `q` to quit.

---

## 📂 Real-World Application Tasks

| Task                                 | Command Example                   |
| ------------------------------------ | --------------------------------- |
| Stop Apache (webserver)              | `sudo systemctl stop apache2`     |
| Enable a firewall to start at boot   | `sudo systemctl enable firewalld` |
| Restart the cron job manager         | `sudo systemctl restart cron`     |
| Prevent Bluetooth from ever starting | `sudo systemctl mask bluetooth`   |

---

## 🧠 Reflection Questions

1. What is the difference between `disable` and `stop`?
2. When should you `reload` a service instead of `restart`?
3. What does `mask` prevent?
4. What command shows whether a service will start on boot?
5. How can you see a service’s detailed status and logs?

---

## ✅ Completion Checklist

| Task                                     | Status |
| ---------------------------------------- | ------ |
| Listed all running services              | ✅      |
| Checked the status of a specific service | ✅      |
| Started and stopped a service            | ✅      |
| Restarted and reloaded a service         | ✅      |
| Enabled and disabled service at boot     | ✅      |
| Masked and unmasked a service            | ✅      |
| Viewed service logs via `journalctl`     | ✅      |

---

## 📎 Summary

By completing this lab, you now have hands-on experience with:

* Managing service states (start/stop/restart/reload)
* Controlling boot-time behavior (enable/disable)
* Enforcing security through `mask/unmask`
* Auditing service logs and statuses

> This is a **core competency** in Linux system administration and service hardening.