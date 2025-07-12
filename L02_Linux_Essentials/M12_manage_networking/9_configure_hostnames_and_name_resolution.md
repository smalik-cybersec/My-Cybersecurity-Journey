Here is your complete, professional-grade Markdown documentation for:

---

# 🏷️ Linux Essentials – **Configure Hostnames and Name Resolution**

> 🧭 **Objective**: Learn how to view, set, and persistently configure hostnames and control how Linux resolves domain names using both **local files** and **DNS resolvers**.
> 🔐 **Cybersecurity Relevance**: Misconfigured hostnames and name resolution can lead to broken services, logging inconsistencies, MITM risks, and troubleshooting nightmares.

---

## 🧭 Table of Contents

- [🏷️ Linux Essentials – **Configure Hostnames and Name Resolution**](#️-linux-essentials--configure-hostnames-and-name-resolution)
  - [🧭 Table of Contents](#-table-of-contents)
  - [📘 Introduction](#-introduction)
  - [🏷️ What Is a Hostname?](#️-what-is-a-hostname)
  - [📂 Key Configuration Files](#-key-configuration-files)
  - [🔁 View and Change Hostname](#-view-and-change-hostname)
    - [🔍 View Current Hostname](#-view-current-hostname)
    - [✍️ Temporarily Change Hostname](#️-temporarily-change-hostname)
  - [🧩 Persistent Hostname Configuration](#-persistent-hostname-configuration)
    - [📄 `/etc/hostname`](#-etchostname)
    - [📄 `/etc/hosts`](#-etchosts)
  - [🌐 Configure Local Name Resolution](#-configure-local-name-resolution)
    - [🧩 File: `/etc/hosts`](#-file-etchosts)
    - [🔁 Order of resolution is defined in:](#-order-of-resolution-is-defined-in)
  - [🌍 Configure DNS Resolvers](#-configure-dns-resolvers)
    - [📄 File: `/etc/resolv.conf`](#-file-etcresolvconf)
    - [Check DNS with:](#check-dns-with)
  - [🧪 Lab Exercise](#-lab-exercise)
    - [✅ Task Checklist](#-task-checklist)
  - [📝 Summary](#-summary)
  - [📌 Key Takeaways](#-key-takeaways)

---

## 📘 Introduction

In Linux, a **hostname** is the name of the system on the network. It plays a vital role in:

* Network communication
* Logging and auditing
* DNS and name resolution
* Remote access and service identification

Name resolution determines **how Linux maps names (like `google.com`) to IP addresses**. This happens via:

* `/etc/hosts` (local resolution)
* `/etc/resolv.conf` (DNS servers)

---

## 🏷️ What Is a Hostname?

| Type                   | Description                                                                  |
| ---------------------- | ---------------------------------------------------------------------------- |
| **Static Hostname**    | The default name set in `/etc/hostname`                                      |
| **Transient Hostname** | Temporary; lost on reboot (e.g., via `hostnamectl set-hostname --transient`) |
| **Pretty Hostname**    | Optional, human-readable (not used for DNS or SSH)                           |

---

## 📂 Key Configuration Files

| File                 | Purpose                                                  |
| -------------------- | -------------------------------------------------------- |
| `/etc/hostname`      | Stores the system’s static hostname                      |
| `/etc/hosts`         | Maps hostnames to IP addresses locally                   |
| `/etc/resolv.conf`   | Contains DNS nameserver entries                          |
| `/etc/nsswitch.conf` | Defines the order of resolution (e.g., `files` vs `dns`) |

---

## 🔁 View and Change Hostname

### 🔍 View Current Hostname

```bash
hostname
hostnamectl
```

---

### ✍️ Temporarily Change Hostname

```bash
sudo hostnamectl set-hostname myserver01
```

> ⚠️ This changes hostname immediately, but it may not persist across reboots unless `/etc/hostname` is updated.

---

## 🧩 Persistent Hostname Configuration

### 📄 `/etc/hostname`

```bash
sudo nano /etc/hostname
```

```text
myserver01
```

### 📄 `/etc/hosts`

```bash
sudo nano /etc/hosts
```

Add or update:

```text
127.0.1.1   myserver01.localdomain   myserver01
```

> 🧠 **Why this matters**: Many services resolve local names using `/etc/hosts` before querying DNS. A mismatch here can break SSH, Apache, or Postfix.

---

## 🌐 Configure Local Name Resolution

### 🧩 File: `/etc/hosts`

Purpose: Local mapping of IP ↔ name (bypasses DNS)

Example:

```text
127.0.0.1       localhost
127.0.1.1       myserver01.localdomain   myserver01
192.168.56.10   db01.local   db01
192.168.56.11   web01.local  web01
```

### 🔁 Order of resolution is defined in:

```bash
cat /etc/nsswitch.conf
```

Look for:

```text
hosts: files dns
```

> Means: Try `/etc/hosts` first, then DNS

---

## 🌍 Configure DNS Resolvers

### 📄 File: `/etc/resolv.conf`

```bash
sudo nano /etc/resolv.conf
```

Example:

```text
nameserver 8.8.8.8
nameserver 1.1.1.1
```

> ⚠️ Many modern distros use `systemd-resolved` which dynamically manages this file. If changes are not sticking:

### Check DNS with:

```bash
systemd-resolve --status
```

Or:

```bash
nmcli dev show | grep DNS
```

---

## 🧪 Lab Exercise

> 🛠️ Configure and validate hostname and name resolution on your system.

### ✅ Task Checklist

* [x] Set hostname to `lab-node01`
* [x] Edit `/etc/hostname` with the same name
* [x] Add mapping in `/etc/hosts`: `127.0.1.1 lab-node01.local lab-node01`
* [x] Configure `/etc/resolv.conf` with two DNS servers
* [x] Test:

```bash
hostname
hostname -f
ping lab-node01
ping google.com
dig google.com
```

---

## 📝 Summary

Understanding and configuring hostname and name resolution ensures that services operate reliably, logs are traceable, and systems are discoverable on networks. It’s a **foundational skill** for any Linux admin or cybersecurity professional.

---

## 📌 Key Takeaways

* Use `hostnamectl` to change the hostname, but always update `/etc/hostname` and `/etc/hosts` for persistence.
* `/etc/hosts` enables local name mapping without DNS.
* `/etc/resolv.conf` defines which DNS servers are used for name resolution.
* `systemd-resolved` may override DNS configs unless managed properly.
* Misconfigurations can break SSH, logging, mail servers, or name resolution tools.

---

Would you like a **Guided Lab** to walk through this setup interactively, or a **diagnostic script** that checks hostname and DNS consistency on any Linux box? Let me know — I’m ready to build it!
