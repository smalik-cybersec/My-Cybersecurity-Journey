Here’s your **Guided Exercise** for:

---

# 🧪 Guided Exercise: Edit Network Configuration Files

📂 `Lesson04-Edit-Network-Config-Files.md`
🎓 **Linux Essentials Level 3 – Module 12: Managed Networking**
🔧 Focus: Manual network configuration on RHEL systems using config files

---

## 🎯 Objective

You will manually edit and apply a static or DHCP network configuration by modifying the correct files under `/etc/sysconfig/network-scripts/` in RHEL. You’ll validate your changes, troubleshoot issues, and log every step.

---

## 🛠️ Environment Setup

| Component      | Detail                      |
| -------------- | --------------------------- |
| OS             | RHEL 9 (or compatible)      |
| Interface name | Use `enp0s3`, `eth0`, etc.  |
| Permissions    | Root / `sudo` required      |
| Tools          | `vi`, `nmcli`, `ip`, `ping` |

---

## 🧾 Step-by-Step Instructions

---

### ✅ Step 1: Identify Interface

```bash
nmcli device status
```

Note your active interface (e.g., `enp0s3`).

---

### ✅ Step 2: Navigate to Config Directory

```bash
cd /etc/sysconfig/network-scripts/
```

List existing interface files:

```bash
ls ifcfg-*
```

---

### ✅ Step 3: Backup Old Config

```bash
sudo cp ifcfg-enp0s3 ifcfg-enp0s3.bak
```

---

### ✅ Step 4: Edit for Static IP Configuration

Open the interface config file:

```bash
sudo vi ifcfg-enp0s3
```

Replace or insert:

```ini
TYPE=Ethernet
BOOTPROTO=none
DEVICE=enp0s3
ONBOOT=yes
IPADDR=192.168.100.100
NETMASK=255.255.255.0
GATEWAY=192.168.100.1
DNS1=8.8.8.8
```

Save and exit.

---

### ✅ Step 5: Apply Config

```bash
sudo nmcli con reload
sudo nmcli con up enp0s3
```

---

### ✅ Step 6: Validate Configuration

```bash
ip a | grep enp0s3
ip r
cat /etc/resolv.conf
```

Test connectivity:

```bash
ping -c 2 8.8.8.8
ping -c 2 google.com
```

---

### 🛠️ Step 7: Edit for DHCP (Optional)

Edit the file again:

```bash
BOOTPROTO=dhcp
```

Remove static entries:

```bash
# Remove: IPADDR, NETMASK, GATEWAY, DNS1
```

Then:

```bash
sudo nmcli con reload
sudo nmcli con up enp0s3
```

---

### 📋 Step 8: Document in Journal

In your Obsidian daily log or lab notebook, record:

* Interface used
* Static vs DHCP config
* Commands used
* Output from `ip`, `nmcli`, and `ping`
* Problems faced (if any) and how you fixed them

---

## 🚨 Troubleshooting Checklist

| Symptom                  | Check                                         |
| ------------------------ | --------------------------------------------- |
| No IP after reboot       | `ONBOOT=yes` present?                         |
| DNS doesn't resolve      | `DNS1` in config? `/etc/resolv.conf` valid?   |
| Interface won't activate | `nmcli con reload/up` ran? File syntax clean? |
| Reverting changes fails  | Use `.bak` backup file                        |

---

## 🧠 Reflection Prompts

* What does `BOOTPROTO=none` do?
* Why must you run `nmcli con reload` after edits?
* What would happen if you mistype `DEVICE=enp0s3` as `DEVICE=enps03`?

---

## 📁 Submission Snapshot (Optional)

Include in your GitHub/Obsidian vault:

```bash
lab-edit-network-config/
├── ifcfg-enp0s3-static.conf
├── ifcfg-enp0s3-dhcp.conf
├── lab-journal.md
├── ping-test.txt
├── ip-a-output.txt
```

---

## 📌 Job Role Alignment

| Role          | Skill Relevance                                    |
| ------------- | -------------------------------------------------- |
| Linux Admin   | Primary task — servers rarely use GUI              |
| SOC Analyst   | Spot config anomalies or rogue IP settings         |
| Pentester     | Find misconfigs or alter network behavior covertly |
| IR Specialist | Audit and rollback suspicious config changes       |

---

## 🎓 Cert Mapping

* ✅ **CompTIA Linux+ (Domain: System Configuration)**
* ✅ **CEH (Network Scanning / Recon)**
* ✅ **RHCSA (Network Configuration & Troubleshooting)**

---

## 🔁 Revision Plan

| Day | Task                                                            |
| --- | --------------------------------------------------------------- |
| 1   | Configure static IP from file, bring interface up, validate     |
| 3   | Break config intentionally (typos), fix and log troubleshooting |
| 7   | Switch from DHCP → static → DHCP fully via CLI + journal steps  |
| 30  | Red team: simulate rogue DNS or duplicate IP, fix as blue team  |

---

Let me know if you'd like:

* 📁 Ready-made sample config files
* 🛡️ Red/Blue team lab variant
* 🧩 YAML-to-config-file auto-generator for Obsidian

Your mastery is just a few labs away. What’s next?
