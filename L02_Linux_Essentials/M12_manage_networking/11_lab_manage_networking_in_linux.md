Here is your full, GitHub-ready, recruiter-quality Markdown documentation for:

---

# 🧪 Lab: **Manage Networking in Linux**

> 🔧 **Goal**: Practice essential networking commands, interface management, DNS setup, and troubleshooting using only the Linux command line.
> 🧠 **Skill Level**: Beginner → Intermediate
> 🎯 **Module Context**: Linux Essentials – Manage Networking
> 🔐 **Cybersecurity Relevance**: Secure, correct network setup is foundational for penetration testing, monitoring, intrusion detection, firewalling, and forensic analysis.

---

## 🧭 Table of Contents

- [🧪 Lab: **Manage Networking in Linux**](#-lab-manage-networking-in-linux)
  - [🧭 Table of Contents](#-table-of-contents)
  - [📘 Lab Objectives](#-lab-objectives)
  - [🧰 Prerequisites](#-prerequisites)
  - [📦 Lab Environment Setup](#-lab-environment-setup)
  - [✅ Step 1: Identify Active Interfaces](#-step-1-identify-active-interfaces)
  - [✅ Step 2: Assign a Temporary Static IP](#-step-2-assign-a-temporary-static-ip)
  - [✅ Step 3: Add a Default Gateway](#-step-3-add-a-default-gateway)
  - [✅ Step 4: Configure DNS Settings](#-step-4-configure-dns-settings)
  - [✅ Step 5: Test Local and Internet Connectivity](#-step-5-test-local-and-internet-connectivity)
  - [✅ Step 6: Use `tcpdump` to Monitor Traffic](#-step-6-use-tcpdump-to-monitor-traffic)
  - [📝 Lab Report Template](#-lab-report-template)
  - [📌 Key Takeaways](#-key-takeaways)

---

## 📘 Lab Objectives

By the end of this lab, you will be able to:

* Check Linux network interfaces and IPs
* Assign a static IP address from the CLI
* Add a default route to reach external networks
* Configure DNS resolvers manually
* Test and validate both local and global connectivity
* Monitor real-time traffic using `tcpdump`

---

## 🧰 Prerequisites

| Item            | Description                                           |
| --------------- | ----------------------------------------------------- |
| OS              | Linux VM or bare-metal (Ubuntu, Debian, CentOS, etc.) |
| Access          | `sudo` privileges                                     |
| Installed Tools | `iproute2`, `ping`, `tcpdump`, `dig` or `bind-utils`  |

> ✅ Tip: If not installed:

```bash
sudo apt install iproute2 dnsutils tcpdump -y      # Debian/Ubuntu  
sudo yum install iproute bind-utils tcpdump -y     # RHEL/CentOS  
```

---

## 📦 Lab Environment Setup

* Your system is connected via a **bridged or NAT** interface.
* You will **temporarily assign** network settings (reset after reboot).
* Replace `eth0` with your actual interface name (`ens33`, `enp0s3`, etc.).

---

## ✅ Step 1: Identify Active Interfaces

```bash
ip link show
ip addr show
```

> 📌 Note interface names like `eth0`, `ens33`, or `enp0s3`.

---

## ✅ Step 2: Assign a Temporary Static IP

```bash
sudo ip addr flush dev eth0                # Optional: remove old IPs  
sudo ip addr add 192.168.56.50/24 dev eth0
```

> This assigns IP `192.168.56.50` with subnet mask `/24` to `eth0`.

---

## ✅ Step 3: Add a Default Gateway

```bash
sudo ip route add default via 192.168.56.1
ip route
```

> Output should show:

```text
default via 192.168.56.1 dev eth0
```

---

## ✅ Step 4: Configure DNS Settings

```bash
sudo nano /etc/resolv.conf
```

Add:

```text
nameserver 8.8.8.8
nameserver 1.1.1.1
```

> ⚠️ If overwritten, manage via `systemd-resolve --status` or `nmcli`.

---

## ✅ Step 5: Test Local and Internet Connectivity

```bash
ping -c 4 192.168.56.1           # Ping gateway  
ping -c 4 8.8.8.8                # Ping external IP  
ping -c 4 google.com             # Ping domain (test DNS)  
dig github.com                  # DNS resolution test
```

> ✅ All tests should succeed.

---

## ✅ Step 6: Use `tcpdump` to Monitor Traffic

```bash
sudo tcpdump -i eth0 icmp
```

> This will show ICMP traffic (like ping). In another terminal:

```bash
ping -c 4 google.com
```

You should see packets captured live.

> 🧠 Try variations:

```bash
sudo tcpdump -i eth0 port 80
sudo tcpdump -i eth0 not port 22
```

---

## 📝 Lab Report Template

> 🧾 Use this template to record your work:

```text
👤 Interface Name: eth0
📦 Static IP: 192.168.56.50
🌐 Gateway: 192.168.56.1
🌍 DNS: 8.8.8.8, 1.1.1.1
🔁 Routes Configured: ✅ Yes
🌐 Ping Gateway: ✅
🌐 Ping Internet IP: ✅
🌐 Ping Domain: ✅
🔍 DNS Resolution: ✅
📊 Tcpdump Output: ICMP packets captured? ✅
```

---

## 📌 Key Takeaways

* The `ip` command suite is the modern way to configure interfaces, routes, and IPs.
* Changes made via `ip` are **temporary** unless persisted in config files.
* Always verify DNS separately using tools like `dig` or `nslookup`.
* `tcpdump` is a powerful tool for real-time network analysis — critical for cybersecurity.

---

Would you like:

* 📜 A version of this lab that saves the configuration **permanently**?
* 🧪 A **troubleshooting version** where students fix broken configs?
* 🧰 A **Bash script generator** that configures the interface with user input?

Just say the word. I'm ready for your next topic!
