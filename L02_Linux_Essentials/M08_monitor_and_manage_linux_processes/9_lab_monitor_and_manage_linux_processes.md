````markdown
# 🧪 Lab: Monitor and Manage Linux Processes

## 1. 🧠 What Is It (Definition + Explanation)
* Monitoring and managing Linux processes involves **observing**, **controlling**, and **optimizing** the execution of programs (processes) running on a Linux system.
* This includes identifying running processes, analyzing their resource usage (CPU, memory, I/O), and managing their behavior using tools like `ps`, `top`, `htop`, `kill`, and `nice/renice`.

---

## 2. 💡 Real-World Use Cases
* **System Administration** – Detect and stop runaway or zombie processes.
* **Cybersecurity** – Identify suspicious or malicious processes.
* **DevOps Monitoring** – Ensure services/applications don’t overload system resources.
* **Performance Tuning** – Monitor and prioritize critical processes.
* **Scripting Automation** – Build scripts to monitor and terminate specific processes.

---

## 3. 💻 Examples

### 🔍 View All Running Processes
```bash
ps aux
````

### 🧠 Monitor in Real Time

```bash
top
```

### 🧠 Interactive Monitoring

```bash
htop
```

### 🧊 Stop or Kill Process

```bash
kill <PID>
kill -9 <PID>   # Forcefully kill
```

### 🔢 Sort Processes by Resource Usage

```bash
ps aux --sort=-%mem | head -5
```

### 🎯 Change Process Priority

```bash
nice -n 10 ./my_script.sh      # Start with lower priority
renice -n -5 -p <PID>          # Increase priority of existing process
```

---

## 4. 🧪 Lab Task (Hands-On Practice)

> ⚠️ **!! CRITICAL SAFETY WARNING !!:** Tasks **MUST ONLY** be done in safe, controlled environments (VMs, isolated labs), NEVER on real systems without explicit permission.

---

### 🎯 Lab Objective:

Use command-line tools to monitor, prioritize, and terminate Linux processes safely and efficiently.

---

## 🧪 Lab Setup Steps:

### 🔧 Step 1: Start a Simulated Process Load

```bash
yes > /dev/null &
stress --cpu 2 --timeout 60 &
```

> (Install stress tool with `sudo apt install stress -y` if needed)

---

### 🔎 Step 2: View and Analyze Processes

```bash
ps aux | head -5
```

```bash
top
```

```bash
htop   # Optional
```

* Sort by CPU or memory.
* Identify PIDs of the load-generating processes.

---

### ⚙️ Step 3: Adjust Process Priorities

#### A) Launch a new process with lower priority:

```bash
nice -n 15 sleep 300 &
```

#### B) Increase priority (lower nice value) of a running process:

```bash
sudo renice -n -5 -p <PID>
```

---

### 🛑 Step 4: Kill Processes Safely

1. List all `yes` processes:

```bash
ps aux | grep yes
```

2. Kill them:

```bash
killall yes
```

3. Force kill if needed:

```bash
kill -9 <PID>
```

---

### 🔁 Step 5: Use `pidstat` to Monitor a Specific PID

```bash
sudo apt install sysstat -y
pidstat -p <PID> 1
```

---

### 📊 Step 6: Optional - Monitor I/O

```bash
sudo iotop
```

---

## ✅ Post-Lab Checklist

✅ Launched and monitored high-load processes
✅ Identified and analyzed CPU/memory usage
✅ Changed process priority using `nice` and `renice`
✅ Terminated processes using `kill` and `killall`
✅ Used `ps`, `top`, `htop`, `pidstat`, and `iotop`

---

## 5. 📋 Quiz (Knowledge Check)

1. What command shows a static snapshot of all current processes?

   * A) top
   * B) ps aux
   * C) kill
   * D) jobs
     ✅ **Answer:** B
     *`ps aux` shows all running processes with their details.*

---

2. How do you forcefully kill a process by PID?

   * A) kill -1 PID
   * B) kill PID
   * C) kill -9 PID
   * D) pkill PID
     ✅ **Answer:** C
     *`kill -9` sends SIGKILL, forcefully ending the process.*

---

3. Which command allows changing the priority of a running process?

   * A) nice
   * B) renice
   * C) top
   * D) iotop
     ✅ **Answer:** B
     *`renice` modifies the nice value of already-running processes.*

---

4. What is the purpose of the `nice` command?

   * A) List all running processes
   * B) Start a process with lower or higher priority
   * C) Terminate all processes
   * D) Make your shell look colorful
     ✅ **Answer:** B
     *`nice` starts a new process with a specified scheduling priority.*

---

5. What tool allows monitoring real-time I/O usage by process?

   * A) ps
   * B) top
   * C) iotop
   * D) vmstat
     ✅ **Answer:** C
     *`iotop` shows real-time disk I/O per process.*

---

## 6. 🚨 Common Mistakes

* **Killing critical system processes** like `init`, `systemd`, or `sshd`.
* **Misusing `kill -9`** without trying `kill` (SIGTERM) first.
* **Incorrect PID usage** — confusing with Job IDs (`%1`).
* **Not using `sudo`** where required (`iotop`, `renice`, etc.).
* **Forgetting to clean up background processes** after monitoring.

---

## 7. ✨ Tips, Tricks, Best Practices

* Use `top`/`htop` to monitor, then `kill`/`renice` intelligently.
* Use `ps aux --sort=-%cpu` to catch greedy processes quickly.
* Log monitoring data using `pidstat > log.txt`.
* Avoid overusing `kill -9`; prefer graceful exits for stability.
* Monitor and script with `watch` + `ps` for automation.

---

## 8. ✅ Summary

* You can **monitor**, **adjust**, and **terminate** processes using built-in Linux tools.
* Use `ps`, `top`, `htop`, `pidstat`, `iotop`, and process control commands (`kill`, `nice`, `renice`).
* Be careful when handling processes; some are critical to system stability.
* Real-time monitoring supports both performance tuning and cybersecurity.

---

## 9. 🔗 Related Topics

* Linux Signals & Process Lifecycle
* Job Control (`fg`, `bg`, `jobs`)
* Shell Scripting with Monitoring
* Cron-Based System Health Checks
* System Performance Analysis (SAR, vmstat)

---

Would you like to integrate this lab into a **custom shell script** to automatically monitor and kill high-resource processes? 🚀

```
```
