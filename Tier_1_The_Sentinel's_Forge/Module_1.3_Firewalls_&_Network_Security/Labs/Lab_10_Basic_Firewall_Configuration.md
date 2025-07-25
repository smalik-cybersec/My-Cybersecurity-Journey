```markdown
# 🧪 Lab 10: Basic Firewall Configuration with `firewalld`

### Date: 2025-07-24
### Mentor: *The Da Vinci Cypher*
### Protocol Tier: Tier 1 — The Sentinel's Forge
### Module: Module 1.3 — Firewalls & Network Security

---

## 🎯 1. Objective
To interact with the `firewalld` service on a Red Hat Enterprise Linux system. The goal is to learn how to inspect the current firewall ruleset, add a new rule to allow a service, and understand the security implications of modifying the firewall configuration.

## 🧰 2. Tools Used
| Tool/Command | Purpose |
|--------------|---------|
| `systemctl`  | Manages system services, used here to check the status of `firewalld`. |
| `firewall-cmd` | The primary command-line tool for managing `firewalld` rules. |

---

## 🖥️ 3. Process & Commands (Live Data Capture)

### 🔹 Step 1: Inspecting the Initial Firewall State

* **Command:** `sudo firewall-cmd --list-all`
* **Initial Output:**
  ```plaintext
  public (default, active)
    ...
    services: cockpit dhcpv6-client ssh
    ...
  ```

### 🔹 Step 2: Adding a New Permanent Rule and Reloading

* **Command to Add the Rule:**

  ```bash
  sudo firewall-cmd --permanent --add-service=http
  ```

* **Command to Activate the Rule:**

  ```bash
  sudo firewall-cmd --reload
  ```

### 🔹 Step 3: Verifying the New Firewall State

* **Command:** `sudo firewall-cmd --list-all`
* **Final Output:**

  ```plaintext
  public (default, active)
    ...
    services: cockpit dhcpv6-client http ssh
    ...
  ```

---

## 🔎 4. Observations & Analysis

* The initial firewall configuration only allowed incoming traffic for `cockpit`, `dhcpv6-client`, and `ssh`. Based on the principle of **Implicit Deny**, all other incoming traffic, including for a web server on port 80, would have been blocked.
* By adding the `http` service, we successfully modified the ruleset to permit traffic on TCP port 80.
* **Security Insight:** This action deliberately **increased the attack surface** of the server. While necessary for the server to fulfill its function as a web server, it exposes the web server software to the network. This is a classic example of the security trade-off between functionality and risk reduction. The decision to open a port must always be a conscious one, followed by efforts to secure the newly exposed service.

---

## ✅ 5. Conclusion

This lab provided practical experience in managing a host-based firewall on Linux. We learned how to list existing rules and add new ones to enable required services. The key takeaway is understanding that a firewall is the primary tool for managing a system's network attack surface. Every rule addition must be a deliberate, justified action, as each open port represents a potential entry point for an attacker that must be monitored and secured.

```
