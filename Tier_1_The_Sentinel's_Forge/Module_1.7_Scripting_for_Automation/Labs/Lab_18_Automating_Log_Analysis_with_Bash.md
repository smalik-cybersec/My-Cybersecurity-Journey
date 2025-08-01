```markdown
# 🧪 Lab 18: Automating Log Analysis with Bash

### Date: 2025-07-25
### Mentor: *The Da Vinci Cypher*
### Protocol Tier: Tier 1 — The Sentinel's Forge
### Module: Module 1.7 — Scripting for Automation

---

## 🎯 1. Objective
To write a simple but effective Bash script to automate a common SOC analyst task: searching a log file for a specific IP address. The goal is to evolve the script from a static, hardcoded version to a flexible, reusable tool that accepts command-line arguments.

## 🧰 2. Tools Used
| Tool/Command | Purpose |
|--------------|---------|
| `nano`       | A text editor used to write the Bash script. |
| `chmod +x`   | A command to make the script file executable. |
| Bash Shell   | The environment for running the script, utilizing variables, `if` statements, and arguments (`$1`). |
| `grep`       | The core search tool called by the script to find the IP address in the log file. |

---

## 📜 3. Script Development

### 🔹 Version 1: Static Script

A simple script named `log_hunter.sh` was created with a hardcoded log file and IP address.
```bash
#!/bin/bash
LOG_FILE="access.log"
IP_TO_FIND="45.33.32.11"
echo "Hunting for IP address ${IP_TO_FIND}..."
grep "${IP_TO_FIND}" "${LOG_FILE}"
```

### 🔹 Version 2: Dynamic Script with Argument Handling

The script was upgraded to accept the IP address as a command-line argument (`$1`) and include error checking.

```bash
#!/bin/bash
LOG_FILE="access.log"

if [ -z "$1" ]; then
  echo "Error: You must provide an IP address to hunt for."
  exit 1
fi

IP_TO_FIND="$1"
echo "Hunting for IP address ${IP_TO_FIND}..."
grep "${IP_TO_FIND}" "${LOG_FILE}"
```

---

## 🔎 4. Execution & Analysis

* **Test 1 (No Argument):** Running `./log_hunter.sh` correctly triggered the error check, providing a helpful usage message.
* **Test 2 (With Argument):** Running `./log_hunter.sh 192.168.5.26` successfully passed the IP address to the script, which then correctly filtered the `access.log` file for the relevant entry.
* **Security Insight:** This lab demonstrates the core principle of security automation. A manual, repetitive task (running `grep` over and over) was codified into a reusable, consistent, and efficient tool. By accepting arguments, the script becomes a powerful force multiplier, allowing an analyst to investigate numerous alerts with speed and accuracy, reducing the risk of human error and accelerating incident response.

---

## ✅ 5. Conclusion

This lab served as a practical introduction to the power of Bash scripting for security automation. We successfully created a dynamic and reusable tool for a common log analysis task. This exercise highlights how scripting is not just a convenience but a fundamental skill for any Blue Team professional. It enables scalability, consistency, and speed, freeing up analysts to focus on higher-level analysis rather than being bogged down by repetitive manual tasks.

```
