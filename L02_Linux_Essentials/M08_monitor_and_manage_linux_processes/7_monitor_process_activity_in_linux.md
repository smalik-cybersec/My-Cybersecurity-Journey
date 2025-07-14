# 📊 **Lesson: Monitor Process Activity in Linux**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 257*

---

## 📚 Table of Contents

- [📊 **Lesson: Monitor Process Activity in Linux**](#-lesson-monitor-process-activity-in-linux)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [🧠 Why Monitor Process Activity?](#-why-monitor-process-activity)
  - [📋 Tools to Monitor Processes](#-tools-to-monitor-processes)
  - [🔎 Using `ps` – Static Snapshot](#-using-ps--static-snapshot)
    - [🔸 Basic Usage](#-basic-usage)
    - [🔸 View All Processes](#-view-all-processes)
    - [🔸 Custom Output](#-custom-output)
  - [📈 Using `top` – Dynamic Monitor](#-using-top--dynamic-monitor)
    - [Key Features](#key-features)
    - [Sample Output Columns](#sample-output-columns)
  - [📊 Using `htop` – Enhanced Interactive Monitor](#-using-htop--enhanced-interactive-monitor)
    - [Features Over `top`](#features-over-top)
  - [🔍 Other Useful Tools](#-other-useful-tools)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 🎯 Introduction

Monitoring process activity is essential for:

- Identifying CPU- or memory-intensive tasks
- Investigating system slowness or bottlenecks
- Troubleshooting stuck or zombie processes
- Verifying the health of system and user services

> Linux offers powerful tools like `ps`, `top`, and `htop` for **real-time and static monitoring**.

---

## 🧠 Why Monitor Process Activity?

| Purpose                           | Benefit                       |
| --------------------------------- | ----------------------------- |
| Detect high CPU or memory usage   | Optimize performance          |
| Spot zombie or stuck processes    | Ensure system stability       |
| Track unauthorized activity       | Improve system security       |
| Monitor long-running scripts/apps | Verify runtime and efficiency |

---

## 📋 Tools to Monitor Processes

| Tool    | Type     | Description                                  |
| ------- | -------- | -------------------------------------------- |
| `ps`    | Snapshot | Lists current processes at a single point    |
| `top`   | Dynamic  | Real-time process monitor with live stats    |
| `htop`  | Dynamic  | Interactive, colorful, and user-friendly top |
| `pgrep` | Search   | Filters process list by name or pattern      |
| `pidof` | Lookup   | Returns PID of a specific running process    |

---

## 🔎 Using `ps` – Static Snapshot

The `ps` command captures a **one-time snapshot** of all running processes.

### 🔸 Basic Usage

```bash
ps
```

### 🔸 View All Processes

```bash
ps aux
```

| Flag | Meaning                                 |
| ---- | --------------------------------------- |
| `a`  | All users                               |
| `u`  | Show user/CPU/mem columns               |
| `x`  | Show processes not attached to terminal |

### 🔸 Custom Output

```bash
ps -eo pid,ppid,stat,%cpu,%mem,cmd --sort=-%cpu
```

✅ Sorts processes by CPU usage

---

## 📈 Using `top` – Dynamic Monitor

`top` gives a **live, updating** view of system and process activity.

```bash
top
```

### Key Features

- Sort by CPU or memory
- Press `k` to kill a process
- Press `r` to renice (change priority)
- Press `q` to quit

### Sample Output Columns

| Column    | Description              |
| --------- | ------------------------ |
| `PID`     | Process ID               |
| `%CPU`    | CPU usage                |
| `%MEM`    | Memory usage             |
| `TIME+`   | Total CPU time           |
| `COMMAND` | The command/process name |

---

## 📊 Using `htop` – Enhanced Interactive Monitor

> Requires installation: `sudo apt install htop` or `sudo yum install htop`

```bash
htop
```

### Features Over `top`

- Color-coded bars
- Scrollable interface
- Use arrow keys to navigate
- Press `F9` to kill a process
- Press `F6` to sort columns

---

## 🔍 Other Useful Tools

| Tool                         | Description                         |
| ---------------------------- | ----------------------------------- |
| `pgrep nginx`                | Returns PID of process by name      |
| `pidof firefox`              | Quick PID lookup by exact name      |
| `watch ps aux`               | Updates `ps` output every 2 seconds |
| `vmstat`, `iostat`, `mpstat` | Advanced system-level metrics       |

---

## 🧠 Quiz Yourself

1. What’s the difference between `ps` and `top`?
2. How do you sort `ps` output by CPU usage?
3. Which tool offers a color-coded, interactive interface?
4. What key in `top` lets you kill a process?
5. How do you list all currently running processes with full details?

---

## 📎 Summary

- Use `ps` for **snapshot** process reporting
- Use `top` or `htop` for **live system monitoring**
- Monitor CPU, memory, and runtime usage for each process
- Tools like `pgrep` and `pidof` help identify PIDs quickly
- Mastering these tools is essential for performance tuning, process debugging, and operational visibility