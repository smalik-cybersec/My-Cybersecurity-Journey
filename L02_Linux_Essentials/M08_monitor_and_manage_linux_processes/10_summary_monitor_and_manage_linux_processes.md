# 📎 **Summary: Monitor and Manage Linux Processes**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 266*

---

## 📖 Overview

In this lesson, you learned how to **monitor, manage, and control Linux processes** using both **real-time** and **snapshot-based** tools. You explored commands like `ps`, `top`, `htop`, `kill`, `pkill`, and `nice/renice` to observe process activity and intervene when needed.

---

## 🔍 Key Concepts

### 🔸 What Is a Process?

A **process** is an instance of a running program, managed by the Linux kernel. Every process has:

* A **PID** (Process ID)
* A **PPID** (Parent PID)
* A state (Running, Sleeping, Zombie, etc.)

---

## 🛠️ Tools You Learned

| Tool      | Description                                        |
| --------- | -------------------------------------------------- |
| `ps`      | Displays a snapshot of all current processes       |
| `top`     | Real-time process monitoring and sorting           |
| `htop`    | Enhanced interactive version of `top` (color UI)   |
| `jobs`    | Manages foreground/background jobs in the shell    |
| `kill`    | Sends signals to processes using PID               |
| `pkill`   | Kills processes by name/pattern                    |
| `killall` | Kills all processes with a given exact name        |
| `nice`    | Starts a process with a specific priority          |
| `renice`  | Changes the priority of an already running process |

---

## 📊 Monitoring Techniques

| Method     | Use Case                                  |
| ---------- | ----------------------------------------- |
| `ps aux`   | View all running processes (static view)  |
| `top`      | Monitor live CPU and memory usage         |
| `htop`     | Interactive process control with sorting  |
| `watch ps` | Auto-refresh output of `ps` every few sec |

---

## 🧠 Process Control Techniques

| Command                | Purpose                                   |
| ---------------------- | ----------------------------------------- |
| `Ctrl + Z`             | Suspend a foreground job                  |
| `bg %1`                | Resume suspended job in background        |
| `fg %1`                | Bring background job to foreground        |
| `kill -9 <PID>`        | Forcefully terminate a process            |
| `pkill sleep`          | Kill all matching processes by name       |
| `renice -n 5 -p <PID>` | Change CPU priority (lower = higher prio) |

---

## 🧩 Job vs. Process

| Job (Shell-managed)             | Process (Kernel-managed)         |
| ------------------------------- | -------------------------------- |
| Identified with `%1`, `%2`      | Identified by numeric PID        |
| Managed with `fg`, `bg`, `jobs` | Managed with `kill`, `ps`, `top` |

---

## 🔐 Why This Matters in Cybersecurity & Admin Work

* Detect **suspicious or rogue processes**
* Terminate **malware or reverse shells**
* Monitor **resource usage and bottlenecks**
* Ensure **critical services are alive**
* Improve system **performance and uptime**

---

## ✅ You Can Now

* 🔍 Monitor process activity live and statically
* 🚦 Suspend, resume, and terminate processes
* 🧠 Identify resource hogs using memory/CPU stats
* 🎛️ Adjust process priorities with `nice` and `renice`
* 🔒 Control processes safely using best practices

---

> ✅ **Pro Tip:** Always try `kill -15` (graceful) before using `kill -9` (force).

---
