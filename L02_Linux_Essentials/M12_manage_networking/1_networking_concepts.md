Here's your professional, structured, GitHub-ready Markdown documentation for:

---

# 📘 Linux Essentials – **Module 12: Manage Networking**

> 🔐 **Focus**: Learn how to configure, validate, troubleshoot, and secure network interfaces in Linux environments.
> 🧠 **Level**: Beginner → Intermediate
> 🛡️ **Cybersecurity Use Case**: Essential for ethical hackers, sysadmins, and forensic analysts who need reliable connectivity and secure communications in networked environments.

---

## 🧭 Table of Contents

- [📘 Linux Essentials – **Module 12: Manage Networking**](#-linux-essentials--module-12-manage-networking)
  - [🧭 Table of Contents](#-table-of-contents)
  - [📘 Introduction](#-introduction)
  - [🌐 Networking Concepts Overview](#-networking-concepts-overview)
  - [🔍 Validating Network Configuration](#-validating-network-configuration)
    - [✅ View All Network Interfaces](#-view-all-network-interfaces)
    - [✅ Check IP Address (short format)](#-check-ip-address-short-format)
    - [✅ Check Routing Table](#-check-routing-table)
    - [✅ DNS Resolver](#-dns-resolver)
    - [✅ Test Network Connectivity](#-test-network-connectivity)
  - [⚙️ Configuring Networking from CLI](#️-configuring-networking-from-cli)
    - [🛠 Assign Static IP (Temporary)](#-assign-static-ip-temporary)
    - [🌐 Enable or Disable Interface](#-enable-or-disable-interface)
  - [📝 Editing Network Configuration Files](#-editing-network-configuration-files)
    - [📌 Debian/Ubuntu](#-debianubuntu)
    - [📌 RHEL/CentOS/AlmaLinux](#-rhelcentosalmalinux)
    - [🧩 Restart Networking](#-restart-networking)
  - [📛 Configuring Hostnames and DNS](#-configuring-hostnames-and-dns)
    - [🔄 Change Hostname (Temporarily)](#-change-hostname-temporarily)
    - [📂 Permanent Hostname Configuration](#-permanent-hostname-configuration)
    - [🔍 DNS Resolution Check](#-dns-resolution-check)
  - [🧪 Lab: Manage Linux Networking](#-lab-manage-linux-networking)
    - [✅ Task Checklist](#-task-checklist)
    - [🧰 Tools to Use](#-tools-to-use)
  - [📝 Summary](#-summary)
  - [📌 Key Takeaways](#-key-takeaways)
  - [❓ Reflection Questions](#-reflection-questions)
  - [🧠 Quiz Section](#-quiz-section)

---

## 📘 Introduction

Linux systems are heavily used as servers, containers, and embedded systems—all of which require proper network configuration to communicate effectively. This module teaches you how to **view**, **configure**, and **troubleshoot** networking interfaces using the **command-line interface (CLI)** and **configuration files**.

---

## 🌐 Networking Concepts Overview

Networking on Linux is based on the **TCP/IP model**, and interfaces are typically managed using tools like:

| Tool                              | Description                                                   |
| --------------------------------- | ------------------------------------------------------------- |
| `ip`                              | Modern CLI utility for interface, IP, and route configuration |
| `ifconfig`                        | Legacy tool for interface configuration                       |
| `nmcli`                           | Command-line tool for NetworkManager                          |
| `systemd-resolve`                 | Used to check DNS resolution under systemd                    |
| `/etc/network/interfaces`         | Legacy Debian interface config file                           |
| `/etc/sysconfig/network-scripts/` | RHEL-based interface scripts                                  |

---

## 🔍 Validating Network Configuration

### ✅ View All Network Interfaces

```bash
ip addr show
```

### ✅ Check IP Address (short format)

```bash
ip a
```

### ✅ Check Routing Table

```bash
ip route
```

### ✅ DNS Resolver

```bash
cat /etc/resolv.conf
```

### ✅ Test Network Connectivity

```bash
ping 8.8.8.8
ping google.com
```

---

## ⚙️ Configuring Networking from CLI

### 🛠 Assign Static IP (Temporary)

```bash
sudo ip addr add 192.168.1.100/24 dev eth0
sudo ip route add default via 192.168.1.1
```

### 🌐 Enable or Disable Interface

```bash
sudo ip link set eth0 up
sudo ip link set eth0 down
```

> ⚠️ Temporary changes. Lost after reboot.

---

## 📝 Editing Network Configuration Files

> 📁 Configuration file location depends on distro:

### 📌 Debian/Ubuntu

File: `/etc/network/interfaces`

```bash
auto eth0
iface eth0 inet static
  address 192.168.1.100
  netmask 255.255.255.0
  gateway 192.168.1.1
  dns-nameservers 8.8.8.8 8.8.4.4
```

### 📌 RHEL/CentOS/AlmaLinux

File: `/etc/sysconfig/network-scripts/ifcfg-eth0`

```ini
DEVICE=eth0
BOOTPROTO=static
ONBOOT=yes
IPADDR=192.168.1.100
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=8.8.8.8
```

### 🧩 Restart Networking

```bash
sudo systemctl restart networking   # Debian
sudo systemctl restart network      # RHEL
```

---

## 📛 Configuring Hostnames and DNS

### 🔄 Change Hostname (Temporarily)

```bash
sudo hostnamectl set-hostname linux-node01
```

### 📂 Permanent Hostname Configuration

```bash
cat /etc/hostname
cat /etc/hosts
```

Example `/etc/hosts`:

```text
127.0.0.1   localhost
127.0.1.1   linux-node01
```

### 🔍 DNS Resolution Check

```bash
dig google.com
nslookup google.com
```

> Tip: If `/etc/resolv.conf` is overwritten by `systemd`, manage it via:

```bash
systemd-resolve --status
```

---

## 🧪 Lab: Manage Linux Networking

### ✅ Task Checklist

* [x] Check IP address of your system
* [x] Temporarily assign a static IP to `eth0`
* [x] Configure a default gateway and DNS
* [x] Test internet access using `ping` and `dig`
* [x] Edit `/etc/hosts` and `/etc/hostname` to define system hostname
* [x] Restart networking and validate persistence
* [x] Use `tcpdump` to monitor traffic on an interface

### 🧰 Tools to Use

* `ip`, `ping`, `dig`, `tcpdump`, `nmcli`, `hostnamectl`

---

## 📝 Summary

This module empowers you with foundational skills to **validate**, **configure**, and **troubleshoot** Linux networking. Whether managing servers, configuring lab environments, or preparing for real-world cyber challenges, understanding networking is **non-negotiable** for any cybersecurity or sysadmin role.

---

## 📌 Key Takeaways

* `ip` is preferred over `ifconfig` in modern systems.
* Permanent IP configuration requires editing network config files.
* DNS settings are usually found in `/etc/resolv.conf`.
* The hostname must match entries in `/etc/hosts` for local resolution.
* Learn `nmcli` for modern systems using NetworkManager.

---

## ❓ Reflection Questions

1. What happens if you don’t define a default gateway?
2. Why is it better to use `ip` instead of `ifconfig`?
3. How does the `/etc/hosts` file impact name resolution?

---

## 🧠 Quiz Section

**Q1.** What command would you use to check the current IP address on a modern Linux system?
a) `ifconfig`
b) `ip addr`
c) `netstat -i`
d) `hostname`

✅ **Answer**: **b) `ip addr`**

---

**Q2.** Where do you configure a static IP permanently on Debian-based systems?
a) `/etc/sysconfig/ifcfg-eth0`
b) `/etc/network/interfaces`
c) `/etc/hostname`
d) `/etc/resolv.conf`

✅ **Answer**: **b) `/etc/network/interfaces`**

---

**Q3.** What tool is used to test DNS resolution?
a) `ping`
b) `dig`
c) `netstat`
d) `curl`

✅ **Answer**: **b) `dig`**

---

If you'd like, I can also generate:

* 🧪 **Extra Labs** for penetration testing scenarios involving DNS spoofing, MITM, etc.
* 🔁 **Version Differences** between NetworkManager, systemd-networkd, netplan, etc.
* 🎯 **Real-world examples** of network misconfiguration leading to breaches

Let me know what you want next!
