# 📘 `Lesson01-Describe-Networking-Concepts.md`

**Module 12: Managed Networking | Linux Essentials Level 3 (RHEL)**

---

## 🧭 Introduction

In Linux systems, networking isn't just about IP addresses or cables—it's about enabling **secure, efficient communication** between systems, services, and users. This lesson lays the **foundational concepts** required to understand Linux-managed networking, preparing you for interface management, routing, firewalls, and advanced troubleshooting.

---

## 🧠 Core Concepts (Feynman Style)

| Concept               | Feynman Explanation                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------ |
| **Network**           | A group of connected computers that share resources or data—like people in a room talking. |
| **IP Address**        | A computer's "home address" on the network.                                                |
| **MAC Address**       | A hardware ID for network cards—like a fingerprint.                                        |
| **Subnet**            | A mini-network inside a bigger one, with devices grouped together.                         |
| **Gateway**           | The door from your subnet to the internet/world.                                           |
| **DNS**               | Like a phonebook—it translates domain names to IPs.                                        |
| **DHCP**              | The automatic system that gives devices an IP address temporarily.                         |
| **Routing**           | The path that data takes across networks—like GPS for packets.                             |
| **Ports & Protocols** | Like different channels or lanes for types of traffic (e.g., HTTP = port 80).              |
| **Firewall**          | A security guard filtering good/bad network traffic.                                       |

---

## 🖥️ Diagram: Basic Linux Networking Components

```plaintext
            +------------+                     +-------------+
            |  Linux PC  |---------------------|  Switch     |
            | (RHEL VM)  |                     |             |
            +------------+                     +-------------+
                 |                                   |
            [eth0 | enp0s3]                   [other devices]
                 |
          +-------------+
          |  Router /   | ➜ Internet (Gateway: 192.168.1.1)
          |  Gateway    |
          +-------------+
```

---

## ⚙️ Commands & Configs (RHEL)

### 🔍 Check IP Address (RHEL)

```bash
ip addr show
# OR
ip a
```

### 🔍 View Routing Table

```bash
ip route
```

### 🔍 View DNS Settings

```bash
cat /etc/resolv.conf
```

### 🔍 Show Network Interfaces (RHEL 8+)

```bash
nmcli device status
```

### 🛠 Risk Awareness

| Misconfiguration | Risk/Impact                          | Detection Tip                                |
| ---------------- | ------------------------------------ | -------------------------------------------- |
| Wrong gateway    | No internet or external access       | `ip route` will show incorrect default route |
| No DNS servers   | Can't resolve domains                | Test with `dig` or `ping google.com`         |
| Duplicate IP     | Conflicts, unstable connectivity     | Use `arp-scan`, `ip neigh`                   |
| Unmanaged NIC    | Interface won’t auto-connect at boot | Check `nmcli connection`                     |

---

## 🧪 Labs

### 🧑‍💻 Beginner Lab: View Current Network Configuration

```bash
# Step 1: Check IP and interfaces
ip a

# Step 2: Check the gateway
ip route

# Step 3: Check DNS settings
cat /etc/resolv.conf
```

> 🔎 Lab Journal Prompt:
> “Did your system receive an IP from DHCP or is it static? What DNS server is listed? Can you ping 8.8.8.8 and google.com?”

---

### 🎯 Tactical Lab: Identify Misconfigurations

1. Disconnect the interface using `nmcli`
2. Manually configure a wrong IP or gateway
3. Use `ping`, `dig`, and `traceroute` to diagnose
4. Reconfigure correctly using `nmtui` or `nmcli`

---

### ⚔️ Red/Blue Simulation

| Role         | Task                                                                                                 |
| ------------ | ---------------------------------------------------------------------------------------------------- |
| 🟥 Red Team  | Set up rogue DHCP server on test subnet to spoof gateway/DNS                                         |
| 🟦 Blue Team | Detect IP conflicts and rogue DHCP via `journalctl -u NetworkManager` logs, use `tcpdump` on port 67 |

---

## ❓ Quiz (MCQs + Logs)

### ✅ Multiple Choice

**1. What command shows your default gateway on RHEL?**
A) `nmcli con show`
B) `ip route`
C) `ifconfig`
D) `ping`

**Answer:** B

**2. What file holds DNS resolver settings in most Linux distros?**
A) `/etc/hosts`
B) `/etc/network/interfaces`
C) `/etc/resolv.conf`
D) `/etc/sysconfig/dns`

**Answer:** C

---

### 📁 Log Analysis

**Log Sample:**

```log
Jul 16 13:22:17 rhel-vm NetworkManager[1234]: device (enp0s3): state change: activated → disconnected
```

**Question:**
What might cause this log entry?

**Answer:**
Manual disconnection via `nmcli` or cable unplugged.

---

## 🧾 Summary Table + Checklist

| Element              | Covered |
| -------------------- | ------- |
| Network Terms        | ✅       |
| Commands (ip, nmcli) | ✅       |
| Config Files         | ✅       |
| Basic Labs           | ✅       |
| Red/Blue Simulation  | ✅       |
| Logs + Quiz          | ✅       |
| Job/Cert Mapping     | ✅       |
| Revision Plan        | ✅       |

---

## 🧭 Job & Certification Mapping

| Role               | Relevance                               |
| ------------------ | --------------------------------------- |
| SOC Analyst        | Network event logs, misconfig alerts    |
| Pentester          | Discover misconfigs, rogue DHCP, DNS    |
| Incident Responder | Analyze routing or interface-level logs |

| Certification  | Topics Mapped                         |
| -------------- | ------------------------------------- |
| CompTIA Linux+ | Networking basics, interfaces         |
| CEH            | Network enumeration, DHCP/DNS attacks |
| OSCP           | Network visibility during engagement  |

---

## 🗓️ Revision Plan + Journal

### 📅 Day 1

* Run basic labs
* Note current IP, Gateway, DNS

### 📅 Day 3

* Disconnect NIC, manually assign IP/gateway, observe logs

### 📅 Day 7

* Try Red/Blue scenario on test VM
* Compare `nmcli`, `ip`, and logs

### 📅 Day 30

* Revisit with advanced routing concepts

---

### 📓 Journaling Prompts

* Can I explain networking using everyday analogies?
* Can I spot a misconfigured IP, DNS, or gateway from logs or output?
* Which tools help confirm network state reliably?

---

## ✅ Filename

```
Lesson01-Describe-Networking-Concepts.md
```

---

Ready to proceed to the **next lesson in Module 12**? Just give me the lesson title or number, and I’ll follow this exact structure again.

Let’s keep building! 💪
