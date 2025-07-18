Absolutely, Shahid. Here's the full **Guided Exercise** for:

---

# 🧭 Guided Exercise: Enable DNF Software Repositories

**Module:** 14 — Install and Update Software Packages
**Lesson:** Enable DNF Software Repositories
**Type:** Guided Exercise
**Platform:** RHEL 9.x
**Protocol:** Cybersecurity Documentation Protocol — Ultra Edition v5.0

---

## 🧪 Exercise Objectives

You will:

* Verify the availability of repositories
* Enable/disable official RHEL repos using `subscription-manager`
* Create and validate a custom `.repo` file
* Inspect related logs
* Map red/blue simulation behavior

---

## 🛠️ Prerequisites

* ✅ You are on a registered RHEL 9.x system
* ✅ Have sudo/root access
* ✅ Internet access or access to a custom repo baseurl

---

## 🧩 Step-by-Step Instructions

---

### 🔹 Step 1: View All Available Repositories

```bash
dnf repolist all
```

**Expected Output:**

```
repo id                             repo name                               status
rhel-9-for-x86_64-baseos-rpms      Red Hat Enterprise Linux 9 BaseOS RPMs  enabled
rhel-9-for-x86_64-appstream-rpms   Red Hat Enterprise Linux 9 AppStream    enabled
rhel-9-for-x86_64-supplementary    Red Hat Enterprise Linux 9 Supplementary disabled
```

---

### 🔹 Step 2: Enable a Disabled Repo (e.g. Supplementary)

```bash
sudo subscription-manager repos --enable=rhel-9-for-x86_64-supplementary-rpms
```

**Expected Output:**

```
Repository 'rhel-9-for-x86_64-supplementary-rpms' is enabled for this system.
```

Verify:

```bash
dnf repolist enabled
```

---

### 🔹 Step 3: Create a Custom `.repo` File

```bash
sudo vi /etc/yum.repos.d/custom-tools.repo
```

**Insert content:**

```ini
[custom-tools]
name=Internal Security Tools
baseurl=http://192.168.56.10/repos/rhel9
enabled=1
gpgcheck=0
```

> ⚠️ `gpgcheck=0` disables signature verification — dangerous in prod environments. Use only in controlled labs.

---

### 🔹 Step 4: Validate Custom Repo

```bash
dnf clean all
dnf repolist
```

**Expected Output (partial):**

```
repo id               repo name
custom-tools          Internal Security Tools
```

If `dnf repolist` throws an error, test connectivity:

```bash
curl -I http://192.168.56.10/repos/rhel9/
```

---

### 🔹 Step 5: Review DNF Logs

```bash
less /var/log/dnf.log
```

Look for entries like:

```
Added repository: custom-tools
```

This helps verify whether the repo was parsed correctly.

---

## ⚔️ Red/Blue Insight (Mini-Sim)

**Red Team:**

* Could inject a malicious `.repo` with fake `baseurl` to deliver trojan RPMs
* Disable `gpgcheck` to avoid signature verification

**Blue Team:**

* Detect new or unauthorized `.repo` files with tripwire or file integrity tools
* Monitor `/var/log/dnf.log` for new repo additions or unusual package downloads
* Enforce GPG keys via automation tools like Ansible

---

## ✅ Success Criteria

| Task                              | Verified? |
| --------------------------------- | --------- |
| All available repos listed        | ✅         |
| Supplementary repo enabled        | ✅         |
| Custom `.repo` created and tested | ✅         |
| Logs reviewed                     | ✅         |

---

## 📚 Reflection Questions

* What is the difference between enabling via `subscription-manager` and `.repo` file?
* What risk is introduced by disabling `gpgcheck`?
* Could a user without root privileges create a fake repo? Why/why not?

---

## 🧠 Challenge (Advanced)

Simulate a MITM attack by setting up a local repo with a tampered `.rpm` file and observe what happens when installed with `gpgcheck=0`.

---

✅ Let me know when you're ready for the **next topic** or want the **Red/Blue Simulation Lab** for this lesson.
