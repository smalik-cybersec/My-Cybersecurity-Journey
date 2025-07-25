# 📝 Notes: Core Security Concepts & Threat Modeling

### Date: 2025-07-24

### Mentor: The Da Vinci Cypher

---

## 1. The CIA Triad: The Goals of Security

The CIA Triad is the foundational model for information security. Every attack is an attempt to compromise one or more of these principles.

* **Confidentiality:** Secrecy and privacy. Ensuring data is only seen by authorized individuals.
  * **Defense Example:** Encryption.
* **Integrity:** Accuracy and trustworthiness. Ensuring data has not been altered without authorization.
  * **Defense Example:** Hashing, Digital Signatures.
* **Availability:** Reliability and uptime. Ensuring data and services are accessible when needed.
  * **Defense Example:** Redundancy, Backups, DDoS Protection.

---

## 2. The Attack Surface: The Field of Battle

The Attack Surface is the sum of all points where an attacker can attempt to interact with a system.

* **Analogy:** All the doors, windows, and weak points of a castle.
* **Digital Examples:** Open network ports, web application login forms, employees susceptible to phishing.
* **Defender's Goal:** To **reduce the attack surface** by closing unnecessary ports, hardening systems, and training users.
* **Attacker's Goal:** To **enumerate the attack surface** to find the single weakest point of entry.

---

## 3. Threat Modeling & STRIDE: Thinking Like an Attacker

Threat Modeling is the proactive process of identifying potential threats and vulnerabilities during the design phase of a system. STRIDE is a framework for categorizing these threats.

* **S - Spoofing:** Illegitimately assuming another's identity. (Violates Authenticity)
* **T - Tampering:** Unauthorized modification of data. (Violates Integrity)
* **R - Repudiation:** Denying having performed an action. (Violates Non-Repudiation)
* **I - Information Disclosure:** Revealing data to unauthorized parties. (Violates Confidentiality)
* **D - Denial of Service (DoS):** Making a system unavailable to legitimate users. (Violates Availability)
* **E - Elevation of Privilege:** Gaining capabilities without proper authorization. (Violates Authorization)

**Key Insight:** A single root vulnerability (e.g., Tampering via a Cross-Site Scripting attack) can lead to a chain reaction that violates multiple STRIDE principles (Information Disclosure, Spoofing, etc.).
