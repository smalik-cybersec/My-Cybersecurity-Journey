# 🧪 Lab 15b: Live Traffic Analysis with tcpdump & Wireshark

### Date: 2025-07-25

### Mentor: *The Da Vinci Cypher*

### Protocol Tier: Tier 2 — The Cipher's Labyrinth (Blue Path)

### Module: Module 3.7 (Adapted) — Blue Teaming & Defensive Strategy

---

## 🎯 1. Objective

To perform a live-fire network reconnaissance exercise by capturing and analyzing traffic from a simulated attack. The goal is to use `tcpdump` to capture traffic on a victim machine while it is being scanned by `nmap` from an attacker machine, and then use Wireshark to analyze the resulting packet capture to identify the attacker's actions and findings.

## 🧰 2. Tools Used

| Tool/Command | Purpose | Role |
|--------------|---------|------|
| `nmap -sT -A`| To perform an active TCP connect scan against a target. | Attacker |
| `tcpdump`    | To capture raw network traffic on a live interface. | Defender |
| `scp`        | To securely copy the evidence file from the victim to the analyst machine. | Forensics |
| `Wireshark`  | To perform deep-packet inspection and analysis on the captured file. | Analyst |

---

## 🖥️ 3. Process & Findings

### 🔹 Step 1: Evidence Capture

* `tcpdump` was initiated on the victim machine (Metasploitable 2) to begin capturing all network traffic.
* An `nmap` scan was launched from the attacker machine (Kali Linux) against the victim.
* `tcpdump` was stopped, and the resulting `capture.pcap` file was securely transferred to the Kali machine for analysis.

### 🔹 Step 2: Analysis of Reconnaissance Activity

* The `capture.pcap` was opened in Wireshark.
* A display filter was applied: `tcp.flags.syn == 1 and tcp.flags.ack == 0`
* **Finding:** A flood of TCP SYN packets was observed originating from the Kali IP address and targeting a wide range of ports on the Metasploitable 2 IP address. This is the definitive signature of an `nmap` port scan.

### 🔹 Step 3: Analysis of Scan Results

* The display filter was changed to: `tcp.flags.syn == 1 and tcp.flags.ack == 1`
* **Finding:** This filter isolated the reply packets from the victim machine. Packets with these flags are sent by a host when it has a service listening on a port that has just received a SYN packet. The source ports of these reply packets confirmed that numerous services were open, including ports `80` (HTTP), `6000` (X11), and `8180` (Unknown Service).

---

## 🔎 4. Observations & Analysis

* This lab successfully demonstrated the full cycle of a live-fire analysis: setting up a capture, executing a simulated attack, and analyzing the resulting evidence.
* By filtering for specific TCP flags in Wireshark, we were able to move beyond just "looking at traffic" and could identify the specific actions and results of the reconnaissance scan at the packet level.
* **Security Insight:** This exercise highlights the "chattiness" of unstealthy network scanning. A simple TCP connect scan (`-sT`) is extremely loud and easy for a defender to spot using an IDS like Suricata or by analyzing raw packet captures. An attacker must either be very stealthy or assume their reconnaissance will be detected.

---

## ✅ 5. Conclusion

This practical, live-fire lab provided an invaluable lesson in both offensive operations and defensive analysis. We successfully generated our own forensic evidence and used Wireshark to deconstruct the attacker's reconnaissance phase. The ability to capture traffic with `tcpdump` and analyze it with Wireshark to confirm suspicious activity is a fundamental, hands-on skill for any SOC Analyst, Incident Responder, or Threat Hunter. This process of validating alerts by "going to the packets" is a cornerstone of high-fidelity security investigations.
