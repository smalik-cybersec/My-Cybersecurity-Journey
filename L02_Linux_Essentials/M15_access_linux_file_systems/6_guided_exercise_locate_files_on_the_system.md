Absolutely, Shahid. Here's the **🧪 Guided Exercise** for:

> **🧩 Lesson 4: Locate Files on the System**
> **Module 15 – Access Linux File Systems | RHEL 9**

Structured precisely for your **Cybersecurity Documentation Protocol — Ultra Edition v5.0 (Master Grade Edition)**.

---

# 🧪 Guided Exercise: Locate Files on the System (RHEL 9)

> 🧠 Master real-time and indexed file search techniques using `find`, `locate`, and `which`. Learn how to hunt for logs, binaries, and forensic artifacts like a SOC/IR professional.

---

## 🎯 Objective

* Search for files by name, size, and modification time.
* Use both real-time (`find`) and indexed (`locate`) tools.
* Discover command binaries using `$PATH`.
* Simulate incident detection scenarios.

---

## 🧱 Prerequisites

* RHEL 9 system with `mlocate` package installed:

```bash
sudo dnf install -y mlocate
```

* Ensure `updatedb` has run at least once:

```bash
sudo updatedb
```

---

## 🔧 Exercise Steps

---

### ✅ Task 1: Find All `.conf` Files in `/etc`

```bash
find /etc -type f -name "*.conf"
```

📘 *Result: Lists all config files across `/etc`.*

---

### ✅ Task 2: Find All SUID Binaries

```bash
find / -perm -4000 -type f 2>/dev/null
```

📘 *SUID binaries can be abused for privilege escalation.*

---

### ✅ Task 3: Find Files Modified in the Last 24 Hours

```bash
find /var/log -type f -mtime -1
```

📘 *Helpful for investigating what changed recently during an incident.*

---

### ✅ Task 4: Find Large Files (>500MB)

```bash
find / -type f -size +500M -exec ls -lh {} \; 2>/dev/null
```

📘 *Great for spotting logs, core dumps, or rogue data exfiltration dumps.*

---

### ✅ Task 5: Use `locate` to Quickly Find Known Files

```bash
sudo updatedb
locate sshd_config
```

📘 *`locate` is fast but must be updated regularly using `updatedb`.*

---

### ✅ Task 6: Find Executable Path of Commands

```bash
which bash
type nano
```

📘 *Useful in scripts or validating malicious binaries hiding in PATH.*

---

## 🎯 Simulation Scenario (Blue Team Exercise)

> **Scenario**: You suspect the attacker dropped a file in `/tmp` in the last 30 minutes.

```bash
find /tmp -type f -mmin -30 -exec ls -lh {} \;
```

🛡️ Blue Team Actions:

* Validate ownership: `ls -l`
* Check file type: `file <filename>`
* Quarantine: `mv` or `chmod 000`
* Preserve evidence: `cp --preserve`

---

## 📝 Checklist

| Task                       | Command                    | Done |
| -------------------------- | -------------------------- | ---- |
| Find config files          | `find /etc -name "*.conf"` | ✅    |
| SUID binaries              | `find / -perm -4000`       | ✅    |
| Recently modified logs     | `find /var/log -mtime -1`  | ✅    |
| Locate large files         | `find / -size +500M`       | ✅    |
| Quick search with `locate` | `locate passwd`            | ✅    |
| Command path               | `which bash` / `type bash` | ✅    |

---

## 🧪 Bonus Challenge

> 🧑‍💻 **Find all `.sh` scripts owned by root modified in the last 2 days:**

```bash
find / -type f -name "*.sh" -user root -mtime -2 2>/dev/null
```

---

Would you like me to now export this in Obsidian/GitHub-compatible Markdown format or move on to the next lesson in Module 15?
