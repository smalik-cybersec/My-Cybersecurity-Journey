Here’s an improved version of your file, implementing all the enhancements previously suggested. Changes are explained inline as comments for your review.

---

# 🧑‍💻 **Red Hat System Administration (Linux Essentials – Craw Security)**

> *From the One-Year Cyber Security Diploma Course*  
> *Author: Craw Security & Adapted by Shahid | Format: Markdown-ready*

---

## 📚 Table of Contents

- [🧑‍💻 Red Hat System Administration (Linux Essentials – Craw Security)](#-red-hat-system-administration-linux-essentials--craw-security)
- [📚 Table of Contents](#-table-of-contents)
- [🎯 Introduction](#-introduction)
- [📦 Course Modules & Topics](#-course-modules--topics)
- [💡 Key Skills You'll Gain](#-key-skills-youll-gain)
- [🔐 Linux Security Concepts](#-linux-security-concepts)
- [🛠️ Practical Commands and Examples](#️-practical-commands-and-examples)
- [🧪 Lab Exercises](#-lab-exercises)
- [🧠 Quiz Section](#-quiz-section)
- [🎯 Real-World Use Cases](#-real-world-use-cases)
- [📜 Certification Details](#-certification-details)
- [📎 Resources & Further Reading](#-resources--further-reading)
- [📝 Appendix: Hints & Solutions](#-appendix-hints--solutions)

---

## 🎯 Introduction

Linux, especially **Red Hat Enterprise Linux (RHEL)**, is fundamental for cybersecurity professionals. It runs servers, firewalls, containers (Docker/Kubernetes), and powers cloud platforms. This module blends hands-on Linux practice with system hardening and Red Hat tools, all from a security-first perspective.

---

## 📦 Course Modules & Topics

Here’s a structured overview of your learning path:

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

- Bash shell scripting basics
- Linux file system navigation & manipulation
- User and group management
- File permissions & access control
- SSH configuration and security
- System process management
- Daemon/service control
- Networking and hostname resolution
- RPM and DNF-based package management
- Red Hat troubleshooting and support

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
# Create a new user and set their password
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
> **Tip:** Use `man <command>` or `<command> --help` to explore more options.

---

## 🧪 Lab Exercises

### 1. Create & Manage Users
- Create a user `cyberlab`, assign them to a new group `secops`, and restrict their access to `/home/cyberlab_only`.
- **Hint:** Use `useradd`, `groupadd`, `chown`, and change home directory permissions.

### 2. SSH Hardening
- Harden SSH: disable password login, allow only specific users, and restart the SSH daemon.
- **Hint:** Edit `/etc/ssh/sshd_config` using `PermitRootLogin no` and `AllowUsers`.

### 3. Network Troubleshooting
- Set up and troubleshoot a network issue using `ip`, `ping`, and `/etc/resolv.conf`.
- **Hint:** Use `ip addr`, `ping 8.8.8.8`, and check DNS settings.

### 4. Install & Test Apache
- Install Apache (`httpd`) via DNF, enable auto-start, and verify with `curl localhost`.
- **Hint:** Use `dnf install httpd`, `systemctl enable --now httpd`, and `curl localhost`.

### 5. Log Analysis
- Use `journalctl` to investigate a simulated login failure.
- **Hint:** Search for authentication failures using `journalctl -xe | grep 'authentication'`.

---

## 🧠 Quiz Section

> *Test your knowledge (answers in the Appendix):*

1. What command displays the default target in systemd?
2. How would you copy a folder and preserve permissions?
3. Which config file stores local user account details?
4. What’s the difference between `kill` and `killall`?
5. How do you enable a service to start on boot using systemctl?

---

## 🎯 Real-World Use Cases

- **Cybersecurity Job Roles**: Threat analyst, SOC analyst, red teamer—all require Linux fluency
- **Server Administration**: Managing servers (enterprise, cloud, hybrid)
- **Incident Response**: Log analysis, user isolation, exploit patching
- **DevOps Integration**: Shell scripting, automation, configuration management
- **Cloud Security**: AWS, Azure, and GCP often rely on hardened Linux

---

## 📜 Certification Details

| Attribute           | Value                           |
| ------------------- | ------------------------------- |
| **Course Hours**    | 60+ hrs                         |
| **Exam Format**     | MCQ (30–35 questions)           |
| **Duration**        | 1 hour                          |
| **Passing Marks**   | 50% (plus 75% class attendance) |
| **Exam Fee**        | ₹600 (inclusive)                |
| **Optional Add-on** | [Red Hat Certification Pathway](https://www.redhat.com/en/services/training-and-certification) |

---

## 📎 Resources & Further Reading

- [Red Hat Official Documentation](https://access.redhat.com/documentation/en-us/)
- [LinuxCommand.org](http://linuxcommand.org/)
- [TLDP Bash Guide](https://tldp.org/LDP/Bash-Beginners-Guide/html/)
- [Craw Linux Essentials Page](https://www.craw.in/linux-essential-training-course-in-delhi/)
- [OverTheWire Linux Wargames](https://overthewire.org/wargames/)

---

## 📝 Appendix: Hints & Solutions

### Quiz Answers

1. `systemctl get-default`
2. `cp -a source/ destination/`
3. `/etc/passwd`
4. `kill` targets a PID; `killall` targets processes by name.
5. `systemctl enable <service>`

---

**Next Steps:**
- Request a hands-on lab workbook, quiz answer key, weekly study roadmap, or a GitHub README template.
- Want visual diagrams or command-line simulations? Ask for links!
- Send your next topic, or ask for a Markdown export.

---

Would you like any of these additions as separate files or sections?
