Here is your full **Guided Exercise** for:

---

# 🎯 Guided Exercise: **Edit Network Configuration Files in Linux**

> 🛠️ **Objective**: Configure a Linux system with a **persistent static IP address**, **DNS resolvers**, and a **hostname** by editing native configuration files.
> 📍 **Level**: Beginner to Intermediate
> 🔐 **Cybersecurity Relevance**: Persistent misconfigurations can break services or create attack surfaces. Manual configuration skills are critical in secure, GUI-less environments.

---

## 🧭 Table of Contents

- [🎯 Guided Exercise: **Edit Network Configuration Files in Linux**](#-guided-exercise-edit-network-configuration-files-in-linux)
  - [🧭 Table of Contents](#-table-of-contents)
  - [📘 Learning Outcomes](#-learning-outcomes)
  - [🧰 Requirements](#-requirements)
  - [📦 Setup Notes](#-setup-notes)
  - [✅ Task 1: Locate Your Interface Name](#-task-1-locate-your-interface-name)
  - [✅ Task 2: Configure a Persistent Static IP](#-task-2-configure-a-persistent-static-ip)
    - [📍 Debian/Ubuntu: `/etc/network/interfaces`](#-debianubuntu-etcnetworkinterfaces)
    - [📍 RHEL/CentOS: `/etc/sysconfig/network-scripts/ifcfg-eth0`](#-rhelcentos-etcsysconfignetwork-scriptsifcfg-eth0)
  - [✅ Task 3: Add DNS Servers to `/etc/resolv.conf`](#-task-3-add-dns-servers-to-etcresolvconf)
  - [✅ Task 4: Set Hostname and Local Mapping](#-task-4-set-hostname-and-local-mapping)
    - [🖋️ Set hostname:](#️-set-hostname)
    - [🖋️ Edit `/etc/hostname`:](#️-edit-etchostname)
    - [🖋️ Edit `/etc/hosts`:](#️-edit-etchosts)
  - [✅ Task 5: Restart and Validate Changes](#-task-5-restart-and-validate-changes)
    - [🔁 Restart networking:](#-restart-networking)
    - [🔍 Verify:](#-verify)
  - [🧪 Optional Challenge: Reboot Test \& Troubleshoot](#-optional-challenge-reboot-test--troubleshoot)
    - [🛠️ If config fails:](#️-if-config-fails)
  - [📝 Lab Log Template](#-lab-log-template)

---

## 📘 Learning Outcomes

By the end of this lab, you will be able to:

* Configure a static IP address persistently
* Set and resolve custom hostnames
* Configure DNS nameservers manually
* Validate and troubleshoot your network settings

---

## 🧰 Requirements

| Resource | Description                                                       |
| -------- | ----------------------------------------------------------------- |
| OS       | Linux VM or physical machine (Ubuntu, Debian, CentOS, RHEL, etc.) |
| Access   | `sudo` or root privileges                                         |
| Tools    | `nano`, `cat`, `ip`, `ping`, `dig`, `hostnamectl`                 |

---

## 📦 Setup Notes

* Use a **Bridged** or **NAT** adapter if using VirtualBox/VMware.
* Replace `eth0` with your actual interface name (check using `ip a`).

---

## ✅ Task 1: Locate Your Interface Name

```bash
ip link show
```

* Identify your primary NIC (e.g., `eth0`, `ens33`, `enp0s3`).

👉 **Write it down** — you'll use it in all configurations.

---

## ✅ Task 2: Configure a Persistent Static IP

> ✍️ This step varies by distro. Use the one that applies.

---

### 📍 Debian/Ubuntu: `/etc/network/interfaces`

```bash
sudo nano /etc/network/interfaces
```

Add or modify:

```text
auto eth0
iface eth0 inet static
  address 192.168.56.50
  netmask 255.255.255.0
  gateway 192.168.56.1
  dns-nameservers 8.8.8.8 1.1.1.1
```

---

### 📍 RHEL/CentOS: `/etc/sysconfig/network-scripts/ifcfg-eth0`

```bash
sudo nano /etc/sysconfig/network-scripts/ifcfg-eth0
```

Add/Modify:

```ini
DEVICE=eth0
BOOTPROTO=static
ONBOOT=yes
IPADDR=192.168.56.50
NETMASK=255.255.255.0
GATEWAY=192.168.56.1
DNS1=8.8.8.8
DNS2=1.1.1.1
```

---

## ✅ Task 3: Add DNS Servers to `/etc/resolv.conf`

```bash
sudo nano /etc/resolv.conf
```

Add:

```text
nameserver 8.8.8.8
nameserver 1.1.1.1
```

> ⚠️ On `systemd-resolved` systems, this file may auto-revert. If so, use:

```bash
sudo resolvectl status
```

---

## ✅ Task 4: Set Hostname and Local Mapping

### 🖋️ Set hostname:

```bash
sudo hostnamectl set-hostname lab-node01
```

---

### 🖋️ Edit `/etc/hostname`:

```bash
sudo nano /etc/hostname
```

```text
lab-node01
```

---

### 🖋️ Edit `/etc/hosts`:

```bash
sudo nano /etc/hosts
```

Ensure this line exists:

```text
127.0.1.1   lab-node01.localdomain   lab-node01
```

---

## ✅ Task 5: Restart and Validate Changes

### 🔁 Restart networking:

```bash
sudo systemctl restart networking    # Debian/Ubuntu
sudo systemctl restart network       # RHEL/CentOS
```

### 🔍 Verify:

```bash
ip addr show eth0
ip route
dig google.com
ping -c 4 google.com
hostname
hostname -f
```

---

## 🧪 Optional Challenge: Reboot Test & Troubleshoot

* Reboot your system:

```bash
sudo reboot
```

* After reboot, verify:

```bash
ip a
ping -c 3 8.8.8.8
ping -c 3 google.com
hostname -f
```

### 🛠️ If config fails:

* Use recovery terminal or boot into single-user mode
* Temporarily assign IP:

```bash
sudo ip addr add 192.168.56.55/24 dev eth0
sudo ip route add default via 192.168.56.1
```

---

## 📝 Lab Log Template

> 📓 Use this to document your setup in your lab book or GitHub repository:

```text
🔧 Interface: eth0
🖥️ Static IP: 192.168.56.50/24
🌐 Gateway: 192.168.56.1
🧠 DNS Servers: 8.8.8.8, 1.1.1.1
🏷️ Hostname: lab-node01
🌍 FQDN: lab-node01.localdomain
✅ Internet Connectivity: Yes / No
✅ Name Resolution: Yes / No
📂 Config Files Edited:
  - [x] /etc/network/interfaces OR ifcfg-eth0
  - [x] /etc/resolv.conf
  - [x] /etc/hostname
  - [x] /etc/hosts
```

---

Would you like me to generate a **diagnostic Bash script** that automatically checks all your network config files and shows color-coded results? Just ask — I’m ready!
