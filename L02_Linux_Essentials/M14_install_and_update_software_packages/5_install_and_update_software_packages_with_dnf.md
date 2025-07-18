Here is your complete lesson for:

---

# 📦 Install and Update Software Packages with DNF

**Module:** 14 – Install and Update Software Packages
**Track:** Linux Essentials – Level 3
**Platform:** RHEL 9+ (dnf)
**Protocol:** Cybersecurity Documentation Protocol — Ultra Edition v5.0 (Master Grade Edition)

---

## 1. 🔎 Introduction

In Red Hat Enterprise Linux (RHEL), `dnf` (Dandified YUM) is the modern package manager that replaced the legacy `yum` command. It handles package installations, updates, removals, and dependency management using clean dependency resolution and transaction history.

This lesson focuses on mastering `dnf` for securely installing and updating software, interpreting real-world output, logging activity, mitigating risks, and understanding how red/blue teams interact with software lifecycle events.

---

## 2. 🧠 Core Concepts (with Feynman Analogy + Diagram)

### 🧠 Feynman Analogy

Think of `dnf` as a **concierge at a software hotel**:

* When you ask to install a package, it **checks availability**, **books dependencies**, and **logs everything**.
* If a guest (package) causes trouble later, you can **trace its check-in history**, **review the logs**, or even **remove it cleanly**.
* For updates, `dnf` ensures only **certified guests (signed RPMs)** are upgraded — unless you override security checks.

---

### 🔧 Core Features of `dnf`:

* Resolves dependencies automatically.
* Handles package groups (`@core`, `@development-tools`).
* Supports GPG signature checking.
* Maintains **transaction history** (`dnf history`).
* Uses `.repo` files to fetch metadata and packages.

---

### 📊 Visual Flow:

```
Install Package ─┬─> Checks Repos
                 ├─> Resolves Dependencies
                 ├─> Verifies GPG Signature
                 ├─> Downloads RPMs
                 └─> Installs + Logs Transaction
```

---

## 3. 💻 Commands & Configs (Real RHEL Output + Risk Tips)

### 🧪 Basic: Install a package

```bash
sudo dnf install nano
```

**Sample Output:**

```
Dependencies resolved.
================================================================================
 Package      Arch   Version           Repo                  Size
================================================================================
Installing:
 nano         x86_64 5.9-2.el9         rhel-9-baseos         690 k

Transaction Summary
================================================================================
Install  1 Package

Total download size: 690 k
Installed size: 2.0 M
Is this ok [y/N]: y
```

---

### 🔄 Update all packages

```bash
sudo dnf update
```

**Sample Output (shortened):**

```
Upgraded:
  openssl-libs x86_64 1:3.0.7-24.el9_3
  kernel       x86_64 5.14.0-362.24.1.el9_3

Complete!
```

---

### 🔍 Search for packages

```bash
dnf search nmap
```

**Output:**

```
Last metadata expiration check: 1:22:00 ago.
============================== Name & Summary Matched: nmap ===================
nmap.x86_64 : Network exploration tool and security scanner
zenmap.noarch : GUI for nmap
```

---

### 📦 View info about a package

```bash
dnf info nmap
```

**Output:**

```
Name         : nmap
Version      : 7.92
Release      : 6.el9
Architecture : x86_64
Summary      : Network exploration tool and security scanner
Repository   : rhel-9-appstream-rpms
License      : GPLv2
```

---

### ❌ Remove a package

```bash
sudo dnf remove nano
```

---

### 📜 View transaction history

```bash
dnf history
```

**Sample Output:**

```
ID | Command line        | Date and time    | Action(s)      | Altered
-------------------------------------------------------------------------------
 5 | install nmap        | 2025-07-18 14:03 | Install        |    1
 4 | update              | 2025-07-17 17:29 | Upgrade        |   11
```

---

### 🔁 Roll back a specific transaction

```bash
sudo dnf history undo 5
```

---

## 4. 🧪 Labs (Beginner ➜ Tactical ➜ Red/Blue Simulation)

### 🟢 Beginner Lab: Install, update, and remove

1. Install packages:

   ```bash
   sudo dnf install wget tree
   ```

2. Update system:

   ```bash
   sudo dnf update
   ```

3. Remove a package:

   ```bash
   sudo dnf remove tree
   ```

4. Review:

   ```bash
   dnf history
   ```

---

### 🟡 Tactical Lab: Detect and rollback misconfigured packages

1. Install `nmap`:

   ```bash
   sudo dnf install nmap
   ```

2. Break it (simulate config issue).

3. Undo install:

   ```bash
   sudo dnf history undo <ID>
   ```

---

### 🔴 Simulation Lab: Package Manipulation & Logs

**Red Team:**

* Replace `/usr/bin/nmap` with a custom script.
* Retain RPM name but alter behavior.

**Blue Team:**

* Run:

  ```bash
  rpm -V nmap
  ```
* Check:

  * `/var/log/dnf.log`
  * `/var/log/audit/audit.log` (if auditd is running)

---

## 5. ⚔️ Red/Blue Simulation (MITRE ATT\&CK, Logs, Tools)

### Technique: T1222 – File and Directory Permissions Modification

### Technique: T1070 – Indicator Removal on Host

#### 🔴 Red Team:

* Abuse `dnf` or direct `rpm -U` to install a trojaned `.rpm`.
* Clean logs using `truncate -s 0 /var/log/dnf.log`.

#### 🔵 Blue Team:

* Monitor file integrity via `rpm -V`, AIDE, or tripwire.
* Detect unsigned packages or transactions outside `dnf`.

**Relevant Logs:**

* `/var/log/dnf.log`
* `/var/log/messages`
* `/var/log/audit/audit.log`

---

## 6. 🧩 Quiz (scenario-based + log interpretation)

### Q1: What does `dnf update` do?

A. Only updates nano
B. Reinstalls packages
C. Updates all available packages ✅
D. Removes old packages

---

### Q2: You run `dnf install nmap` and it fails due to “No match found”. What’s likely the cause?

✅ Repos are not enabled or metadata expired

---

### Q3: How do you undo the last package removal?

→ `dnf history redo` ❌
→ `dnf history undo <ID>` ✅

---

### Q4: Which command lists past installs/updates?

→ `dnf history` ✅

---

### Q5: You suspect `/usr/bin/wget` has been altered. What’s your first action?

→ `rpm -V wget` ✅

---

## 7. 📌 Summary Table + Checklist

| Task                                 | Status |
| ------------------------------------ | ------ |
| Installed package via `dnf install`  | ✅      |
| Updated system via `dnf update`      | ✅      |
| Used `dnf history` for rollback      | ✅      |
| Verified tampering with `rpm -V`     | ✅      |
| Explored real-world logs (`dnf.log`) | ✅      |

---

## 8. 📚 Journaling + Confidence Tracker

> Today I mastered how to use `dnf` for package lifecycle management in RHEL. I now understand how to securely install, verify, rollback, and audit software using both command-line and logs. I also explored how attackers may manipulate `dnf`-based installations and how to detect it with RPM verification.

🟩 **Confidence Level:** 9 / 10
📝 Notes: Try using `dnf module list` and package groups (`dnf group list`)

---

## 9. 🧭 Job Role + Cert Mapping

| Role                | Relevance                                                      |
| ------------------- | -------------------------------------------------------------- |
| **Linux SysAdmin**  | Core task: Install, update, rollback packages                  |
| **SOC Analyst**     | Analyze install/update logs for anomalies                      |
| **IR Specialist**   | Detect rogue software installs                                 |
| **Red Team (OSCP)** | Abuse `.rpm` with malicious payloads                           |
| **Certs**           | RHCSA, CompTIA Linux+, CEH — Software Lifecycle & Log Analysis |

---

## 10. 🔁 Revision Planner (Day 1, 3, 7, 30)

| Day        | Task                                              |
| ---------- | ------------------------------------------------- |
| **Day 1**  | Install and remove 3 packages via `dnf`           |
| **Day 3**  | Use `dnf history` and rollback transactions       |
| **Day 7**  | Simulate tampered package and detect via `rpm -V` |
| **Day 30** | Create custom `.repo` file and install from it    |

---

✅ **Topic complete.**
Ready for the next topic in Module 14 when you are, Shahid.
