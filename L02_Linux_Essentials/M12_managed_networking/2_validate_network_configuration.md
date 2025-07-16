Perfect, Shahid. Let’s dive into the **next lesson** in **Module 12: Managed Networking**—
📘 **Lesson 02: Validate Network Configuration** (Linux Essentials Level 3, RHEL)

We'll follow the **Ultra Edition v4.0+ protocol**, with markdown-ready docs, diagrams, labs, red/blue simulations, log-based validation, quizzes, and cert/job-role alignment.

---

# 📘 `Lesson02-Validate-Network-Configuration.md`

**Module:** Managed Networking
**Level:** Linux Essentials Level 3 (RHEL)
**Lesson:** Validate Network Configuration
**Goal:** Accurately verify current networking state on a RHEL system

---

## 🧭 Introduction

Validating network configuration ensures that your Linux system can **communicate properly**, access DNS, use gateways, and follow routing rules. This is a **critical diagnostic skill** for SOC Analysts, Incident Responders, and System Admins.

---

## 🧠 Core Concepts (Feynman Style)

| Concept              | Feynman Explanation                                                                |
| -------------------- | ---------------------------------------------------------------------------------- |
| IP Validation        | Check if your system has an address like checking your house has a postal address. |
| Gateway Verification | Ensure your “exit door” to the internet exists and is unlocked.                    |
| DNS Testing          | Can your system "look up phone numbers" (domain resolution)?                       |
| Routing Table        | Like a **Google Maps** route for where to send packets.                            |
| Interface Status     | Are your "network wires" plugged in and working?                                   |

---

## 📟 RHEL Validation Commands (with Real Examples)

> 🔧 These are core tools used by Red Teamers to assess network context and by Blue Teamers to validate connectivity issues.

---

### 🔍 1. Show IP Addresses + Interfaces

```bash
ip a
```

✅ Check for:

* IP address assigned
* Interface `UP` status

---

### 🔍 2. Check Gateway & Routes

```bash
ip route
```

✅ Check for:

* `default via <gateway IP>`
* Subnet route (e.g., `192.168.1.0/24`)

---

### 🔍 3. View DNS Settings

```bash
cat /etc/resolv.conf
```

✅ Should show:

```bash
nameserver 8.8.8.8
```

---

### 🔍 4. Check NIC Status via NetworkManager

```bash
nmcli device status
```

✅ Shows if interface is `connected` or `disconnected`.

---

### 🔍 5. Test Domain Resolution

```bash
ping google.com -c 2
```

✅ Confirms DNS working.

---

### 🔍 6. Test Raw Connectivity

```bash
ping 8.8.8.8 -c 2
```

✅ Confirms gateway + routing are valid.

---

### 🔍 7. Trace the Route to Internet

```bash
traceroute google.com
```

✅ Shows each hop (useful for IR/Pentesting).

---

### 🔍 8. DNS Lookup Tool (Optional)

```bash
dig google.com
```

---

## 🛠️ Risk Factors & Misconfigurations

| Issue          | Risk/Impact                     | Detection                                  |
| -------------- | ------------------------------- | ------------------------------------------ |
| No IP Address  | Interface won’t communicate     | `ip a` shows no address                    |
| Missing DNS    | Can’t resolve domains           | Ping to IP works, but domain fails         |
| Wrong Gateway  | Can’t access external networks  | `ip route` wrong or empty                  |
| Duplicate IP   | Intermittent loss, ARP conflict | Check logs: `journalctl -u NetworkManager` |
| Interface DOWN | No communication                | `nmcli device status`                      |

---

## 🧪 Labs

### 🧑‍💻 Beginner Lab: Validate Your Network in 5 Steps

```bash
# Step 1: Show interfaces and IP
ip a

# Step 2: Show route + gateway
ip route

# Step 3: Show DNS config
cat /etc/resolv.conf

# Step 4: Ping by IP and domain
ping 8.8.8.8 -c 2
ping google.com -c 2

# Step 5: Review interface state
nmcli device status
```

> ✏️ Journal Prompt:
> “What is your IP, Gateway, and DNS? Are you getting a response from 8.8.8.8 and google.com?”

---

### 🧰 Tactical Lab: Break and Fix Network Config

1. Set DNS to a **wrong IP** in `/etc/resolv.conf`
2. Remove default gateway using:

```bash
sudo ip route del default
```

3. Observe behavior with `ping`, `dig`, `ip route`

4. Restore:

```bash
sudo ip route add default via 192.168.1.1
```

---

### ⚔️ Red/Blue Team Simulation

| Role         | Objective                                                     |
| ------------ | ------------------------------------------------------------- |
| 🟥 Red Team  | Enumerate target subnet via interface + route info            |
| 🟦 Blue Team | Detect and fix a misconfigured gateway or missing DNS setting |

---

## ❓ Quiz (MCQs, Logs, Real-World)

### ✅ Multiple Choice

**1. Which file holds DNS resolver settings?**
A) `/etc/hostname`
B) `/etc/resolv.conf`
C) `/etc/nsswitch.conf`
D) `/etc/iproute.conf`

> **Answer:** B

---

**2. Which command shows the default gateway?**
A) `ip a`
B) `cat /etc/resolv.conf`
C) `ip route`
D) `ping`

> **Answer:** C

---

**3. You can ping 8.8.8.8 but not google.com. What's wrong?**
A) Bad gateway
B) DNS issue
C) Routing loop
D) DHCP expired

> **Answer:** B

---

### 📁 Log Analysis

**Log Entry:**

```log
Jul 16 17:20:01 rhel-vm NetworkManager[1234]: dns: no servers available
```

**Q:** What's the issue?

> **Answer:** No valid DNS configured.

---

## 🧾 Summary Table + Checklist

| Validation Task       | Checked ✅ |
| --------------------- | --------- |
| Interface is UP       | ✅         |
| IP address assigned   | ✅         |
| Default route present | ✅         |
| DNS resolves names    | ✅         |
| Ping external IP      | ✅         |

---

## 🧭 Cert + Job Role Mapping

| Role          | Relevance                               |
| ------------- | --------------------------------------- |
| SOC Analyst   | Validate alerts caused by net failures  |
| Pentester     | Enumerate live hosts via IP/route info  |
| IR Specialist | Confirm config after compromise or DDoS |

| Certification  | Topics Mapped                         |
| -------------- | ------------------------------------- |
| CompTIA Linux+ | `ip`, `nmcli`, `resolv.conf`, routing |
| CEH            | Network enumeration basics            |
| OSCP           | Manual recon, interface enumeration   |

---

## 🗓️ Revision Plan

| Day | Focus                                                      |
| --- | ---------------------------------------------------------- |
| 1   | Run `ip`, `ping`, `route` — document findings              |
| 3   | Misconfigure DNS/gateway and recover                       |
| 7   | Analyze boot-time logs + network bring-up sequence         |
| 30  | Red/Blue simulate misconfig + recovery + Wireshark capture |

---

## 📓 Journaling Prompts

* Can I determine if my system is online using CLI only?
* Can I validate connectivity from interface to DNS end-to-end?
* What is the first thing I would check if `ping google.com` fails?

---

## ✅ Filename

```
Lesson02-Validate-Network-Configuration.md
```

---

Let me know if you're ready for:

* 📘 **Quiz** for this lesson
* 🧪 Lab workbook export
* 🚀 Proceed to next lesson in Module 12 (please share title)

We’re building **deep mastery**—one interface, route, and resolver at a time. 💻
