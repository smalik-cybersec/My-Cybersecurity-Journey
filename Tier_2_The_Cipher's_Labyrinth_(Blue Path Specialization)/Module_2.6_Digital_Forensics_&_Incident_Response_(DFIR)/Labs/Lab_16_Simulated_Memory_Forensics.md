# 🧪 Lab 16: Simulated Memory Forensics

### Date: 2025-07-25

### Mentor: *The Da Vinci Cypher*

### Protocol Tier: Tier 2 — The Cipher's Labyrinth (Blue Path)

### Module: Module 2.6 — Digital Forensics & Incident Response (DFIR)

---

## 🎯 1. Objective

To simulate a basic memory forensics investigation by analyzing a text file representing the readable "strings" from a compromised machine's memory dump. The goal is to identify key Indicators of Compromise (IOCs), including network artifacts (C2 servers) and host artifacts (persistence mechanisms).

## 🧰 2. Tools Used

| Tool/Command | Purpose |
|--------------|---------|
| `nano`       | A text editor used to create the simulated evidence file. |
| `cat`        | A command to display the contents of a file. |
| `grep`       | The primary analysis tool, used to search the evidence file for specific patterns. |

---

## 🖥️ 3. Process & Findings

### 🔹 Step 1: Evidence Generation

* A text file named `simulated_memory_strings.txt` was created to represent the output of running the `strings` tool on a real memory dump (`.vmem` file). This file contained a mix of legitimate and malicious text artifacts.

### 🔹 Step 2: Hunting for Network Indicators

* **Command:** `cat simulated_memory_strings.txt | grep "http"`
* **Finding:** The search revealed several URLs. Two identical and highly suspicious URLs were identified as the primary network IOC:

    ```
    http://malicious-c2-server.com/implant.dat
    ```

* **Analysis:** The domain name and the filename "implant.dat" strongly indicate that this is a Command and Control (C2) server used by malware to receive commands and exfiltrate data.

### 🔹 Step 3: Hunting for Host-Based Indicators

* **Command:** `cat simulated_memory_strings.txt | grep "net user"`
* **Finding:** A command executed by the attacker was discovered:

    ```
    cmd.exe /c "net user hacker Password123 /add && net localgroup administrators hacker /add"
    ```

* **Analysis:** This command represents a classic persistence technique. The attacker performed two actions:
    1. Created a new local user named `hacker`.
    2. Added that new user to the local `administrators` group.

---

## 🔎 4. Overall Conclusion

The investigation successfully identified the critical elements of a compromise by analyzing the simulated memory artifacts. We found both the attacker's C2 infrastructure and their on-host persistence mechanism.

* **What Happened:** An attacker gained access to the machine and executed a command to create a new, privileged user account. This account serves as a backdoor.
* **How They Maintain Control:** The compromised machine communicates with `malicious-c2-server.com` via a malware implant to receive commands.
* **Security Insight:** This lab demonstrates the immense power of **Memory Forensics**. Even if an attacker uses "fileless" malware that never touches the hard drive, the commands they run, the network connections they make, and the user accounts they create can leave behind tell-tale artifacts in RAM. Capturing and analyzing a memory dump is one of the most effective ways for an Incident Responder to uncover the true actions of an attacker.
