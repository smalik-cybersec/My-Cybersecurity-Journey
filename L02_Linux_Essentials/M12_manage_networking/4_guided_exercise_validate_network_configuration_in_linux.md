Here is your **Guided Exercise** for:

---

# 🎯 Guided Exercise: **Validate Network Configuration in Linux**

> 🧩 **Goal**: Step-by-step guide to help you **verify, test, and understand** network configuration on a Linux system using command-line tools.
>
> 📚 **Skill Level**: Beginner → Intermediate
> 🔐 **Cybersecurity Relevance**: Misconfigured or unsecured networking leads to vulnerabilities like DNS hijacking, MITM attacks, and denial of service.

---

## 🧭 Table of Contents

- [🎯 Guided Exercise: **Validate Network Configuration in Linux**](#-guided-exercise-validate-network-configuration-in-linux)
  - [🧭 Table of Contents](#-table-of-contents)
  - [🧠 Learning Objectives](#-learning-objectives)
  - [🧰 Tools Required](#-tools-required)
  - [📦 Pre-Check Setup](#-pre-check-setup)
  - [✅ Task 1: Check Interface Status](#-task-1-check-interface-status)
  - [✅ Task 2: Confirm IP Address and Netmask](#-task-2-confirm-ip-address-and-netmask)
  - [✅ Task 3: Verify Routing Table](#-task-3-verify-routing-table)
  - [✅ Task 4: Validate DNS Resolution](#-task-4-validate-dns-resolution)
  - [✅ Task 5: Confirm Hostname and FQDN](#-task-5-confirm-hostname-and-fqdn)
  - [✅ Task 6: Check Internet and LAN Connectivity](#-task-6-check-internet-and-lan-connectivity)
  - [✅ Task 7: Optional Troubleshooting Steps](#-task-7-optional-troubleshooting-steps)
  - [📌 Reflection \& Reporting](#-reflection--reporting)

---

## 🧠 Learning Objectives

By the end of this guided lab, you will be able to:

* Identify active interfaces and their status
* Confirm IP configuration and routing settings
* Verify DNS resolver configuration
* Check system hostname and name resolution
* Troubleshoot basic network connectivity problems

---

## 🧰 Tools Required

| Tool                      | Purpose                                    |
| ------------------------- | ------------------------------------------ |
| `ip`                      | View interface & routing info              |
| `ping`                    | Test host reachability                     |
| `dig`, `nslookup`         | Test DNS resolution                        |
| `hostname`, `hostnamectl` | View/set system hostname                   |
| `nmcli` (if available)    | View connections in NetworkManager         |
| `traceroute`              | Trace path to a host                       |
| `cat`, `less`             | View config files (`resolv.conf`, `hosts`) |

---

## 📦 Pre-Check Setup

✅ Use a real or virtual Linux machine (Ubuntu, Debian, CentOS, etc.)
✅ Have `sudo` or root access
✅ Ensure `net-tools`, `dnsutils`, or `bind-utils` are installed:

```bash
sudo apt install net-tools dnsutils  # Debian/Ubuntu
sudo yum install net-tools bind-utils  # CentOS/RHEL
```

---

## ✅ Task 1: Check Interface Status

```bash
ip link show
```

* 🔎 Look for interfaces with `state UP`
* Check MAC address (starts with `link/ether`)
* Identify the default interface (usually `eth0`, `ens33`, or `enpXsY`)

---

## ✅ Task 2: Confirm IP Address and Netmask

```bash
ip addr show
```

* Check for `inet` lines
* Example:

  ```
  inet 192.168.1.10/24 brd 192.168.1.255 scope global eth0
  ```

> 🧠 **Q**: What does `/24` mean in this context?

---

## ✅ Task 3: Verify Routing Table

```bash
ip route
```

* Look for `default via ...` (default gateway)
* Check routes for local subnets

> 🧠 **Q**: What will happen if the `default` route is missing?

---

## ✅ Task 4: Validate DNS Resolution

```bash
cat /etc/resolv.conf
```

* Ensure valid `nameserver` entries are listed (e.g., `8.8.8.8`)
* Test DNS using:

```bash
dig google.com
nslookup github.com
```

> 🧠 **Q**: What’s the difference between `dig` and `ping google.com`?

---

## ✅ Task 5: Confirm Hostname and FQDN

```bash
hostname
hostnamectl
hostname -f
```

* Check short name, static name, and fully qualified domain name
* Optional: View `/etc/hosts` to see mappings

> Example:

```bash
127.0.1.1   myhost.localdomain   myhost
```

---

## ✅ Task 6: Check Internet and LAN Connectivity

```bash
ping -c 4 8.8.8.8          # Ping Google DNS (IP only)
ping -c 4 google.com       # Ping with DNS
traceroute google.com      # Trace path to internet
```

> ❗ If `ping 8.8.8.8` works but `ping google.com` fails → DNS problem
> ❗ If both fail → gateway/interface issue

---

## ✅ Task 7: Optional Troubleshooting Steps

| Issue             | Fix                                                 |
| ----------------- | --------------------------------------------------- |
| Interface down    | `sudo ip link set eth0 up`                          |
| Wrong IP          | `sudo dhclient -v eth0` or set static IP            |
| No default route  | `sudo ip route add default via <gateway>`           |
| DNS broken        | Edit `/etc/resolv.conf` to use `nameserver 8.8.8.8` |
| Hostname mismatch | `sudo hostnamectl set-hostname newname`             |

---

## 📌 Reflection & Reporting

✅ **Document the following** in your cybersecurity journal or lab notes:

* Interface Name and IP
* DNS Server(s)
* Default Gateway
* FQDN
* Whether ping and DNS tests passed

> ✍️ Example Journal Entry:

```text
Interface: eth0
IP: 192.168.1.101/24
Gateway: 192.168.1.1
DNS: 8.8.8.8
FQDN: node01.local
Ping Google: ✅
DNS Resolution: ✅
```

---

Would you like a **custom Bash script** to automate all validation steps above, or a **PDF lab worksheet** to print and practice?
Let me know and I’ll create it!
