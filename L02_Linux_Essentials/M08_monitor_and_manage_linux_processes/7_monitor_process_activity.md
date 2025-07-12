````markdown
# 📈 Monitor Process Activity

## 1. 🧠 What Is It (Definition + Explanation)
* **Monitoring process activity** means observing the real-time behavior and performance of running processes on a system, including their resource usage (CPU, memory), I/O activity, and execution state.
* This is crucial for performance tuning, system auditing, incident response, and identifying rogue or malfunctioning programs.
* Common tools include `top`, `htop`, `ps`, `pidstat`, `vmstat`, and `iotop`.

---

## 2. 💡 Real-World Use Cases

* **Performance Troubleshooting** – Identify high CPU or memory-consuming processes.
* **Security Auditing** – Spot abnormal processes that may indicate malware.
* **Server Monitoring** – Track load, I/O usage, and process health in real-time.
* **System Hardening** – Observe unauthorized background tasks or suspicious behavior.
* **Incident Response** – Investigate processes during or after a compromise.

---

## 3. 💻 Examples

### 🔎 View Real-Time System Process Summary
```bash
top
````

* Use `Shift + P` to sort by CPU, `Shift + M` for memory.

---

### 🎛️ Interactive Process Viewer (Advanced)

```bash
htop
```

* Press `F6` to sort by different columns.
* Press `F9` to kill a process.

---

### 📄 Static Process Snapshot

```bash
ps aux
```

* Lists all processes with CPU, memory, and execution details.

---

### 📊 Monitor Specific Process I/O and CPU (pidstat)

```bash
pidstat -p <PID> 1
```

* Refreshes every second for selected process.

---

### 🔁 Monitor Disk I/O by Process (iotop)

```bash
sudo iotop
```

* Shows real-time disk I/O per process.

---

### 🧠 Get Memory Usage Summary (vmstat)

```bash
vmstat 1
```

* Displays memory, CPU, and swap activity per second.

---

## 4. 🧪 Lab Task (Hands-On Practice)

> ⚠️ **!! CRITICAL SAFETY WARNING !!:** Tasks **MUST ONLY** be done in safe, controlled environments (VMs, isolated labs), NEVER on real systems without explicit permission.

### 🎯 Objective:

Use multiple Linux tools to observe and analyze real-time process activity.

---

### 🧪 Step-by-Step:

#### 1. **Launch a Sample Process:**

```bash
yes > /dev/null &
```

#### 2. **Monitor with `top`:**

```bash
top
```

* Press `Shift + P` to sort by CPU usage.
* Press `k` to kill a process from within `top`.

#### 3. **Try `htop` (if installed):**

```bash
htop
```

* Use arrow keys to navigate and `F9` to kill.

#### 4. **Check all processes:**

```bash
ps aux --sort=-%mem | head -10
```

#### 5. **Monitor process CPU/I/O:**

```bash
pidstat -p <PID> 1
```

#### 6. **Track Disk I/O (optional):**

```bash
sudo iotop
```

#### 7. **Stop the test process:**

```bash
killall yes
```

---

## 5. 📋 Quiz (Knowledge Check)

1. What command provides a real-time overview of running processes?

   * A) ps
   * B) ls
   * C) top
   * D) df
     ✅ **Answer:** C
     *`top` gives a real-time display of system and process performance.*

---

2. Which tool provides a user-friendly interface for process management?

   * A) vmstat
   * B) ps
   * C) pidstat
   * D) htop
     ✅ **Answer:** D
     *`htop` is a full-screen interactive tool for monitoring and managing processes.*

---

3. What does `ps aux` display?

   * A) All user-installed software
   * B) File permissions
   * C) List of all current processes
   * D) Disk usage statistics
     ✅ **Answer:** C
     *It lists all currently running processes with details.*

---

4. What tool is best suited for monitoring per-process disk I/O?

   * A) top
   * B) iotop
   * C) kill
   * D) free
     ✅ **Answer:** B
     *`iotop` shows real-time disk read/write activity by process.*

---

5. What does `pidstat` primarily monitor?

   * A) Network traffic
   * B) File system permissions
   * C) CPU and I/O stats of specific PIDs
   * D) Installed packages
     ✅ **Answer:** C
     *`pidstat` reports statistics for specific processes, including CPU usage.*

---

## 6. 🚨 Common Mistakes

* **Misusing `ps` as a real-time tool**: It gives only a snapshot, not live updates.
* **Killing critical system processes** while trying to stop high-resource usage tasks.
* **Confusing PIDs with Job IDs** when monitoring or terminating.
* **Running `iotop` without `sudo`** – It may fail to show output.
* **Ignoring memory-hogging processes** that slowly consume all RAM.

---

## 7. ✨ Tips, Tricks, Best Practices

* Combine `ps aux --sort=-%cpu` or `--sort=-%mem` with `head` for quick high-usage listings.
* Use `htop` over `top` for color-coded, interactive process management.
* Use `watch -n 1 ps aux` for a dynamic view without `top`.
* Log resource usage to file using `pidstat > log.txt` for long-term analysis.
* Combine process monitoring with alerts (like `cron` + `mail` or `logwatch`).

---

## 8. ✅ Summary

* Monitoring process activity helps track CPU, memory, disk, and system usage.
* Tools include `top`, `htop`, `ps`, `pidstat`, `vmstat`, and `iotop`.
* `top` and `htop` offer live views; `ps` provides snapshots.
* Regular monitoring prevents performance issues and detects anomalies.
* Always verify high-usage processes before termination.

---

## 9. 🔗 Related Topics

* Process Management (`kill`, `pkill`, `jobs`)
* Linux Performance Tuning
* Security Auditing and Malware Detection
* Memory and CPU Usage Optimization
* Shell Scripting for Monitoring (`cron`, `logrotate`, `watch`)

```
```
