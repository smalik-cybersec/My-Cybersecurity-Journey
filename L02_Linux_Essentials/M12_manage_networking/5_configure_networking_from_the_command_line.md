Here is your complete **Markdown documentation** for:

---

# ⚙️ Linux Essentials – **Configure Networking from the Command Line**

> 🔧 **Module Focus**: Learn how to manually assign IP addresses, set default gateways, and manage network interfaces entirely through the Linux CLI.
> 🛠️ **Why It Matters**: In many enterprise, server, and cybersecurity scenarios, a GUI isn't available. CLI mastery is essential for both troubleshooting and automation.
> 🎯 **Level**: Beginner to Intermediate
> 📌 **Cybersecurity Relevance**: Misconfigurations at the CLI level can lead to IP conflicts, broken routing, or even exposed attack surfaces.

---

## 🧭 Table of Contents

- [⚙️ Linux Essentials – **Configure Networking from the Command Line**](#️-linux-essentials--configure-networking-from-the-command-line)
  - [🧭 Table of Contents](#-table-of-contents)
  - [📘 Introduction](#-introduction)
  - [🌐 Static vs Dynamic IP Addressing](#-static-vs-dynamic-ip-addressing)
  - [🧰 CLI Tools You’ll Use](#-cli-tools-youll-use)
  - [📦 Set a Static IP (Temporary)](#-set-a-static-ip-temporary)
    - [✅ Step 1: Bring Interface Down](#-step-1-bring-interface-down)
    - [✅ Step 2: Assign Static IP](#-step-2-assign-static-ip)
    - [✅ Step 3: Add Default Gateway](#-step-3-add-default-gateway)
    - [✅ Step 4: Bring Interface Up](#-step-4-bring-interface-up)
    - [🧪 Validate:](#-validate)
  - [🔁 Set a Static IP (Persistent)](#-set-a-static-ip-persistent)
    - [📍 Debian / Ubuntu (`/etc/network/interfaces`)](#-debian--ubuntu-etcnetworkinterfaces)
    - [📍 RHEL / CentOS / Fedora (`/etc/sysconfig/network-scripts/`)](#-rhel--centos--fedora-etcsysconfignetwork-scripts)
  - [🌍 Configure DNS Settings](#-configure-dns-settings)
  - [🌐 Add Default Gateway via CLI](#-add-default-gateway-via-cli)
  - [🛠 Optional Tools](#-optional-tools)
  - [🧪 Lab: Command-Line Network Configuration](#-lab-command-line-network-configuration)
    - [✅ Task Checklist](#-task-checklist)
  - [📝 Summary](#-summary)
  - [📌 Key Takeaways](#-key-takeaways)

---

## 📘 Introduction

In Linux systems, especially servers and virtual environments, **network configuration from the command line** is a critical task. Unlike GUI-based tools, CLI configurations are **precise**, **scripting-friendly**, and **remote-friendly**.

---

## 🌐 Static vs Dynamic IP Addressing

| Mode        | Description                  | Use Case                         |
| ----------- | ---------------------------- | -------------------------------- |
| **Static**  | Manually assigned IP address | Servers, routers, firewalls      |
| **Dynamic** | Assigned by DHCP server      | End-user devices, mobile devices |

---

## 🧰 CLI Tools You’ll Use

| Tool                 | Purpose                            |
| -------------------- | ---------------------------------- |
| `ip`                 | Manage IP addresses and interfaces |
| `ifconfig`           | Legacy tool for interface settings |
| `route` / `ip route` | View/set routing tables            |
| `nmcli`              | Control NetworkManager connections |
| `hostnamectl`        | Set or show system hostname        |
| `cat`, `vi`, `nano`  | View and edit config files         |

---

## 📦 Set a Static IP (Temporary)

> ⚠️ This method resets after a reboot.

### ✅ Step 1: Bring Interface Down

```bash
sudo ip link set eth0 down
```

### ✅ Step 2: Assign Static IP

```bash
sudo ip addr add 192.168.1.50/24 dev eth0
```

### ✅ Step 3: Add Default Gateway

```bash
sudo ip route add default via 192.168.1.1
```

### ✅ Step 4: Bring Interface Up

```bash
sudo ip link set eth0 up
```

### 🧪 Validate:

```bash
ip addr show eth0
ip route
ping -c 4 8.8.8.8
```

---

## 🔁 Set a Static IP (Persistent)

This depends on your distro.

### 📍 Debian / Ubuntu (`/etc/network/interfaces`)

```bash
sudo nano /etc/network/interfaces
```

```text
auto eth0
iface eth0 inet static
  address 192.168.1.50
  netmask 255.255.255.0
  gateway 192.168.1.1
  dns-nameservers 8.8.8.8 1.1.1.1
```

Then:

```bash
sudo systemctl restart networking
```

---

### 📍 RHEL / CentOS / Fedora (`/etc/sysconfig/network-scripts/`)

File: `/etc/sysconfig/network-scripts/ifcfg-eth0`

```ini
DEVICE=eth0
BOOTPROTO=static
ONBOOT=yes
IPADDR=192.168.1.50
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=8.8.8.8
```

Then:

```bash
sudo systemctl restart network
```

---

## 🌍 Configure DNS Settings

Edit `/etc/resolv.conf`:

```bash
sudo nano /etc/resolv.conf
```

Add:

```text
nameserver 8.8.8.8
nameserver 1.1.1.1
```

> ⚠️ If overwritten by systemd-resolved, use:

```bash
systemd-resolve --status
```

---

## 🌐 Add Default Gateway via CLI

```bash
sudo ip route add default via 192.168.1.1
```

---

## 🛠 Optional Tools

| Tool      | Use                                  |
| --------- | ------------------------------------ |
| `nmcli`   | Good for laptops, GUI-driven servers |
| `netplan` | Used in newer Ubuntu versions        |
| `ethtool` | Interface diagnostics                |
| `tcpdump` | Traffic analysis on an interface     |

---

## 🧪 Lab: Command-Line Network Configuration

> 📘 **Objective**: Assign a static IP and test internet access using CLI only

### ✅ Task Checklist

* [x] Use `ip` commands to assign IP `192.168.56.50/24` to `eth0`
* [x] Add default route `192.168.56.1`
* [x] Set DNS to `8.8.8.8` and `1.1.1.1`
* [x] Validate configuration with `ip addr`, `ip route`, `ping`
* [x] Edit appropriate config files for persistence

---

## 📝 Summary

CLI-based network configuration is a **critical, scriptable, and server-ready** skill. Whether you’re deploying 1 system or 100, understanding the manual process ensures that you can recover or troubleshoot networks without GUI access.

---

## 📌 Key Takeaways

* Use `ip addr` and `ip route` for temporary IP setups.
* Persist static IPs via `/etc/network/interfaces` or `ifcfg-*` files.
* Always verify DNS, gateway, and routes after configuration.
* Learn `nmcli` and `netplan` for more advanced or distro-specific tasks.

---

Would you like a **Bash script generator** that builds your IP config from user input, or a **PDF lab worksheet** for this task? Let me know, and I’ll build it for you!
