Here is your complete, professional, GitHub-ready Markdown documentation for:

---

# 🛠️ Linux Essentials – **Edit Network Configuration Files**

> 📂 **Focus**: Understand and edit key Linux configuration files that control IP addresses, gateways, DNS, and interface behavior.
> 🎯 **Use Case**: Enables persistent network configurations, useful for servers, static IP setups, and controlled environments.
> 🔐 **Cybersecurity Relevance**: Misconfigured files can expose systems to sniffing, spoofing, or isolation—knowing what to edit, and how, is essential.

---

## 🧭 Table of Contents

- [🛠️ Linux Essentials – **Edit Network Configuration Files**](#️-linux-essentials--edit-network-configuration-files)
  - [🧭 Table of Contents](#-table-of-contents)
  - [📘 Introduction](#-introduction)
  - [🔧 Key Network Config Files](#-key-network-config-files)
  - [📍 Debian/Ubuntu – `/etc/network/interfaces`](#-debianubuntu--etcnetworkinterfaces)
    - [🔹 Sample Static IP Configuration](#-sample-static-ip-configuration)
    - [🔹 DHCP Configuration (default)](#-dhcp-configuration-default)
  - [📍 RHEL/CentOS – `ifcfg-*` Scripts](#-rhelcentos--ifcfg--scripts)
    - [🔹 File Location](#-file-location)
    - [🔹 Sample Static IP Configuration](#-sample-static-ip-configuration-1)
    - [🔹 DHCP Configuration](#-dhcp-configuration)
  - [🌐 DNS Configuration – `/etc/resolv.conf`](#-dns-configuration--etcresolvconf)
    - [📁 Edit DNS resolvers manually:](#-edit-dns-resolvers-manually)
  - [🏷️ Hostname and Local Resolution](#️-hostname-and-local-resolution)
    - [📄 File: `/etc/hostname`](#-file-etchostname)
    - [📄 File: `/etc/hosts`](#-file-etchosts)
    - [🔁 Change hostname via CLI](#-change-hostname-via-cli)
  - [🔄 Restarting Network Services](#-restarting-network-services)
  - [🧪 Lab: Edit and Apply Network Configs](#-lab-edit-and-apply-network-configs)
    - [✅ Task Checklist](#-task-checklist)
  - [📝 Summary](#-summary)
  - [📌 Key Takeaways](#-key-takeaways)

---

## 📘 Introduction

Linux networking files provide a **persistent** way to configure network settings. These files define how interfaces behave after reboot, what IPs and gateways are used, and how domain names are resolved. Editing them manually is critical in **server environments**, **recovery modes**, and **network troubleshooting**.

---

## 🔧 Key Network Config Files

| File                                     | Purpose                  | OS Family            |
| ---------------------------------------- | ------------------------ | -------------------- |
| `/etc/network/interfaces`                | Interface configuration  | Debian, Ubuntu       |
| `/etc/sysconfig/network-scripts/ifcfg-*` | Interface config scripts | RHEL, CentOS, Fedora |
| `/etc/resolv.conf`                       | DNS name servers         | All                  |
| `/etc/hostname`                          | System hostname          | All                  |
| `/etc/hosts`                             | Local name resolution    | All                  |

---

## 📍 Debian/Ubuntu – `/etc/network/interfaces`

### 🔹 Sample Static IP Configuration

```bash
sudo nano /etc/network/interfaces
```

```text
auto eth0
iface eth0 inet static
  address 192.168.1.100
  netmask 255.255.255.0
  gateway 192.168.1.1
  dns-nameservers 8.8.8.8 1.1.1.1
```

### 🔹 DHCP Configuration (default)

```text
auto eth0
iface eth0 inet dhcp
```

> 💡 Use `sudo systemctl restart networking` to apply.

---

## 📍 RHEL/CentOS – `ifcfg-*` Scripts

### 🔹 File Location

```bash
/etc/sysconfig/network-scripts/ifcfg-eth0
```

### 🔹 Sample Static IP Configuration

```ini
DEVICE=eth0
BOOTPROTO=static
ONBOOT=yes
IPADDR=192.168.1.100
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=8.8.8.8
DNS2=1.1.1.1
```

### 🔹 DHCP Configuration

```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```

> 💡 Restart with `sudo systemctl restart network`

---

## 🌐 DNS Configuration – `/etc/resolv.conf`

### 📁 Edit DNS resolvers manually:

```bash
sudo nano /etc/resolv.conf
```

```text
nameserver 8.8.8.8
nameserver 1.1.1.1
```

> ⚠️ **Note**: On `systemd` systems, this file may be overwritten. Use:

```bash
systemd-resolve --status
```

Or manage DNS via NetworkManager:

```bash
nmcli dev show
```

---

## 🏷️ Hostname and Local Resolution

### 📄 File: `/etc/hostname`

```bash
sudo nano /etc/hostname
```

```text
myserver01
```

### 📄 File: `/etc/hosts`

```bash
sudo nano /etc/hosts
```

```text
127.0.0.1   localhost
127.0.1.1   myserver01.localdomain   myserver01
```

### 🔁 Change hostname via CLI

```bash
sudo hostnamectl set-hostname myserver01
```

---

## 🔄 Restarting Network Services

| Action                  | Debian/Ubuntu                        | RHEL/CentOS                                              |
| ----------------------- | ------------------------------------ | -------------------------------------------------------- |
| Restart networking      | `sudo systemctl restart networking`  | `sudo systemctl restart network`                         |
| Bring interface up/down | `sudo ifdown eth0 && sudo ifup eth0` | `nmcli connection down eth0 && nmcli connection up eth0` |

---

## 🧪 Lab: Edit and Apply Network Configs

> 🔧 **Goal**: Configure a static IP and DNS settings that persist after reboot.

### ✅ Task Checklist

* [x] Open and edit the appropriate config file
* [x] Set IP: `192.168.56.50/24`, GW: `192.168.56.1`, DNS: `8.8.8.8`
* [x] Set hostname to `lab-node01`
* [x] Edit `/etc/hosts` to reflect hostname
* [x] Restart networking
* [x] Validate with `ip addr`, `ip route`, `dig`, and `ping`

---

## 📝 Summary

Manual editing of Linux networking files ensures you have full control over interface behavior, even without automation or GUI tools. This is crucial for **cybersecurity professionals**, **system engineers**, and **incident responders** working in bare-metal or recovery situations.

---

## 📌 Key Takeaways

* Know the difference between Debian (`/etc/network/interfaces`) and RHEL (`ifcfg-*`) configuration.
* Edit `/etc/resolv.conf` cautiously—it's often overwritten in systemd environments.
* Use `hostnamectl`, `/etc/hostname`, and `/etc/hosts` for consistent name resolution.
* Always restart networking to apply persistent changes.
* Validate every step using tools like `ip`, `ping`, `dig`, and `nmcli`.

---

Would you like a **step-by-step guided exercise**, a **YAML-to-script converter**, or a **diagnostic shell script** to automatically validate your network config files? Let me know and I’ll build it for you!
