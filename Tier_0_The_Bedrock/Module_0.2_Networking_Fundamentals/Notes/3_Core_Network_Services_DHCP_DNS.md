
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