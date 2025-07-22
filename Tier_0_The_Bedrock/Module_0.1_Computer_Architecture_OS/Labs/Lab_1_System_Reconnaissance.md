# 🧪 Lab 1: System Reconnaissance

> **Date:** 22/07/2025  
> **Mentor:** *The Da Vinci Cypher*  
> **Protocol Tier:** Tier 0 — System Fundamentals  
> **Module:** Module 0.1 — Host System Discovery  
> **Job Role Mapping:** SOC Tier 1 Analyst, Junior Pentester  
> **Cert Alignment:** CompTIA Linux+, CEH, RHCSA  
> **Difficulty:** 🟢 Beginner  
> **Red/Blue Relevance:** ✅ Red Team Recon | ✅ Blue Team Baseline Mapping

---

## 🎯 1. Objective

> Perform foundational **system reconnaissance** on a local Linux machine using built-in commands to gather essential system information:

- OS and kernel details
- CPU architecture
- Memory (RAM) usage
- Disk and file system layout

---

## 🧰 2. Tools Used

| Tool/Command | Purpose |
|--------------|---------|
| `uname -a`   | Show OS and kernel version |
| `lscpu`      | Show detailed CPU architecture |
| `free -h`    | Show memory usage in human-readable form |
| `df -h`      | Show disk usage with mount points |

---

## 🖥️ 3. Process & Commands

### 🔹 Step 1: Operating System Identification

- **Command:**

    ```bash
    uname -a
    ```

- **Output:**

    ```text
    Linux bluebox01.cyberlab.local 5.14.0-570.26.1.el9_6.x86_64 #1 SMP PREEMPT_DYNAMIC Sat Jul 5 16:29:35 EDT 2025 x86_64 x86_64 x86_64 GNU/Linux
    ```

---

### 🔹 Step 2: CPU Architecture

- **Command:**

    ```bash
    lscpu
    ```

- **Output:**

    ```text
    Architecture:           x86_64
    CPU op-mode(s):         32-bit, 64-bit
    Address sizes:          45 bits physical, 48 bits virtual
    Byte Order:             Little Endian
    CPU(s):                 2
    On-line CPU(s) list:    0,1
    Vendor ID:              AuthenticAMD
    Model name:             AMD Ryzen 5 5500U with Radeon Graphics
    ...
    Virtualization:         full
    Hypervisor:             VMware
    L1/L2/L3 Cache:         64 KiB / 1 MiB / 8 MiB
    NUMA Node:              1 (0,1)
    Vulnerabilities:        Multiple mitigated, some present
    ```

---

### 🔹 Step 3: Memory (RAM) Analysis

- **Command:**

    ```bash
    free -h
    ```

- **Output:**

    ```text
                  total        used        free      shared  buff/cache   available
    Mem:           1.7Gi       1.2Gi       260Mi        13Mi       401Mi       482Mi
    Swap:          2.0Gi       6.0Mi       2.0Gi
    ```

---

### 🔹 Step 4: Storage Analysis

- **Command:**

    ```bash
    df -h
    ```

- **Output:**

    ```text
    Filesystem             Size  Used Avail Use% Mounted on
    devtmpfs               4.0M     0  4.0M   0% /dev
    tmpfs                  870M     0  870M   0% /dev/shm
    tmpfs                  348M  1.5M  347M   1% /run
    /dev/mapper/rhel-root   17G  5.1G   12G  31% /
    /dev/nvme0n1p2        1014M  405M  610M  40% /boot
    /dev/nvme0n1p1         599M  7.1M  592M   2% /boot/efi
    /dev/sr0               110M  110M     0 100% /run/media/shahid/CDROM
    /dev/sr1               9.0G  9.0G     0 100% /run/media/shahid/RHEL-9-2-0-BaseOS-x86_64
    ```

---

## 🔎 4. Observations & Analysis

> *(Translate the raw output into structured, human-readable insights. You can complete the statements.)*

- ✅ The system is running **Red Hat Enterprise Linux 9** on a **64-bit x86_64** architecture.
- ✅ It is hosted on **VMware** (indicating virtualization).
- ✅ The CPU is an **AMD Ryzen 5 5500U**, supporting **hardware virtualization**.
- ✅ The system has **1.7 GiB RAM**, with **1.2 GiB in use**, and **2.0 GiB of swap**.
- ✅ Root partition `/` is **17 GiB total**, with **12 GiB available**.
- ✅ Two ISO devices are mounted, one being the **RHEL 9 installer**.

---

## ✅ 5. Conclusion

> *(Summarize what you’ve learned. You may write something like this.)*

This lab introduced the essentials of host-level system reconnaissance using built-in Linux tools. From a defender's perspective, knowing your hardware and software environment is foundational to security baselining and capacity planning. From an attacker’s perspective, such intel can reveal potential virtualization weaknesses, memory constraints, or OS fingerprinting opportunities.

---

## 🧠 6. Red/Blue Simulation (MITRE Mapping)

| Team | Technique | Tactic            | Tool Used  |
|------|-----------|-------------------|------------|
| Red  | T1082     | System Information Discovery | `uname`, `lscpu`, `free`, `df` |
| Blue | T1082.D   | Baseline Monitoring & Change Detection | SIEM parsing of system inventory |

---

## 📋 7. Checklist

- [x] Identified OS & kernel version  
- [x] Collected CPU architecture details  
- [x] Assessed RAM and Swap usage  
- [x] Mapped disk layout and usage  
- [x] Analyzed output for security insights  
- [ ] Logged results to GitHub Lab Journal

---

## 📝 8. Journaling & Confidence Meter

**Reflection Questions:**

- What would an attacker look for in this output?
- How would a defender use this info for baseline monitoring?

**Confidence Score:** `█ █ █ █ ░` (4/5)  
**Next Action:** Push this markdown log to your GitHub portfolio and continue to the next module in the Genesis Protocol.

---

## 🧭 9. Spaced Repetition Plan

| Day | Task                                |
|-----|-------------------------------------|
| 1   | Review system commands (`uname`, `lscpu`, etc.) |
| 3   | Re-run the lab on a new system or VM |
| 7   | Explain outputs to a peer or mentor |
| 30  | Apply recon in real-world troubleshooting |

---
