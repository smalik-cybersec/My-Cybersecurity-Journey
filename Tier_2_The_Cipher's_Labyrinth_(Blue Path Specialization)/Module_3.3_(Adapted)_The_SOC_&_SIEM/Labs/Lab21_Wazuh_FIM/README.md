```markdown
# Lab 21: The Unbroken Seal - File Integrity Monitoring (FIM)

### **Objective**
This lab demonstrates the configuration and validation of Wazuh's File Integrity Monitoring (FIM) capabilities. The goal was to detect an unauthorized modification of a critical system file on a monitored endpoint in real-time.

### **Lab Architecture**
- **Analyst VM:** Wazuh Manager, used for central configuration and alert analysis.
- **Target VM:** Ubuntu Server endpoint with a Wazuh agent.
- **File System Target:** The `/etc` directory on the Target VM.

### **Execution Steps**

**1. FIM Configuration (on Analyst VM):**
The following configuration was added to `/var/ossec/etc/shared/default/agent.conf` and pushed to the agent. This instructs the agent to monitor the `/etc` directory in real-time.
```xml
<agent_config>
  <syscheck>
    <directories check_all="yes" realtime="yes">/etc</directories>
  </syscheck>
</agent_config>
```

**2. Triggering the Event (on Target VM):**
To break the integrity "seal," a comment was appended to the `/etc/hosts` file using the command:

```bash
sudo bash -c 'echo "# DVC Lab 21 FIM Test - Seal Broken" >> /etc/hosts'
```

### **Evidence of Analysis (The Detection)**

The following screenshot from the Wazuh dashboard shows the resulting "Integrity checksum changed" alert.

### **Analysis and Conclusion**

* **Asset Identification (`syscheck.path`):** The alert correctly identified the exact file that was modified: `/etc/hosts`.

* **Content Analysis (`syscheck.diff`):** The `syscheck.diff` field provided the ground truth of the modification, showing the exact line of text that was added. This moves beyond simply knowing *that* a file changed to knowing precisely *how* it changed.

* **Threat Assessment:** An unauthorized change to `/etc/hosts` is a high-severity security event. It is a primary indicator of a **DNS Hijacking** or **Pharming** attack, where an adversary attempts to redirect legitimate user traffic to a malicious server to steal credentials or serve malware. The Wazuh FIM module provided the immediate and detailed alert necessary to detect and respond to such a threat.

```
---

Complete this document, ensuring you get a clear screenshot that includes the `syscheck.diff` field. This is your proof of mastering a critical HIDS capability. When you are ready, we will conclude with our final debrief.
