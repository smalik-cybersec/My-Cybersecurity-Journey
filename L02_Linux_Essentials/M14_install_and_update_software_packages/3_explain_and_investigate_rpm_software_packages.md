Here is your full lesson under **Module 14: Install and Update Software Packages** — following the **Cybersecurity Documentation Protocol — Ultra Edition v5.0 (Master Grade Edition)**.

---

# 📦 Explain and Investigate RPM Software Packages

**Module:** 14 – Install and Update Software Packages
**Track:** Linux Essentials – Level 3
**Focus:** RPM Package Internals, Investigation, and Integrity Validation
**Platform:** RHEL 9+ (dnf + rpm tools)

---

## 1. 🔎 Introduction

RPM (Red Hat Package Manager) is the core package format used in RHEL and its derivatives. Understanding RPMs is essential for secure package management, validating software sources, forensics, and ensuring system integrity.

This lesson explores how to **explain, inspect, query, verify, and investigate RPM packages** — both installed and standalone `.rpm` files. You'll learn how Red Teamers can backdoor or tamper packages, and how Blue Teamers can detect it using logs, metadata, and hashes.

---

## 2. 🧠 Core Concepts (with Feynman Analogies + Diagrams)

### 🧠 Feynman Analogy:

Think of an **RPM package** like a **sealed medicine box**:

* It includes the **drug (software binaries)**,
* The **prescription (metadata: version, arch, license)**,
* A **tamper-evident seal (GPG signature)**.

If you want to **investigate** or **verify** an RPM:

* You don’t just check the label, you **open the box**, read the **prescription**, verify the **seal**, and **compare contents** with what was expected.

### 📦 RPM Internals:

* **Header:** Contains metadata (name, version, arch, license, summary, dependencies).
* **Payload:** The actual files (binaries, configs, docs).
* **Signature:** GPG key used to validate authenticity.

Diagram:

```
+-------------------------------+
|        RPM Package            |
+-------------------------------+
| GPG Signature (Optional)      |
+-------------------------------+
| Header (Metadata)             |
| - Name, Version, Release      |
| - Architecture, Group         |
| - File list, Dependencies     |
+-------------------------------+
| Payload (Compressed Archive)  |
| - /usr/bin/myapp              |
| - /etc/myapp.conf             |
+-------------------------------+
```

---

## 3. 💻 Commands & Configs (real RHEL output + risks)

### 📄 View RPM metadata (installed package)

```bash
rpm -qi bash
```

**Sample Output:**

```
Name        : bash
Version     : 5.1.8
Release     : 7.el9
Architecture: x86_64
Install Date: Mon 10 Jul 2025
Group       : System Environment/Shells
License     : GPLv3+
Size        : 3788016
URL         : https://www.gnu.org/software/bash
Summary     : The GNU Bourne Again shell
Description :
Bash is a shell...
```

---

### 📁 List files from an installed RPM

```bash
rpm -ql bash
```

**Sample Output:**

```
/bin/bash
/usr/share/doc/bash
/usr/share/licenses/bash-5.1.8
```

---

### 📦 Investigate a local `.rpm` file (without installing)

```bash
rpm -qip ./wget-1.21.1-10.el9.x86_64.rpm
```

**Sample Output:**

```
Name        : wget
Version     : 1.21.1
Release     : 10.el9
Architecture: x86_64
Group       : Applications/Internet
License     : GPLv3+
Description :
A utility for retrieving files using HTTP, HTTPS, and FTP.
```

---

### 🔍 Extract file list from `.rpm` file

```bash
rpm -qlp ./wget-1.21.1-10.el9.x86_64.rpm
```

---

### 🧾 Check which package owns a file

```bash
rpm -qf /bin/bash
```

**Output:**

```
bash-5.1.8-7.el9.x86_64
```

---

### ✅ Verify integrity of installed package

```bash
rpm -V bash
```

**Output (no output = no issues):**

```
(no output)
```

If modified:

```
S.5....T.  c /etc/bashrc
```

Each character indicates a type of mismatch (S = size, 5 = checksum, T = timestamp, etc.).

---

### 🔑 Verify GPG signature of a downloaded package

```bash
rpm --checksig ./wget-1.21.1-10.el9.x86_64.rpm
```

**Output (valid):**

```
wget-1.21.1-10.el9.x86_64.rpm: rsa sha1 (md5) pgp md5 OK
```

---

## 4. 🧪 Labs (Beginner ➜ Tactical ➜ Red/Blue Simulation)

### 🟢 Beginner Lab: Basic RPM Queries

1. Run:

   ```bash
   rpm -qi coreutils
   rpm -ql coreutils
   rpm -qf /usr/bin/ls
   ```
2. Explore `/usr/share/doc/coreutils/` to confirm.

---

### 🟡 Tactical Lab: Investigate a `.rpm` File Before Installing

1. Download `wget` RPM from Red Hat CDN.
2. Run:

   ```bash
   rpm -qip ./wget*.rpm
   rpm -qlp ./wget*.rpm
   rpm --checksig ./wget*.rpm
   ```
3. Compare metadata vs what's in `/etc/yum.repos.d`.

---

### 🔴 Red/Blue Simulation Lab

#### Setup:

Simulate a malicious `.rpm` injected with a reverse shell or backdoored binary.

#### Red Team:

* Create a fake `.rpm` with modified `/usr/bin/nano` using `rpmbuild`.

#### Blue Team:

* Use `rpm -V nano` to detect tampering.
* Check `/var/log/yum.log` or `/var/log/dnf.log` for suspicious installs.
* Verify GPG signature fails.

---

## 5. ⚔️ Red/Blue Simulation (MITRE ATT\&CK, Logs, Tools)

### Red Team Tactic: T1195.002 – Supply Chain Compromise: Compromise Software Dependency

* Inject payload into `.rpm` and host on a private repo.
* Trick sysadmin into manual install.

### Blue Team Detection:

* Monitor changes in package checksums (`rpm -V`, AIDE, tripwire).
* Monitor for unsigned RPM installations via `auditd`.

**Key Logs:**

* `/var/log/rhsm/rhsm.log` (RHSM repo behavior)
* `/var/log/yum.log` or `/var/log/dnf.log` (package install history)
* `/var/log/audit/audit.log` (file changes, unsigned package usage)

---

## 6. 🧩 Quiz (scenario-based + log interpretation)

### Q1: What does `rpm -V bash` return if `/bin/bash` was modified?

A. Nothing
B. 404 Error
C. A string of mismatch flags
D. SIGKILL

✅ **Correct:** C

---

### Q2: You downloaded a `.rpm` from a third-party source. How do you verify it wasn’t tampered?

→ `rpm --checksig` ✅

---

### Q3: You suspect `/etc/ssh/sshd_config` was replaced. What command helps you validate?

→ `rpm -V openssh-server`

---

### Q4: What log helps confirm the original install of a suspicious RPM?

→ `/var/log/dnf.log` ✅

---

### Q5: `rpm -qf /usr/bin/nmap` returns:

`file /usr/bin/nmap is not owned by any package`. What does this imply?

✅ A file was added manually — possibly suspicious.

---

## 7. 📌 Summary Table + Checklist

| Task                                  | Done |
| ------------------------------------- | ---- |
| Use `rpm -qi` to read metadata        | ✅    |
| Use `rpm -ql` to list files           | ✅    |
| Verify ownership with `rpm -qf`       | ✅    |
| Detect tampering with `rpm -V`        | ✅    |
| Check GPG signature with `--checksig` | ✅    |
| Audit package installation logs       | ✅    |

---

## 8. 📚 Journaling + Confidence Tracker

> Today I learned how to explain, inspect, and validate RPM packages — both installed and downloaded. I practiced verifying file integrity, checking metadata, and investigating potential tampering or unsigned packages. I now understand how Red Teamers can abuse `.rpm` and how Blue Teams can detect such compromise.

🟩 **Confidence Level:** 9 / 10
📝 **Personal Notes:**

* Practice `rpm -V` on tampered config files
* Learn more about `rpmbuild` for package creation

---

## 9. 🧭 Job Role + Cert Mapping

| Role                       | Relevance                                                   |
| -------------------------- | ----------------------------------------------------------- |
| **SOC Analyst**            | Investigate suspicious packages and installation patterns   |
| **Linux SysAdmin (RHCSA)** | Day-to-day use of RPM for integrity checks                  |
| **IR Specialist**          | Forensic analysis of rogue `.rpm` installs                  |
| **Red Teamer (OSCP)**      | Create backdoored RPMs, evade detection                     |
| **Certs**                  | RHCSA, CompTIA Linux+, CEH — Software Management & Security |

---

## 10. 🔁 Revision Planner (Day 1, 3, 7, 30)

| Day        | Task                                                         |
| ---------- | ------------------------------------------------------------ |
| **Day 1**  | Run all `rpm -qi`, `-ql`, `-qf`, `-V`, `--checksig` commands |
| **Day 3**  | Investigate a `.rpm` downloaded from the internet            |
| **Day 7**  | Simulate RPM tampering and detect using verification         |
| **Day 30** | Create your own `.rpm` with `rpmbuild` for testing           |

---

✅ Topic complete. Ready for the **next lesson** in Module 14 whenever you are, Shahid.
