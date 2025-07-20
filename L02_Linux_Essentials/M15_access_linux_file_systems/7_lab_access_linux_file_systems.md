Excellent, Shahid. Here’s your **🔬 Full Lab** for:

> **📁 Module 15: Access Linux File Systems**
> **🎓 Lab: Access Linux File Systems**
> **Level**: Linux Essentials Level 3 — RHEL 9
> **Protocol**: Follows Cybersecurity Documentation Protocol Ultra Edition v5.0 (Master Grade Edition)

---

# 🔬 Lab: Access Linux File Systems (RHEL 9)

> 🔐 Build real-world mastery in mounting, unmounting, locating, and investigating Linux file systems. This lab blends system administration with Blue Team/IR skills.

---

## 🎯 Objective

By the end of this lab, you will:

* Identify and mount block devices manually
* Mount ISO files using loop devices
* Locate system files using `find`, `locate`, and `which`
* Perform forensic-style file investigations
* Log file system events for security monitoring

---

## 🧱 Environment

* RHEL 9 or RHEL-compatible VM (Rocky/Alma Linux)
* USB device or virtual disk (`/dev/sdb1`)
* ISO file (`~/Downloads/rhel.iso`)
* Sudo-enabled user access

---

## 🧪 Lab Tasks

---

### ✅ Task 1: Identify Available File Systems

```bash
lsblk -f
```

📌 *Use this to find devices not mounted (e.g., `/dev/sdb1`)*

---

### ✅ Task 2: Mount a USB Drive Manually

```bash
sudo mkdir -p /mnt/usb
sudo mount /dev/sdb1 /mnt/usb
```

🧪 Verify:

```bash
df -hT /mnt/usb
```

---

### ✅ Task 3: Unmount the USB Safely

```bash
sudo umount /mnt/usb
```

---

### ✅ Task 4: Mount an ISO Image

```bash
sudo mkdir -p /mnt/iso
sudo mount -o loop ~/Downloads/rhel.iso /mnt/iso
```

📌 *ISO will be read-only*

🧪 Verify:

```bash
ls /mnt/iso
df -hT /mnt/iso
```

---

### ✅ Task 5: Use `find` to Search for Large Files

```bash
find / -type f -size +500M -exec ls -lh {} \; 2>/dev/null
```

---

### ✅ Task 6: Use `locate` to Search Fast

```bash
sudo updatedb
locate sshd_config
```

---

### ✅ Task 7: Find All SUID Binaries (Security Focus)

```bash
find / -perm -4000 -type f 2>/dev/null
```

📌 *Used to audit for privilege escalation risks*

---

### ✅ Task 8: Find Recently Modified Files in `/tmp`

```bash
find /tmp -type f -mmin -30 -exec file {} \;
```

---

### ✅ Task 9: Monitor File System Activity (Blue Team Drill)

```bash
sudo auditctl -w /mnt/usb -p rwxa -k usb-monitor
```

🧪 Simulate activity:

```bash
echo "test" | sudo tee /mnt/usb/test.txt
```

📜 View audit logs:

```bash
sudo ausearch -k usb-monitor
```

---

### ✅ Task 10: Clean Up

```bash
sudo umount /mnt/iso
sudo umount /mnt/usb
sudo auditctl -W /mnt/usb -k usb-monitor
```

---

## 📋 Lab Checklist

| Task               | Command                           | Status |
| ------------------ | --------------------------------- | ------ |
| Identify devices   | `lsblk -f`                        | ✅      |
| Mount USB          | `mount /dev/sdb1 /mnt/usb`        | ✅      |
| Unmount USB        | `umount /mnt/usb`                 | ✅      |
| Mount ISO          | `mount -o loop rhel.iso /mnt/iso` | ✅      |
| Use `find`         | `find / -size +500M`              | ✅      |
| Use `locate`       | `locate sshd_config`              | ✅      |
| Check SUID files   | `find / -perm -4000`              | ✅      |
| Investigate `/tmp` | `find /tmp -mmin -30`             | ✅      |
| Monitor FS         | `auditctl` + `ausearch`           | ✅      |

---

## 🛡️ Real-World Blue Team Mapping

| Task                  | Use Case                   | MITRE ATT\&CK             |
| --------------------- | -------------------------- | ------------------------- |
| Mount image read-only | Forensic Triage            | T1005 (Data Staging)      |
| Monitor `/mnt/usb`    | Detect USB exfiltration    | T1200 (Hardware Addition) |
| SUID Scan             | Privilege Escalation Audit | T1548.001                 |

---

## 🧠 Reflection & Confidence Journal

* 🟩 I can mount/unmount USB/ISO devices confidently.
* 🟩 I can use `find`/`locate` for file discovery and investigation.
* 🟨 I need more practice with `auditctl` and logging tools.
* 🟥 I want to learn how to create persistent mounts using `/etc/fstab`.

---

## 🗓️ Spaced Repetition Plan

* **Day 1**: Repeat this full lab with real devices (USB + ISO)
* **Day 3**: Add SUID scans and forensic timeline tracking
* **Day 7**: Combine with `/etc/fstab` for persistent mounts
* **Day 30**: Create your own custom Red/Blue Lab with audit logging + file hunts

---

Would you like me to now provide the **Obsidian/GitHub-compatible Markdown version** of this full lab for publishing?
