# 🧪 **Lab: Control Services and Daemons in Linux**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 297*

---

## 🎯 Objective

In this lab, you will:

* Manage essential Linux services (a.k.a. **daemons**)
* Start, stop, enable, disable, mask, and unmask services
* Inspect service **status**, **logs**, and **boot behavior**
* Harden your system by controlling which services run and when

> This lab solidifies your control over background services—a vital skill for system administration and security hardening.

---

## 🧰 Requirements

* Linux machine (VM, server, or WSL with `systemd`)
* User with **sudo** privileges
* Services available: `sshd`, `cron`, `firewalld`, `bluetooth` (or equivalents)

---

## 🧭 Step-by-Step Instructions

---

### 🔹 **Step 1: List All Services on the System**

```bash
systemctl list-unit-files --type=service
```

✅ This shows all service units and whether they’re enabled, disabled, masked, etc.

---

### 🔹 **Step 2: Identify Active Running Services**

```bash
systemctl list-units --type=service --state=running
```

✅ You’ll see currently active daemons, like `sshd`, `systemd-logind`, `NetworkManager`, etc.

---

### 🔹 **Step 3: Investigate and Manage a Key Service (`sshd`)**

1. **Check if it is enabled:**

```bash
systemctl is-enabled sshd
```

2. **Check current status and logs:**

```bash
systemctl status sshd
journalctl -u sshd --since today
```

3. **Stop and start the service:**

```bash
sudo systemctl stop sshd
sudo systemctl start sshd
```

4. **Enable and disable it at boot:**

```bash
sudo systemctl disable sshd
sudo systemctl enable sshd
```

---

### 🔹 **Step 4: Mask and Unmask a Service**

1. **Mask (prevent any startup):**

```bash
sudo systemctl mask sshd
```

2. **Try starting (should fail):**

```bash
sudo systemctl start sshd
```

3. **Unmask and restart:**

```bash
sudo systemctl unmask sshd
sudo systemctl start sshd
```

---

### 🔹 **Step 5: Practice with Another Daemon (e.g., `cron`)**

```bash
sudo systemctl status cron
sudo systemctl restart cron
sudo systemctl enable cron
sudo systemctl is-enabled cron
```

> Replace `cron` with `crond` if you're on RHEL/CentOS.

---

### 🔹 **Step 6: Harden the System by Disabling/Masking Unused Services**

```bash
sudo systemctl stop bluetooth
sudo systemctl disable bluetooth
sudo systemctl mask bluetooth
```

✅ Use this for services you don't use (like `telnet`, `cups`, `avahi-daemon`, etc.)

---

### 🔹 **Step 7: Check Boot Time and Performance Impact**

```bash
systemd-analyze blame
```

✅ See which services delayed your boot—useful for optimization.

---

## 📂 Final Commands Summary

```bash
systemctl list-unit-files --type=service
systemctl list-units --type=service --state=running
systemctl status sshd
systemctl start|stop|restart|reload <service>
systemctl enable|disable <service>
systemctl mask|unmask <service>
systemctl is-enabled <service>
journalctl -u <service>
systemd-analyze blame
```

---

## 🧠 Reflection Questions

1. What’s the difference between **enabled** and **active**?
2. Why would you **mask** a service rather than just disable it?
3. Which command shows how long services delayed boot?
4. What service(s) would you disable or mask on a hardened server?
5. How can logs help diagnose service failures?

---

## ✅ Completion Checklist

| Task                                                     | Status |
| -------------------------------------------------------- | ------ |
| Listed all and running services                          | ✅      |
| Managed a key service (`sshd` or `cron`)                 | ✅      |
| Masked and unmasked a service                            | ✅      |
| Enabled/disabled services at boot                        | ✅      |
| Viewed boot performance with `systemd-analyze`           | ✅      |
| Reviewed logs with `journalctl`                          | ✅      |
| Practiced security hardening by disabling unused daemons | ✅      |

---

## 📎 Summary

You now know how to:

* Manage system daemons using `systemctl`
* Start/stop/restart services manually
* Enable/disable services for boot-time control
* Mask services to block them completely
* Check service logs and troubleshoot failures
* Identify performance bottlenecks caused by services

> These are critical administration tasks in **cybersecurity**, **hardening**, and **performance tuning**.