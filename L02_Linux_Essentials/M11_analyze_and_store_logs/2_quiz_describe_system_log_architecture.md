Great timing, Shahid! Here's a well-crafted, recruiter-ready **Quiz** for:

> **Topic:** Describe System Log Architecture
> **Page Ref:** \~342
> **Purpose:** Test your understanding of Linux logging concepts, structure, and tools — essential for any cybersecurity, SOC, or Linux role.

---

# 🧠 Quiz: Describe System Log Architecture

## 📝 Instructions:

* Total Questions: 15
* Format: Mix of MCQs, True/False, and Short Answers
* Difficulty: Beginner to Intermediate
* Suggested Time: \~20 minutes

---

### ✅ Section 1: Multiple Choice (Choose the BEST answer)

---

**Q1.** Which file contains system-wide authentication and authorization logs on a Debian-based system?

A. `/var/log/syslog`
B. `/var/log/kern.log`
C. `/var/log/auth.log`
D. `/etc/ssh/sshd_config`

> ✅ **Answer:** C

---

**Q2.** Which daemon is primarily responsible for managing log messages on most traditional Linux systems?

A. cron
B. rsyslog
C. ufw
D. auditd

> ✅ **Answer:** B

---

**Q3.** What command allows you to see logs from the current boot session in systemd-based systems?

A. `less /var/log/syslog`
B. `tail -f /boot.log`
C. `journalctl -b`
D. `uptime`

> ✅ **Answer:** C

---

**Q4.** Which of the following best describes `logrotate`?

A. A system log viewer
B. A firewall configuration tool
C. A log management and rotation utility
D. A package manager

> ✅ **Answer:** C

---

**Q5.** Which command shows real-time updates to a log file?

A. `nano /var/log/syslog`
B. `tail -f /var/log/syslog`
C. `head /var/log/syslog`
D. `cat -f /var/log/syslog`

> ✅ **Answer:** B

---

### ✅ Section 2: True or False

---

**Q6.** `/var/log/kern.log` contains logs related to user login attempts.

> ❌ **False** — It contains kernel messages; login attempts go to `auth.log`.

---

**Q7.** The `systemd-journald` daemon stores logs in a binary format.

> ✅ **True**

---

**Q8.** `rsyslog` cannot forward logs to a remote SIEM system.

> ❌ **False** — `rsyslog` can forward logs over TCP/UDP to remote log servers.

---

**Q9.** It’s safe to delete old log files manually from `/var/log` without checking logrotate settings.

> ❌ **False** — This may break system or compliance monitoring.

---

**Q10.** Log rotation is important to prevent the `/var` partition from filling up.

> ✅ **True**

---

### ✅ Section 3: Short Answer

---

**Q11.** What is the role of `ClientAliveInterval` in SSH logs?

> **Answer:** It defines how often the server sends keepalive messages to the client. It's useful for detecting idle sessions, and failed replies may show up in logs as session timeouts.

---

**Q12.** Name two log files that help in investigating a brute-force SSH attack.

> **Answer:**

* `/var/log/auth.log` (Debian/Ubuntu)
* `/var/log/secure` (RHEL/CentOS)

---

**Q13.** What tool would you use to extract lines containing “failed” from `auth.log`?

> **Answer:**

```bash
grep "failed" /var/log/auth.log
```

---

**Q14.** What is the default directory where most Linux logs are stored?

> **Answer:** `/var/log/`

---

**Q15.** What is the difference between `syslog` and `journald`?

> **Answer:**

* `syslog` (`rsyslog`, `syslog-ng`) uses plain-text files and the syslog protocol.
* `journald` (used in `systemd` systems) stores logs in a binary format and integrates tightly with systemd.

---

## 🧮 Scoring

| Range         | Your Level                                               |
| ------------- | -------------------------------------------------------- |
| 13–15 correct | 🧠 **Mastered**: Ready for SOC or Linux admin interviews |
| 10–12 correct | 👍 **Competent**: Solid foundation                       |
| 7–9 correct   | ⚠️ **Needs Review**                                      |
| <7 correct    | ❌ **Go Back and Reread Chapter**                         |

---

## 📦 Bonus Task (Optional)

Write a command to monitor all SSH activity in real-time:

> **Answer:**

```bash
sudo tail -f /var/log/auth.log | grep sshd
```

---

Would you like this quiz in `.md` format or a printable `.pdf` for your documentation repo?

Next topic or lab—just say the word, Shahid.
