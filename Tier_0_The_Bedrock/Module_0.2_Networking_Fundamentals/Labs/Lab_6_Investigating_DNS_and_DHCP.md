# 🧪 Lab 6: Investigating DNS and DHCP

### Date: 2025-07-23

### Mentor: _The Da Vinci Cypher_

### Protocol Tier: Tier 0 — System Fundamentals

### Module: Module 0.2 — Networking Fundamentals

---

## 🎯 1. Objective

To use command-line tools to investigate two core network services: the Domain Name System (DNS) and the Dynamic Host Configuration Protocol (DHCP). The goal is to learn how to perform a manual DNS lookup and how to inspect system logs for DHCP lease information.

## 🧰 2. Tools Used

| Tool/Command | Purpose                                                                 |
| ------------ | ----------------------------------------------------------------------- |
| `dig`        | (Domain Information Groper) A powerful tool for making DNS queries.     |
| `journalctl` | A command to query and display logs from the systemd journal.           |
| `grep`       | A tool to filter text and search for lines matching a specific pattern. |

---

## 🖥️ 3. Process & Commands (Live Data Capture)

### 🔹 Step 1: Performing a DNS Lookup

- **Command:** `dig google.com`
- **Output:**

  ```plaintext
  ; <<>> DiG 9.16.23-RH <<>> google.com
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 45739
  ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

  ;; QUESTION SECTION:
  ;google.com.			IN	A

  ;; ANSWER SECTION:
  google.com.		218	IN	A	142.250.192.110

  ;; SERVER: 2409:40d5:100a:bf91::9b#53(2409:40d5:100a:bf91::9b)
  ```

### 🔹 Step 2: Investigating DHCP Lease History from Logs

- **Command:** `journalctl -u NetworkManager.service | grep "dhcp4 (ens160)"`
- **Output Sample:**
  ```plaintext
  Jul 16 15:37:14 localhost.localdomain NetworkManager[993]: <info>  [1752660434.8055] dhcp4 (ens160): state changed new lease, address=192.168.11.131
  Jul 22 23:47:05 bluebox01.cyberlab.local NetworkManager[1070]: <info>  [1753208225.5663] dhcp4 (ens160): state changed new lease, address=10.81.8.93
  ```

---

## 🔎 4. Observations & Analysis

- **DNS Analysis:** The `dig` command successfully queried the DNS server at `2409:40d5:100a:bf91::9b` on port `53`. The server returned an `A` record (an IPv4 address) for `google.com`, which was `142.250.192.110`. This demonstrates the successful translation of a human-readable domain name to a machine-readable IP address, which is the core function of DNS.

- **DHCP Analysis:** The system logs provide a clear history of DHCP leases. On July 16, the machine was assigned the IP `192.168.11.131`. On July 22, it was assigned a completely different IP, `10.81.8.93`.

- **Security Insight:** This log analysis proves that IP addresses assigned via DHCP are **dynamic and non-permanent**. This is expected behavior. However, from a security perspective, an unexpected change in IP address or network range could be an indicator of a malicious event, such as a **Rogue DHCP server** attack on the local network, designed to redirect user traffic through an attacker's machine.

---

## ✅ 5. Conclusion

This lab provided practical experience with two essential, yet often invisible, network services. Using `dig` allowed us to manually perform the function that our computers do automatically thousands of times a day. By inspecting the `journalctl` logs, we were able to find tangible evidence of the DHCP process at work. Understanding how these services operate and how they can be attacked (via DNS or DHCP spoofing) is fundamental for network security analysis and defense.

````

---
And here is your notes file.

**File Name:** `3_Core_Network_Services_DHCP_DNS.md`
**Location:** `Module_0.2.../Notes/`

```markdown
# 📝 Notes: Core Network Services (DHCP & DNS)

### Date: 2025-07-23
### Mentor: The Da Vinci Cypher

---

## 1. Key Definitions

*   **DHCP (Dynamic Host Configuration Protocol):** An application layer protocol that automates the process of assigning IP addresses and other network configuration information (like the default gateway and DNS servers) to devices on a network.
*   **DORA Process:** The four-step process used by DHCP: **D**iscover, **O**ffer, **R**equest, **A**cknowledge.
*   **DNS (Domain Name System):** The internet's global, hierarchical system for translating human-friendly domain names (e.g., `www.google.com`) into machine-readable IP addresses (e.g., `142.250.192.110`).
*   **A Record:** A type of DNS record that maps a domain name to an IPv4 address.

---

## 2. Core Analogies

*   **DHCP is the "Automated Apartment Concierge":** When a new tenant (your device) arrives, it shouts for a concierge (Discover). The concierge offers an available apartment number/IP address (Offer). The tenant accepts (Request), and the concierge finalizes the lease (Acknowledge).
*   **DNS is the "Internet's Phonebook":** It's a massive, distributed contact list that allows you to look up someone's name (`google.com`) to find their phone number (IP address) so you can make a call (initiate a connection).

---

## 3. Cybersecurity Relevance

DHCP and DNS are two of the most commonly targeted core services due to their critical role and trusted position in network communications.

*   **DHCP Attacks:**
    *   **Rogue DHCP Server:** An attacker sets up a malicious DHCP server on a public Wi-Fi network. They can then assign victims an IP address but set the "Default Gateway" to their own laptop. This creates a classic **Man-in-the-Middle (MITM)** attack, where all the victim's internet traffic flows through the attacker's machine for sniffing and manipulation.

*   **DNS Attacks:**
    *   **DNS Poisoning/Spoofing:** An attacker compromises a DNS server or intercepts a DNS query to provide a malicious IP address for a legitimate domain name (e.g., sending a user to a fake banking website).
    *   **DNS Tunneling:** Advanced attackers use DNS queries to exfiltrate data or as a covert **Command and Control (C2)** channel, as DNS traffic is often less scrutinized by firewalls than regular web traffic.

---

## 4. Personal Reflections & Questions

*   *Key Takeaway:* These automated background services are built on trust. Attacking them is effective because it undermines the very foundation of how a device joins a network and navigates to a destination.
*   *Further Question:* "If DNS can be poisoned, what mechanisms exist to protect it and verify that the IP address you receive is authentic?" (This foreshadows technologies like DNSSEC - DNS Security Extensions).
````

This completes our work on this topic. You have now covered the essentials of how individual machines connect and navigate the network.

We have one final, crucial topic to cover in this networking module: the command-line tools that let us tie all this knowledge together. Let me know when you are ready.
