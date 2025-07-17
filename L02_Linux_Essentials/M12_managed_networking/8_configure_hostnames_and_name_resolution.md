Here’s your full 🔧 **Lesson 05** breakdown for:

---

# 🧠 Lesson 05: Configure Hostnames and Name Resolution

📂 `Lesson05-Hostnames-NameResolution.md`
🎓 Linux Essentials Level 3 | Module 12: Managed Networking
🖥️ RHEL Focused | CLI First | Red/Blue Team Ready

---

## 📘 1. Introduction

Hostname and name resolution are core to both identity and connectivity. In Linux, managing **hostnames** ensures your system has a recognizable label, while **name resolution** translates human-readable domains like `google.com` to IP addresses.

---

## 🔍 2. Core Concepts (Feynman Style)

| Concept                          | Feynman Analogy                                                                      |
| -------------------------------- | ------------------------------------------------------------------------------------ |
| **Hostname**                     | Like your computer’s nickname on the network — useful for identification.            |
| **DNS**                          | Like asking a directory service to convert a contact name into a phone number.       |
| **FQDN**                         | Full Name (like `laptop1.mylab.local`) vs just “Laptop1”.                            |
| **/etc/hosts**                   | A personal address book: maps names to IPs without asking DNS.                       |
| **/etc/resolv.conf**             | The page that tells Linux where the DNS server is.                                   |
| **Static vs Transient Hostname** | Static = permanent label; Transient = temporary nickname set during boot or by DHCP. |

---

## 🧾 3. Commands & Configs (with Examples)

### 🔹 Set Hostname Using hostnamectl

```bash
sudo hostnamectl set-hostname redteam-node01.localdomain
```

View current settings:

```bash
hostnamectl status
```

Output sample:

```
Static hostname: redteam-node01.localdomain
Transient hostname: redteam-node01
Icon name: computer-vm
Chassis: vm
```

---

### 🔹 Add FQDN to /etc/hosts

```bash
sudo vi /etc/hosts
```

Add:

```text
127.0.0.1   redteam-node01.localdomain redteam-node01
```

---

### 🔹 Verify DNS Resolution with dig

```bash
dig google.com
```

Check where queries go:

```bash
cat /etc/resolv.conf
```

---

### 🔹 resolv.conf Example

```text
nameserver 8.8.8.8
```

> ⚠️ On RHEL, this file may be overwritten by NetworkManager unless you control it via `nmcli` or `systemd-resolved`.

---

## 🧪 4. Labs

### 🔰 Beginner Lab: Set and Persist Hostname

```bash
sudo hostnamectl set-hostname blue-node.lab.local
hostnamectl status
```

Edit `/etc/hosts` to reflect:

```
127.0.0.1 blue-node.lab.local blue-node
```

Reboot. Run:

```bash
hostname
hostname -f
```

---

### 🧩 Tactical Lab: Simulate DNS Failure

1. Temporarily replace DNS with bad IP:

```bash
sudo vi /etc/resolv.conf
# Change:
nameserver 8.8.8.8
# To:
nameserver 10.10.10.10
```

2. Try:

```bash
ping google.com
```

3. Observe failure. Fix it. Journal the steps.

---

### 🛡️ Red Team Angle: Mask System Identity

```bash
sudo hostnamectl set-hostname localhost
```

💡 Simulates evasion in post-exploitation to confuse logging systems.

---

### 🔵 Blue Team Detection

* Changes to hostname can be traced in:

```bash
journalctl | grep hostname
```

* Look for suspicious resets to `localhost`, `ubuntu`, etc.

---

## 📋 5. Summary Table

| File/Command            | Purpose                               |                        |
| ----------------------- | ------------------------------------- | ---------------------- |
| `hostnamectl`           | Set/view static hostname              |                        |
| `/etc/hosts`            | Local name resolution override        |                        |
| `/etc/resolv.conf`      | Defines DNS servers                   |                        |
| `nmcli dev show`        | Lists current DNS from NetworkManager |                        |
| `dig`, `ping`, `getent` | Tools to test name resolution         |                        |
| \`journalctl            | grep host\`                           | Track hostname changes |

---

## 📓 6. Journaling Prompts

| Prompt                                                        | Response |
| ------------------------------------------------------------- | -------- |
| What's the difference between static and transient hostnames? | ...      |
| What breaks if `/etc/hosts` is missing or malformed?          | ...      |
| Did you ever face a DNS failure? How did you fix it?          | ...      |

Add logs + commands + ping failures + screenshots to `Lesson05-journal.md`

---

## 🧠 7. Confidence Rating

> Scale: 🌑 (Clueless) → 🌗 (Getting it) → 🌕 (Crystal Clear)

How confident are you now in:

* Setting persistent hostnames?
* Diagnosing DNS problems?
* Reading `/etc/hosts` or `resolv.conf`?
* Using `hostnamectl`, `dig`, and `nmcli`?

> Log your confidence in your journal + revisit in next revision cycles.

---

## 🧭 8. Job & Cert Mapping

| Cert           | Topics Covered                  |
| -------------- | ------------------------------- |
| RHCSA          | Network config, hostname, DNS   |
| CompTIA Linux+ | Name resolution, CLI networking |
| CEH            | Evasion via hostname spoofing   |

| Job Role      | Relevance                         |
| ------------- | --------------------------------- |
| SOC Analyst   | DNS misconfig detection           |
| Pentester     | Identity obfuscation during pivot |
| IR Specialist | Track hostname tampering          |

---

## 🧠 9. Revision Plan

| Day | Task                                                          |
| --- | ------------------------------------------------------------- |
| 1   | Set + persist hostname, edit `/etc/hosts`, validate with ping |
| 3   | Simulate DNS failure, fix `/etc/resolv.conf` manually         |
| 7   | Run red/blue simulation — mask hostname, log detection        |
| 30  | Break host resolution, rebuild from logs + journal only       |

---

Would you like a:

* 📝 Quiz for Lesson 05?
* 🧪 Real Red/Blue lab scenario?
* 📁 GitHub-ready Obsidian markdown?

Let me know, and I’ll prep it instantly.
