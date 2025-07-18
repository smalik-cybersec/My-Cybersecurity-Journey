Here is the **guided exercise** for:

---

# 📦 Guided Exercise: Install and Update Software Packages with `dnf`

**Module:** 14 – Install and Update Software Packages
**Platform:** RHEL 9.x
**Skill Level:** Beginner ➜ Tactical
**Protocol:** Cybersecurity Documentation Protocol — Ultra Edition v5.0

---

## 🎯 Objective

By the end of this guided exercise, you will be able to:

* Use `dnf` to install, update, and remove packages
* Query system state using `dnf history` and `rpm`
* Detect tampering or misconfiguration using real-world log and verification tools

---

## 🧪 Guided Lab Steps

### 🟢 Step 1: Install Multiple Packages

```bash
sudo dnf install nano tree wget -y
```

✅ **Goal:** Ensure basic tools are installed.
🔍 **Why:** These are standard utilities and easy to verify with RPM.

---

### 🟢 Step 2: Search and Inspect a Package

```bash
dnf search nmap
dnf info nmap
```

✅ **Goal:** Learn how to explore package metadata
🔍 **Why:** SOC Analysts must verify package origin, license, and repo.

---

### 🟡 Step 3: Update the Entire System

```bash
sudo dnf update -y
```

✅ **Goal:** Bring all packages up to date
🔍 **Why:** Critical for patching vulnerabilities like CVEs.

---

### 🟡 Step 4: Check DNF Transaction History

```bash
dnf history
```

✅ **Goal:** Understand what packages were installed or updated and when
🔍 **Why:** Helps in incident response to correlate suspicious behavior with package changes.

---

### 🔴 Step 5: Remove a Package

```bash
sudo dnf remove tree -y
```

Then check:

```bash
dnf history list
```

✅ **Goal:** Practice rollback logic
🔍 **Why:** Useful during recovery or malware removal.

---

### 🔴 Step 6: Undo a Transaction

First, get the ID of the previous transaction from `dnf history`, then:

```bash
sudo dnf history undo <ID>
```

✅ **Goal:** Reverse the effects of a change
🔍 **Why:** Fast rollback is essential during software misconfiguration or compromise.

---

### 🛡️ Step 7: Verify Package Integrity (Security Check)

```bash
rpm -V wget
```

✅ **Goal:** Check for tampered files
🔍 **Why:** Red teams might replace binaries — this helps catch it.

---

### 📂 Step 8: Check Logs for Software Activity

```bash
sudo cat /var/log/dnf.log | grep wget
```

✅ **Goal:** Correlate CLI history with log evidence
🔍 **Why:** SOC teams depend on this in real incidents.

---

## 📌 Exercise Completion Checklist

| Task                                 | Completed |
| ------------------------------------ | --------- |
| Installed multiple packages          | ✅         |
| Searched and viewed package metadata | ✅         |
| Updated all packages                 | ✅         |
| Checked install/update history       | ✅         |
| Removed and rolled back a package    | ✅         |
| Verified integrity with `rpm -V`     | ✅         |
| Viewed `/var/log/dnf.log` entries    | ✅         |

---

## 🧭 Guidance for Journaling

> Write in your Obsidian daily journal:

* Which packages you installed
* What transaction ID you used to rollback
* What you found in `/var/log/dnf.log`
* How `rpm -V` helped you verify file integrity

📈 **Confidence Rating:** Rate your comfort with `dnf` from 1–10
💡 **Reflection Prompt:** What would you do if a critical tool (e.g., `curl`) stopped working after an update?

---

✅ **Exercise Complete.**
Let me know when you’re ready for the next guided lab or lesson under Module 14.
