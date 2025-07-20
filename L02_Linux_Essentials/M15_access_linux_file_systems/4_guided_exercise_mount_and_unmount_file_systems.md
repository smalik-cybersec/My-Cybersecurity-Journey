# 🧪 Guided Exercise: Mount and Unmount File Systems (RHEL 9)

> **Context**: These hands-on steps are tested on a real RHEL 9 system. Suitable for labs, exams (e.g., RHCSA), and SOC/Forensic blue team readiness.

---

## 🎯 Objective

* Mount a USB drive manually.
* Mount an ISO file.
* Unmount devices safely.
* Understand how mounting affects the Linux file system.
* Verify using system tools.

---

## 🧱 Prerequisites

* A running **RHEL 9** system.
* A non-root user with **sudo** privileges.
* Access to a removable block device (e.g., USB) and a sample `.iso` file.

---

## 🧰 Step-by-Step Instructions

---

### ✅ Task 1: Identify Available Block Devices

```bash
lsblk
```

📌 *Look for something like `/dev/sdb1` not currently mounted.*

Sample Output:

```bash
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0   50G  0 disk 
├─sda1   8:1    0    1G  0 part /boot
└─sda2   8:2    0   49G  0 part /
sdb      8:16   1   16G  0 disk 
└─sdb1   8:17   1   16G  0 part 
```

---

### ✅ Task 2: Create a Mount Point

```bash
sudo mkdir -p /mnt/usb
```

---

### ✅ Task 3: Mount the USB File System

Assuming the USB is at `/dev/sdb1`:

```bash
sudo mount /dev/sdb1 /mnt/usb
```

---

### ✅ Task 4: Verify the Mount

```bash
df -hT /mnt/usb
```

Sample Output:

```bash
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/sdb1      vfat   16G  1.2G   15G   8% /mnt/usb
```

Or with `mount`:

```bash
mount | grep sdb1
```

---

### ✅ Task 5: View Contents of the USB

```bash
ls /mnt/usb
```

---

### ✅ Task 6: Unmount the File System

```bash
sudo umount /mnt/usb
```

---

### ✅ Task 7: Mount an ISO File

Assuming `rhel.iso` is in your home directory:

```bash
mkdir -p ~/iso_mount
sudo mount -o loop ~/rhel.iso ~/iso_mount
```

---

### ✅ Task 8: Verify ISO Mount

```bash
df -hT ~/iso_mount
```

---

### ✅ Task 9: Unmount the ISO

```bash
sudo umount ~/iso_mount
```

---

### ✅ Task 10: Check System Logs (Optional Forensics Check)

```bash
sudo journalctl | grep mount
```

---

## 📋 Expected Results

| Task                       | Outcome                  |
| -------------------------- | ------------------------ |
| `lsblk`                    | Lists devices            |
| `mount /dev/sdb1 /mnt/usb` | USB mounted              |
| `df -hT`                   | Shows device and type    |
| `umount`                   | Device cleanly unmounted |
| `mount -o loop`            | ISO mounted read-only    |
| `journalctl`               | Shows mount logs         |

---

## 🧪 Bonus Challenge

> 🔐 **Simulate mounting a forensic disk image**:

```bash
sudo mount -o ro,loop suspect.dd /mnt/forensics
```

---

## ✅ Guided Checklist

* [x] Identified block devices
* [x] Mounted and unmounted USB
* [x] Mounted ISO using loop device
* [x] Verified with `df`, `mount`, `lsblk`
* [x] Explored forensic use case

---

Would you like a **Markdown version** for GitHub/Obsidian publishing or want to proceed to persistent mounting using `/etc/fstab`?
