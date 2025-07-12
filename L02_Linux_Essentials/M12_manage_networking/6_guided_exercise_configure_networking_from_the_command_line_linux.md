Here is your **Guided Exercise** for:

---

# 🎯 Guided Exercise: **Configure Networking from the Command Line (Linux)**

> 🛠️ **Objective**: Practice setting up network interfaces, IP addresses, gateways, and DNS using CLI tools only — with **no GUI**.
> 🧠 **Level**: Beginner → Intermediate
> 🔐 **Cybersecurity Relevance**: In security audits, forensic recovery, or penetration testing, GUI tools are often unavailable. CLI configuration is **mission-critical** in isolated, headless, or compromised environments.

---

## 🧭 Table of Contents

- [🎯 Guided Exercise: **Configure Networking from the Command Line (Linux)**](#-guided-exercise-configure-networking-from-the-command-line-linux)
  - [🧭 Table of Contents](#-table-of-contents)
  - [📘 Learning Outcomes](#-learning-outcomes)
  - [🧰 Prerequisites \& Tools](#-prerequisites--tools)
  - [📦 Lab Setup Instructions](#-lab-setup-instructions)
  - [✅ Task 1: Identify Interface Name](#-task-1-identify-interface-name)
  - [✅ Task 2: Assign Temporary Static IP](#-task-2-assign-temporary-static-ip)
  - [✅ Task 3: Add a Default Gateway](#-task-3-add-a-default-gateway)
  - [✅ Task 4: Configure DNS Servers](#-task-4-configure-dns-servers)
  - [✅ Task 5: Validate Full Network Connectivity](#-task-5-validate-full-network-connectivity)
  - [✅ Task 6: Make IP Configuration Persistent](#-task-6-make-ip-configuration-persistent)
    - [📍 Debian/Ubuntu:](#-debianubuntu)
    - [📍 RHEL/CentOS:](#-rhelcentos)
  - [🧪 Bonus: Break \& Fix Scenario](#-bonus-break--fix-scenario)
    - [Step 1: Flush All Network Settings](#step-1-flush-all-network-settings)
    - [Step 2: Try pinging external site:](#step-2-try-pinging-external-site)
    - [Step 3: Reconfigure Manually:](#step-3-reconfigure-manually)
  - [📝 Documentation Template](#-documentation-template)

---

## 📘 Learning Outcomes

By the end of this guided lab, you will be able to:

* Use `ip` and `ip route` to manually assign IPs
* Add a default gateway via command line
* Manually set DNS resolvers
* Test configuration for internet and LAN access
* Persist changes across reboots using config files

---

## 🧰 Prerequisites & Tools

| Requirement       | Description                                           |
| ----------------- | ----------------------------------------------------- |
| OS                | Linux VM or Bare Metal (Ubuntu, Debian, CentOS, etc.) |
| Privileges        | `sudo` access                                         |
| Tools             | `ip`, `ping`, `nano`, `cat`, `dig`, `traceroute`      |
| Package Installed | `dnsutils` or `bind-utils`, `iproute2`                |

---

## 📦 Lab Setup Instructions

✅ If using VirtualBox or VMware, use **Bridged** or **NAT** network mode.
✅ Assume your interface name is `eth0` or `ens33`. (Use `ip a` to check)

---

## ✅ Task 1: Identify Interface Name

```bash
ip link show
```

* Identify your primary network interface.
* Look for common names like `eth0`, `ens33`, `enp0s3`.

> 🔍 Note it down: **Your interface name: \_\_\_\_\_\_\_\_\_\_\_\_**

---

## ✅ Task 2: Assign Temporary Static IP

> This config will be **lost on reboot** — useful for testing or recovery.

```bash
sudo ip addr flush dev eth0  # Optional: clear existing IPs
sudo ip addr add 192.168.1.100/24 dev eth0
```

Verify:

```bash
ip addr show eth0
```

---

## ✅ Task 3: Add a Default Gateway

```bash
sudo ip route add default via 192.168.1.1
```

Check routing table:

```bash
ip route
```

---

## ✅ Task 4: Configure DNS Servers

Edit `/etc/resolv.conf`:

```bash
sudo nano /etc/resolv.conf
```

Add:

```text
nameserver 8.8.8.8
nameserver 1.1.1.1
```

Validate:

```bash
dig google.com
```

---

## ✅ Task 5: Validate Full Network Connectivity

* Ping your default gateway:

```bash
ping -c 4 192.168.1.1
```

* Ping public IP:

```bash
ping -c 4 8.8.8.8
```

* Ping domain:

```bash
ping -c 4 google.com
```

* Trace route:

```bash
traceroute google.com
```

✅ If all pass — your network is correctly configured.

---

## ✅ Task 6: Make IP Configuration Persistent

> Choose based on your Linux distro:

### 📍 Debian/Ubuntu:

Edit `/etc/network/interfaces`

```bash
sudo nano /etc/network/interfaces
```

Example config:

```text
auto eth0
iface eth0 inet static
  address 192.168.1.100
  netmask 255.255.255.0
  gateway 192.168.1.1
  dns-nameservers 8.8.8.8 1.1.1.1
```

Then restart:

```bash
sudo systemctl restart networking
```

---

### 📍 RHEL/CentOS:

Edit `/etc/sysconfig/network-scripts/ifcfg-eth0`

```bash
sudo nano /etc/sysconfig/network-scripts/ifcfg-eth0
```

Example:

```ini
DEVICE=eth0
BOOTPROTO=static
ONBOOT=yes
IPADDR=192.168.1.100
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=8.8.8.8
```

Then restart:

```bash
sudo systemctl restart network
```

---

## 🧪 Bonus: Break & Fix Scenario

> 🧩 Simulate a real-world failure and recover.

### Step 1: Flush All Network Settings

```bash
sudo ip addr flush dev eth0
sudo ip route flush dev eth0
```

### Step 2: Try pinging external site:

```bash
ping 8.8.8.8
```

Should fail.

### Step 3: Reconfigure Manually:

```bash
sudo ip addr add 192.168.1.100/24 dev eth0
sudo ip route add default via 192.168.1.1
echo -e "nameserver 8.8.8.8\nnameserver 1.1.1.1" | sudo tee /etc/resolv.conf
```

✅ Retest ping and DNS resolution.

---

## 📝 Documentation Template

> 🖋️ Fill this in after your exercise. Keep in a cybersecurity lab journal or GitHub logbook.

```text
Interface Name: ____________
Assigned IP: ____________/24
Default Gateway: ____________
DNS Servers: ________________________
Interface Status: UP / DOWN
Ping Gateway: ✅ / ❌
Ping Internet IP: ✅ / ❌
Ping Domain: ✅ / ❌
Persistent Config File Edited: Yes / No
```

---

Let me know if you'd like this turned into:

* ✅ A **Bash script** to automate the entire procedure
* 📄 A **PDF printable worksheet**
* 💡 A **real-world incident simulation** (e.g., server lost IP after reboot — recover using CLI)

Ready when you are for the next topic!
