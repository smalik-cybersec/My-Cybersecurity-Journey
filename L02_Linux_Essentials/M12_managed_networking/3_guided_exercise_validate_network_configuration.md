Absolutely, Shahid. Below is your **🔧 Guided Exercise** for:

> 📘 **Lesson 02 – Validate Network Configuration**
> 🎯 **Module 12 – Linux Essentials Level 3**
> 🛠️ RHEL-based, lab-tested, revision-compatible
> 🧱 Markdown-structured for Obsidian + GitHub Pages

---

# 🧪 `Lesson02-Guided-Exercise-Validate-Network-Configuration.md`

**🎓 Objective:** Learn how to validate and troubleshoot basic network configuration on a RHEL system using command-line tools and logs.
**🧠 Outcome:** By the end, you'll confirm IP, DNS, gateway, interface status, and diagnose issues with connectivity.

---

## 🗺️ Exercise Overview

| 🧩 Task                         | Tool/Command                      | Validation Goal                             |
| ------------------------------- | --------------------------------- | ------------------------------------------- |
| Check Interface Status          | `ip a`, `nmcli device`            | Interface is **UP** and has **IP**          |
| Confirm IP Address & Subnet     | `ip addr show <iface>`            | Correct IP range and subnet mask            |
| Validate Default Gateway        | `ip route`, `ip r`                | A default route exists to the gateway       |
| Check DNS Resolution            | `cat /etc/resolv.conf`, `ping`    | DNS server is set and name resolution works |
| Test Network Connectivity       | `ping 8.8.8.8`, `ping google.com` | Confirms Internet + DNS reachability        |
| View Logs for Validation/Errors | `journalctl -u NetworkManager`    | Detect interface events, DHCP, DNS failures |

---

## 🧑‍🏫 Step-by-Step Instructions

> 🔁 Run each step **in sequence**, document outputs, and troubleshoot if needed.

---

### ✅ Step 1: Check All Interfaces and Status

```bash
ip a
nmcli device status
```

> ✅ Confirm interface like `enp0s3` is `UP` and **has an IP**
> ✏️ **Document:** Interface name + assigned IP

---

### ✅ Step 2: Show IP Address + Subnet Mask

```bash
ip addr show enp0s3
```

> ✅ Note the subnet (e.g., `/24`)
> ✏️ **Document:** Subnet mask (e.g., 255.255.255.0 or `/24`)

---

### ✅ Step 3: Check the Default Gateway

```bash
ip route
```

Expected line:

```bash
default via 192.168.1.1 dev enp0s3
```

> ✏️ **Document:** Gateway IP

---

### ✅ Step 4: Check DNS Configuration

```bash
cat /etc/resolv.conf
```

Expected entry:

```bash
nameserver 8.8.8.8
```

> ✏️ **Document:** All DNS IPs listed

---

### ✅ Step 5: Ping Public IP

```bash
ping 8.8.8.8 -c 2
```

> ✅ If this works: **Internet + Gateway is fine**
> ❌ If this fails: Troubleshoot gateway or interface

---

### ✅ Step 6: Ping Domain Name

```bash
ping google.com -c 2
```

> ✅ If this works: **DNS resolution works**
> ❌ If this fails: Check `/etc/resolv.conf`, try `dig google.com`

---

### ✅ Step 7: Review NetworkManager Logs

```bash
journalctl -u NetworkManager --since "10 minutes ago"
```

> 🔍 Look for:

* Interface state changes (e.g., `activated`, `disconnected`)
* DHCP lease activity
* DNS resolver errors

---

## 🧠 Bonus: Reset Broken Configuration

If something is misconfigured, reset using:

```bash
nmcli con reload
nmcli con up <connection-name>
```

Or manually set DNS:

```bash
nmcli con mod <connection-name> ipv4.dns "8.8.8.8"
nmcli con up <connection-name>
```

---

## 🧾 Guided Output Sheet

| Item              | Output / Your Notes              |
| ----------------- | -------------------------------- |
| Interface name    |                                  |
| IP Address        |                                  |
| Subnet Mask       |                                  |
| Gateway IP        |                                  |
| DNS Servers       |                                  |
| Ping 8.8.8.8      | ✅ / ❌ (Result?)                  |
| Ping google.com   | ✅ / ❌ (Result?)                  |
| Log Errors Found? | Yes / No (if yes, note messages) |
| Overall Result    | Pass / Fail                      |

---

## 🧪 Journal Prompt

> 📝 *“Did every tool confirm the expected network state? If something failed, how did I troubleshoot it?”*
> Rate your confidence in:

* Interface status
* Gateway + DNS detection
* Log reading

---

## 🧭 Mapping to Skills & Certs

| Role          | Relevance                                 |
| ------------- | ----------------------------------------- |
| SOC Analyst   | Confirm endpoints are reachable/loggable  |
| Pentester     | Validate scope visibility before scanning |
| IR Specialist | Quickly detect misconfig causing outage   |

| Certification  | Topics Mapped                           |
| -------------- | --------------------------------------- |
| CompTIA Linux+ | Interface, gateway, DNS troubleshooting |
| CEH            | Network context mapping                 |
| OSCP           | Validate footprinting targets           |

---

## ✅ Filename

```
Lesson02-Guided-Exercise-Validate-Network-Configuration.md
```

---

Would you like to continue with:

* 🧠 **Quiz session** for this lesson?
* 🧪 **Break-Fix lab** to simulate DNS/gateway failure?
* 📘 Move to next lesson in Module 12? (Please share the title)

I'm with you every packet and ping of the way, Shahid! 💥
