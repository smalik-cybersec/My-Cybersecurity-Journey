Here’s your **full structured, lab-ready Markdown module** for:

---

# 📘 `Lesson04-Edit-Network-Config-Files.md`

> ✅ **Module 12 – Managed Networking**
> 🧠 **Linux Essentials Level 3 (RHEL-Focused)**
> 🗂️ Topic: Manual configuration of static and DHCP network settings using file-based methods (non-GUI) on RHEL systems.

---

## 📌 Introduction

In enterprise environments—especially in headless servers or cloud VMs—networking must often be configured via **plain-text configuration files** rather than GUI tools. This lesson focuses on:

* Structure of RHEL network config files
* Manual static/DHCP IP setup
* Persisting configurations across reboots
* Common misconfigurations and troubleshooting
* Red/Blue team implications (e.g., detection of rogue IPs)

---

## 🧠 Core Concepts (Feynman-style)

> "A network config file is like a contract between your Linux system and the network. It says: *Here’s who I am (IP), how I talk (gateway), and where to ask questions (DNS). Without this paper contract, the system can't show up to the network meeting.*"

---

### 🔍 Key Files on RHEL

| File                                     | Purpose                     |
| ---------------------------------------- | --------------------------- |
| `/etc/sysconfig/network-scripts/ifcfg-*` | Main interface config files |
| `/etc/resolv.conf`                       | DNS resolver file           |
| `/etc/hostname`                          | System hostname             |
| `/etc/hosts`                             | Static name resolution      |

---

## 🧪 Beginner Lab: Manual Static IP Configuration

### 🧾 Task: Configure a static IP using a config file

---

### 🔧 Step 1: Identify Your Interface Name

```bash
nmcli device status
```

→ Example: `enp0s3`

---

### 📝 Step 2: Create/Edit the Config File

```bash
sudo vi /etc/sysconfig/network-scripts/ifcfg-enp0s3
```

#### Sample Static IP Config:

```ini
TYPE=Ethernet
BOOTPROTO=none
NAME=enp0s3
DEVICE=enp0s3
ONBOOT=yes
IPADDR=192.168.100.50
NETMASK=255.255.255.0
GATEWAY=192.168.100.1
DNS1=8.8.8.8
```

---

### 🔁 Step 3: Restart Networking Service

```bash
sudo nmcli con reload
sudo nmcli con up enp0s3
```

---

### 📋 Step 4: Validate the Configuration

```bash
ip a
ip r
cat /etc/resolv.conf
```

---

### 🧪 Tactical Variation: Switch to DHCP

```ini
BOOTPROTO=dhcp
```

Then:

```bash
sudo nmcli con reload
sudo nmcli con up enp0s3
```

---

## 🧠 Detection & Troubleshooting

### 🔎 Checkpoints:

| Check               | Command                                           |
| ------------------- | ------------------------------------------------- |
| Interface up?       | `nmcli device status`                             |
| IP assigned?        | `ip a`                                            |
| Gateway reachable?  | `ip r` / `ping -c2 8.8.8.8`                       |
| DNS working?        | `ping google.com`                                 |
| Config file syntax? | `cat /etc/sysconfig/network-scripts/ifcfg-enp0s3` |

---

### ⚠️ Common Errors

| Issue                        | Cause                                      | Fix                                         |
| ---------------------------- | ------------------------------------------ | ------------------------------------------- |
| Interface doesn’t start      | `ONBOOT=no`                                | Set `ONBOOT=yes`                            |
| No IP                        | `BOOTPROTO=none` + no `IPADDR`             | Add static or use `BOOTPROTO=dhcp`          |
| DNS doesn’t work             | `DNS1` missing or `/etc/resolv.conf` empty | Add `DNS1=...` or edit `/etc/resolv.conf`   |
| Overwritten config on reboot | Controlled by NetworkManager               | Use `nmcli` to manage or disable NM control |

---

## ⚔️ Red/Blue Team Simulation

| Role         | Task                                                                |
| ------------ | ------------------------------------------------------------------- |
| 🟥 Red Team  | Manually edit IP config to set a conflicting IP or DNS exfil filter |
| 🟦 Blue Team | Detect change via `diff`, `auditd`, or `tripwire` and revert config |

---

## ❓ Quiz (Inline Sample)

1. **Which file controls the boot behavior of a network interface on RHEL?**
   a) `/etc/network/interfaces`
   b) `/etc/sysconfig/network-scripts/ifcfg-*` ✅
   c) `/etc/hosts`
   d) `/etc/hostname`

2. **If a system has no DNS resolution after a reboot, but can ping IPs, what likely file is misconfigured?**
   ✅ `/etc/resolv.conf`

---

## 📓 Journaling Prompts

> Answer in your daily log after completing this lesson:

1. What are the risks of misconfiguring `BOOTPROTO` or `ONBOOT`?
2. Can I switch between DHCP and static IP using only files?
3. What happens if I forget to reload or bring the connection up?

---

## 🗂 Filename

```bash
Lesson04-Edit-Network-Config-Files.md
```

---

## 🧠 Revision Planner

| Day    | Task                                                            |
| ------ | --------------------------------------------------------------- |
| Day 1  | Write a static config file manually and bring up interface      |
| Day 3  | Switch between DHCP and static using only `vi` + `nmcli`        |
| Day 7  | Troubleshoot a broken config file with bad IP or missing fields |
| Day 30 | Perform a red team test: simulate rogue DNS and fix from CLI    |

---

Would you like the following add-ons next?

* 🧪 **Red/Blue simulation file** (e.g., rogue config detection)?
* 🧾 **Template files** (`ifcfg-sample-static.conf`, `ifcfg-sample-dhcp.conf`)
* 🧠 **Memory diagram or mind map** of networking config flow?

Let me know and we’ll build the next layer of mastery.
