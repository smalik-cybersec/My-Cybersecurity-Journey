Here is the **Guided Exercise** for the topic **“Explain and Investigate RPM Software Packages”**, structured under your Cybersecurity Documentation Protocol — Ultra Edition v5.0 (Master Grade Edition).

---

# 🧪 Guided Exercise: Explain and Investigate RPM Software Packages

**Module:** 14 – Install and Update Software Packages
**Level:** Linux Essentials – Level 3
**Focus:** Applied RPM package investigation (forensics, verification, simulation)

---

## 1. 🔎 Introduction

This guided exercise will take you through a structured RPM package investigation workflow — exactly as a Linux sysadmin, blue team analyst, or digital forensics responder would perform.

You'll:

* Query and verify installed packages.
* Investigate `.rpm` files from third-party sources.
* Simulate RPM tampering and detect it using native tools.
* Extract file listings, ownership, and integrity reports.

---

## 2. 🧠 Core Concepts (Feynman Analogy + Diagram)

### 🧠 Analogy:

Imagine each `.rpm` file as a **sealed crate of software**, shipped to your system. It includes:

* A **manifest** (metadata),
* The **contents** (payload),
* And a **security seal** (GPG signature).

Investigating RPMs means:

* Reading the manifest,
* Verifying the seal,
* Cross-checking the contents with what’s actually deployed.

### 📦 Structure Diagram

```
.rpm
├── Header (name, version, architecture, dependencies)
├── Payload (compressed files: /bin, /etc, /usr/share...)
└── Signature (GPG validation block)
```

---

## 3. 💻 Commands & Configs (with real RHEL output)

### Step 1: Query info of an installed package

```bash
rpm -qi nano
```

**Sample Output:**

```
Name        : nano
Version     : 5.9
Release     : 2.el9
Architecture: x86_64
Install Date: Tue 16 Jul 2025
Group       : Applications/Editors
License     : GPLv3+
```

---

### Step 2: List installed files from a package

```bash
rpm -ql nano
```

**Sample Output:**

```
/bin/nano
/usr/share/nano
/usr/share/doc/nano
```

---

### Step 3: Check which package owns a suspicious binary

```bash
rpm -qf /bin/nano
```

**Sample Output:**

```
nano-5.9-2.el9.x86_64
```

---

### Step 4: Investigate `.rpm` file (without installing)

```bash
rpm -qip ./nano-5.9-2.el9.x86_64.rpm
```

```bash
rpm -qlp ./nano-5.9-2.el9.x86_64.rpm
```

---

### Step 5: Verify GPG signature of `.rpm` file

```bash
rpm --checksig ./nano-5.9-2.el9.x86_64.rpm
```

**Expected Output:**

```
nano-5.9-2.el9.x86_64.rpm: rsa sha1 md5 OK
```

---

### Step 6: Verify integrity of installed package

```bash
rpm -V nano
```

**Output (no issues):**

```
(no output)
```

**Tampered file example:**

```
S.5....T.  c /etc/nanorc
```

---

## 4. 🧪 Labs (Beginner ➜ Tactical ➜ Red/Blue Simulation)

### 🟢 Beginner Lab: Inspect Local Packages

1. List information for bash, nano, coreutils:

   ```bash
   rpm -qi bash
   rpm -ql bash
   rpm -qf /bin/bash
   ```

2. Verify GPG signature for a downloaded `.rpm`:

   ```bash
   rpm --checksig ./wget*.rpm
   ```

---

### 🟡 Tactical Lab: Investigate Suspicious `.rpm`

1. Download a `.rpm` from a non-standard source (for testing only).
2. Use:

   ```bash
   rpm -qip ./suspicious.rpm
   rpm --checksig ./suspicious.rpm
   ```
3. Document mismatches or signature issues.

---

### 🔴 Simulation Lab: Red/Blue RPM Backdoor Detection

#### Red Team:

* Tamper with `/usr/bin/nano` by adding a reverse shell trigger (simulation only).
* Repackage with `rpmbuild` into a fake `nano.rpm`.

#### Blue Team:

* Run:

  ```bash
  rpm -V nano
  ```
* Review:

  * `/var/log/yum.log` or `/var/log/dnf.log`
  * `/var/log/audit/audit.log` for installation events
* Investigate hash or signature mismatches

---

## 5. ⚔️ Red/Blue Simulation (MITRE ATT\&CK + Tools)

### ATT\&CK Technique:

**T1195.002 – Supply Chain Compromise → Software Dependency**

#### 🔴 Red Actions:

* Use `rpmbuild` to inject payloads into `.rpm`.
* Host malicious RPMs on private mirrors.

#### 🔵 Blue Detections:

* Run integrity checks (`rpm -V`)
* Use YUM/DNF logs for tracking installs
* Alert on unsigned `.rpm` usage

---

## 6. 🧩 Quiz (Log + Scenario-Based)

**Q1:** You found a file `/usr/bin/fakenano`. `rpm -qf` says:

```
file /usr/bin/fakenano is not owned by any package
```

**What’s your conclusion?**
✅ The binary was added **outside the package manager**. Possible compromise.

---

**Q2:** You run `rpm -V curl` and get:

```
.M......T  /usr/bin/curl
```

**What does this mean?**
✅ The binary was modified (M = mode, T = timestamp).

---

**Q3:** Which log confirms package installation time?

→ `/var/log/dnf.log` ✅

---

**Q4:** A `.rpm` fails `--checksig` validation. What are your actions?

✅ Block installation, fetch the package from an official repository, notify security team.

---

## 7. 📌 Summary Table + Checklist

| Task                                     | Done |
| ---------------------------------------- | ---- |
| Investigated `.rpm` metadata with `-qip` | ✅    |
| Listed files with `-ql`                  | ✅    |
| Verified installed packages with `-V`    | ✅    |
| Checked GPG signatures                   | ✅    |
| Detected tampered packages               | ✅    |
| Simulated Red/Blue scenarios             | ✅    |

---

## 8. 📚 Journaling + Confidence Tracker

> This hands-on session helped me develop confidence in RPM forensic analysis. I now understand how to verify package integrity, detect tampering, and respond to supply chain threats. I’ll extend this by learning how to build RPMs securely.

🟩 Confidence Level: 8.5 / 10
📝 Notes:

* Try signing your own `.rpm`
* Study `rpmbuild` and `.spec` files

---

## 9. 🧭 Job Role + Cert Mapping

| Role                       | Task                                                  |
| -------------------------- | ----------------------------------------------------- |
| **SOC Analyst**            | Detect rogue RPM installations and unsigned packages  |
| **Linux SysAdmin (RHCSA)** | Maintain package integrity and lifecycle              |
| **Red Team (OSCP)**        | Craft or reverse-engineer `.rpm` payloads             |
| **IR / Forensics**         | Analyze logs and binaries for package origin          |
| **Certs**                  | RHCSA, CompTIA Linux+, CEH – Secure Software Handling |

---

## 10. 🔁 Revision Planner (Day 1, 3, 7, 30)

| Day        | Task                                                             |
| ---------- | ---------------------------------------------------------------- |
| **Day 1**  | Run all RPM investigation commands                               |
| **Day 3**  | Manually tamper a config and detect it with `rpm -V`             |
| **Day 7**  | Forensic drill: find when and how a suspicious RPM was installed |
| **Day 30** | Create, sign, and verify a basic `.rpm` with `rpmbuild`          |

---

✅ **Guided exercise complete.**
Ready for the **next lesson or challenge** in Module 14 when you are, Shahid.
