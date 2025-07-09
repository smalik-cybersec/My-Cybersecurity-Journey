The "Process States and Lifecycle" refer to the various stages and conditions a program undergoes from its creation to its termination on a Linux system. Understanding this concept is crucial for system administrators to effectively manage resources and troubleshoot issues.

Here's a breakdown of processes, their states, and lifecycle:

### What is a Process?
A **process is a running instance of a launched, executable program**. It is a unit for provisioning system resources. Every process has a unique numeric identifier called a **Process ID (PID)**, which is used by the kernel to manage and control it throughout its lifecycle.

A process consists of:
*   An address space of allocated memory.
*   Security properties, including ownership credentials and privileges.
*   One or more execution threads of program code.
*   A process state.
*   An environment, which includes local and global variables, a current scheduling context, and allocated system resources like file descriptors and network ports.

### Process Lifecycle and Hierarchy
Processes are organised hierarchically. The **Linux kernel creates the first process, known as `init` (or `systemd` in modern Red Hat systems)**, which has a PID of 1 and a Parent Process ID (PPID) of 0. All other processes are descendants of this initial process.

When a program is initiated, a process is created in memory. An existing parent process duplicates its own address space through a mechanism called **process fork** to create a child process structure. The child process inherits security identities, file descriptors, privileges, environment variables, and program code from its parent. After a child process exits, it leaves a "zombie" entry in the process table until its parent process cleans up (reaps) its entry, freeing all resources.

The kernel manages processes by starting, pausing, resuming, scheduling, and terminating them. In a multitasking operating system, multiple programs appear to run simultaneously because the kernel rapidly switches between them, giving each process a small **"time slice"** of CPU time. This act of one process giving up control of the CPU to another is called a **context switch**.

### Process States
A process changes its operating state multiple times during its lifecycle, influenced by factors such as processor load, memory availability, and priority. There are five basic process states:

*   **Running (R)**: The process is currently being executed by the CPU or is waiting in a queue, ready to run. On a single CPU system, only one process can truly be running at a time, but several may be in the "Running" state if they are ready to execute as soon as their turn comes.
*   **Sleeping (S)**: The process is waiting for some condition to be met, such as input from a user, a hardware request, or a signal. When the condition is met, it returns to the Running state.
*   **Uninterruptible Sleeping (D)**: Similar to "Sleeping," but this state means the process **does not respond to signals**, typically used when waiting for disk I/O to complete or when interruption might cause an unpredictable device state.
*   **Stopped (T)**: The process is currently halted or suspended, often by a signal from a user or another process (e.g., by pressing Ctrl+Z). It will not run even when its turn comes unless a signal is sent to change its behaviour (e.g., SIGCONT). A process being debugged is also temporarily stopped and shares this 'T' state flag.
*   **Zombie (Z)**: The process is dead, having released all its resources except for its Process ID (PID). Its entry is retained in the process table until its parent process permits it to fully die and cleans up the entry. This state is also referred to as "defunct".
*   **Killable (K)**: A subset of 'D' state, identical to uninterruptible sleep, but modified to allow a waiting task to respond to a kill signal.
*   **Exit Dead (X)**: This is when the parent process has fully reaped and cleaned up the child process structure. This state cannot be observed in process-listing utilities as the process is completely released.

Additional status characters seen in `ps` output can indicate:
*   `<`: The process is running at high priority.
*   `N`: The process is running at low priority (a "nice" process).
*   `L`: The process has pages locked in memory.
*   `s`: The process is a session leader.
*   `l`: The process is multi-threaded.
*   `+`: The process is running in the foreground.

### Tools for Viewing Process Information
Various native tools allow users and administrators to view and monitor processes and their states:
*   **`ps` (process status)**: Provides a snapshot of currently running processes. It can display information like PID, TTY (terminal), CPU time, command name, user ID, parent PID, CPU utilisation, start time, memory usage (VSZ, RSS), and process state (STAT/S). The `--forest` option can display processes in a tree-like hierarchy to show parent/child relationships.
*   **`top` (table of processes)**: Provides a dynamic, real-time view and monitoring of processes and system resources, updating continuously at a configurable interval. It displays a summary header (system uptime, logged-in users, load average, total tasks, CPU usage, memory utilization) followed by a list of processes, sorted by default based on CPU usage. `top` also allows interactive commands to change sorting criteria (e.g., `M` for memory, `P` for CPU), filter by user (`u`), kill processes (`k`), or renice them (`r`).
*   **`pstree`**: Displays a process list arranged in a tree-like pattern, showing parent-child relationships.
*   **`w` command**: Displays the current process running in each shell for all logged-in users, including system uptime and load average.
*   **`free` command**: Used to identify how much memory processes are consuming.
*   **System Monitor (GNOME)**: A graphical tool to view and change running processes, allowing sorting by various fields (e.g., %CPU, Memory), and actions like stopping, continuing, ending, killing, or changing priority via a right-click menu.

The information for each running process is recorded and maintained in the **`/proc` file system**, which `ps` and other commands reference to acquire data. Each process stores its information in a subdirectory named after its PID within `/proc`.

### Process Prioritisation
Processes are spawned at a certain priority, established by a numeric value called **niceness** (or nice value). There are 40 niceness values, ranging from **-20 (highest priority) to +19 (lowest priority)**, with 0 being the default. A higher niceness value means a lower execution priority for the process, receiving less CPU attention. The root user can raise or lower the niceness of any process, while normal users can only make their own processes "nicer" (lower priority). Commands like `nice` and `renice` are used to adjust these priorities. The kernel may also change a process's priority during execution based on CPU consumption.

### Signals for Process Control
Processes communicate using **signals**, which are software interrupts that report events to an executing program. Signals can be generated by errors, external events (like I/O requests), or explicit commands. Each signal has a unique numeric identifier, a name, and a default action (terminate, ignore, core dump, stop, continue).

Common signals include:
*   **SIGHUP (1)**: Hangup signal, often used to instruct a running daemon to re-read its configuration without restarting.
*   **SIGINT (2)**: Interrupt from keyboard (Ctrl+C), causes program termination. It can be blocked or handled.
*   **SIGQUIT (3)**: Quit from keyboard.
*   **SIGKILL (9)**: Terminates a process abruptly and immediately. It cannot be blocked, ignored, or handled by the process.
*   **SIGTERM (15)**: Sends a soft termination signal to stop a process in an orderly fashion. This is the **default signal** if none is specified with the `kill` command. If ignored, the process continues to run.
*   **SIGSTOP (19)**: Suspends a process unconditionally without terminating it. It cannot be blocked or handled.
*   **SIGCONT (18)**: Sent to a process to resume it if stopped. It cannot be blocked.

Commands used to send signals to processes include `kill` and `killall`. Ordinary users can only kill processes they own, while the root user can kill any process on the system.