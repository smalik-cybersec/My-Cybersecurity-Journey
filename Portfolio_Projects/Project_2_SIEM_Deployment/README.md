# Project 2: Deployment of an Enterprise-Grade SIEM & Detection Lab

### Date: 2025-07-31

### Author: Shahid

---

## 1. Executive Summary

This report details the successful design, deployment, and troubleshooting of a complete Security Information and Event Management (SIEM) solution in a custom-built virtual cyber range. The project's objective was to create a stable and persistent Security Operations Center (SOC) environment for future threat detection and incident response exercises. The core of the lab is a Wazuh SIEM server, which centralizes and analyzes logs from a monitored Linux target server. This project involved a multi-day, professional-level troubleshooting process to overcome a series of complex installation and configuration challenges, demonstrating deep resilience and a systematic approach to problem resolution. The final, successful outcome is a fully operational, multi-VM detection lab capable of ingesting and alerting on security events in real-time.

## 2. Lab Architecture & The Forge

A pristine, three-node virtual lab was constructed from scratch to serve as the foundation for this and all future Blue Team projects. This initial "Forge" phase was critical to ensuring a stable and reliable outcome.

* **Attacker Machine:**
  * **OS:** Kali Linux (Fresh Build from Installer ISO)
  * **IP Address:** [Enter Your Kali IP]
  * **Role:** Simulates internal and external threats.
* **Analyst VM (SIEM Server):**
  * **OS:** Ubuntu Server LTS
  * **IP Address:** [Enter Your Analyst-VM IP]
  * **Role:** Hosts the Wazuh SIEM Server, Indexer, and Dashboard. The central "Watchtower" of the SOC.
* **Target VM (The Asset):**
  * **OS:** Ubuntu Server LTS
  * **IP Address:** [Enter Your Target-VM IP]
  * **Role:** Represents a monitored corporate asset, running a Wazuh agent to forward logs to the SIEM.
* **Network Configuration:**
  * **Type:** VMware NAT (VMnet8)
  * **Description:** An isolated virtual network that allows internet access for software installation while providing a private LAN for inter-VM communication. All VMs are protected with "Golden Image" snapshots for rapid restoration.

## 3. SIEM & Agent Deployment: The Mission

The core of the project was the deployment of the Wazuh SIEM, which involved a rigorous, real-world installation and configuration process.

### Step 1: SIEM Server Installation (The "All-in-One" Method)

The Wazuh server, indexer, and dashboard were installed on the Analyst-VM using the official `wazuh-install.sh` script. The `--all-in-one` method was chosen after significant troubleshooting, as it provided the most reliable, self-contained installation path. This included capturing the auto-generated administrator password for the web dashboard.

### Step 2: Agent Deployment

The Wazuh agent was deployed to the Target-VM. The Wazuh dashboard was used to generate the precise, one-line installation command, which included the manager's IP address. This command was then executed on the target to install, register, and start the agent service.

## 4. Troubleshooting Journal: A Case Study in Resilience

This project's most significant learning outcome was the multi-day troubleshooting effort required to achieve a stable system. The following is a summary of the key challenges and their resolutions:

* **Initial Challenge: Unstable Kali Linux VM.**
  * **Symptom:** The pre-built Kali VMware image repeatedly failed during network configuration and system updates.
  * **Resolution:** The pre-built image was abandoned. A new Kali VM was built from scratch using the official installer ISO. A persistent DNS failure was then diagnosed and resolved by manually configuring DNS servers (`8.8.8.8`, `1.1.1.1`) via `nmcli`, demonstrating deep command-line network management.

* **Initial Challenge: Failed Elastic Stack (ELK) SIEM Deployment.**
  * **Symptom:** An initial attempt to build a SIEM with the core Elastic Stack resulted in a complete data pipeline failure. The `Filebeat` agent established a connection but failed to send logs, and the Kibana dashboard showed no data.
  * **Resolution:** After exhausting multiple troubleshooting paths (timestamp mismatches, ILM policies, direct database queries), the problem was deemed to be a deep, unrecoverable configuration conflict. A professional decision was made to **pivot** to a different toolset rather than continue with a broken system.

* **Final Challenge: Wazuh Agent Connection Failure.**
  * **Symptom:** The Wazuh agent was installed on the Target-VM, but it failed to appear in the dashboard and logs showed `Unable to connect to enrollment service`.
  * **Resolution:** Analysis determined the cause was the Analyst-VM's host-based firewall (`ufw`) blocking the necessary agent communication ports. The firewall was systematically reconfigured to allow traffic on ports `443/tcp` (Dashboard), `1514/tcp`, `1515/tcp`, and `55000/tcp` (Agent Services). This action successfully opened the gates and allowed the agent to connect and register.

## 5. Final Outcome & Conclusion

The project successfully concluded with a fully operational, three-node Security Operations Center lab. The `target-vm` agent is now registered and **Active** in the Wazuh dashboard, and its security events are being successfully collected and prepared for analysis.

This project is a testament to the real-world challenges of a security engineer. It proves not only the ability to install and configure complex security tools like Wazuh, but more importantly, the resilience and systematic troubleshooting methodology required to solve the inevitable problems that arise. The resulting cyber range is a stable, persistent, and invaluable platform for the advanced threat detection and incident response projects that will follow.
