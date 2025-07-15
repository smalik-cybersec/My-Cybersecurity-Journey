# 🖥️ **Lesson: Identify Automatically Started System Processes**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 280*

---

## 📚 Table of Contents

- [🖥️ **Lesson: Identify Automatically Started System Processes**](#️-lesson-identify-automatically-started-system-processes)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [🔄 What Are Automatically Started Processes?](#-what-are-automatically-started-processes)
  - [🧠 System Boot and Process Initialization](#-system-boot-and-process-initialization)
    - [Boot Sequence Overview](#boot-sequence-overview)
  - [🔧 Understanding `systemd` and Services](#-understanding-systemd-and-services)
  - [🛠️ Tools to List Auto-Started Processes](#️-tools-to-list-auto-started-processes)
    - [🔹 1. View All Running Services](#-1-view-all-running-services)
    - [🔹 2. View All Enabled Services at Boot](#-2-view-all-enabled-services-at-boot)
    - [🔹 3. Check If a Specific Service Is Enabled](#-3-check-if-a-specific-service-is-enabled)
    - [🔹 4. Get Status of a System Service](#-4-get-status-of-a-system-service)
    - [🔹 5. View Processes with `ps` and Filter by `systemd`](#-5-view-processes-with-ps-and-filter-by-systemd)
    - [🔹 6. Visualize Boot Performance (Optional)](#-6-visualize-boot-performance-optional)
  - [🧪 Practical Examples](#-practical-examples)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)
  - [📋 Key Commands Summary](#-key-commands-summary)

---

## 🎯 Introduction

When a Linux system boots, a set of **system processes and services** are started **automatically**. These include essential background services like:

- `sshd` for remote access
- `cron` for scheduled tasks
- `networking` for interfaces
- Logging daemons and more

Understanding these **auto-started processes** is essential for **security, performance, and system hardening**.

---

## 🔄 What Are Automatically Started Processes?

These are:

- **System-level daemons and services**
- Started by the **init system** (usually `systemd`)
- Can be managed using service management tools
- Often run with **root privileges**

---

## 🧠 System Boot and Process Initialization

### Boot Sequence Overview

1. **BIOS/UEFI** → Hardware POST
2. **Bootloader (GRUB)** → Loads kernel
3. **Kernel** → Initializes hardware and mounts root filesystem
4. **Init system** (`systemd`) → Starts target units and services
5. **System reaches default target** (like `multi-user.target` or `graphical.target`)
6. **Auto-started processes** are launched

---

## 🔧 Understanding `systemd` and Services

Most modern Linux distros (RHEL, CentOS, Ubuntu, Fedora) use **`systemd`** as the init system.

| Term        | Description                                      |
| ----------- | ------------------------------------------------ |
| **Service** | A background process (daemon) managed by systemd |
| **Unit**    | A configuration file representing a resource     |
| **Target**  | A collection of units defining system state      |

---

## 🛠️ Tools to List Auto-Started Processes

### 🔹 1. View All Running Services

```bash
systemctl list-units --type=service
```

✅ Shows services currently **active and running**.

---

### 🔹 2. View All Enabled Services at Boot

```bash
systemctl list-unit-files --type=service | grep enabled
```

✅ Shows services set to **auto-start** on boot.

---

### 🔹 3. Check If a Specific Service Is Enabled

```bash
systemctl is-enabled sshd
```

✅ Returns `enabled` or `disabled`.

---

### 🔹 4. Get Status of a System Service

```bash
systemctl status NetworkManager
```

✅ Provides status, PID, memory usage, logs, and whether it's running.

---

### 🔹 5. View Processes with `ps` and Filter by `systemd`

```bash
ps -eo pid,ppid,cmd | grep systemd
```

✅ View hierarchy of processes launched by `systemd`.

---

### 🔹 6. Visualize Boot Performance (Optional)

```bash
systemd-analyze blame
```

✅ Shows how long each service took to start at boot.

---

## 🧪 Practical Examples

```bash
# List all enabled (auto-started) services
systemctl list-unit-files --type=service | grep enabled

# See running services
systemctl list-units --type=service

# Check if firewalld is enabled
systemctl is-enabled firewalld

# Check status of a specific service
systemctl status sshd

# Analyze boot time and service delays
systemd-analyze blame
```

---

## 🧠 Quiz Yourself

1. What command lists all services currently running?
2. How do you check if a service is enabled at boot?
3. Which tool shows the time each service took to start?
4. What’s the difference between `list-units` and `list-unit-files`?
5. What command checks detailed status of a systemd service?

---

## 📎 Summary

- Auto-started processes are system services initialized during the boot process
- **`systemd`** is the most common init system in modern Linux distributions
- Use `systemctl` to list, inspect, and manage services
- Knowing which services start by default helps with **system hardening**, **performance tuning**, and **debugging boot issues**

---

## 📋 Key Commands Summary

```bash
systemctl list-units --type=service
systemctl list-unit-files --type=service | grep enabled
systemctl is-enabled <service-name>
systemctl status <service-name>
systemd-analyze blame
```
