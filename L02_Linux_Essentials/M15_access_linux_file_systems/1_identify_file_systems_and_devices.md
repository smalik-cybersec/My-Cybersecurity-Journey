Excellent, Shahid ✅

We now begin:

---

# 🧭 **Module 15: Access Linux File Systems**

**🎓 Lesson 1: Identify File Systems and Devices**

> **Track:** Linux Essentials — Level 3
> **Platform:** RHEL 9.x (Real-world SOC/SysAdmin Red/Blue Lab Ready)
> **Protocol:** Cybersecurity Documentation Protocol — Ultra Edition v5.0 (Master Grade Edition)

---

## 1. 🔎 Introduction

In any professional Linux environment — especially in SOC, forensics, or blue team contexts — being able to **identify file systems and their underlying devices** is mission-critical.

Whether you're investigating a compromised server, performing incident response, or managing disk space across multiple volumes, you must know:

* **Which devices are mounted where**
* **What file system types are used (ext4, xfs, vfat, etc.)**
* **Which devices correspond to physical or virtual partitions**
* **Which mounts are persistent or temporary**

This foundational knowledge lets you **audit, defend, troubleshoot, or recover systems under pressure**.

---

## 2. 🧠 Core Concepts (Feynman Style)

### 🔧 Feynman Analogy:

> *"Imagine Linux as a vast office building. Every room (directory) might be located on a different floor (device/partition). Your job is to know which rooms are on which floors, what kind of flooring they use (file system), and whether they’re permanently installed or temporary trailers."*

In this lesson, we focus on identifying:

* Physical and virtual **block devices**
* The **file system types** in use
* Which devices are **mounted where**
* Whether a file system is **read-only**, **temporary**, or **persistent**

### 📊 File Systems Overview

| File System | Usage                            | Notes                             |
| ----------- | -------------------------------- | --------------------------------- |
| `ext4`      | Default Linux fs (older distros) | Good journaling, stable           |
| `xfs`       | Default in RHEL 9                | High performance, large files     |
| `vfat`      | USBs, EFI partitions             | No journaling, Windows-compatible |
| `btrfs`     | Experimental, snapshots          | Not used in RHEL 9 by default     |
| `tmpfs`     | Temporary RAM-backed storage     | Auto-clears on reboot             |

---

## 3. 💻 Commands & Configs (RHEL 9.x Real Output)

### 🔍 View mounted file systems

```bash
mount | column -t
```

**Sample output:**

```plaintext
/dev/mapper/rhel-root  on  /      type  xfs     (rw,relatime,attr2,...)
devtmpfs               on  /dev   type  devtmpfs(rw,nosuid,seclabel,...
tmpfs                  on  /run   type  tmpfs   (rw,nosuid,nodev,seclabel,...
```

### 🔎 View block devices and their file systems

```bash
lsblk -f
```

**Sample output:**

```plaintext
NAME            FSTYPE LABEL UUID                                 MOUNTPOINT
sda                                                                
├─sda1          xfs          a1b2c3d4-e5f6-7890-abcd-ef0123456789 /
├─sda2          xfs          b2c3d4e5-f678-9012-abcd-ef2345678901 /home
└─sda3          swap         c3d4e5f6-7890-1234-abcd-ef3456789012 [SWAP]
```

### 🧠 Tip: To include file system **labels, UUIDs**, and types, always use:

```bash
lsblk -o NAME,FSTYPE,LABEL,UUID,MOUNTPOINT
```

### 📁 Check persistent mounts (used at boot)

```bash
cat /etc/fstab
```

**Sample output:**

```plaintext
UUID=a1b2...  /      xfs     defaults        0 0
UUID=b2c3...  /home  xfs     defaults        0 0
```

### 🛠️ View mounted file systems in a tree format:

```bash
findmnt
```

**Sample output:**

```plaintext
TARGET SOURCE                        FSTYPE OPTIONS
/      /dev/mapper/rhel-root         xfs    rw,...
├─/home /dev/mapper/rhel-home        xfs    rw,...
├─/boot /dev/sda1                    xfs    rw,...
```

---

## 4. 🧪 Labs

### 🟢 Beginner Lab: Identify Devices and File Systems

**Goal:** Use `lsblk`, `mount`, and `findmnt` to map devices → mount points

1. Run:

   ```bash
   lsblk -f
   mount | column -t
   findmnt
   ```

2. Note down:

   * All mount points and corresponding devices
   * File system types for `/`, `/home`, `/boot`, `/var`, etc.

---

### 🟡 Tactical Lab: Find Temporary & Encrypted File Systems

1. Run:

   ```bash
   mount | grep tmpfs
   ```

2. Check:

   * Which directories use `tmpfs` (RAM)
   * Are any `/tmp`, `/run`, `/var/tmp` using tmpfs?

3. Run:

   ```bash
   lsblk -o NAME,FSTYPE,TYPE,MOUNTPOINT
   ```

4. Check for:

   * LUKS-encrypted devices (may show `crypto_LUKS` as FSTYPE)

---

### 🔴 Simulation Lab: SOC Analyst Audits File System

> A SOC analyst suspects a USB was used to exfiltrate logs. Investigate all mounted external media.

1. Run:

   ```bash
   lsblk -f
   mount
   ```

2. Use:

   ```bash
   journalctl | grep 'mount'
   ```

3. Check if any devices like `/dev/sdb1` were mounted under `/media` or `/run/media`

---

## 5. ⚔️ Red/Blue Simulation (MITRE ATT\&CK)

| Phase     | Technique ID | Description                  |
| --------- | ------------ | ---------------------------- |
| Discovery | T1083        | File and Directory Discovery |
| Discovery | T1120        | Peripheral Device Discovery  |

**Red Team Tactic:** Use `mount` and `lsblk` to identify target storage areas for staging data or finding misconfigurations.

**Blue Team Response:**

* Monitor `journalctl -k` for USB insertion or volume mount logs
* Harden `udisks2` policies to restrict auto-mounts
* Use auditd to monitor `mount` and `umount` system calls

---

## 6. 🧩 Quiz

**Q1.** What command lists all devices and their mount points in a tree view?
**A.** `findmnt`

**Q2.** Which file defines persistent mount points on RHEL?
**A.** `/etc/fstab`

**Q3.** A system shows `/dev/sdb1` as `vfat` mounted at `/run/media/shahid/USB`. What does this indicate?
**A.** A USB device with a Windows-compatible file system is currently mounted.

**Q4.** How do you find whether `/tmp` is using `tmpfs`?
**A.** Run `mount | grep /tmp` or `findmnt /tmp`

---

## 7. 📌 Summary Table + Checklist

| Task                    | Command            |              |
| ----------------------- | ------------------ | ------------ |
| List devices + FS types | `lsblk -f`         |              |
| View mounted FSs        | `mount`, `findmnt` |              |
| Check temporary FSs     | \`mount            | grep tmpfs\` |
| View persistent mounts  | `cat /etc/fstab`   |              |
| Audit USB mounts        | \`journalctl       | grep mount\` |

---

## 8. 📚 Journaling + Confidence Tracker

* ✅ I can now map devices to mount points using `lsblk`, `mount`, and `findmnt`
* ✅ I understand `tmpfs`, `xfs`, `vfat`, and `ext4` distinctions
* ✅ I can identify persistent vs temporary mounts
* 🧠 Still practicing identifying encrypted volumes

---

## 9. 🧭 Job Role + Cert Mapping

| Role             | Relevance                                     |
| ---------------- | --------------------------------------------- |
| SOC Analyst      | Auditing mounts for USB or rogue devices      |
| Linux SysAdmin   | Managing volumes, `/etc/fstab`, diagnostics   |
| Forensic Analyst | Examining removable media, boot configs       |
| Red Teamer       | Mapping out filesystem targets (T1083, T1120) |

| Certification | Topic                                       |
| ------------- | ------------------------------------------- |
| RHCSA         | File systems, `lsblk`, `/etc/fstab`, mounts |
| CEH           | Enumeration, persistence vectors            |
| Security+     | Disk security, removable media management   |

---

## 10. 🔁 Spaced Repetition Planner

| Day | Activity                                                     |
| --- | ------------------------------------------------------------ |
| 1   | Run `lsblk`, `mount`, `findmnt` on a VM — record findings    |
| 3   | Modify `/etc/fstab` with a test volume, reboot, test         |
| 7   | Simulate USB device mount and investigate via `journalctl`   |
| 30  | Forensic challenge: identify mounted malicious USB from logs |

---

Ready for the **next lesson** whenever you are. Just send the title and we’ll continue evolving your mastery.
