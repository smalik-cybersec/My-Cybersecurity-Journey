Perfect, Shahid. Below is a clean, Obsidian/GitHub-compatible **quiz session** covering the **three lessons** completed under **Module 11: Analyze and Store Logs**. Each lesson section includes a **sufficient number of thoughtful, mastery-focused questions** — no answers are provided so you can practice active recall.

---

## 📄 `QuizSession11-SystemLogging-RHEL.md`

# 📘 Quiz Session – Module 11: Analyze and Store Logs

🔍 Focus: RHEL | Lessons 01–03
🎯 Objective: Self-assess understanding of Linux logging systems (syslog, journald, log review)

---

## 🧠 Lesson 11.01: Describe System Log Architecture

1. What are the key components of the Linux system log architecture?
2. How do `journald` and `rsyslog` interact in RHEL-based systems?
3. What is the difference between log **generation**, **collection**, and **storage**?
4. What directory typically stores persistent log files in RHEL?
5. What’s the role of `/dev/log` in the system logging pipeline?
6. Compare and contrast the roles of `systemd-journald` and `rsyslog`.
7. Which services typically generate log entries in a Linux system?
8. Why might some logs go missing or appear incomplete?
9. What does the `logger` command do? Where do its entries go?
10. What potential risks are involved in misconfigured logging systems?

---

## 📘 Lesson 11.02: Review Syslog Files

1. In RHEL, what is the purpose of the `/var/log/messages` file?
2. What types of logs are stored in `/var/log/secure`?
3. How would you find all failed SSH login attempts using syslog?
4. How can you watch live system logs using native RHEL tools?
5. What is the difference between `/var/log/cron` and `/var/log/dmesg`?
6. What log file would you inspect to investigate a failed `sudo` command?
7. What is the structure of a typical syslog entry?
8. How does log rotation affect the content in `/var/log/`?
9. What does the `tail -f` command do in log monitoring?
10. How would you detect a tampering attempt on `/var/log/secure`?

---

## 📘 Lesson 11.03: Review System Journal Entries

1. What command shows logs from the current boot in `journald`?
2. How are logs stored in the journal different from `/var/log/` logs?
3. Where are **persistent** journal logs stored in RHEL?
4. What’s the effect of the command: `journalctl --list-boots`?
5. How can you filter logs by systemd unit (like `sshd`) using `journalctl`?
6. What are the severity levels used by `journalctl -p` and what do they mean?
7. How would you extract logs only for a specific time range?
8. How does `journald` handle stdout/stderr from services?
9. What command would you use to review logs for a previous system crash?
10. How would you detect a red team attempt to clear or tamper with journal entries?

---

## 🧾 Instructions

* Try to **answer each question verbally or in writing**.
* For command-based questions, **replicate them in your RHEL VM**.
* After completing, mark areas where you were unsure — we'll reinforce those in revision.

---

## 📘 Metadata

* **Filename**: `QuizSession11-SystemLogging-RHEL.md`
* **Tags**: `#linux`, `#logging`, `#rhel`, `#syslog`, `#journald`, `#module11`, `#quiz`
* **Difficulty**: 🟡 Intermediate
* **Mapped Roles**: SOC Analyst, SysAdmin, Incident Responder
* **Certs Aligned**: RHCSA, CompTIA Linux+, CEH, OSCP

---

Let me know once you're ready to begin journaling your reflections or if you'd like the **answer key in a separate file** for spaced review.

When ready, we’ll move to:
🔜 **Lesson 11.04: Preserve the System Journal**
