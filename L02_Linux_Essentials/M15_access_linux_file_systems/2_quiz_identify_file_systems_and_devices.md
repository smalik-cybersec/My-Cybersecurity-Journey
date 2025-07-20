Absolutely, Shahid 👨‍🏫⚙️ — let’s now create a **GitHub/Obsidian-ready deep quiz** for:

---

# 🧪 **Quiz: Identify File Systems and Devices**

📁 *Module 15: Access Linux File Systems — Lesson 1*
🎯 *Goal: Test and reinforce your understanding of partitions, file systems, block devices, and identification tools in RHEL*

---

## ✅ **Quiz Format**

* Total Questions: **12**
* Difficulty: **Mixed (Beginner ➜ Tactical)**
* Style: **Real-world scenarios**, **command interpretation**, **log analysis**, **Red Team awareness**, **job-role alignment**
* Output: Clean **Markdown**, directly usable in Obsidian or GitHub

---

## 📘 **Quiz Starts**

---

### 🔹 **Q1. Multiple Choice**

What is the purpose of the `UUID` in a file system?

**A.** It is a unique identifier tied to the kernel module for each filesystem.
**B.** It ensures persistent identification of a partition, even if the device path changes.
**C.** It is required only for swap partitions.
**D.** It matches the file system label to the mount point automatically.

<details><summary>📝 Answer</summary>
**B.** UUIDs are used in `/etc/fstab` to ensure reliable device recognition, even if `/dev/sdX` paths change.
</details>

---

### 🔹 **Q2. Fill in the Blank**

The command `lsblk -f` shows file system types, mount points, and \_\_\_\_\_\_\_\_\_\_\_\_ for each block device.

<details><summary>📝 Answer</summary>
**UUID** (and optionally LABEL)
</details>

---

### 🔹 **Q3. Command Interpretation**

You're given the output of `blkid`:

```bash
/dev/sda1: UUID="9f6c9e50-02a1-4c5e-94f0-71b7262f18a7" TYPE="xfs" PARTUUID="0001d95d-01"
/dev/sda2: UUID="d3144ba3-70c1-4c1e-843f-9e67be67bdb4" TYPE="swap" PARTUUID="0001d95d-02"
```

**Which device is likely mounted as the root filesystem (`/`) and why?**

<details><summary>📝 Answer</summary>
Likely `/dev/sda1`, because it uses `xfs`, the default RHEL root filesystem. Swap partitions are rarely mounted as `/`.
</details>

---

### 🔹 **Q4. Scenario (Red Team Awareness)**

You plug in a USB drive, and nothing appears under `/media/`. Which two commands would you use to verify:

* The system sees the physical device
* The file system type is recognized

<details><summary>📝 Answer</summary>

```bash
lsblk -f       # To list device tree and file system
dmesg | tail   # To check kernel logs for new device attachment
```

</details>

---

### 🔹 **Q5. Short Answer**

Explain why `/dev/sda1` might appear differently on different systems (e.g., as `/dev/vda1` or `/dev/nvme0n1p1`).

<details><summary>📝 Answer</summary>
Device names are dynamically assigned by the kernel based on the **storage driver** and **device type**:  
- `sda` → SATA/SCSI  
- `vda` → VirtIO virtual disk  
- `nvme0n1p1` → NVMe SSD  
Use UUIDs for consistency.
</details>

---

### 🔹 **Q6. True or False**

The `mount` command can automatically detect the file system type of a partition without user input.

<details><summary>📝 Answer</summary>
**True.** `mount` can auto-detect file systems using `blkid` under the hood.
</details>

---

### 🔹 **Q7. Practical Task**

A user accidentally formatted a disk and mounted it without a label. How do you assign a label to `/dev/sdb1` (XFS) and verify it?

<details><summary>📝 Answer</summary>

```bash
xfs_admin -L "DATA_DISK" /dev/sdb1
lsblk -f | grep sdb1
```

</details>

---

### 🔹 **Q8. Log Reading**

You check `/etc/fstab` and see this entry:

```bash
UUID=ac12efab-3f6a-4447-9c6d-948cc99e1a4e /mnt/backup xfs defaults 0 2
```

**What happens if this UUID is no longer valid or the disk is unplugged at boot?**

<details><summary>📝 Answer</summary>
The system will either boot with an error, enter emergency mode, or skip mounting depending on boot flags and rescue settings.
</details>

---

### 🔹 **Q9. Scenario (DFIR Context)**

During IR triage, you need to verify all block devices and file system types. The output of `mount` is cluttered. What cleaner command gives a readable tree of devices and mount points?

<details><summary>📝 Answer</summary>
`lsblk -f` or `findmnt` — both offer clean, hierarchical views.
</details>

---

### 🔹 **Q10. Deep Reasoning**

What would be the real-world risk of using device paths like `/dev/sdb1` in `/etc/fstab` instead of UUIDs or labels?

<details><summary>📝 Answer</summary>
Device names can **change order** on reboot (especially in virtualized or hotplug environments), leading to **mount failures**, **data loss**, or **system boot errors**. UUIDs are persistent.
</details>

---

### 🔹 **Q11. Tool Match-Up**

Match the tool to its primary purpose:

| Tool       | Purpose                           |
| ---------- | --------------------------------- |
| `lsblk`    | A. Low-level device attributes    |
| `blkid`    | B. List mountable devices in tree |
| `df -h`    | C. Show used/free space           |
| `mount`    | D. Show active mounts             |
| `fdisk -l` | E. View partition layout          |

<details><summary>📝 Answer</summary>

* `lsblk` → B
* `blkid` → A
* `df -h` → C
* `mount` → D
* `fdisk -l` → E

</details>

---

### 🔹 **Q12. Red/Blue Team Application**

Why is understanding file systems and block devices essential in:

**a. Red Team operations**
**b. Blue Team detection and forensics**

<details><summary>📝 Answer</summary>

**Red Team:** Mounting hidden partitions, bypassing audit logs, or hiding malware in non-standard mount points (e.g., `/mnt/.backup`)

**Blue Team:** Ensuring all partitions are accounted for, detecting rogue USB devices, and identifying suspicious mount flags or hidden persistence.

</details>

---

## 📘 Summary

* This quiz covered:
  ✅ UUIDs, file system types, partitions
  ✅ Real command usage (`blkid`, `lsblk`, `mount`)
  ✅ `/etc/fstab` behavior and risks
  ✅ Forensic/Red Team use of mounting and visibility
  ✅ Labeling and managing unknown devices

---

Would you like this quiz in `.md` format for your **Cybersecurity Documentation Protocol v5.0**?
Or shall we move to the next lesson: **Mount and Unmount File Systems**?

Let me know, Captain Shahid 🧠⚔️📚
