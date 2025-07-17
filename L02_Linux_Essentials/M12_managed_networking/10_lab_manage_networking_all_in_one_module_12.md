🔥 **Lab Activated:**

# 🧪 Lab: Manage Networking (All-in-One – Module 12)

📂 `Module12-AllInOne-Lab.md`
🎓 Linux Essentials Level 3 – RHEL Edition
🛠️ Unified Simulation Lab | GitHub-Ready | Real-World | Red/Blue Integrated

---

## 🧭 **🎯 Lab Objective**

In this full-scale simulation, you’ll operate as a **Linux Systems Engineer** tasked with deploying a secure and fully operational RHEL-based server in a simulated enterprise lab.

You’ll:

* Build and validate network configuration from the ground up.
* Set static IP, subnet, and gateway using CLI and config files.
* Edit `/etc/hosts`, `/etc/resolv.conf`, and manage DNS behavior.
* Set and validate hostnames across reboots.
* Analyze logs for hostname and interface behavior.
* Simulate Red Team tampering and Blue Team detection.

> 🔗 Each section connects logically to the next, mimicking a **real-world deployment + defense scenario**.

---

## 🗂️ **Lab Structure**

| Phase   | Objective                                        |
| ------- | ------------------------------------------------ |
| Phase 1 | Environment Check + Interface Mapping            |
| Phase 2 | IP Addressing and Routing                        |
| Phase 3 | Hostname + Name Resolution Setup                 |
| Phase 4 | Configuration File Hardening                     |
| Phase 5 | Red Team Simulation: Hostname Spoof + DNS Poison |
| Phase 6 | Blue Team Detection: Log Analysis & Response     |

---

## 🧱 **Phase 1: Environment Check + Interface Mapping**

### 🔹 View Interfaces + Routing Table

```bash
ip addr show
ip route show
nmcli dev show
```

> ✅ Document interface names (e.g., `enp0s3`), MAC, assigned IPs, and gateways.

### 🔹 Check DNS Resolver

```bash
cat /etc/resolv.conf
```

---

## 🔧 **Phase 2: IP Addressing and Routing (Static Configuration)**

### 🔹 Assign Static IP via `nmcli`

```bash
sudo nmcli con mod "Wired connection 1" ipv4.addresses 192.168.10.50/24
sudo nmcli con mod "Wired connection 1" ipv4.gateway 192.168.10.1
sudo nmcli con mod "Wired connection 1" ipv4.dns 8.8.8.8
sudo nmcli con mod "Wired connection 1" ipv4.method manual
sudo nmcli con up "Wired connection 1"
```

> 💡 Use `nmcli con show` to confirm changes.

---

## 🖥️ **Phase 3: Hostname + Name Resolution Setup**

### 🔹 Set Static Hostname

```bash
sudo hostnamectl set-hostname fileserver1.cyberlab.local
```

### 🔹 Add Entry to `/etc/hosts`

```bash
sudo vi /etc/hosts
```

Add:

```
127.0.0.1   fileserver1.cyberlab.local fileserver1
```

### 🔹 Configure DNS in `/etc/resolv.conf`

```bash
nameserver 8.8.8.8
nameserver 1.1.1.1
```

⚠️ **NOTE:** If NetworkManager overrides this, make DNS changes persistent via `nmcli`.

---

## 🔐 **Phase 4: Configuration File Hardening**

### 🔹 Manually Edit Network Files

```bash
sudo vi /etc/sysconfig/network-scripts/ifcfg-enp0s3
```

Ensure it includes:

```bash
BOOTPROTO=static
ONBOOT=yes
IPADDR=192.168.10.50
GATEWAY=192.168.10.1
DNS1=8.8.8.8
```

### 🔹 Restart Network Services

```bash
sudo systemctl restart NetworkManager
```

---

## ⚔️ **Phase 5: Red Team Simulation – Spoof + DNS Poison**

### 🔹 Tamper Hostname (Anti-Forensics)

```bash
sudo hostnamectl set-hostname localhost
```

### 🔹 Poison `/etc/hosts`

```bash
echo "192.168.10.66 google.com" | sudo tee -a /etc/hosts
```

Test:

```bash
ping google.com
```

🔴 **If ping resolves to a local IP, poisoning is successful.**

---

## 🛡️ **Phase 6: Blue Team Detection – Logs + Analysis**

### 🔹 Detect Hostname Tampering

```bash
journalctl -u systemd-hostnamed
```

### 🔹 Detect DNS Poisoning

```bash
cat /etc/hosts | grep google
```

### 🔹 Reset to Safe State

```bash
sudo hostnamectl set-hostname fileserver1.cyberlab.local
sudo vi /etc/hosts   # remove fake google.com entry
```

---

## ✅ **Final Verification Checklist**

| Item                                     | Status |
| ---------------------------------------- | ------ |
| Network Interface Mapped                 | ✅      |
| Static IP & Gateway Set                  | ✅      |
| DNS Resolvers Working                    | ✅      |
| Hostname Persisted                       | ✅      |
| `/etc/hosts` + `/etc/resolv.conf` Edited | ✅      |
| Manual Config File Reviewed              | ✅      |
| Red Team Tampering Simulated             | ✅      |
| Blue Team Detection Performed            | ✅      |
| System Rebooted + All Persistent         | ✅      |

---

## 📘 Export Info

* Filename: `Module12-AllInOne-Lab.md`
* Store in: `labs/module12/`
* Associated images:

  * `images/network-topology.png`
  * `images/redteam-hostname-poisoning.png`

---

## 🧠 Confidence Journaling Prompts

* Can I differentiate between static, transient, and pretty hostnames?
* Can I explain how DNS works in RHEL vs other distros?
* What are the risks of poorly managed `/etc/hosts`?
* How would a SOC detect name resolution manipulation?

📝 Save reflections in `journals/module12-lab-journal.md`

---

## 🧠 Revision Plan

| Day    | Task                                            |
| ------ | ----------------------------------------------- |
| Day 1  | Repeat Lab + Watch DNS behavior                 |
| Day 3  | Quiz + simulate Red/Blue name spoofing          |
| Day 7  | Rewrite `/etc/sysconfig/` manually from scratch |
| Day 30 | Complete blind-lab (no notes)                   |

---

✅ Shahid, this is your **All-in-One Network Management Lab** — complete, structured, cert-ready, simulation-driven, and GitHub-publishable.

Would you like me to export this into raw Markdown format for GitHub/Obsidian/MkDocs right now?
