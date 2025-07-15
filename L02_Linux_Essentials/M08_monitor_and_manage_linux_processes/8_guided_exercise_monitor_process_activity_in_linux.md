# 🧪 **Guided Exercise: Monitor Process Activity in Linux**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 261*

---

## 🎯 Objective

In this hands-on lab, you’ll learn to:

* Monitor active processes using `ps`, `top`, and `htop`
* Sort and filter process information by CPU, memory, and PID
* Observe process behavior in real time
* Identify processes consuming excessive resources

> Mastering process monitoring helps you troubleshoot performance issues, detect anomalies, and maintain system health.

---

## 🧰 Requirements

* A Linux terminal (local machine, VM, or WSL)
* A regular user account (e.g., `shahid`)
* Optional: Install `htop` (for enhanced visualization)

---

## 🧭 Step-by-Step Lab Instructions

---

### 🔹 **Step 1: Use `ps` to View a Static Snapshot of Processes**

```bash
ps
```

✅ Shows only your current shell and related processes.

Now list **all running processes**:

```bash
ps aux
```

✅ You’ll see output like:

```bash
USER   PID  %CPU %MEM  VSZ   RSS   TTY  STAT  START  TIME  COMMAND
```

---

### 🔹 **Step 2: Sort Processes by CPU or Memory**

```bash
ps -eo pid,ppid,stat,%cpu,%mem,cmd --sort=-%cpu
```

✅ This lists all processes sorted by CPU usage (descending). You can change to memory by using `--sort=-%mem`.

---

### 🔹 **Step 3: Monitor Processes Dynamically with `top`**

```bash
top
```

### While inside `top`

* Press `P` → Sort by CPU
* Press `M` → Sort by memory
* Press `k` → Kill a process by PID
* Press `r` → Renice (change priority)
* Press `q` → Quit

✅ Try observing which process is using the most CPU.

---

### 🔹 **Step 4: Use `htop` (if installed)**

```bash
htop
```

> If not installed, run:

```bash
sudo apt install htop    # Debian/Ubuntu  
sudo yum install htop    # RHEL/CentOS  
```

### In `htop`, try

* Arrow keys → Navigate
* `F6` → Sort by different columns
* `F9` → Kill selected process
* `F3` → Search for a process
* `F10` → Quit

✅ Notice how much easier it is to interact with processes using `htop`.

---

### 🔹 **Step 5: Watch a Repeating Command with `watch`**

```bash
watch -n 2 'ps -eo pid,ppid,stat,%cpu,%mem,cmd --sort=-%cpu | head -10'
```

✅ This command refreshes every 2 seconds, showing top 10 CPU-consuming processes.

---

## 🧪 Bonus: Monitor a Specific Application

Start a long-running dummy process:

```bash
sleep 300 &
```

Use:

```bash
ps aux | grep sleep
```

Then monitor it with:

```bash
top
```

✅ Observe how it uses almost no CPU but remains active in memory.

---

## 📂 Final Commands Practiced

```bash
ps
ps aux
ps -eo pid,ppid,stat,%cpu,%mem,cmd --sort=-%cpu
top
htop
watch -n 2 'ps -eo pid,ppid,%cpu,%mem,cmd --sort=-%cpu | head -10'
```

---

## 🧠 Reflection Questions

1. What’s the difference between `ps` and `top`?
2. Why might `htop` be preferred over `top`?
3. How do you kill a process from `top` or `htop`?
4. What command allows you to sort `ps` output by CPU?
5. How can you continuously monitor process usage in real-time?

---

## ✅ Completion Checklist

| Task                                                 | Status |
| ---------------------------------------------------- | ------ |
| Viewed all processes with `ps aux`                   | ✅      |
| Sorted processes by CPU/memory usage                 | ✅      |
| Monitored activity live with `top`                   | ✅      |
| Installed and used `htop` (optional but recommended) | ✅      |
| Used `watch` to refresh command output continuously  | ✅      |
| Observed real process behavior                       | ✅      |

---

## 📎 Summary

You now have hands-on experience with:

* Monitoring current and real-time process activity
* Identifying CPU- and memory-hogging processes
* Navigating and using `ps`, `top`, `htop`, and `watch` effectively
* Using these tools as part of **system administration and performance tuning**

> This lab reinforces your ability to **analyze**, **optimize**, and **troubleshoot** Linux systems based on live process behavior.
