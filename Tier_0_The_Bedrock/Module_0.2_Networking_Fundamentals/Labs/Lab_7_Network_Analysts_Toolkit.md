# 🧪 Lab 7: The Network Analyst's Toolkit in Action

### Date: 2025-07-24

### Mentor: *The Da Vinci Cypher*

### Protocol Tier: Tier 0 — System Fundamentals

### Module: Module 0.2 — Networking Fundamentals

---

## 🎯 1. Objective

To use a suite of fundamental command-line tools (`traceroute`, `netstat`, `whois`) to perform network diagnostics and open-source intelligence (OSINT) gathering.

## 🧰 2. Tools Used

| Tool/Command | Purpose |
|--------------|---------|
| `traceroute` | Maps the network path (hops) from a source to a destination. |
| `netstat -antp` | Shows active TCP network connections and listening services on the local machine. |
| `whois`      | Queries public databases for domain name registration information. |

---

## 🖥️ 3. Process & Commands (Live Data Capture)

### 🔹 Step 1: Mapping a Network Path

* **Command:** `traceroute google.com`
* **Output:**

  ```plaintext
  traceroute to google.com (142.250.192.110), 30 hops max, 60 byte packets
   1  _gateway (192.168.31.2)  0.372 ms  0.668 ms  0.618 ms
   2  * * *
   3  * * *
  ...
  ```

### 🔹 Step 2: Inspecting Local Network Connections

* **Command:** `sudo netstat -antp`
* **Output:**

  ```plaintext
  Active Internet connections (servers and established)
  Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
  tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1115/sshd: /usr/sbi 
  tcp6       0      0 :::22                   :::*                    LISTEN      1115/sshd: /usr/sbi 
  ```

### 🔹 Step 3: Gathering Domain Intelligence (OSINT)

* **Command:** `whois google.com`
* **Output Snippet:**

  ```plaintext
     Domain Name: GOOGLE.COM
     Registrar: MarkMonitor Inc.
     Creation Date: 1997-09-15T04:00:00Z
     Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited
     Name Server: NS1.GOOGLE.COM
  ```

---

## 🔎 4. Observations & Analysis

* **`traceroute` Analysis:** The successful first hop to the gateway (`192.168.31.2`) followed by asterisks (`* * *`) indicates that the local connection is working, but routers further out on the internet are configured not to respond to `traceroute` probes, likely for security reasons. This is a common and expected result.
* **`netstat` Analysis:** The output confirmed that the `sshd` service (PID 1115) is in a `LISTEN` state on port `22`. The local address `0.0.0.0` signifies it is listening on all available IPv4 interfaces, making it accessible from any machine that can reach the host's IP address. This highlights the need for firewall rules to control access.
* **`whois` Analysis:** While direct contact details were redacted for privacy, crucial intelligence was gathered:
  * **Registrar:** `MarkMonitor Inc.` is a high-end corporate registrar, suggesting a sophisticated target. This information can be used to craft more targeted phishing attacks.
  * **Domain Status:** The multiple "Prohibited" statuses indicate strong security controls against domain hijacking.
  * **Name Servers:** The listed name servers (`NS1.GOOGLE.COM`, etc.) provide direct targets for more advanced DNS reconnaissance techniques like zone transfer attempts.

---

## ✅ 5. Conclusion

This lab demonstrated the practical application of a network analyst's core toolkit. We successfully mapped a network path, identified a firewalled route, inspected local listening services, and performed open-source intelligence gathering on a domain. These three tools (`traceroute`, `netstat`, `whois`) provide critical visibility into network paths, local machine state, and public-facing infrastructure, forming the foundation of both network troubleshooting and cybersecurity reconnaissance.
