Here is your completed and professional-grade Markdown for **Lab 3: File System and Boot Services Investigation**, following the `Cybersecurity Documentation Protocol — Ultra Edition v5.0`. I've expanded the Observations, Analysis, and Conclusion sections with real-world security context, using your output.

---

# 🧪 Lab 3: File System and Boot Services Investigation

### Date: 2025-07-22

### Mentor: *The Da Vinci Cypher*

### Protocol Tier: Tier 0 — System Fundamentals

### Module: Module 0.1 — System State & Configuration Analysis

---

## 🎯 1. Objective

To investigate critical file system permissions and analyze the system's boot-time services. The goal is to understand how to manually inspect security-critical file permissions and identify which services are configured to start automatically when the system boots.

---

## 🧰 2. Tools Used

| Tool/Command | Purpose                                                                                      |
| ------------ | -------------------------------------------------------------------------------------------- |
| `ls -l`      | **L**i**s**ts file information in a **l**ong format, showing permissions, owner, group, etc. |
| `systemctl`  | The master tool for controlling the **systemd** init system, used to manage services.        |

---

## 🖥️ 3. Process & Commands

### 🔹 Step 1: Investigating Critical File Permissions

The `/etc/shadow` file stores user password hashes. It should be one of the most protected files on the system.

* **Command:**

  ```bash
  ls -l /etc/shadow
  ```

* **Output:**

  ```
  -rw-r----- 1 root root 1099 Jul 19 12:12 /etc/shadow
  ```

---

### 🔹 Step 2: Listing All Enabled Boot-Time Services

This command lists all service units that are "enabled," meaning they are configured to start automatically on boot.

* **Command:**

  ```bash
  systemctl list-unit-files --type=service --state=enabled
  ```

* **Output:**

<details>
<summary>🗂️ Click to expand full output (49 services)</summary>

```plaintext
accounts-daemon.service            enabled enabled 
atd.service                        enabled enabled 
auditd.service                     enabled enabled 
avahi-daemon.service               enabled enabled 
bluetooth.service                  enabled enabled 
chronyd.service                    enabled enabled 
crond.service                      enabled enabled 
cups.service                       enabled enabled 
dbus-broker.service                enabled enabled 
firewalld.service                  enabled enabled 
gdm.service                        enabled enabled 
getty@.service                     enabled enabled 
insights-client-boot.service       enabled enabled 
irqbalance.service                 enabled enabled 
iscsi-onboot.service               enabled enabled 
iscsi-starter.service              enabled disabled
iscsi.service                      enabled enabled 
kdump.service                      enabled enabled 
libstoragemgmt.service             enabled enabled 
low-memory-monitor.service         enabled enabled 
lvm2-monitor.service               enabled enabled 
mcelog.service                     enabled enabled 
mdmonitor.service                  enabled enabled 
microcode.service                  enabled enabled 
ModemManager.service               enabled enabled 
multipathd.service                 enabled enabled 
NetworkManager-dispatcher.service  enabled enabled 
NetworkManager-wait-online.service enabled disabled
NetworkManager.service             enabled enabled 
nis-domainname.service             enabled enabled 
nvmefc-boot-connections.service    enabled enabled 
ostree-remount.service             enabled enabled 
power-profiles-daemon.service      enabled enabled 
qemu-guest-agent.service           enabled enabled 
rhsmcertd.service                  enabled enabled 
rsyslog.service                    enabled enabled 
rtkit-daemon.service               enabled enabled 
selinux-autorelabel-mark.service   enabled enabled 
smartd.service                     enabled enabled 
sshd.service                       enabled enabled 
sssd.service                       enabled enabled 
switcheroo-control.service         enabled enabled 
systemd-boot-update.service        enabled enabled 
systemd-network-generator.service  enabled enabled 
tuned.service                      enabled enabled 
udisks2.service                    enabled enabled 
upower.service                     enabled enabled 
vgauthd.service                    enabled disabled
vmtoolsd.service                   enabled enabled 
```

</details>

---

## 🔎 4. Observations & Analysis

### 🔐 File Permission Analysis — `/etc/shadow`

* **Owner:** `root`
* **Group:** `root`
* **Permissions:** `-rw-r-----`

#### Breakdown

* `-rw-r-----`

  * `-` → Regular file.
  * `rw-` (owner = `root`): Read & write permissions.
  * `r--` (group = `root`): Read-only access for root group.
  * `---` (others = none): No access for other users.

> 🧠 **Security Insight:**
> This permission configuration is **critical** for system security. Only `root` can write to or read the file. Regular users (like `shahid`) **cannot access this file**, even to read. Since it contains **password hashes**, any exposure can lead to offline brute-force or hash-cracking attacks.

> 🔒 **Defense Mechanism:**
> Attackers who gain access to `/etc/shadow` may attempt to exfiltrate it for offline cracking. Proper permissions act as the **first line of defense**.

---

### 🚦 Service Startup Analysis — `systemctl list-unit-files`

#### 📌 Recognized Services

| Service Name        | Function                                                       |
| ------------------- | -------------------------------------------------------------- |
| `sshd.service`      | Enables the **OpenSSH daemon**, allowing remote login via SSH. |
| `crond.service`     | Manages **scheduled tasks** via `cron`. Used for automation.   |
| `firewalld.service` | Provides **dynamic firewall management**.                      |
| `auditd.service`    | Records **security audit logs**, vital for SIEM integration.   |
| `rsyslog.service`   | System logging daemon that captures logs into `/var/log`.      |

> 🧠 **Security Context:**

* If an attacker installs a **persistence mechanism**, they often create or modify a service unit file.
* Example: A malicious service like `malware-update.service` could be disguised as legitimate.
* **Enabled services** are auto-started at boot, so reviewing this list is essential for **IR (Incident Response)** and **threat hunting**.

> 🔍 **Blue Team Tip:**
> Compare boot-time services with a **baseline** system. Any new or suspicious entries (e.g., with unusual names or binary paths) should be investigated immediately.

---

## ✅ 5. Conclusion

This lab demonstrated two core elements of system investigation:

1. **File Permission Awareness:** Understanding and validating permissions on sensitive files (like `/etc/shadow`) helps prevent unauthorized access and credential theft.
2. **Boot-Time Service Enumeration:** By reviewing enabled services, we can spot suspicious or misconfigured services that may indicate malware, rootkits, or persistence.

These skills are foundational for system hardening, vulnerability assessment, digital forensics, and incident response.

> 🔐 **Key Takeaway:**
> Every attack that achieves persistence must leave a footprint. Services and file permissions are often the **first footprints** defenders can follow.
