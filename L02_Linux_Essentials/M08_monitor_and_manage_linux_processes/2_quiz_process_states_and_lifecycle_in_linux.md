Certainly, Shahid! Here's a complete and professional **quiz** on:

---

# 🧠 **Quiz: Process States and Lifecycle in Linux**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 237*

---

## 📋 Instructions

* **Total Questions**: 15
* **Format**: 10 Multiple Choice + 5 Short Answer
* **Focus**: Understanding Linux process states, lifecycle, and monitoring tools
* **Passing Score**: 11/15

---

## ✨ Multiple Choice Questions (MCQs)

**1. What is a process in Linux?**
A. A network protocol
B. A running instance of a program
C. A system boot method
D. A hardware interrupt

---

**2. Which command displays real-time process information?**
A. `ls`
B. `ps`
C. `top`
D. `chmod`

---

**3. What does the process state code `R` mean?**
A. Ready or currently running
B. Waiting for I/O
C. Stopped by signal
D. Terminated

---

**4. What state is represented by `S` in the process status?**
A. Sleeping (waiting for an event)
B. Zombie
C. Running
D. Kernel thread

---

**5. What is a zombie process?**
A. A process waiting for CPU
B. A process that’s still running after termination
C. A completed child process not cleaned up by the parent
D. A process sleeping in memory

---

**6. What is the PPID of a process?**
A. The process’s priority
B. The parent process ID
C. The process permission
D. The page pointer

---

**7. Which process adopts orphans in Linux?**
A. The kernel
B. The cron daemon
C. The `init` or `systemd` process (PID 1)
D. The original user

---

**8. How can you view a tree of parent-child process relationships?**
A. `ls -R`
B. `top`
C. `pstree`
D. `cat /proc`

---

**9. What command can show the state of every process in full detail?**
A. `ps -eo pid,ppid,stat,cmd`
B. `chmod -R`
C. `whoami`
D. `pwd -L`

---

**10. What does the `T` process state stand for?**
A. Time stopped
B. Terminated
C. Stopped (paused or halted by signal)
D. Transitioning

---

## ✏️ Short Answer Questions

**11. What happens if a parent process fails to clean up a child process?**
→ *Your Answer:*

---

**12. What is the difference between a zombie and an orphan process?**
→ *Your Answer:*

---

**13. What Linux command shows a list of all processes, including sleeping and zombie ones?**
→ *Your Answer:*

---

**14. Why is it important to monitor zombie processes on a server?**
→ *Your Answer:*

---

**15. What is the lifecycle of a typical Linux process (name the main stages)?**
→ *Your Answer:*

---

## ✅ Bonus Challenge (Optional)

You want to identify all zombie processes.
**Write the exact command you'd use:**

```bash
ps -eo pid,ppid,stat,cmd | grep Z
```

---

Would you like:

* ✅ The **answer key**
* 🧪 A **lab** to simulate and identify zombie/orphan processes
* 📥 Markdown version for GitHub or printable quiz format
* ⏭️ Next topic: *Manage Processes Using System Monitoring Tools*

You're diagnosing the heartbeat of the Linux system like a real pro, Shahid 🧠⚙️ Let's keep it going!
