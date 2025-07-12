Here is your **Guided Exercise** for:

---

# 🎯 Guided Exercise: **Configure Hostnames and Name Resolution in Linux**

> 🏷️ **Objective**: Learn how to set and persist hostnames, configure local hostname resolution, and manage DNS settings using Linux configuration files.
> 🔐 **Cybersecurity Relevance**: Improper hostname or name resolution can cause serious issues in logging, SSH, mail services, IDS/IPS, and automated scripts.

---

## 🧭 Table of Contents

- [🎯 Guided Exercise: **Configure Hostnames and Name Resolution in Linux**](#-guided-exercise-configure-hostnames-and-name-resolution-in-linux)
  - [🧭 Table of Contents](#-table-of-contents)
  - [📘 Learning Objectives](#-learning-objectives)
  - [🧰 Tools \& Requirements](#-tools--requirements)
  - [📦 Setup Notes](#-setup-notes)
  - [✅ Task 1: Check the Current Hostname](#-task-1-check-the-current-hostname)
  - [✅ Task 2: Set a New Hostname](#-task-2-set-a-new-hostname)
  - [✅ Task 3: Persist Hostname Across Reboots](#-task-3-persist-hostname-across-reboots)
  - [✅ Task 4: Update `/etc/hosts` for Local Name Resolution](#-task-4-update-etchosts-for-local-name-resolution)
  - [✅ Task 5: Set Up DNS Resolvers](#-task-5-set-up-dns-resolvers)
  - [✅ Task 6: Test Name Resolution](#-task-6-test-name-resolution)
    - [🧪 Hostname Validation](#-hostname-validation)
    - [🌐 External Name Resolution](#-external-name-resolution)
  - [🧪 Optional Challenge: Misconfig \& Recover](#-optional-challenge-misconfig--recover)
  - [📝 Lab Report Template](#-lab-report-template)

---

## 📘 Learning Objectives

After completing this lab, you will be able to:

* View and change the hostname of a Linux machine
* Persist hostname changes across reboots
* Resolve hostnames locally using `/etc/hosts`
* Configure DNS settings using `/etc/resolv.conf`
* Troubleshoot common name resolution problems

---

## 🧰 Tools & Requirements

| Requirement | Description                                                                    |
| ----------- | ------------------------------------------------------------------------------ |
| OS          | Any modern Linux (Ubuntu, Debian, CentOS, RHEL, etc.)                          |
| Access      | Root or `sudo` privileges                                                      |
| Tools Used  | `hostnamectl`, `nano`, `ping`, `dig`, `cat`, `systemd-resolve` (if applicable) |

---

## 📦 Setup Notes

* Replace `lab-node01` with any hostname you want.
* Replace interface names as necessary (`eth0`, `ens33`, etc.).

---

## ✅ Task 1: Check the Current Hostname

```bash
hostnamectl
hostname
hostname -f
```

> The `-f` flag shows the **Fully Qualified Domain Name (FQDN)**.

---

## ✅ Task 2: Set a New Hostname

```bash
sudo hostnamectl set-hostname lab-node01
```

> This updates the system's hostname immediately but **not permanently** unless `/etc/hostname` is updated too.

---

## ✅ Task 3: Persist Hostname Across Reboots

Edit the hostname file:

```bash
sudo nano /etc/hostname
```

```text
lab-node01
```

> Save and close (`Ctrl + X`, then `Y`, then `Enter`).

---

## ✅ Task 4: Update `/etc/hosts` for Local Name Resolution

```bash
sudo nano /etc/hosts
```

Add or edit the line:

```text
127.0.1.1   lab-node01.localdomain   lab-node01
```

> 🧠 This allows the system to resolve its own name **without DNS**.

Optional: Add local mappings for other machines:

```text
192.168.56.10   db01.local   db01
192.168.56.11   web01.local  web01
```

---

## ✅ Task 5: Set Up DNS Resolvers

```bash
sudo nano /etc/resolv.conf
```

Add:

```text
nameserver 8.8.8.8
nameserver 1.1.1.1
```

> ⚠️ This file may be **overwritten** by NetworkManager or systemd. If that's the case:

```bash
systemd-resolve --status
```

Or:

```bash
nmcli dev show | grep DNS
```

---

## ✅ Task 6: Test Name Resolution

### 🧪 Hostname Validation

```bash
hostname
hostname -f
ping lab-node01
```

### 🌐 External Name Resolution

```bash
ping -c 4 google.com
dig github.com
```

> ✅ Success means your hostname and DNS config are working.

---

## 🧪 Optional Challenge: Misconfig & Recover

Simulate a failure:

1. Delete `/etc/hostname` and reboot.
2. Observe that the system loses its hostname.
3. Use `hostnamectl` and `/etc/hostname` to recover it.

---

## 📝 Lab Report Template

```text
System: Debian 12 (VirtualBox)

👤 Hostname Set: lab-node01
📄 /etc/hostname Updated: ✅ Yes
📄 /etc/hosts Entry: 127.0.1.1 lab-node01.localdomain lab-node01
🌐 DNS Config (/etc/resolv.conf):
  - nameserver 8.8.8.8
  - nameserver 1.1.1.1
🔁 Persistent After Reboot: ✅ Yes
🔍 Name Resolution Tests:
  - hostname: ✅
  - hostname -f: ✅
  - ping lab-node01: ✅
  - ping google.com: ✅
```

---

Would you like this lab as a **PDF worksheet**, a **quiz**, or a **validation Bash script** to check your config automatically? I'm ready when you are for the next topic.
