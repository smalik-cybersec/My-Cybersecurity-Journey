```markdown
# 🧪 Lab 4: Network Reconnaissance & Configuration

### Date: 2025-07-23
### Mentor: *The Da Vinci Cypher*
### Protocol Tier: Tier 0 — System Fundamentals
### Module: Module 0.2 — Networking Fundamentals

---

## 🎯 1. Objective
To investigate the network configuration of a local Linux machine. The goal is to identify its IP address, MAC address, and to test basic network connectivity to both local and external hosts.

## 🧰 2. Tools Used

| Tool/Command | Purpose | OSI Layer |
|--------------|---------|-----------|
| `ip addr`    | Shows network interface details, including IP and MAC addresses. | Layer 3 & 2 |
| `ip route`   | Displays the system's IP routing table, revealing the default gateway. | Layer 3 |
| `ping`       | Tests reachability to another host by sending ICMP echo requests. | Layer 3 |

---

## 🖥️ 3. Process & Commands (Live Data Capture)

### 🔹 Step 1: Identifying Network Addresses

* **Command:** `ip addr`
* **Output:**
  ```plaintext
  1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
      link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
      inet 127.0.0.1/8 scope host lo
         valid_lft forever preferred_lft forever
  2: ens160: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
      link/ether 00:0c:29:ff:0c:1d brd ff:ff:ff:ff:ff:ff
      inet 192.168.11.131/24 brd 192.168.11.255 scope global noprefixroute ens160
         valid_lft forever preferred_lft forever
  ```

### 🔹 Step 2: Identifying the Default Gateway

* **Command:** `ip route`
* **Output:**

  ```plaintext
  default via 192.168.11.1 dev ens160 proto static metric 100 
  192.168.11.0/24 dev ens160 proto kernel scope link src 192.168.11.131 metric 100 
  ```

### 🔹 Step 3: Testing Local & External Connectivity

* **Command (Local):** `ping -c 4 192.168.11.1`
* **Output:**

  ```plaintext
  PING 192.168.11.1 (192.168.11.1) 56(84) bytes of data.

  --- 192.168.11.1 ping statistics ---
  4 packets transmitted, 0 received, 100% packet loss, time 3091ms
  ```

* **Command (External):** `ping -c 4 8.8.8.8`
* **Output:**

  ```plaintext
  PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.

  --- 8.8.8.8 ping statistics ---
  4 packets transmitted, 0 received, 100% packet loss, time 3087ms
  ```

---

## 🔎 4. Observations & Analysis

* The primary network interface `ens160` has a **MAC Address** of `00:0c:29:ff:0c:1d` (Layer 2) and an **IP Address** of `192.168.11.131` (Layer 3).
* The system's **Default Gateway** is correctly identified as `192.168.11.1`. This is the designated router for all non-local traffic.
* The `ping` tests resulted in **100% packet loss** for both the local gateway and the external Google DNS server.
* **Security Insight:** This is a critical finding. The `100% packet loss` indicates that while the host is configured for the network, it cannot send or receive ICMP traffic to its gateway or beyond. The most likely cause is a **firewall rule** (either on the host, the hypervisor, or the gateway router) or a **network address translation (NAT) misconfiguration**. The host is effectively in an **internet-isolated state**.

---

## ✅ 5. Conclusion

This lab successfully demonstrated the foundational commands for network reconnaissance on a Linux system. The unexpected `ping` failures provided a valuable real-world troubleshooting scenario. The key takeaway is that network diagnostics is a process of logical deduction. We established the host's identity (`ip addr`), discovered its intended path to the internet (`ip route`), and then tested that path (`ping`), revealing a network-level block. For any security professional, determining if a host is isolated or has full internet egress is a primary and critical piece of intelligence.

```