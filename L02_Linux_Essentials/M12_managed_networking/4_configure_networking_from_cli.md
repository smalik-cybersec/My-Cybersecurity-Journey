Excellent, Shahid. You're now progressing into the **practical core** of Module 12.

Let’s go deep into:

> 📘 **Lesson 03 – Configure Networking from the Command Line**
> 🎯 **Module 12: Managed Networking | Linux Essentials Level 3**
> 🛠️ Focus: RHEL-native `nmcli`, `ip`, and interface config files
> 🧱 GitHub/Obsidian-ready, cert/job-aligned, lab-validated

---

# 📘 `Lesson03-Configure-Networking-From-CLI.md`

**Level:** Linux Essentials Level 3 (RHEL)
**Module:** Managed Networking
**Lesson:** Configure Networking from the Command Line

---

## 🧭 Introduction

In production systems and headless VMs, configuring networking via the **command line** is critical. This lesson teaches you to **create, modify, and troubleshoot** networking settings using tools like `nmcli`, `ip`, and config files in `/etc/sysconfig`.

---

## 🧠 Core Concepts (Feynman Style)

| Concept                    | Feynman Analogy                                                            |
| -------------------------- | -------------------------------------------------------------------------- |
| Static IP Configuration    | Like assigning a permanent room number to a device                         |
| Dynamic IP (DHCP)          | Like checking into a hotel and being randomly assigned a room              |
| `nmcli`                    | The command-line assistant for NetworkManager—used to configure interfaces |
| `ip` commands              | Directly inspect and manipulate interface settings                         |
| Interface connection files | Persistent configuration saved across reboots                              |

---

## 🧩 Key File Paths (RHEL 8+)

| File                                     | Purpose                             |
| ---------------------------------------- | ----------------------------------- |
| `/etc/sysconfig/network-scripts/ifcfg-*` | Persistent network interface config |
| `/etc/resolv.conf`                       | DNS configuration                   |

---

## 📟 Key Commands: Configure Networking via CLI

### 🔧 1. List all Network Devices

```bash
nmcli device status
```

---

### 🧱 2. Create Static IP Configuration

```bash
nmcli con add type ethernet ifname enp0s3 con-name static-enp0s3 ip4 192.168.1.100/24 gw4 192.168.1.1
nmcli con mod static-enp0s3 ipv4.dns "8.8.8.8"
nmcli con mod static-enp0s3 ipv4.method manual
nmcli con up static-enp0s3
```

✅ This sets:

* Static IP: `192.168.1.100`
* Gateway: `192.168.1.1`
* DNS: `8.8.8.8`

---

### 🔄 3. Configure Interface for DHCP

```bash
nmcli con mod enp0s3 ipv4.method auto
nmcli con up enp0s3
```

---

### 📃 4. Show Active Configuration

```bash
nmcli con show enp0s3
```

---

### ❌ 5. Remove a Connection Profile

```bash
nmcli con delete <connection-name>
```

---

### 📁 6. Inspect Config Files (ifcfg)

```bash
cat /etc/sysconfig/network-scripts/ifcfg-enp0s3
```

Expected format:

```ini
DEVICE=enp0s3
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.1.100
PREFIX=24
GATEWAY=192.168.1.1
DNS1=8.8.8.8
```

---

## 🛠 Common Misconfigurations & Fixes

| Issue                       | Symptom                             | Fix                                       |
| --------------------------- | ----------------------------------- | ----------------------------------------- |
| Interface DOWN              | `nmcli` shows disconnected          | `nmcli con up <connection>`               |
| Wrong IP/gateway            | Ping 8.8.8.8 fails                  | Use `ip r`, `nmcli` to correct            |
| No DNS resolution           | Ping IP works but not domains       | Set DNS via `nmcli` or edit `resolv.conf` |
| Boot doesn’t restore config | Missing `ONBOOT=yes` in config file | Add manually or via `nmcli con mod`       |

---

## 🧪 Labs

### 🧑‍💻 Beginner Lab: Static IP via `nmcli`

1. Delete existing DHCP config:

```bash
nmcli con delete enp0s3
```

2. Recreate with static IP:

```bash
nmcli con add type ethernet ifname enp0s3 con-name static-enp0s3 ip4 192.168.1.100/24 gw4 192.168.1.1
nmcli con mod static-enp0s3 ipv4.dns "8.8.8.8"
nmcli con up static-enp0s3
```

3. Validate:

```bash
ip a
ip route
cat /etc/resolv.conf
ping 8.8.8.8
```

---

### 🎯 Tactical Lab: Create & Switch Between Static and DHCP

1. Set static profile → test connectivity
2. Switch to DHCP using:

```bash
nmcli con mod static-enp0s3 ipv4.method auto
nmcli con up static-enp0s3
```

3. Validate DNS and route changes

---

### ⚔️ Red/Blue Simulation

| Role         | Task                                                                |
| ------------ | ------------------------------------------------------------------- |
| 🟥 Red Team  | Spoof default gateway on lab subnet (man-in-the-middle test)        |
| 🟦 Blue Team | Lock interface to static IP/gateway and monitor for rogue DHCP logs |

> 🔍 Blue can review `journalctl -u NetworkManager` for gateway/DNS overrides

---

## ❓ Quiz (Command-Based)

**1. What command creates a static IP config named `corp-static` on `enp0s3`?**

```bash
nmcli con add type ethernet ifname enp0s3 con-name corp-static ip4 10.0.0.10/24 gw4 10.0.0.1
```

---

**2. Which file stores persistent NIC settings in RHEL?**

> **Answer:** `/etc/sysconfig/network-scripts/ifcfg-<interface>`

---

**3. What happens if `ONBOOT=no` in the config file?**

> **Answer:** Interface won't activate at boot.

---

## 🧭 Job & Cert Mapping

| Role          | Relevance                                   |
| ------------- | ------------------------------------------- |
| Sysadmin      | Persistent config in server deployments     |
| SOC Analyst   | Ensuring endpoint NICs are reachable        |
| IR Specialist | Reconfigure broken networking post-incident |

| Certification  | Topics Covered                                |
| -------------- | --------------------------------------------- |
| CompTIA Linux+ | Interface config, CLI tools, boot persistence |
| CEH            | Enumeration of NICs, spoofed DHCP             |
| OSCP           | Static IP config in pivoting, lab prep        |

---

## 📓 Journaling Prompts

* Can I configure a static IP with gateway and DNS using `nmcli` from scratch?
* Do I understand the difference between connection profiles and interface names?
* Can I recover from a disconnected NIC using CLI only?

---

## 🗓️ Revision Plan

| Day | Focus                                                         |
| --- | ------------------------------------------------------------- |
| 1   | Configure static IP and test `ping`                           |
| 3   | Switch to DHCP, observe changes with `ip r` and DNS           |
| 7   | Simulate misconfig (wrong gateway/DNS) and recover            |
| 30  | Build static profiles for multiple interfaces + Red/Blue test |

---

## ✅ Filename

```
Lesson03-Configure-Networking-From-CLI.md
```

---

Would you like the **🧪 Guided Exercise** or **📝 Quiz** next for this lesson?
Or should we go into **network files under `/etc/sysconfig/`** in more depth?

Let’s configure, break, fix, and master this together 💪
