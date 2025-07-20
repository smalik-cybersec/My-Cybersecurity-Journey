## 📦 Module 15: Access Linux File Systems

### 🧩 Lesson 3: Mount and Unmount File Systems (RHEL-based)

> **Cert/Job Mapping**: \[RHCSA], \[CEH Blue Team Ops], \[SOC Analyst], \[Forensic Analyst]

---

### 🧭 1. Introduction

Mounting a file system in Linux means making a storage device (e.g., disk partition, USB, ISO) accessible through a specific directory (mount point). Unmounting detaches that device safely from the system.

Understanding how to manage mounts is crucial in system administration, forensics, incident response, and secure data handling.

---

### 🧠 2. Core Concepts (Feynman Style)

#### What is Mounting?

> In Linux, devices are not automatically linked to paths like in Windows (e.g., `D:\`). Instead, they must be “mounted” into the main file system tree at a chosen directory (e.g., `/mnt/usb` or `/media/disk1`).

#### Mount Points

> A **mount point** is a directory where the file system appears. Once mounted, files from the device show up inside that directory.

#### File System Types

* `ext4`, `xfs` (common in RHEL)
* `vfat`, `ntfs` (Windows-compatible)
* `iso9660` (CD/DVD)
* `nfs` (Network File Systems)

#### Manual vs. Automatic

* **Manual Mounting**: using the `mount` command
* **Automatic**: via `/etc/fstab` or `systemd` mount units

#### Unmounting

> Done via `umount` command. Required before removing a device to avoid data corruption.

---

### 🧪 3. Commands & Configs (with Real RHEL Output)

#### 🔹 Mounting a Device

```bash
sudo mount /dev/sdb1 /mnt/usb
```

Check with:

```bash
$ mount | grep sdb1
/dev/sdb1 on /mnt/usb type vfat (rw,nosuid,nodev...)
```

#### 🔹 Unmounting

```bash
sudo umount /mnt/usb
```

Or using device:

```bash
sudo umount /dev/sdb1
```

#### 🔹 Viewing Mounted File Systems

```bash
$ df -hT
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/sda2      xfs    50G   15G   35G  30% /
```

#### 🔹 List Block Devices

```bash
lsblk
```

Sample Output:

```bash
NAME   MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
sda      8:0    0  50G  0 disk 
└─sda2   8:2    0  50G  0 part /
sdb      8:16   1  16G  0 disk 
└─sdb1   8:17   1  16G  0 part /mnt/usb
```

---

### 🧰 4. Labs (Beginner → Tactical → Simulation)

#### 🔰 Beginner Lab

**Goal**: Mount a USB device and view its contents.

1. Insert USB (`/dev/sdb1`)
2. Create mount point:

   ```bash
   sudo mkdir -p /mnt/usb
   ```
3. Mount it:

   ```bash
   sudo mount /dev/sdb1 /mnt/usb
   ```
4. View contents:

   ```bash
   ls /mnt/usb
   ```
5. Unmount:

   ```bash
   sudo umount /mnt/usb
   ```

#### ⚙️ Tactical Lab

**Goal**: Mount an ISO image.

1. Download ISO (`example.iso`)
2. Create mount point:

   ```bash
   sudo mkdir /mnt/iso
   ```
3. Mount ISO:

   ```bash
   sudo mount -o loop example.iso /mnt/iso
   ```
4. Validate with `df -hT` and `ls /mnt/iso`

#### 🎯 Simulation Lab

**Scenario**: During forensic triage, you need to mount a suspect’s disk image on a live RHEL machine.

1. Attach `.dd` image as loop device
2. Use `losetup` and `mount`
3. Mount read-only:

   ```bash
   sudo mount -o ro,loop suspect.dd /mnt/forensics
   ```
4. Log all access attempts (simulate auditd)

---

### 🛡️ 5. Red/Blue Simulation (MITRE + Logs)

| Team    | Simulation                                     | Tooling                 | MITRE Technique                     | Logs                          |
| ------- | ---------------------------------------------- | ----------------------- | ----------------------------------- | ----------------------------- |
| 🔴 Red  | Remount system as read/write to plant backdoor | `mount -o remount,rw /` | T1547.010 (Boot or Logon Autostart) | `auditd`, `/var/log/messages` |
| 🔵 Blue | Detect unauthorized mount from USB             | `auditctl`, `ausearch`  | T1200 (Hardware Additions)          | `audit.log`, `journalctl`     |

#### 📘 Audit Rule (Detect USB Mount)

```bash
auditctl -w /bin/mount -p x -k mount-watch
```

Check activity:

```bash
ausearch -k mount-watch
```

---

### 🧠 6. Deep Quiz

1. What does `mount -o loop` do?
2. Why must devices be unmounted before removal?
3. What is the purpose of `/etc/fstab`?
4. What happens if you mount over an existing directory?
5. How to remount root FS as read-only?

---

### 📊 7. Summary Table + Checklist

| Task                  | Command                           | Verified |
| --------------------- | --------------------------------- | -------- |
| Mount block device    | `mount /dev/sdX1 /mnt/target`     | ✅        |
| Unmount safely        | `umount /mnt/target`              | ✅        |
| List mounted FS       | `df -hT`                          | ✅        |
| Mount ISO             | `mount -o loop file.iso /mnt/iso` | ✅        |
| Monitor mount actions | `auditctl`, `ausearch`            | ✅        |

---

### 📓 8. Journaling + Confidence Tracker

* 🟩 I can mount/unmount devices and ISOs
* 🟨 I partially understand `loop`, `fstab`
* 🟥 I need to review filesystem types

---

### 🧭 9. Job & Cert Mapping

| Role                 | Skill Required                         |
| -------------------- | -------------------------------------- |
| 🛡️ SOC Analyst      | Detect unauthorized device mounts      |
| 🧰 Linux Admin       | Manage local and remote mounts         |
| 🕵️ Forensic Analyst | Mount disk images read-only            |
| 📜 RHCSA             | Mount, unmount, configure `/etc/fstab` |

---

### 🗓️ 10. Spaced Repetition Plan

* **Day 1**: Perform manual mount + umount of USB and ISO
* **Day 3**: Simulate forensic image mount + audit logging
* **Day 7**: Automate via `/etc/fstab` + simulate red team remount
* **Day 30**: Build a cheat sheet for all FS types and mount options

---

Ready for next sub-lesson or want to dive into `/etc/fstab` automation and persistent mounting next?
