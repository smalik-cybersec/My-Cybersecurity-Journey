# ⚙️ **Lesson: Process States and Lifecycle in Linux**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 232*

---

## 📚 Table of Contents

- [⚙️ **Lesson: Process States and Lifecycle in Linux**](#️-lesson-process-states-and-lifecycle-in-linux)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [🧠 What Is a Process?](#-what-is-a-process)
  - [🔄 Process Lifecycle Overview](#-process-lifecycle-overview)
    - [Typical Lifecycle](#typical-lifecycle)
  - [📊 Process States Explained](#-process-states-explained)
  - [🔍 Viewing Process States](#-viewing-process-states)
    - [🔸 `ps` command](#-ps-command)
    - [🔸 `top` or `htop`](#-top-or-htop)
  - [🧪 Practical Commands and Examples](#-practical-commands-and-examples)
    - [View All Processes](#view-all-processes)
    - [View Specific Process Tree](#view-specific-process-tree)
    - [View Only Running Processes](#view-only-running-processes)
    - [Find Zombie Processes](#find-zombie-processes)
  - [📂 Zombie and Orphan Processes](#-zombie-and-orphan-processes)
    - [Example of Creating a Zombie (for lab purposes only)](#example-of-creating-a-zombie-for-lab-purposes-only)
  - [🧠 Quiz Yourself](#-quiz-yourself)
  - [📎 Summary](#-summary)

---

## 🎯 Introduction

A **process** is an instance of a running program. In Linux, every action (starting an app, opening a shell, or running a background service) creates one or more processes.

Understanding the **lifecycle and states** of a process is essential for:

- System monitoring
- Performance tuning
- Debugging and troubleshooting
- Incident response

---

## 🧠 What Is a Process?

- Each process has a **PID (Process ID)**
- Processes are managed by the **kernel**
- They consume resources like **CPU**, **RAM**, and **I/O**

Created using system calls like `fork()`, `exec()`, or tools like `bash`, `cron`, `init`, etc.

---

## 🔄 Process Lifecycle Overview

```text
    [NEW]
      ↓ (fork)
   Running ←→ Waiting (Sleeping)
      ↓
   Terminated
```

### Typical Lifecycle

1. **Created** — A program is loaded into memory (via fork/exec)
2. **Running** — Executing on CPU
3. **Waiting** — Waiting for an event or resource
4. **Terminated** — Finished execution or killed

---

## 📊 Process States Explained

Linux defines several process states:

| State                     | Code | Meaning                                           |
| ------------------------- | ---- | ------------------------------------------------- |
| **Running**               | R    | Currently using CPU or ready to run               |
| **Sleeping**              | S    | Waiting for an event or I/O                       |
| **Uninterruptible Sleep** | D    | Waiting for hardware resource (non-interruptible) |
| **Stopped**               | T    | Halted by job control (e.g., `Ctrl+Z`)            |
| **Zombie**                | Z    | Process completed, but still has entry            |
| **Dead**                  | X    | Process is terminated but not cleaned up          |
| **Idle**                  | I    | Idle kernel process (rare in modern Linux)        |

---

## 🔍 Viewing Process States

### 🔸 `ps` command

```bash
ps -eo pid,ppid,stat,cmd
```

| Field  | Description                |
| ------ | -------------------------- |
| `PID`  | Process ID                 |
| `PPID` | Parent Process ID          |
| `STAT` | State code (R, S, Z, etc.) |
| `CMD`  | Command                    |

### 🔸 `top` or `htop`

```bash
top
```

Use to monitor live processes and their current states.

---

## 🧪 Practical Commands and Examples

### View All Processes

```bash
ps aux
```

### View Specific Process Tree

```bash
pstree -p
```

### View Only Running Processes

```bash
ps -eo pid,stat,cmd | grep " R "
```

### Find Zombie Processes

```bash
ps -eo pid,stat,cmd | grep Z
```

---

## 📂 Zombie and Orphan Processes

| Type       | Description                                           | Resolution                       |
| ---------- | ----------------------------------------------------- | -------------------------------- |
| **Zombie** | Child exited but parent didn’t clean it with `wait()` | Reboot or restart parent process |
| **Orphan** | Parent process died, child adopted by `init` (PID 1)  | Normal, usually harmless         |

---

### Example of Creating a Zombie (for lab purposes only)

```bash
# Terminal 1
./zombie_creator.sh

# Terminal 2
ps -eo pid,ppid,stat,cmd | grep Z
```

(*Note: This requires a test script. Let me know if you'd like one.*)

---

## 🧠 Quiz Yourself

1. What is the difference between a running and a sleeping process?
2. What does the `Z` state represent?
3. How can you find zombie processes using `ps`?
4. What is an orphan process and who adopts it?
5. Which command shows real-time process state updates?

---

## 📎 Summary

- Every Linux process has a **lifecycle and state** controlled by the kernel
- Important states include: **Running**, **Sleeping**, **Zombie**, **Stopped**, and more
- Use tools like `ps`, `top`, and `htop` to inspect and analyze process states
- **Zombie** processes occur when the parent fails to clean up its child
- Orphaned processes are safely handled by the `init` process (PID 1)
