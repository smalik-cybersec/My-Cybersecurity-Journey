Absolutely, Shahid! Here's your full **🧪 Guided Exercise** for:

---

# 🧪 Guided Exercise: Configure Hostnames and Name Resolution

📂 `Lesson05-Hostnames-NameResolution.md`
🎓 Linux Essentials Level 3 – Module 12 (RHEL)
🛠️ Mode: CLI Hands-on • Real Logs • Static + Transient • DNS Debug

---

## 🎯 Objective

You will:

1. Set static and transient hostnames
2. Configure `/etc/hosts` for local resolution
3. Test DNS with `dig`, `ping`, and `getent`
4. Debug real-world DNS issues
5. Review logs for hostname or DNS events

---

## 🧱 Setup

* 🔧 RHEL VM (or compatible)
* 👤 `sudo` access
* 🧰 Tools: `hostnamectl`, `ping`, `dig`, `nmcli`, `journalctl`
* ✍️ Editor: `vi` or `nano`

---

## 🧪 Step-by-Step Exercise

### ✅ 1. View Current Hostname States

```bash
hostname
hostnamectl
```

> 📋 Output example:

```bash
Static hostname: attacker01.lab.local
Transient hostname: attacker01
```

---

### 🧩 2. Set a Static Hostname

```bash
sudo hostnamectl set-hostname bluebox01.cyberlab.local
```

Check:

```bash
hostnamectl status
hostname -f
```

---

### 🧩 3. Configure /etc/hosts for FQDN Mapping

Edit `/etc/hosts`:

```bash
sudo vi /etc/hosts
```

Add:

```
127.0.0.1   bluebox01.cyberlab.local bluebox01
```

Save and close.

---

### 🔍 4. Configure DNS Resolver

Check current nameservers:

```bash
cat /etc/resolv.conf
```

If missing or incorrect:

```bash
sudo vi /etc/resolv.conf
```

Add Google DNS:

```
nameserver 8.8.8.8
```

💡 **Note**: On RHEL, NetworkManager may overwrite this. You can verify via:

```bash
nmcli dev show | grep DNS
```

---

### 🔍 5. Test Name Resolution

```bash
ping google.com
dig redhat.com
getent hosts google.com
```

If resolution fails:

* Check `/etc/resolv.conf`
* Check firewall/connection

---

### 🛡️ 6. Red Team Simulation — Mask Host Identity

```bash
sudo hostnamectl set-hostname localhost
```

> ✅ Simulates anti-forensic hostname obfuscation

Check logs:

```bash
journalctl -u systemd-hostnamed | tail -n 10
```

📝 Journal what changes were logged!

---

### 🧠 7. Blue Team Check — Detect Tampering

Use:

```bash
journalctl | grep hostname
```

Inspect any suspicious hostname resets (e.g., to `localhost`, `ubuntu`, etc.)

---

### 🔁 8. Reboot & Verify Persistence

```bash
sudo reboot
```

After reboot:

```bash
hostnamectl
cat /etc/hosts
```

---

## 🧪 End of Exercise – Validation Checklist ✅

| Task                                    | Done |
| --------------------------------------- | ---- |
| Static + transient hostname set         | ✅    |
| `/etc/hosts` correctly edited           | ✅    |
| DNS tested with `dig`, `ping`, `getent` | ✅    |
| DNS failure simulated and resolved      | ✅    |
| Red team hostname spoofing simulated    | ✅    |
| Detected hostname tampering via logs    | ✅    |

---

## 📓 Journal Prompts

* What is the difference between transient and static hostname?
* What happens if `/etc/hosts` is missing a FQDN entry?
* How did you simulate and fix DNS failure?
* What hostname tampering patterns would trigger blue team alerts?

Add your answers to `journals/Lesson05-journal.md`

---

## ✅ Ready for More?

Would you like to:

* 🔁 Do a **Quiz Session** on this lesson?
* 🧨 Simulate a **Red vs Blue DNS Poisoning Scenario**?
* 📁 Export all this as Obsidian/GitHub Markdown?

Say the word, and it’s yours.
