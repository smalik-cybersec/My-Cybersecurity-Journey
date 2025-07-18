Perfect, Shahid. Below is the **Guided Lab** for:

---

# 🧪 Lab: Install and Update Software Packages

**Module:** 14 — Install and Update Software Packages
**Lesson Type:** Guided Lab
**Platform:** RHEL 9.x
**Protocol:** Cybersecurity Documentation Protocol — Ultra Edition v5.0

---

## 🎯 Lab Objectives

You will:

* Search, install, and update software using `dnf`
* Investigate package metadata and version control
* Manage cache and transaction history
* Simulate package rollback
* Observe logs and simulate attack behaviors with Red/Blue focus

---

## 🧱 Environment Requirements

* RHEL 9 (VM or physical)
* Internet or custom local repository
* `sudo` access
* Ensure system is **registered with Red Hat**

---

## 🧩 Step-by-Step Lab Tasks

---

### 🔹 Task 1: Search for a Package (e.g. `vim`)

```bash
dnf search vim
```

**Expected Output:**

```
vim-enhanced.x86_64 : A version of the VIM editor which includes recent enhancements
vim-common.x86_64   : Files shared by all the VIM packages
...
```

---

### 🔹 Task 2: View Info About the Package

```bash
dnf info vim-enhanced
```

**Output Sample:**

```
Name         : vim-enhanced
Version      : 9.0.0000
Release      : 4.el9
Architecture : x86_64
Size         : 1.4 M
Repo         : rhel-9-for-x86_64-appstream-rpms
Summary      : A version of the VIM editor which includes recent enhancements
```

---

### 🔹 Task 3: Install the Package

```bash
sudo dnf install vim-enhanced
```

**Output Preview:**

```
Installed:
  vim-enhanced-9.0.0000-4.el9.x86_64
...
Complete!
```

---

### 🔹 Task 4: Check If Installed

```bash
rpm -q vim-enhanced
```

**Output:**

```
vim-enhanced-9.0.0000-4.el9.x86_64
```

---

### 🔹 Task 5: Check Package Files

```bash
rpm -ql vim-enhanced
```

This lists all files installed by the RPM. You can see binary locations like:

```
/usr/bin/vim
/usr/share/man/man1/vim.1.gz
...
```

---

### 🔹 Task 6: Update the Package (if a new version exists)

```bash
sudo dnf update vim-enhanced
```

If already updated:

```
Dependencies resolved.
Nothing to do.
Complete!
```

---

### 🔹 Task 7: Roll Back Using History (if update occurred)

List recent transactions:

```bash
dnf history
```

Then roll back:

```bash
sudo dnf history rollback <transaction_id>
```

Example:

```bash
sudo dnf history rollback 12
```

---

### 🔹 Task 8: Clean the Cache

```bash
sudo dnf clean all
```

---

### 🔹 Task 9: View Logs

```bash
less /var/log/dnf.log
```

Look for:

```
Installed: vim-enhanced-9.0.0000-4.el9.x86_64
```

---

## ⚔️ Red/Blue Simulation Insights

### Red Team

* Drop a malicious `.rpm` named like a legitimate one (e.g., `vim-enhanced-9.0.0001-evil.el9.rpm`)
* Use a poisoned repo (MITM) + social engineering to trigger manual install

### Blue Team

* Monitor `/var/log/dnf.log`, `/var/log/yum.log`, and `/etc/yum.repos.d`
* Detect installation of unsigned or unexpected packages
* Enforce `gpgcheck=1`, and use FIM to detect `.repo` file tampering

---

## 🧠 Post-Lab Questions

* How can you verify package authenticity before installing?
* What file lists all the package files after install?
* Can a rollback bring back deleted config files?

---

## ✅ Completion Checklist

| Task | Description                          | Done |
| ---- | ------------------------------------ | ---- |
| ✅    | Searched for and installed a package |      |
| ✅    | Inspected package version and repo   |      |
| ✅    | Updated and optionally rolled back   |      |
| ✅    | Investigated DNF logs                |      |
| ✅    | Identified red/blue scenarios        |      |

---

Let me know if you want to move forward to:

* **Red/Blue Simulation Lab**
* **Quiz + log interpretation**
* **Next lesson** from Module 14
* Or **generate GitHub/Obsidian-ready Markdown** from this content

Ready when you are.
