A process in Linux is essentially a **running instance of an executable program, command, or application**. It serves as the fundamental unit for provisioning system resources. The Linux kernel is responsible for managing a process throughout its entire lifespan.

### Process Lifecycle and Creation
The lifecycle of a process on a Linux system typically begins with the **`systemd` process**, which has a Process ID (PID) of 1. All other processes on a Red Hat system are descendants of `systemd`. Historically, the `init` daemon also had PID 1 and was considered the "mother of all processes".

Processes are brought into existence when a program is initiated. A new process, known as a **child process**, is created when an existing **parent process** duplicates its own address space through a mechanism called a **process fork**. When a child process is forked, it inherits various attributes from its parent, including security identities, file descriptors, port and resource privileges, environment variables, and program code.

Typically, a parent process will "sleep" while its child process runs, setting a "wait request" to be signalled upon the child's completion. Once a child process exits, it releases and discards its resources and environment, but it leaves behind a **zombie resource**, which is an entry in the process table. The parent process is then responsible for cleaning up this remaining entry.

### Process Attributes
Each process is assigned a **unique numeric identifier called a Process ID (PID)**. While PIDs are unique for currently running processes, they can be reused by new processes once a process terminates. Processes also have a **Parent Process ID (PPID)**, which indicates the PID of the process that created them.

Other key attributes of a process include:
*   An **address space of allocated memory**.
*   Security properties, including **ownership credentials and privileges**. Processes are associated with a user ID (UID) and a group ID (GID).
*   One or more **execution threads** of program code.
*   An environment containing **local and global variables**, a **current scheduling context**, and **allocated system resources**, such as file descriptors and network ports.
*   A **kernel context**, which records process-specific information allowing the kernel to manage and control its execution.
*   A private and protected **virtual address space**.
*   Three standard file descriptors (standard input, standard output, and standard error) are already open and ready for immediate use.
*   A **controlling terminal**, which serves as the default source and destination for standard file streams.
*   Expansion of wildcard characters in command-line arguments.

### Process States
A process's operating state can change multiple times throughout its lifecycle. At any given moment, a process is in one of several states:
*   **Running (R)**: The process is actively executing on a CPU or is queued and ready to run.
*   **Sleeping (S)**: The process is not running, but is waiting for an event, such as user input, input from another process, a hardware request, system resource access, or a signal.
*   **Waiting (D)**: This indicates an uninterruptible sleep state, typically meaning the process is waiting for I/O to complete. This state also encompasses `TASK_KILLABLE` (K) and `TASK_REPORT_IDLE` (I) for kernel threads.
*   **Stopped (T)**: The process has been halted or suspended, usually by a signal, and will not execute until a signal is sent to resume it. This state also applies to processes being debugged (`TASK_TRACED`).
*   **Zombie (Z)**: A process that has terminated but still has an entry in the process table because its parent has not yet "reaped" it. A zombie process consumes no resources other than its PID entry.
*   **EXIT_DEAD (X)**: This is the final state where the parent process cleans up the child's structure, and the process is completely released. This state cannot be observed using process-listing utilities.

Other characters may follow the primary state flag to indicate specific process characteristics, such as `<` for high priority, `N` for low priority (`niceness`), `L` for pages locked in memory, `s` for a session leader, `l` for multi-threaded, and `+` for running in the foreground.

### Process Management Tools
Several tools are available to monitor and manage processes:
*   **`ps` (process status)**: Provides a snapshot of currently running processes. It can display detailed information about processes, including UID, PID, PPID, CPU usage, memory usage, terminal association, state, start time, and command. `ps --forest` can display processes in a tree format to show parent/child relationships.
*   **`top` (table of processes)**: Offers a real-time, dynamic view of system processes and resources. Its output includes system uptime, number of users, load averages, CPU usage, and memory/swap utilization, with processes sorted by CPU or memory usage.
*   The **`/proc` filesystem** contains raw data and information about running processes, accessible through directories named after their PIDs.
*   **`pstree`**: Displays processes in a hierarchical tree format, useful for visualizing parent-child relationships.
*   **GUI tools** like `System Monitor` (GNOME) or `KDE Process Manager (kpm)` also provide graphical interfaces for process viewing and management.

### Process Control
Administrators can control processes using various methods:
*   **Signals**: Commands such as **`kill`**, **`pkill`**, and **`killall`** are used to send software interrupts (signals) to processes. Common signals include `SIGHUP` (hangup/re-read config), `SIGINT` (keyboard interrupt, e.g., Ctrl+C), `SIGTERM` (soft termination, default for `kill`), `SIGKILL` (abrupt termination, cannot be ignored), `SIGSTOP` (pause unconditionally), and `SIGCONT` (resume a paused process).
*   **Prioritisation**: The **`nice`** and **`renice`** commands allow adjusting a process's scheduling priority, or "niceness". Niceness values typically range from -20 (highest priority) to +19 (lowest priority), with 0 being the default.
*   **Job Control**: Shell features allow a single shell instance to manage multiple commands simultaneously, including moving processes between the **foreground** and **background**. Commands like **`jobs`**, **`fg`** (foreground), **`bg`** (background), and **`wait`** are used for this purpose. Pressing `Ctrl+Z` can suspend a foreground job.
*   **Control Groups (cgroups)**: The Linux kernel uses cgroups to organize processes for resource monitoring and control, allowing for limiting, isolating, and prioritizing resource usage (CPU, memory, network bandwidth, disk I/O). `systemd` utilizes cgroups to manage services.
*   **SELinux Contexts**: SELinux assigns security contexts to processes, affecting their access rights. This context includes user, role, type (or domain), and level. The `ps -Z` command can display these contexts. Processes started by `init` (`systemd`) are given new contexts according to SELinux policy, while child processes generally inherit their parent's context.