Here is a custom quiz on "Process States and Lifecycle", drawing directly from the provided sources:

---

### Custom Quiz: Process States and Lifecycle

**1. Process Definition and Lifecycle**
    a. What is a **process**, and what **essential components** does it consist of from the moment it is created?
    b. What is the **unique numeric identifier** assigned to each process by the kernel?
    c. On a Red Hat system, which **initial process** serves as the ancestor for all other processes?

**2. Process States**
    a. Identify and briefly describe the **five basic process states** in Linux.
    b. Which specific state indicates a process that has **terminated but still retains its Process ID (PID)** entry in the process table, waiting for its parent to clean it up?

**3. Process Monitoring Tools and Attributes**
    a. Name **two common command-line utilities** used for viewing and monitoring processes on a Linux system, differentiating their primary use cases.
    b. When examining the output of the `ps` command, what does a **question mark (?) in the TTY column** signify for a process?
    c. What is "**load average**" as displayed by `top`, and how is it typically interpreted?

**4. Process Prioritization and Control**
    a. Explain the concept of "**niceness**" in Linux process prioritisation, including its range of values and what a higher niceness value indicates.
    b. Which two commands are used to **send signals** to processes, and what is the key difference between the **SIGTERM (15)** and **SIGKILL (9)** signals?

---

### Solutions

**1. Process Definition and Lifecycle**
    a. A **process** is a running instance of a launched, executable program. From the moment it is created, it consists of:
        *   An **address space** of allocated memory.
        *   **Security properties**, including ownership credentials and privileges.
        *   One or more **execution threads** of program code.
        *   A **process state**.
        Its environment also includes local and global variables, a current scheduling context, and allocated system resources like file descriptors and network ports.
    b. The unique numeric identifier assigned to each process by the kernel is the **Process ID (PID)**.
    c. On a Red Hat system, all processes are descendants of the first system process, which is **`systemd`**. In older systems, this was often `init`.

**2. Process States**
    a. The five basic process states in Linux are:
        *   **Running (R)**: The process is currently being executed by the CPU or is waiting to run.
        *   **Sleeping (S)**: The process is waiting for some condition to be met, such as input from a user or another process, a hardware request, or a signal.
        *   **Uninterruptible Sleeping (D)**: Similar to "Sleeping", but the process does not respond to signals, typically when waiting for disk I/O to complete. (Note: Source lists "Waiting" as a separate state, which Source consolidates under "Sleeping" or "Running/Runnable" categories, while Source provides "TASK_INTERRUPTIBLE" for S and "TASK_UNINTERRUPTIBLE" for D).
        *   **Stopped (T)**: The process is currently halted or suspended, often by a signal from a user or another process (e.g., Ctrl+Z), and will not run even when its turn comes unless a signal is sent to change its behaviour. A process being debugged also shares this 'T' state flag.
        *   **Zombie (Z)**: The process is dead, having released all its resources except for its Process ID (PID). Its entry is retained in the process table until its parent process cleans up its entry. It is also referred to as "defunct".
    b. The specific state that indicates a process has terminated but still retains its Process ID (PID) entry in the process table, waiting for its parent to clean it up, is **Zombie (Z)**.

**3. Process Monitoring Tools and Attributes**
    a. Two common command-line utilities for viewing and monitoring processes are:
        *   **`ps` (process status)**: Provides a snapshot of currently running processes. It is primarily used to list detailed information for current processes.
        *   **`top` (table of processes)**: Provides a dynamic, real-time view and monitoring of processes and system resources, updating continuously at a configurable interval.
    b. A question mark **(?) in the TTY column** of `ps` output signifies that the process is not associated with any terminal, typically indicating a **daemon process**.
    c. **Load average** in `top` refers to the number of processes that are waiting to run, which means the number of processes that are in a runnable state and are sharing the CPU. `top` displays three values for load average, representing the average for the last 1, 5, and 15 minutes. Values less than 1.0 generally indicate that the machine is not busy.

**4. Process Prioritization and Control**
    a. **Niceness** is a numeric value that determines a process's priority in getting kernel attention to run. Niceness values range from **-20 (highest priority)** to **+19 (lowest priority)**, with **0 being the default**. A higher niceness value signifies a lower execution priority for the process, meaning it will receive less CPU attention.
    b. The two commands used to send signals to processes are **`kill`** and **`killall`**.
        *   **SIGTERM (15)**: This is the **default signal** sent by the `kill` command. It asks a process to terminate in an orderly or "nicely" fashion. A process can catch or ignore this signal, and if ignored, the process continues to run.
        *   **SIGKILL (9)**: This signal terminates a process **abruptly and immediately**. It is an unblockable signal, meaning the process cannot catch, block, or ignore it.
    The signal sent to resume a stopped or suspended process is **SIGCONT (18)**.