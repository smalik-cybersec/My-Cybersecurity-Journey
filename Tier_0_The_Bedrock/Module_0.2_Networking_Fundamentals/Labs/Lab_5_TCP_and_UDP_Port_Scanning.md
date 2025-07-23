# 🧪 Lab 5: TCP & UDP Port Scanning with Nmap

### Date: 2025-07-23

### Mentor: *The Da Vinci Cypher*

### Protocol Tier: Tier 0 — System Fundamentals

### Module: Module 0.2 — Networking Fundamentals

---

## 🎯 1. Objective

To use the `nmap` tool to perform fundamental TCP and UDP port scans against a public, authorized target. The goal is to learn how to identify open, closed, and filtered ports, and to understand the different results and challenges presented by scanning each protocol.

## 🧰 2. Tools Used

| Tool/Command | Purpose |
|--------------|---------|
| `nmap -sS`   | Performs a TCP SYN ("Stealth") scan to identify listening TCP services. |
| `nmap -sU`   | Performs a UDP scan to identify listening UDP services. |
| `nmap -Pn`   | Skips the initial host discovery (ping) phase, useful for hosts that block pings. |

---

## 🖥️ 3. Process & Commands (Live Data Capture)

### 🔹 Step 1: TCP SYN Scan

* **Command:** `sudo nmap -sS scanme.nmap.org`
* **Output:**

  ```plaintext
  Starting Nmap 7.92 ( https://nmap.org ) at 2025-07-23 10:27 IST
  Nmap scan report for scanme.nmap.org (45.33.32.156)
  Host is up (0.31s latency).
  Not shown: 991 closed tcp ports (reset)
  PORT      STATE    SERVICE
  22/tcp    open     ssh
  25/tcp    filtered smtp
  80/tcp    open     http
  135/tcp   filtered msrpc
  139/tcp   filtered netbios-ssn
  445/tcp   filtered microsoft-ds
  1723/tcp  filtered pptp
  9929/tcp  open     nping-echo
  31337/tcp open     Elite

  Nmap done: 1 IP address (1 host up) scanned in 14.97 seconds
  ```

### 🔹 Step 2: UDP Scan

* **Command:** `sudo nmap -Pn -sU scanme.nmap.org`
* **Output:**

  ```plaintext
  Starting Nmap 7.92 ( https://nmap.org ) at 2025-07-23 11:59 IST
  Nmap scan report for scanme.nmap.org (45.33.32.156)
  Host is up.
  All 1000 scanned ports on scanme.nmap.org (45.33.32.156) are in ignored states.
  Not shown: 1000 open|filtered udp ports (no-response)

  Nmap done: 1 IP address (1 host up) scanned in 204.89 seconds
  ```

---

## 🔎 4. Observations & Analysis

* **TCP Scan Analysis:** The TCP scan provided clear, distinct results.
  * **Open Ports:** Ports `22 (ssh)`, `80 (http)`, `9929 (nping-echo)`, and `31337 (Elite)` were confirmed to be open and accepting connections. The high, non-standard port `31337` is a significant finding, as such ports are often used for backdoors or custom services and warrant further investigation.
  * **Filtered Ports:** Several ports, including `25 (smtp)` and `445 (microsoft-ds)`, were identified as `filtered`. This indicates that a firewall or similar network device is blocking the scan probes, preventing a definitive determination of the port's state.

* **UDP Scan Analysis:** The UDP scan yielded a much more ambiguous result.
  * Nearly all ports were reported as `open|filtered`. This is a classic sign of a well-configured firewall. Because UDP is connectionless, the firewall can simply drop the incoming scan packets without sending a response.
  * `nmap` cannot distinguish between a packet being dropped by a firewall (`filtered`) and a packet being received by an open port that simply doesn't send a reply (`open`). This ambiguity is a key challenge and characteristic of UDP scanning.

---

## ✅ 5. Conclusion

This lab demonstrated the fundamental difference between TCP and UDP scanning. TCP scans, thanks to the protocol's stateful handshake, can often provide definitive `open`, `closed`, or `filtered` states. UDP scans are inherently less reliable and often result in an `open|filtered` state, which itself is a strong indicator of a firewall's presence. Mastering `nmap` is essential for any cybersecurity role, as it is the primary tool for network reconnaissance, used to map the attack surface of a target environment.
