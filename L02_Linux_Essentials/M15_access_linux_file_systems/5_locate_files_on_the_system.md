Perfect, Shahid. Let’s now document the lesson:

---

# 📁 Module 15: Access Linux File Systems

## 🧩 Lesson 4: Locate Files on the System

> **Linux Essentials Level 3 – RHEL 9**
> **Cert/Job Alignment**: RHCSA, CEH (Blue Team), SOC Tier 1, IR Analyst

---

## 🧭 1. Introduction

Being able to **locate files** on a Linux system is essential for **administration, incident response, digital forensics**, and **automation scripting**. Whether you're looking for suspicious binaries, misplaced configs, or validating file presence across systems, mastering file location tools is foundational.

This lesson teaches you how to:

* Use the `find`, `locate`, and `which` utilities.
* Use `find` with conditions (e.g., size, type, permissions, time).
* Configure and refresh file indexing with `updatedb`.

---

## 🧠 2. Core Concepts (Feynman Style)

| Tool             | Purpose                             | Key Advantage              |
| ---------------- | ----------------------------------- | -------------------------- |
| `find`           | Real-time filesystem search         | Most flexible, accurate    |
| `locate`         | Indexed database search             | Fast, but needs `updatedb` |
| `which` / `type` | Show path of executables in `$PATH` | Good for scripts, binaries |

---

### 🔍 `find`: Real-Time Precision

```bash
find <path> <conditions> -exec <action> \;
```

* ✅ Searches live filesystem (not database)
* 🔁 Slower but more accurate
* 🧠 Can filter by **name, type, size, owner, permissions, time**

---

### ⚡ `locate`: Indexed Speed

```bash
locate passwd
```

* Uses `/var/lib/mlocate/mlocate.db`
* Much faster than `find`
* Requires regular `updatedb` to stay current

---

### 🧰 `which`, `type`: Executable Discovery

```bash
which bash
type ls
```

* Scans `$PATH` to find command locations.

---

## 🔧 3. Commands & Real RHEL Output

---

### 🔹 Using `find`

```bash
# Find all ".conf" files in /etc
find /etc -name "*.conf"

# Find files larger than 100MB
find / -type f -size +100M

# Find files modified in the last 24 hours
find /var/log -type f -mtime -1

# Find and delete .tmp files (Dangerous - use with care)
find /tmp -name "*.tmp" -exec rm -v {} \;
```

🛡️ Blue Team Tip:

```bash
# Find SUID binaries (often abused by attackers)
find / -perm -4000 -type f 2>/dev/null
```

---

### 🔹 Using `locate`

```bash
sudo updatedb            # Update the database
locate sshd_config
```

---

### 🔹 Using `which` and `type`

```bash
which nano
# /bin/nano

type nano
# nano is /bin/nano
```

---

## 🧪 4. Labs (Beginner → Tactical → Simulation)

---

### 🔰 Beginner Lab

> **Objective**: Locate `.conf` files and SUID binaries.

```bash
find /etc -name "*.conf"
find / -perm -4000 -type f 2>/dev/null
```

---

### ⚙️ Tactical Lab

> **Objective**: Find large files (>500MB) and analyze.

```bash
find / -type f -size +500M -exec ls -lh {} \; 2>/dev/null
```

---

### 🎯 Simulation Lab

> **Scenario**: You suspect the attacker dropped a binary in `/tmp` in the last 30 minutes.

```bash
find /tmp -type f -mmin -30 -exec file {} \;
```

🛡️ Respond:

* Check ownership, hashes, behavior
* Move to evidence drive

---

## 🛡️ 5. Red/Blue Simulation (MITRE ATT\&CK + Logs)

| Team    | Use Case                   | Tool                     | MITRE Technique                  | Response           |
| ------- | -------------------------- | ------------------------ | -------------------------------- | ------------------ |
| 🔴 Red  | Hide payload in `/var/tmp` | `mv payload /var/tmp/.a` | T1036.004 (Masquerading)         | `auditd`, `find`   |
| 🔵 Blue | Detect SUID abuse tools    | `find / -perm -4000`     | T1548.001 (Privilege Escalation) | Harden permissions |

---

## ❓ 6. Deep Quiz

1. What is the key difference between `find` and `locate`?
2. How can you find files modified in the last 15 minutes?
3. Which command finds all directories owned by a user?
4. How do you prevent `find` errors for inaccessible dirs?
5. What command locates executables in your `$PATH`?

---

## 📋 7. Summary Table + Checklist

| Goal                   | Command                    | Verified |
| ---------------------- | -------------------------- | -------- |
| Find config files      | `find /etc -name "*.conf"` | ✅        |
| Find large files       | `find / -size +500M`       | ✅        |
| List SUID binaries     | `find / -perm -4000`       | ✅        |
| Find recent files      | `find /tmp -mmin -30`      | ✅        |
| Use `locate` for speed | `locate sshd_config`       | ✅        |
| Check command path     | `which`, `type`            | ✅        |

---

## 📓 8. Journaling + Confidence Tracker

* 🟩 Confident with `find` and basic filtering
* 🟨 Need more practice with `-exec`, time-based search
* 🟥 Unsure about `locate` database freshness

---

## 🧭 9. Job & Cert Role Mapping

| Role                 | Use Case                                |
| -------------------- | --------------------------------------- |
| 🛡️ SOC Analyst      | Locate malware or altered binaries      |
| 🧰 SysAdmin          | Audit config files, debug issues        |
| 🕵️ Forensic Analyst | Find artifacts by time, size, ownership |
| 📜 RHCSA             | Master `find`, `locate`, `which` usage  |

---

## 🗓️ 10. Spaced Repetition Plan

* **Day 1**: Practice all `find` examples
* **Day 3**: Run targeted forensic simulations (`-mmin`, `-exec`)
* **Day 7**: Build a one-page cheat sheet
* **Day 30**: Apply on real-world incident case

---

Would you like the guided hands-on **exercise version** next or should I export this in clean Markdown for your Obsidian/GitHub publishing?
