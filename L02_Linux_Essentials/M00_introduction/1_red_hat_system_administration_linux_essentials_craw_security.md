Excellent, Shahid. Based on your request and the Craw Cyber Security syllabus, the module you're referring to is part of **Level 2: Linux Essentials**, and the **Red Hat System Administration** content is fully integrated into it — including practical Linux administration topics using Red Hat Enterprise Linux (RHEL) as the base.

Here’s your **professionally structured documentation** for:

---

# 🧑‍💻 **Red Hat System Administration (Linux Essentials – Craw Security)**

> *From the One-Year Cyber Security Diploma Course*
> *Author: Craw Security & Adapted by Shahid | Format: Markdown-ready*

---

## 📚 Table of Contents

- [🧑‍💻 **Red Hat System Administration (Linux Essentials – Craw Security)**](#-red-hat-system-administration-linux-essentials--craw-security)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [📦 Course Modules \& Topics](#-course-modules--topics)
  - [💡 Key Skills You'll Gain](#-key-skills-youll-gain)
  - [🔐 Linux Security Concepts](#-linux-security-concepts)
  - [🛠️ Practical Commands and Examples](#️-practical-commands-and-examples)
  - [🧪 Lab Exercises](#-lab-exercises)
  - [🧠 Quiz Section](#-quiz-section)
  - [🎯 Real-World Use Cases](#-real-world-use-cases)
  - [📜 Certification Details](#-certification-details)
  - [📎 Resources \& Further Reading](#-resources--further-reading)

---

## 🎯 Introduction

Linux, particularly **Red Hat Enterprise Linux (RHEL)**, is a foundational skill in the cybersecurity world. It powers servers, firewalls, container environments (like Docker/Kubernetes), cloud platforms, and more. System administration in Red Hat-based distributions focuses on user management, networking, process control, logging, software packaging, and securing the system.

This module forms a **core component** of your cybersecurity education, blending hands-on Linux commands, system hardening, and Red Hat tools with security thinking.

---

## 📦 Course Modules & Topics

Here’s a structured view of what you’ll master across the Red Hat System Administration path as per the syllabus:

| Module No. | Module Name                         | Key Concepts Covered                                          |
| ---------- | ----------------------------------- | ------------------------------------------------------------- |
| **01**     | Getting Started with Red Hat Linux  | What is Linux? History, Open Source Benefits                  |
| **02**     | Accessing the Command Line          | Bash shell, TTY, CLI vs GUI                                   |
| **03**     | Managing Files from Command Line    | Filesystem hierarchy, `ls`, `cd`, `cp`, `mv`, `rm`            |
| **04**     | Getting Help in Red Hat             | `man`, `--help`, `info`, `whatis`, `apropos`                  |
| **05**     | Editing Text Files                  | `cat`, `nano`, `vim`, redirection, environment variables      |
| **06**     | Managing Users and Groups           | `useradd`, `passwd`, `groupadd`, `/etc/passwd`, `/etc/shadow` |
| **07**     | Controlling File Access             | Permissions (`rwx`), `chmod`, `chown`, `umask`                |
| **08**     | Monitoring and Managing Processes   | `ps`, `top`, `kill`, background jobs                          |
| **09**     | Services and Daemons                | `systemctl`, `service`, `chkconfig`, runlevels                |
| **10**     | Configuring and Securing SSH        | `sshd`, `ssh-keygen`, `/etc/ssh/sshd_config`                  |
| **11**     | Logging and Journaling              | `journalctl`, `/var/log/`, `rsyslog`, log rotation            |
| **12**     | Networking on Linux                 | `ip`, `nmcli`, `ifconfig`, DNS, `/etc/hosts`, `ping`          |
| **13**     | Archiving and File Transfers        | `tar`, `scp`, `rsync`                                         |
| **14**     | Installing Software                 | `dnf`, `rpm`, `yum`, repositories, updates                    |
| **15**     | Filesystem Access                   | Mounting, `df`, `du`, locating files                          |
| **16**     | Server Analysis and Red Hat Support | Troubleshooting, RHEL Portal, `sosreport`, Insights           |



---

## 💡 Key Skills You'll Gain

* Bash shell scripting basics
* Linux file system navigation & manipulation
* User and group management
* File permissions & access control
* SSH configuration and security
* System process management
* Daemon/service control
* Networking and hostname resolution
* RPM and DNF-based package management
* Red Hat troubleshooting and support

---

## 🔐 Linux Security Concepts

| Concept                    | Description                                                    |
| -------------------------- | -------------------------------------------------------------- |
| **User Permissions**       | Prevent unauthorized access using `chmod`, `umask`, and `ACLs` |
| **SUID, SGID, Sticky Bit** | Advanced permissions for executable control                    |
| **Firewall**               | Configure `firewalld` or `iptables`                            |
| **SSH Hardening**          | Disable root login, use key authentication                     |
| **Log Monitoring**         | Track suspicious behavior using `journalctl` and `/var/log/`   |
| **Package Integrity**      | Use `gpgcheck=1` in repos; verify RPM packages                 |
| **Patch Management**       | Apply security updates with `dnf updateinfo`                   |
| **SELinux (Optional)**     | Red Hat's advanced Mandatory Access Control system             |

---

## 🛠️ Practical Commands and Examples

```bash
# Create a new user
sudo useradd shahid && sudo passwd shahid

# Check open network ports
sudo ss -tuln

# Change file permissions
chmod 755 /home/shahid/script.sh

# Transfer files securely
scp file.txt user@remote:/home/user/

# Monitor system logs
journalctl -xe

# View running services
systemctl list-units --type=service
```

---

## 🧪 Lab Exercises

1. **🧑‍💻 Create a user "cyberlab", assign them to a new group "secops", and restrict their access to only one directory.**
2. **🔐 Harden SSH on your VM: disable password login, allow only specific users, and restart the SSH daemon.**
3. **📡 Setup and troubleshoot a network issue using `ip`, `ping`, and `/etc/resolv.conf`.**
4. **📦 Install Apache (httpd) via DNF, set it to auto-start, and verify it using `curl localhost`.**
5. **🔍 Use journalctl to investigate a fake “login failure” scenario. Document the steps.**

---

## 🧠 Quiz Section

> *Try answering these to test your fundamentals:*

1. What command displays the default target in `systemd`?
2. How would you copy a folder and preserve permissions?
3. Which config file stores local user account details?
4. What’s the difference between `kill` and `killall`?
5. How do you enable a service to start on boot using systemctl?

---

## 🎯 Real-World Use Cases

* **Cybersecurity Job Roles**: Threat analyst, SOC analyst, red teamer— all require Linux fluency
* **Server Administration**: Managing servers across enterprise, cloud, or hybrid systems
* **Incident Response**: Analyzing logs, isolating users, and patching exploits
* **DevOps Integration**: Shell scripting, automation, and configuration management
* **Cloud Security**: AWS, Azure, and GCP often rely on hardened Linux instances

---

## 📜 Certification Details

| Attribute           | Value                           |
| ------------------- | ------------------------------- |
| **Course Hours**    | 60+ hrs                         |
| **Exam Format**     | MCQ (30–35 questions)           |
| **Duration**        | 1 hour                          |
| **Passing Marks**   | 50% (plus 75% class attendance) |
| **Exam Fee**        | ₹600 (inclusive)                |
| **Optional Add-on** | Red Hat Certification Pathway   |



---

## 📎 Resources & Further Reading

* [Red Hat Official Documentation](https://access.redhat.com/documentation/en-us/)
* [LinuxCommand.org](http://linuxcommand.org/)
* [TLDP Bash Guide](https://tldp.org/LDP/Bash-Beginners-Guide/html/)
* [Craw Linux Essentials Page](https://www.craw.in/linux-essential-training-course-in-delhi/)

---

📌 **Next Steps**
Let me know if you want:

* 🧪 A hands-on lab workbook
* 📝 Answer key for the quiz
* 🧭 Weekly study roadmap
* 📦 GitHub README template

Or simply send your next topic — I’m ready to document it!

Would you like a **Markdown export** of this file as well?
