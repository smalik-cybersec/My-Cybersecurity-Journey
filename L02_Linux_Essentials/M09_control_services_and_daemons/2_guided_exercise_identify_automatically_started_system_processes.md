# 🧪 **Guided Exercise: Identify Automatically Started System Processes**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 285*

---

## 🎯 Objective

This hands-on exercise will help you:

* Identify which system services and daemons are started **automatically at boot**
* Understand how to query their **status**, **enablement**, and **startup time**
* Use `systemctl` and related tools to monitor and manage system-level processes

> This skill is essential for **system optimization**, **boot time troubleshooting**, and **security auditing**.

---

## 🧰 Requirements

* Linux system (VM, server, or WSL with `systemd` support)
* Terminal access with a user who has **sudo privileges**

---

## 🧭 Step-by-Step Lab Instructions

---

### 🔹 **Step 1: View All Active (Running) Services**

Use `systemctl` to list currently running services:

```bash
systemctl list-units --type=service --state=running
```

✅ This displays all active services started after boot (e.g. `sshd`, `NetworkManager`, etc.)

---

### 🔹 **Step 2: View All Services Enabled at Boot**

These are services **configured to auto-start** at boot:

```bash
systemctl list-unit-files --type=service | grep enabled
```

✅ Sample output:

```text
sshd.service                     enabled
cron.service                    enabled
firewalld.service               enabled
```

---

### 🔹 **Step 3: Check If a Specific Service Is Enabled**

Choose a service like `sshd` or `cron` and run:

```bash
systemctl is-enabled sshd
```

Expected result:

```bash
enabled
```

✅ Now try it with a service not enabled:

```bash
systemctl is-enabled bluetooth
```

---

### 🔹 **Step 4: Get the Status of a Service**

```bash
systemctl status sshd
```

✅ Output includes:

* Active/inactive status
* Whether it failed or succeeded
* Recent logs
* Main PID and memory usage

---

### 🔹 **Step 5: Identify Which Services Took Long to Start**

```bash
systemd-analyze blame
```

✅ This command shows **boot time breakdown**:

```text
5.020s NetworkManager.service
3.511s sshd.service
1.003s systemd-logind.service
```

> Use this to investigate **slow boot issues**.

---

### 🔹 **Step 6: Visualize Systemd Tree (Optional)**

```bash
systemctl list-dependencies
```

✅ See how units are linked in the systemd boot chain.

---

## 🧪 Bonus: Discover Systemd Targets (Like Runlevels)

```bash
systemctl get-default
```

✅ Typical output:

```bash
graphical.target
```

To list all targets:

```bash
systemctl list-units --type=target
```

---

## 📂 Summary of Commands Used

```bash
systemctl list-units --type=service --state=running
systemctl list-unit-files --type=service | grep enabled
systemctl is-enabled <service>
systemctl status <service>
systemd-analyze blame
systemctl list-dependencies
systemctl get-default
```

---

## 🧠 Reflection Questions

1. What’s the difference between `enabled` and `active` services?
2. How do you identify the service that causes boot delays?
3. Why might you disable a service from starting at boot?
4. Which command shows the startup status and logs of a service?
5. What target does your system boot into by default?

---

## ✅ Completion Checklist

| Task                                                | Status |
| --------------------------------------------------- | ------ |
| Listed all running services                         | ✅      |
| Listed all services enabled at boot                 | ✅      |
| Checked enablement status of a specific service     | ✅      |
| Viewed status and logs of a service                 | ✅      |
| Analyzed boot time using `systemd-analyze blame`    | ✅      |
| Explored system targets and dependencies (optional) | ✅      |

---

## 📎 Summary

You’ve now practiced how to:

* Identify and inspect **auto-started services**
* Distinguish between **enabled**, **disabled**, and **masked** services
* Analyze **boot time delays** caused by specific daemons
* Understand **systemd targets** and **dependency trees**

> This helps ensure **faster boots**, **fewer vulnerabilities**, and **better resource usage** on your Linux systems.

---

✅ Let me know if you'd like:

* 🧠 A quiz to review this lab
* 📥 Markdown or PDF version for GitHub
* ⏭️ Next lesson: *Analyze and Manage System Logs*

You’re now reading your system’s startup like a digital forensics expert, Shahid 🧠🚀 Let’s move forward!
