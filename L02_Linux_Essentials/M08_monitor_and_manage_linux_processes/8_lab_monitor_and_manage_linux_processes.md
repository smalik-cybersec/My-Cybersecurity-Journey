📘 Title: Lab: Monitor and Manage Linux Processes

🧠 Theory:
In Linux, managing processes is a fundamental skill for system administrators and cybersecurity professionals. A process is an instance of an executing program. Understanding process states, their lifecycle, and how to control them is crucial for system monitoring, troubleshooting, and ensuring optimal performance and security. This lab will cover how to determine the status, resource usage, and ownership of running programs, manage jobs, terminate processes, and monitor process activity.

Key concepts include:

  * **Process States and Lifecycle**: Processes transition through various states (e.g., Running, Sleeping, Stopped, Zombie) from creation to termination. Each process has a unique Process ID (PID) and a Parent Process ID (PPID).
  * **Job Control**: Managing multiple processes started from the same terminal session, allowing you to move processes to the background or foreground.
  * **Killing Processes**: Terminating unresponsive or malicious processes using signals.
  * **Monitoring Process Activity**: Observing process resource consumption (CPU, memory) and overall system load.

💡 Use Cases:

  * **System Administration**: Identifying resource-intensive applications, managing background tasks, and ensuring system stability.
  * **Troubleshooting**: Killing hung processes, diagnosing performance bottlenecks, and identifying runaway scripts.
  * **Security**: Detecting unauthorized processes, terminating malware, and enforcing process-level access controls.
  * **Ethical Hacking**: Understanding how processes behave, identifying vulnerable processes, and managing tools in the background.

💻 For Linux Topics:

This lab focuses on evaluating and controlling processes on a Red Hat Enterprise Linux system.

**Process States and Lifecycle** 

A process is a running instance of a launched, executable program. It comprises an address space, security properties (ownership, privileges), execution threads, and a state. The process environment includes variables, scheduling context, and allocated system resources like file descriptors and network ports.

When a parent process forks to create a child process, the child inherits the parent's security identities, file descriptors, port privileges, environment variables, and program code. Each new process receives a unique Process ID (PID) and inherits its parent's PID (PPID). On Red Hat systems, all processes descend from `systemd`, the first system process.

A parent process typically sleeps while its child runs, waiting for the child to complete. Upon exiting, a child process releases its resources and leaves a "zombie" entry in the process table. The parent, signaled upon the child's exit, cleans up this entry and frees the child's remaining resources.

Linux process states include:

  * **Running (R)**: The process is either executing on a CPU or waiting to run (queued).
  * **Sleeping (S)**: The process is waiting for an event (e.g., I/O completion, a signal).
  * **Stopped (T)**: The process has been suspended, usually by a signal (e.g., `SIGSTOP`, `SIGTSTP`).
  * **Zombie (Z)**: The process has terminated, but its entry still exists in the process table because the parent has not yet reaped it.

**Control Jobs** 

Jobs are processes that you start from your current shell session. You can send jobs to the background, bring them to the foreground, or stop them.

  * **Starting a background job**: Use `&` at the end of a command.

    ```bash
    # Run a long-running command in the background
    sleep 30 &
    # Output:
    # [1] 12345  (Job number and PID)
    ```

  * **Listing jobs**: Use the `jobs` command.

    ```bash
    # List active jobs
    jobs
    # Output:
    # [1]+  Running                 sleep 30 &
    ```

  * **Bringing a job to the foreground**: Use `fg %job_number`.

    ```bash
    # Bring job 1 to the foreground
    fg %1
    # (The `sleep 30` command would now run in the foreground,
    # occupying the terminal until it finishes or is stopped)
    ```

  * **Sending a foreground job to the background**:

    1.  Press `Ctrl+Z` to suspend the current foreground process.
    2.  Use `bg %job_number` to send it to the background.

    <!-- end list -->

    ```bash
    # (Assume `vim` is running in the foreground)
    # Press Ctrl+Z
    # Output:
    # ^Z
    # [1]+  Stopped                 vim

    # Send vim to the background
    bg %1
    # Output:
    # [1]+ vim &
    ```

**Kill Processes** 

The `kill` command is used to send signals to processes, which can terminate them, stop them, or modify their behavior.

  * **Finding process ID (PID)**: Use `ps` or `pgrep`.

    ```bash
    # Find the PID of a running process named 'nginx'
    ps aux | grep nginx
    # Output might look like:
    # root      1000  0.0  0.1  12345  6789 ?        Ss   Jul01   0:00 nginx: master process /usr/sbin/nginx
    # www-data  1001  0.0  0.1  12345  6789 ?        S    Jul01   0:00 nginx: worker process
    # (PID is 1000 for master process)

    # Alternatively, use pgrep for just the PID
    pgrep nginx
    # Output: 1000
    ```

  * **Killing a process**: Use `kill PID`.

      * `kill PID` (sends SIGTERM, default, allowing graceful shutdown)
      * `kill -9 PID` (sends SIGKILL, forces immediate termination, non-graceful)

    <!-- end list -->

    ```bash
    # Gracefully terminate process with PID 12345
    kill 12345

    # Forcefully terminate process with PID 12345 (use with caution)
    kill -9 12345
    ```

  * **Killing multiple processes by name**: Use `pkill` or `killall`.

    ```bash
    # Terminate all processes named 'my_script.sh'
    pkill my_script.sh

    # Alternatively, killall
    killall my_script.sh
    ```

**Monitor Process Activity** 

Several commands allow you to monitor processes and system resources.

  * **`ps` (Process Status)**: Displays information about running processes.

    ```bash
    # Display all processes
    ps aux

    # Display processes in a hierarchical tree format
    ps axjf

    # Display user-owned processes
    ps -u <username>
    ```

  * **`top` (Table Of Processes)**: Provides a dynamic real-time view of running processes.

    ```bash
    # Start top to view processes dynamically
    top
    # (Press 'q' to quit)
    ```

    `top` output typically includes:

      * **PID**: Process ID
      * **USER**: User running the process
      * **PR**: Priority
      * **NI**: Nice value (re-prioritization)
      * **VIRT**: Virtual memory used
      * **RES**: Resident (physical) memory used
      * **SHR**: Shared memory
      * **S**: Process status (e.g., R=running, S=sleeping, Z=zombie)
      * **%CPU**: CPU usage percentage
      * **%MEM**: Memory usage percentage
      * **TIME+**: Total CPU time used
      * **COMMAND**: Command name

  * **`htop`**: An interactive process viewer, often considered a more user-friendly alternative to `top` (may need to be installed).

    ```bash
    # Start htop
    htop
    # (Provides interactive features like sorting, filtering, and killing processes)
    ```

  * **`pstree`**: Displays running processes as a tree.

    ```bash
    # Display process tree
    pstree
    ```

  * **`vmstat` (Virtual Memory Statistics)**: Reports information about processes, memory, paging, block I/O, traps, and CPU activity.

    ```bash
    # Report once every 2 seconds
    vmstat 2 
    # Output includes:
    # procs: r (running or runnable), b (blocked)
    # memory: swpd (virtual memory used), free (idle memory), buff (buffers), cache (cache)
    # swap: si (swapped in), so (swapped out)
    # io: bi (blocks in), bo (blocks out)
    # system: in (interrupts), cs (context switches)
    # cpu: us (user time), sy (system time), id (idle time), wa (wait I/O), st (steal time)
    ```

🧪 Labs / Exercises:

**Lab: Monitor and Manage Linux Processes** 

**Goal**: Evaluate and control processes that run on a Red Hat Enterprise Linux system.

**Objectives**:

  * Determine the status, resource use, and ownership of running programs on a system, to control them.
  * Use Bash job control to manage multiple processes that were started from the same terminal session.
  * Use commands to kill and communicate with processes, define the characteristics of a daemon process, and stop user sessions and processes.
  * Define load average and determine resource-intensive server processes.

**Instructions:**

1.  **Preparation**:

      * Log in to your Linux environment (e.g., a virtual machine or lab system).
      * Ensure you have `sudo` privileges or access to a root account for certain commands.

2.  **Explore Process States and Lifecycle**:

      * Open a terminal and run a simple long-running command, e.g., `sleep 600 &`. Note its PID using `echo $!`.
      * Immediately run `ps aux | grep sleep` to observe its state (likely 'S' for sleeping).
      * Open another terminal and try to `kill -STOP <PID_of_sleep>` and then `ps aux | grep sleep` to see if it changes to 'T' (stopped).
      * Then, `kill -CONT <PID_of_sleep>` to resume it.
      * Finally, `kill <PID_of_sleep>` to terminate it gracefully. Verify with `ps`.

3.  **Job Control**:

      * In a terminal, start `ping google.com` (without `&`).
      * Press `Ctrl+Z` to suspend the `ping` process.
      * Run `jobs` to see the suspended job.
      * Send the `ping` job to the background using `bg`.
      * Observe that `ping` continues to run in the background.
      * Bring it back to the foreground using `fg`.
      * Press `Ctrl+C` to terminate the `ping` process.

4.  **Killing Processes**:

      * Open a new terminal.
      * Start a new `sleep 3600 &` process.
      * Identify its PID using `pgrep sleep` or `ps aux | grep sleep`.
      * Attempt to kill it gracefully: `kill <PID>`. Verify it's gone.
      * If it doesn't terminate (e.g., if it were a stubborn process), try `kill -9 <PID>`.
      * Create a simple script `my_loop.sh`:
        ```bash
        #!/bin/bash
        while true; do
            echo "Running..."
            sleep 5
        done
        ```
      * Make it executable: `chmod +x my_loop.sh`.
      * Run it: `./my_loop.sh &`.
      * Use `pkill -f my_loop.sh` to kill it by name. The `-f` option matches against the full command line.

5.  **Monitoring Process Activity**:

      * Run `top` in your terminal. Observe the system load average, CPU usage, memory usage, and the list of processes. Identify processes consuming high CPU or memory.
      * Press `M` to sort by memory usage, `P` to sort by CPU usage.
      * Press `q` to quit `top`.
      * Install `htop` if it's not available: `sudo yum install htop` (for RHEL/CentOS) or `sudo apt install htop` (for Debian/Ubuntu).
      * Run `htop`. Explore its interactive features:
          * F1: Help
          * F2: Setup (customize columns, meters, etc.)
          * F3: Search
          * F4: Filter
          * F5: Tree view
          * F9: Kill a process (select and press F9, then choose signal)
      * Run `vmstat 1 5` to get 5 reports, one every second, on system activity. Analyze the output for `r` (runnable processes), `b` (blocked processes), `si`/`so` (swap activity), and CPU `us`/`sy`/`id`/`wa` percentages.

6.  **Analyze System Load**:

      * Open multiple terminals and run CPU-intensive tasks in the background, e.g., `yes > /dev/null &` (run this in 2-3 terminals).
      * Observe the load average in `top` (first line) and the increase in `%CPU` for the `yes` processes.
      * Kill the `yes` processes using `pkill yes`.

🧠 Tips & Tricks:

  * **PID 1 is Special**: On modern Linux systems (like RHEL 9), PID 1 is usually `systemd`, the init system. It's the parent of all other processes. Never kill PID 1\!
  * **Signals**: `SIGTERM` (15) is the default and preferred way to kill a process as it allows graceful shutdown. `SIGKILL` (9) is a last resort as it forcibly terminates the process without cleanup.
  * **`nice` and `renice`**: Use `nice` to start a process with a lower priority, and `renice` to change the priority of an already running process. This helps manage resource allocation for background tasks.
  * **`nohup`**: Use `nohup command &` to run a command in the background that will continue to run even if you close the terminal.
  * **`jobs -l`**: Shows job numbers and their PIDs.
  * **`top` interactive commands**: Many keys within `top` can change its display and behavior (e.g., `k` to kill a process, `r` to renice).

📝 Summary/Recap:

  * Linux processes are instances of running programs, each with a unique PID and state.
  * The `ps` command provides a snapshot of processes, while `top` and `htop` offer real-time interactive monitoring.
  * Bash job control (`&`, `jobs`, `fg`, `bg`, `Ctrl+Z`) allows managing processes within a terminal session.
  * The `kill` command sends signals to processes, typically to terminate them. `SIGTERM` (graceful) and `SIGKILL` (forceful) are common signals.
  * `pkill` and `killall` can terminate processes by name.
  * `vmstat` provides detailed system performance statistics, including CPU, memory, and I/O.

🗂️ Related Topics:

  * **System Services and Daemons**: Understanding how background services run and how to manage them with `systemctl`.
  * **Linux File System Hierarchy**: Knowing where executables and configuration files related to processes are stored.
  * **Permissions**: How file and directory permissions affect process execution and user privileges.
  * **Shell Scripting**: Automating process management tasks through scripts.