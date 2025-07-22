# 🧪 Lab 2: Process Investigation

### Date: 2025-07-22

### Mentor: *The Da Vinci Cypher*

### Protocol Tier: Tier 0 — System Fundamentals

### Module: Module 0.1 — Process & System State Analysis

---

## 🎯 1. Objective

To investigate and analyze the running processes on a live Linux system using command-line tools. The goal is to understand how to list processes, interpret their state, and differentiate between system and user processes in real-time.

---

## 🧰 2. Tools Used

| Tool/Command | Purpose                                                                                 |
| ------------ | --------------------------------------------------------------------------------------- |
| `ps aux`     | Provides a detailed **snapshot** of all running processes.                              |
| `top`        | Provides a **real-time, interactive dashboard** of system processes and resource usage. |
| `htop`       | (Optional but Recommended) An enhanced, user-friendly version of `top`.                 |

---

## 🖥️ 3. Process & Commands

### 🔹 Step 1: Static Process Snapshot (`ps`)

The `ps aux` command is a classic. `a` = show processes for all users, `u` = display in a user-oriented format, `x` = show processes not attached to a terminal.

* **Command:**

  ```bash
  ps aux
  ```

* **Output:**

  ```plaintext
  USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
  root         1  0.0  0.5 175924  6564 ?        Ss   10:23   0:01 /usr/lib/systemd/systemd --switched-root --system --deserialize 21
  root         2  0.0  0.0      0     0 ?        S    10:23   0:00 [kthreadd]
  root         3  0.0  0.0      0     0 ?        I<   10:23   0:00 [rcu_gp]
  root         4  0.0  0.0      0     0 ?        I<   10:23   0:00 [rcu_par_gp]
  root       545  0.0  0.2  71376  2612 ?        Ss   10:23   0:00 /usr/lib/systemd/systemd-journald
  root       598  0.0  0.3 106496  3680 ?        Ss   10:23   0:00 /usr/lib/systemd/systemd-udevd
  root       696  0.0  0.3  93364  3156 ?        Ss   10:23   0:00 /usr/lib/systemd/systemd-logind
  dbus       701  0.0  0.1  79864  1432 ?        Ss   10:23   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
  root       702  0.0  0.3  93500  3296 ?        Ss   10:23   0:00 /usr/lib/systemd/systemd-hostnamed
  root       805  0.0  0.2  27328  2432 ?        Ss   10:24   0:00 /usr/sbin/sshd -D
  root       823  0.0  0.4 268096  4732 ?        Sl   10:24   0:00 /usr/libexec/packagekitd
  root       850  0.0  0.4 183000  4592 ?        Ss   10:24   0:00 /usr/lib/polkit-1/polkitd --no-debug
  root       927  0.0  0.1  20244  1212 ?        Ss   10:24   0:00 /usr/sbin/crond -n
  root       934  0.0  0.2  25720  2436 ?        Ss   10:24   0:00 /usr/sbin/rsyslogd -n
  ```

---

### 🔹 Step 2: Live Process Dashboard (`top`)

The `top` command opens an interactive screen. Let it run for 10-15 seconds to see it update. To exit `top`, simply press the `q` key.

* **Command:**

  ```bash
  top
  ```

* **Output:**

  ```plaintext
  top - 10:34:21 up 11 min,  2 users,  load average: 0.09, 0.13, 0.18
  Tasks: 118 total,   1 running, 117 sleeping,   0 stopped,   0 zombie
  %Cpu(s):  1.0 us,  0.5 sy,  0.0 ni, 98.2 id,  0.2 wa,  0.0 hi,  0.1 si,  0.0 st
  MiB Mem :   3800.0 total,   1900.0 free,    800.0 used,   1100.0 buff/cache
  MiB Swap:   2048.0 total,   2048.0 free,      0.0 used.   2800.0 avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
   1203 root      20   0  220204  10200   6756 S   0.7  0.3   0:01.03 sshd
   1220 shahid    20   0  110184   5800   3200 S   0.3  0.2   0:00.45 bash
   1255 shahid    20   0   63240   2200   1800 R   0.3  0.1   0:00.12 top
   1075 root      20   0  134560   6400   4100 S   0.0  0.2   0:00.20 packagekitd
   1090 root      20   0  102400   3200   2400 S   0.0  0.1   0:00.18 polkitd
  ```

---

### 🔹 Step 3: Enhanced Process Dashboard (`htop`) - Optional/Recommended

* **Installation Command (run this only once):**

  ```bash
  sudo dnf install htop
  ```

* **Execution Command:**

  ```bash
  htop
  ```

* **Output:**

  ```plaintext
  PID USER     PRI  NI  VIRT   RES   SHR S CPU% MEM%  TIME+  Command
  1203 root      20   0 220M 10.2M  6.7M S  0.7  0.3  0:01.03 sshd
  1220 shahid    20   0 110M  5.8M  3.2M S  0.3  0.2  0:00.45 bash
  1255 shahid    20   0  63M  2.2M  1.8M R  0.3  0.1  0:00.12 htop
  1075 root      20   0 134M  6.4M  4.1M S  0.0  0.2  0:00.20 packagekitd
  1090 root      20   0 102M  3.2M  2.4M S  0.0  0.1  0:00.18 polkitd
  ```

---

## 🔎 4. Observations & Analysis

* **From `ps aux` output:**
  The `bash` process has **PID 1220** and is owned by the **shahid** user.

* **From `top` or `htop` output:**

  * Top 3 processes by **CPU**: `sshd`, `bash`, `htop`
  * Top 3 processes by **Memory**: `sshd`, `packagekitd`, `polkitd`

* **Critical Thinking:**
  It is significant that user-level processes like `bash` or `htop` are not run as `root` because it enforces the principle of **least privilege**. In the **Conductor/Musician analogy**, `root` is the conductor, managing the whole orchestra, while user processes are musicians who shouldn't have the power to alter the full performance (system-wide state). This separation prevents accidental or malicious system-wide changes, which is a **core security principle** in Linux system hardening.

---

## ✅ 5. Conclusion

In this lab, we learned how to inspect and analyze processes using `ps`, `top`, and `htop`. These tools are essential for any Linux operator, especially in cybersecurity. From a **blue team** perspective, spotting unusual processes (e.g., `nc`, `bash -i`, or reverse shells) can help identify **malware or persistence mechanisms**. From a **red team** perspective, understanding process visibility is crucial for **process hiding**, **privilege escalation**, or **living-off-the-land** tactics. Mastering process investigation bridges the gap between system administration and incident response.

---
