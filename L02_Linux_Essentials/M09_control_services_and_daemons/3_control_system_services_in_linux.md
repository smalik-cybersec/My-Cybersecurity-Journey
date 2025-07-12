Absolutely, Shahid! Here's your complete, professional, and GitHub-friendly documentation for:

---

# 🛠️ **Lesson: Control System Services in Linux**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 289*

---

## 📚 Table of Contents

- [🛠️ **Lesson: Control System Services in Linux**](#️-lesson-control-system-services-in-linux)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [⚙️ What Are System Services?](#️-what-are-system-services)
  - [🧠 `systemd` and Unit Files](#-systemd-and-unit-files)
  - [🛠️ Manage Services with `systemctl`](#️-manage-services-with-systemctl)
  - [🔐 Service States: Active, Enabled, Masked](#-service-states-active-enabled-masked)
  - [📂 Real-World Service Examples](#-real-world-service-examples)
    - [1. **SSH Service**](#1-ssh-service)
    - [2. **Firewall Service**](#2-firewall-service)
    - [3. **Disable a Service Permanently**](#3-disable-a-service-permanently)
    - [4. **Mask a Risky Service**](#4-mask-a-risky-service)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)
  - [📋 Key Commands Recap](#-key-commands-recap)

---

## 🎯 Introduction

Linux system services—also called **daemons**—run in the background and handle essential functions such as networking, scheduled tasks, remote access, and logging.

Using **`systemctl`**, you can **start, stop, enable, disable, reload, and restart** these services with precision and control.

> Mastering this skill is critical for **system admins**, **security analysts**, and **DevOps engineers**.

---

## ⚙️ What Are System Services?

| Feature          | Description                                          |
| ---------------- | ---------------------------------------------------- |
| **Daemon**       | A background service (e.g., `sshd`, `cron`, `httpd`) |
| **Service Unit** | A configuration file for systemd-managed services    |
| **Managed by**   | `systemd`, the init system on most modern distros    |

Service files are usually found in:

* `/etc/systemd/system/`
* `/lib/systemd/system/`
* `/usr/lib/systemd/system/`

---

## 🧠 `systemd` and Unit Files

Each **service** is defined by a **unit file** with the `.service` extension.

Example: `/lib/systemd/system/sshd.service`

A service unit file may define:

* Description
* ExecStart, ExecReload, ExecStop
* Restart policy
* Dependencies

---

## 🛠️ Manage Services with `systemctl`

Here’s a breakdown of the most common service control commands:

| Command                          | Description                                     |
| -------------------------------- | ----------------------------------------------- |
| `systemctl start <service>`      | Start a service **immediately**                 |
| `systemctl stop <service>`       | Stop a service immediately                      |
| `systemctl restart <service>`    | Stop and start the service                      |
| `systemctl reload <service>`     | Reload config without restarting (if supported) |
| `systemctl enable <service>`     | Enable auto-start at boot                       |
| `systemctl disable <service>`    | Prevent service from starting at boot           |
| `systemctl is-enabled <service>` | Check if enabled                                |
| `systemctl status <service>`     | Show detailed status                            |
| `systemctl mask <service>`       | Prevent starting by users or other services     |
| `systemctl unmask <service>`     | Allow it to be started again                    |

---

## 🔐 Service States: Active, Enabled, Masked

| State        | Description                                                 |
| ------------ | ----------------------------------------------------------- |
| **active**   | Currently running                                           |
| **inactive** | Not currently running                                       |
| **enabled**  | Set to start at boot                                        |
| **disabled** | Will not start at boot                                      |
| **masked**   | Blocked from being started in any way (manual or automatic) |

---

## 📂 Real-World Service Examples

### 1. **SSH Service**

```bash
sudo systemctl start sshd
sudo systemctl enable sshd
sudo systemctl status sshd
```

### 2. **Firewall Service**

```bash
sudo systemctl restart firewalld
sudo systemctl is-enabled firewalld
```

### 3. **Disable a Service Permanently**

```bash
sudo systemctl disable bluetooth
sudo systemctl stop bluetooth
```

### 4. **Mask a Risky Service**

```bash
sudo systemctl mask telnet.socket
```

---

## 🧠 Quiz Yourself

1. What’s the difference between `start` and `enable` in `systemctl`?
2. How do you check if a service is set to auto-start on boot?
3. What happens when you mask a service?
4. What is the effect of running `systemctl reload` instead of `restart`?
5. How can you see recent logs of a service?

> Bonus: Try `journalctl -u <service>`

---

## 📎 Summary

* Linux uses `systemd` to control system services (daemons)
* Each service is managed via a `.service` unit file
* Use `systemctl` to **start, stop, restart, enable, disable, mask**, and **query** services
* Mastering service control improves **availability**, **security**, and **boot management**

---

## 📋 Key Commands Recap

```bash
systemctl start <service>
systemctl stop <service>
systemctl restart <service>
systemctl enable <service>
systemctl disable <service>
systemctl mask <service>
systemctl unmask <service>
systemctl status <service>
systemctl is-enabled <service>
```

---

✅ Let me know if you’d like:

* 🧪 Guided Exercise to practice controlling services
* 🧠 Quiz with answers
* 📥 Markdown export for GitHub
* ⏭️ Next topic: *Lab: Manage System Services with systemctl*

You’re now in command of every service your system runs — a vital Linux skill, Shahid 🚀🧠 Keep going strong!
