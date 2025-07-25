
**Notes File:** `Module_1.3/Notes/1_Firewalls_and_Network_Security.md`

```markdown
# 📝 Notes: Firewalls & Network Security

### Date: 2025-07-24
### Mentor: The Da Vinci Cypher

---

## 1. Key Definitions

*   **Firewall:** A network security device or software that monitors and filters incoming and outgoing network traffic based on a set of security rules.
*   **Packet Filtering:** A firewall technique that makes decisions based on the header information of a network packet.
*   **The Five-Tuple:** The five key pieces of information used in packet filtering: Source IP, Destination IP, Source Port, Destination Port, and Protocol.
*   **Implicit Deny (Default Deny):** The fundamental security principle that any traffic not explicitly permitted by a rule is automatically blocked. This is the most secure firewall posture.

---

## 2. Core Concepts

*   **The Castle Gatehouse Analogy:** A firewall acts as the gatehouse to a network (the castle). It inspects the "paperwork" (the five-tuple) of every packet (cart) and decides whether to allow or block it based on the rules (the guards' orders).
*   **Attack Surface Reduction:** The primary function of a firewall is to reduce the system's attack surface. By blocking all ports except those that are absolutely necessary, it prevents attackers from even communicating with potentially vulnerable services.
*   **Functionality vs. Security:** There is always a trade-off between enabling services for users and maintaining a secure posture. Opening a port in a firewall is a deliberate decision to accept a certain level of risk in order to provide a necessary function.

---

## 3. `firewalld` on RHEL

*   `firewalld` is the default firewall management tool on modern Red Hat systems.
*   It uses the concept of **zones** (e.g., `public`, `internal`, `dmz`) to apply different rule sets depending on the network the interface is connected to.
*   Rules can be added temporarily or made permanent with the `--permanent` flag.
*   After adding a permanent rule, the firewall must be reloaded with `firewall-cmd --reload` for the change to take effect in the live configuration.
