## 📄 `Quiz11.01-System-Log-Architecture.md`

# 🧠 Quiz – Lesson 11.01: Describe System Log Architecture

**Module**: Analyze and Store Logs
**Level**: Linux Essentials (Level 3)
**Type**: Mixed MCQ, True/False, Scenario-Based

---

### ✅ **Multiple Choice Questions (MCQ)**

**Q1.** What is the primary function of `rsyslog` in the Linux logging architecture?
A. Run kernel-level processes
B. Display logs in binary format
C. Collect and route log messages ✅
D. Monitor system services

---

**Q2.** Which command is used to view systemd journal logs?
A. `cat /var/log/messages`
B. `systemctl status`
C. `logrotate`
D. `journalctl` ✅

---

**Q3.** What is the full path of the file that typically stores SSH authentication attempts in Ubuntu?
A. `/var/log/kern.log`
B. `/var/log/secure`
C. `/var/log/auth.log` ✅
D. `/etc/ssh/ssh_config`

---

**Q4.** Which component of the system log architecture generates logs?
A. journald
B. Applications, daemons, kernel ✅
C. `journalctl`
D. Logrotate

---

**Q5.** Which command will list logs only from the previous boot session?
A. `journalctl -p`
B. `journalctl -b -1` ✅
C. `dmesg`
D. `rsyslogd --list`

---

### ✅ **True or False**

**Q6.** `rsyslog` replaces `systemd-journald` in modern distributions.
**Answer:** ❌ False
*(They can work together — `journald` captures logs, `rsyslog` can persist or forward them.)*

---

**Q7.** All logs in `/var/log/` are stored in binary format by default.
**Answer:** ❌ False
*(Only `systemd` logs in `/var/log/journal/` are binary. Most other files are plain text.)*

---

**Q8.** `logger` is a command-line tool used to write messages to the syslog.
**Answer:** ✅ True

---

### 🧠 **Scenario-Based Questions**

**Q9.** You suspect an attacker has cleared authentication logs. You run:

```bash
ls -l /var/log/auth.log
```

It returns a file with a very small size (0 bytes). What should you do next?

A. Reboot the system
B. Restore the file using backup ✅
C. Run `apt update`
D. Ignore it — logs auto-rotate

---

**Q10.** You're troubleshooting failed SSH logins. Which command would give you relevant log entries?

A. `journalctl -u ssh` ✅
B. `cat /etc/hosts`
C. `netstat -tulpn`
D. `whoami`

---

## 🧾 Answer Key

| Q# | Correct Answer |
| -- | -------------- |
| 1  | C              |
| 2  | D              |
| 3  | C              |
| 4  | B              |
| 5  | B              |
| 6  | False          |
| 7  | False          |
| 8  | True           |
| 9  | B              |
| 10 | A              |

---

## 🧠 Reflection Prompts

* Which log file locations did I remember easily?
* Was I able to distinguish between `rsyslog` and `journald` correctly?
* Which command should I practice more?

🧠 **Confidence Level:** `__/10`
📝 **Date Completed:** `__________`

---

Let me know when you're ready for:
🔜 `Lesson11.02-Review-Syslog-Files.md` or
📁 `Lab11.01-Simulation-SystemLogTampering.md` for deeper mastery.
