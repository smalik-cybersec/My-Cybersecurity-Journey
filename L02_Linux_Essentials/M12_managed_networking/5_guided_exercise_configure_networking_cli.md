Here is your 🔧 **Guided Exercise** for:

> 📘 **Lesson 03 – Configure Networking from the Command Line**
> 🎓 Linux Essentials Level 3 – RHEL-based
> 📁 Filename: `Lesson03-Guided-Exercise-Configure-Networking-CLI.md`
> 🔍 Skill: Using `nmcli`, `ip`, and config files to set static and DHCP network profiles

---

# 🧪 `Lesson03-Guided-Exercise-Configure-Networking-CLI.md`

**Objective:** Learn to configure, activate, and validate networking on a RHEL system entirely from the CLI.
**Outcome:** Ability to switch between static and dynamic (DHCP) networking, troubleshoot issues, and persist configurations.

---

## 🧭 Prerequisites

* RHEL 8 or compatible system with `nmcli` and `ip` tools
* Active non-loopback interface (e.g., `enp0s3`)
* Root/sudo access

---

## 🧩 Step-by-Step Tasks

> 🧠 Follow each step, **capture the result**, and answer reflection prompts after.

---

### ✅ Step 1: Identify Your Interface Name

```bash
nmcli device status
```

📝 **Note down:** Your Ethernet interface (e.g., `enp0s3`, `ens33`, etc.)

---

### ✅ Step 2: Delete Any Previous Connection

```bash
nmcli con show
nmcli con delete <connection-name>
```

✅ Removes old config profiles

---

### ✅ Step 3: Create Static IP Connection Profile

```bash
nmcli con add type ethernet \
  con-name static-lab \
  ifname enp0s3 \
  ip4 192.168.100.50/24 \
  gw4 192.168.100.1
```

```bash
nmcli con mod static-lab ipv4.dns "8.8.8.8"
nmcli con mod static-lab ipv4.method manual
```

---

### ✅ Step 4: Bring Up the New Connection

```bash
nmcli con up static-lab
```

✅ Should bring interface online with static IP

---

### ✅ Step 5: Validate Configuration

```bash
ip a
ip r
cat /etc/resolv.conf
```

> ✏️ Log:

* IP Address:
* Gateway:
* DNS:

---

### ✅ Step 6: Test Connectivity

```bash
ping -c 2 8.8.8.8
ping -c 2 google.com
```

✅ IP ping = gateway is OK
✅ Domain ping = DNS is working

---

### ✅ Step 7: Switch to DHCP Mode

```bash
nmcli con mod static-lab ipv4.method auto
nmcli con up static-lab
```

---

### ✅ Step 8: Recheck IP and Gateway (DHCP)

```bash
ip a
ip r
```

📝 New IP? **Yes / No**
📝 Gateway set? **Yes / No**

---

## ⚠️ Common Issues to Simulate

| Problem                | How to Simulate                | How to Fix                                        |
| ---------------------- | ------------------------------ | ------------------------------------------------- |
| No Internet after boot | Set `ONBOOT=no` in config file | `nmcli con mod <name> connection.autoconnect yes` |
| DNS not resolving      | Remove DNS line or use bad IP  | Re-add correct DNS via `nmcli` or config          |
| Interface disconnected | Manually bring down interface  | `nmcli con up <profile>`                          |

---

## 📓 Guided Output Sheet

| Item                    | Value / Your Notes |
| ----------------------- | ------------------ |
| Interface Name          |                    |
| Static IP Used          |                    |
| Gateway                 |                    |
| DNS Server              |                    |
| Was ping to 8.8.8.8 OK? | ✅ / ❌              |
| Was DNS Resolution OK?  | ✅ / ❌              |
| DHCP Config Worked?     | ✅ / ❌              |

---

## 📖 Reflection Prompts

> Answer in your journal:

1. Can I configure a full networking setup without editing files?
2. What steps break internet connectivity and how can I detect them?
3. How would I help a teammate fix a broken DNS or gateway from CLI?

---

## 🧠 Bonus Practice

### 📂 View Config Files

```bash
cat /etc/sysconfig/network-scripts/ifcfg-static-lab
```

🧠 Does it include `ONBOOT=yes`? What does `BOOTPROTO` say?

---

## 🛡 Red/Blue Lab Ideas

| Role         | Task                                                        |
| ------------ | ----------------------------------------------------------- |
| 🟥 Red Team  | Set rogue static IP on test machine (e.g., 192.168.100.254) |
| 🟦 Blue Team | Use CLI to detect and revert the change via `nmcli` + logs  |

---

## 🗂 Filename

```bash
Lesson03-Guided-Exercise-Configure-Networking-CLI.md
```

---

Would you like:

* 📘 A **cheat sheet** for `nmcli`, `ip`, and config files?
* 🧪 A **break-fix simulation** based on this lesson?
* 💡 Convert this into a script-based automation challenge?

Let’s reinforce these concepts till they’re part of muscle memory. 🧠💪
