# 🧪 **Lab: Monitor and Manage Linux Processes**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 266*

---

## 🎯 Objective

In this lab, you will practice:

* Monitoring process activity using `ps`, `top`, and `htop`
* Identifying high resource-consuming processes
* Managing (pausing, resuming, terminating) processes
* Using tools like `kill`, `pkill`, `killall`, and `nice`/`renice` for process control

> This lab brings together everything you’ve learned about **monitoring**, **managing**, and **controlling** Linux processes in real time and statically.

---

## 🧰 Requirements

* A Linux system (VM, WSL, or native install)
* Terminal access with user privileges
* Optional: GUI apps like `gedit`, or access to `htop` (install if needed)

---

## 🧭 Step-by-Step Instructions

---

### 🔹 **Step 1: Launch Test Processes**

Run a few dummy processes in the background:

```bash
sleep 600 &
sleep 900 &
gedit &           # If GUI is available
```

✅ Use `jobs` to confirm background jobs:

```bash
jobs
```

---

### 🔹 **Step 2: Monitor Processes with `ps`**

```bash
ps aux
```

Search for specific processes:

```bash
ps aux | grep sleep
```

Filter and sort by CPU usage:

```bash
ps -eo pid,ppid,%cpu,%mem,stat,cmd --sort=-%cpu | head -10
```

---

### 🔹 **Step 3: Live Monitoring with `top`**

```bash
top
```

In `top`:

* Press `P` → Sort by CPU usage
* Press `M` → Sort by memory
* Press `k` → Enter PID to kill
* Press `r` → Enter PID to renice (change priority)
* Press `q` → Exit

✅ Note high-usage or zombie (`Z`) processes, if any.

---

### 🔹 **Step 4: Use `htop` (Optional but Recommended)**

Install and run:

```bash
sudo apt install htop       # For Debian/Ubuntu
sudo yum install htop       # For RHEL/CentOS
htop
```

In `htop`:

* Use arrow keys to navigate
* Use `F6` to sort
* Use `F9` to kill
* Use `F3` to search
* Use `F10` to quit

---

### 🔹 **Step 5: Pause, Resume, and Kill Jobs**

#### Suspend a job (foreground process)

```bash
Ctrl + Z
```

#### Resume job in background

```bash
bg %1
```

#### Resume job in foreground

```bash
fg %1
```

#### Kill a process by PID

```bash
kill -9 <PID>
```

#### Kill all `sleep` processes

```bash
pkill sleep
```

---

### 🔹 **Step 6: Change Process Priority**

Start a new process with lower priority:

```bash
nice -n 10 sleep 400 &
```

Change priority of an existing process:

```bash
renice -n 5 -p <PID>
```

✅ Check impact in `top` or `htop`.

---

## 📂 Final Commands Used

```bash
sleep 600 &
ps aux
ps -eo pid,%cpu,%mem,cmd --sort=-%cpu
top
htop
kill -9 <PID>
pkill sleep
renice -n 5 -p <PID>
nice -n 10 sleep 400 &
```

---

## 🧠 Reflection Questions

1. What’s the benefit of using `htop` over `top`?
2. How do you kill a process if you don’t know the PID?
3. What’s the effect of using `nice` with a higher value?
4. What command pauses a foreground job?
5. How can you change a running process’s CPU priority?

---

## ✅ Completion Checklist

| Task                                              | Status |
| ------------------------------------------------- | ------ |
| Started multiple background processes             | ✅      |
| Monitored processes using `ps`, `top`, and `htop` | ✅      |
| Killed and resumed jobs                           | ✅      |
| Used `kill`, `pkill`, and `killall`               | ✅      |
| Changed process priority with `nice` and `renice` | ✅      |
| Verified CPU/memory usage in real time            | ✅      |

---

## 📎 Summary

You now know how to:

* Monitor live and snapshot views of Linux processes
* Identify and manage heavy or suspicious processes
* Safely suspend, resume, and terminate processes
* Adjust process priorities to manage CPU usage
* Use both command-line and interactive tools (`top`, `htop`, `ps`, `kill`, etc.)

> This lab strengthens your command over the **Linux process management toolkit** — a critical skill for performance tuning, system recovery, and admin excellence.
