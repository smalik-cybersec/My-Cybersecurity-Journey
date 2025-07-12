# 🧠 Quiz: Process States and Lifecycle

## 📋 Quiz (Knowledge Check)

Test your understanding of **Process States and Lifecycle** with the following multiple-choice questions. Each question includes the correct answer and a short explanation.

---

### 1. **Which of the following states means a process is currently executing on the CPU?**

* A) Ready
* B) Waiting
* C) Running
* D) Terminated
  ✅ **Answer:** C
  *The "Running" state indicates the process is actively executing on the CPU.*

---

### 2. **What does a zombie process represent?**

* A) A background daemon
* B) A process waiting for I/O
* C) A process terminated but not reaped by the parent
* D) A hidden malicious process
  ✅ **Answer:** C
  *A zombie process has finished execution, but the parent process has not yet retrieved its exit status.*

---

### 3. **Which of the following best describes the "Waiting" (or "Blocked") state?**

* A) Process has been killed
* B) Process is waiting for a resource or event
* C) Process is being scheduled
* D) Process is executing user instructions
  ✅ **Answer:** B
  *A process in the waiting/blocked state is paused until some condition (like I/O completion) is met.*

---

### 4. **What does the state code `Z` represent in Linux process management?**

* A) Zombie
* B) Sleeping
* C) Stopped
* D) Running
  ✅ **Answer:** A
  *The `Z` code in `ps` or `top` output stands for a zombie process.*

---

### 5. **Which process automatically adopts orphan processes in Unix-like systems?**

* A) `/bin/bash`
* B) `sshd`
* C) `init` or `systemd`
* D) `cron`
  ✅ **Answer:** C
  *The `init` process (or `systemd` on newer systems) becomes the parent of orphaned processes and is responsible for cleaning them up.*

---

### 6. **Which of the following transitions is NOT valid in a typical process lifecycle?**

* A) Ready → Running
* B) Running → Waiting
* C) Waiting → Running
* D) Running → Terminated
  ✅ **Answer:** C
  *A process must first go back to the Ready state before it can enter the Running state again.*

---

### 7. **What happens if a parent process never performs a `wait()` call for its child?**

* A) The child process keeps running
* B) The system reuses the PID immediately
* C) The child becomes a zombie
* D) The child turns into a daemon
  ✅ **Answer:** C
  *Without `wait()`, the terminated child becomes a zombie process.*

---

### 8. **Which of the following states indicates a process has completed and been fully cleaned up?**

* A) Running
* B) Zombie
* C) Terminated
* D) Waiting
  ✅ **Answer:** C
  *“Terminated” means the process has ended and the OS has cleaned up its resources.*

---

### 9. **What command can be used to list process states in Linux?**

* A) `ls -l`
* B) `grep proc`
* C) `ps -eo pid,state,cmd`
* D) `chmod 777`
  ✅ **Answer:** C
  *The `ps` command with options can show process states and commands.*

---

### 10. **Which of the following is most likely a security risk?**

* A) A running process
* B) A waiting process
* C) Multiple zombie processes accumulating
* D) A newly created process
  ✅ **Answer:** C
  *Many zombie processes may indicate malicious or buggy software and degrade system performance or mask malicious behavior.*

---

Would you like a **printable version** of this quiz, or a follow-up **lab challenge** on process analysis and cleanup?
