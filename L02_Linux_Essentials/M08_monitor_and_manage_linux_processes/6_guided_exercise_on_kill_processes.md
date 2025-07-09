Here is a custom guided exercise on "Kill Processes", drawing on the information from the provided sources.

---

### Custom Guided Exercise: Terminating Processes in Linux

**Introduction**

In Linux, a **process** is essentially a running instance of a program, command, or application on your system. Every process is assigned a **unique numeric identifier called a Process ID (PID)**, which the kernel uses to manage it throughout its lifecycle. Processes consume various system resources, including memory, CPU, and disk I/O.

System administrators often need to terminate processes for several reasons. A common scenario is when processes become "resource hogs," consuming excessive CPU or memory, leading to system sluggishness or unresponsiveness. Another critical reason is when a program misbehaves or becomes unresponsive. The kernel even includes a **protection mechanism called the Out-of-Memory Killer (OOM Killer)**, which terminates processes based on factors like execution time and resource usage when RAM usage is high and no swap is available, to recover system functionality. However, this comes at a cost, as the OOM Killer might terminate critical services like databases or web servers, potentially leaving the system in an unstable state.

To control and terminate processes, Linux uses **signals**, which are software interrupts delivered to a process to report events or instruct it to take a specific action.

**Part 1: Identifying Processes to Terminate**

Before you can terminate a process, you must first identify it. This typically involves finding its PID or its command name.

1.  **Using `ps` for a Snapshot View**:
    *   The `ps` command provides a snapshot of currently running processes.
    *   **To list all processes in a user-oriented format**: Use `ps aux`. You can also use `ps eux` to include environment variables for each process.
    *   **To list processes by a specific user**: Use `ps -u username` (e.g., `ps -u student`).
    *   **To list processes by command name**: Use `ps -C command_name` (e.g., `ps -C firefox`).
    *   **To view a full listing of processes**: Use `ps -ef`.
    *   **To see process priorities and niceness values**: Use `ps -l` or `ps axl`. Look for the `PRI` (priority) and `NI` (niceness) columns. `ps axl` can also help identify the **Parent Process ID (PPID)**, which is crucial for understanding process hierarchy.
    *   **To filter output**: Pipe `ps` output to `grep` to narrow down results. For example, `ps aux | grep [f]irefox` can identify Firefox processes while excluding the `grep` command itself.
    *   **To view a process tree**: Use `pstree` (e.g., `pstree -p user`) to see parent-child relationships, which can be useful when dealing with unresponsive processes where killing the parent might be necessary.

2.  **Using `top` for Real-time Monitoring**:
    *   The `top` command provides a real-time, interactive view of processes and system resource usage.
    *   **To identify CPU/memory-intensive processes**: Run `top` and observe the `%CPU` and `%MEM` columns. You can **sort by CPU usage by pressing `Shift+p`** or **by memory usage by pressing `Shift+m`** while `top` is running.
    *   **To filter processes by user**: While in `top`, **press `u`** (or `Shift+u`) and enter the username.

3.  **Using `pgrep` and `pidof` to Find PIDs by Name**:
    *   These commands directly find the PID of a process given its name.
    *   **To find a PID**: `pidof process_name` (e.g., `pidof emacs`).
    *   **For more advanced criteria**: `pgrep` can find PIDs based on user ID, group ID, or other patterns. For instance, `pgrep -l -u student` lists all processes owned by the `student` user and their PIDs.

4.  **Using `jobs` and `w` for Session Control**:
    *   The `jobs` command lists jobs running or stopped in your current shell session, displaying their job number and PID.
    *   The `w` command lists user logins and their associated terminal devices (TTYs). This can help identify specific sessions to terminate administratively.

**Part 2: Understanding Process Control Signals**

Signals are crucial for communicating with processes. You can get a list of all available signals using the `kill -l` command. Each signal has a numeric identifier and a name, and a predefined **disposition** (action) such as terminate, ignore, perform a core dump, stop, or continue. While signal numbers can vary between Linux hardware platforms, their names and meanings are standard, and it is advised to use signal names over numbers.

Here are some of the most common signals used for process management:

*   **`SIGTERM` (Signal 15)**: This is the **default signal sent by the `kill` command** if no other signal is specified. It sends a **soft termination signal**, requesting a graceful shutdown. Processes can catch and handle this signal, allowing them to perform internal cleanup steps and save data before exiting. **This is the recommended first attempt** when trying to stop a process.

*   **`SIGKILL` (Signal 9)**: This signal causes **abrupt and unconditional program termination**. It cannot be blocked, ignored, or handled by the process, making it consistently fatal. However, because it forces immediate termination without allowing any cleanup, it should be used only as a **last resort** when `SIGTERM` or other signals fail, as it can leave resources allocated or the system in an unstable state.

*   **`SIGHUP` (Signal 1)**: The "Hang up" signal. This is frequently used to instruct a running daemon to **re-read its configuration files without restarting**. For example, `kill -1 PID` can signal `httpd` to reload its configuration.

*   **`SIGINT` (Signal 2)**: The "Interrupt" signal, typically sent by pressing **`Ctrl+C`**. It usually terminates a program.

*   **`SIGQUIT` (Signal 3)**: The "Keyboard quit" signal, often sent by pressing **`Ctrl+\`**. It is similar to `SIGINT` but typically causes a process dump at termination.

*   **`SIGSTOP` (Signal 19)**: This signal **suspends (stops) a process unconditionally**. Unlike `SIGTSTP`, it cannot be blocked or handled by the process.

*   **`SIGTSTP` (Signal 20)**: The "Keyboard stop" signal, sent by pressing **`Ctrl+Z`**. This suspends a foreground process, moving it to a "Stopped" state.

*   **`SIGCONT` (Signal 18)**: This signal **resumes a stopped or suspended process**. It is typically used with the `bg` (background) or `fg` (foreground) commands.

**Part 3: Commands for Terminating Processes**

1.  **`kill` command**:
    *   **Syntax**: `kill [options] PID...`.
    *   **Function**: Sends a specified signal to a process identified by its **Process ID (PID)**.
    *   **Usage**: You can specify a signal by its name (e.g., `-SIGTERM`, `-SIGKILL`, `-HUP`) or its number (e.g., `-15`, `-9`, `-1`).
    *   **Example**:
        *   To gracefully terminate PID `12345`: `kill 12345` (sends `SIGTERM` by default).
        *   To forcefully terminate PID `12345`: `kill -9 12345` or `kill -SIGKILL 12345`.
        *   To make a daemon re-read its configuration without restarting (e.g., if its PID is `1833`): `kill -1 1833` or `kill -SIGHUP 1833`.
    *   **Permissions**: Ordinary users can only kill processes they own. The `root` user can kill any process on the system.

2.  **`killall` command**:
    *   **Syntax**: `killall [options] program_name...`.
    *   **Function**: Signals **multiple processes based on their command name**.
    *   **Usage**: You can use this to terminate all instances of a program. For example, `killall firefox` to kill all Firefox processes, or `killall -9 httpd` to forcefully terminate all Apache web server processes.
    *   **Caution**: Exercise extreme care when using `killall` as the `root` user, especially with wildcard characters, as it can inadvertently stop critical system processes and potentially damage the filesystem.

3.  **`pkill` command**:
    *   **Function**: Signals one or more processes that match **advanced selection criteria**.
    *   **Criteria**: Includes command name, processes owned by a specific user (UID), group (GID), child processes of a specific parent process, or processes running on a specific controlling terminal.
    *   **Example**:
        *   To kill all processes owned by the `student` user: `pkill -u student`.
        *   To kill processes on a specific terminal: `pkill -t tty3`.
        *   To kill all child processes of a parent with PID `8391`: `pkill -P 8391`.
    *   **Combined Usage**: `pkill` can be combined with other commands like `ps` and `gawk` using pipes for complex scenarios, such as `ps -u $USER_ACCOUNT --no-heading | gawk '{print $1}' | xargs -d \n /usr/bin/sudo /bin/kill -9` to forcefully kill a user's processes.

4.  **Interactive Killing with `top`**:
    *   While `top` is running, you can press **`k`** (lowercase K) to kill a process.
    *   You will be prompted for the PID of the process you wish to kill (the default is often the top CPU-consuming process) and then prompted for the signal to send (default is `15/SIGTERM`, but you can type `9` for `SIGKILL`).

5.  **Keyboard Control Sequences (for foreground processes)**:
    *   **`Ctrl+C`**: Sends a `SIGINT` signal to the current foreground process, usually terminating it.
    *   **`Ctrl+\`**: Sends a `SIGQUIT` signal, similar to `SIGINT` but often results in a core dump.
    *   **`Ctrl+Z`**: Sends a `SIGTSTP` signal to suspend the current foreground job, moving it to a "Stopped" state. From this state, you can use `bg` to move it to the background (e.g., `bg %job_ID`) or `fg` to bring it back to the foreground (e.g., `fg %job_ID`).

**Part 4: Adjusting Process Priority (`nice`/`renice`)**

Sometimes, you don't want to kill a process but rather adjust its priority to better manage system resources. This is done using **niceness** values.

*   **Niceness Values**: Linux processes are scheduled based on a niceness value, which ranges from **-20 (highest priority, "less nice" because it takes more CPU time)** to **+19 (lowest priority, "nicer" as it yields CPU time to others)**. The default niceness for most system-started processes is `0`.
*   **`nice` command**: Use `nice` to launch a new command with a specific niceness value. For example, `nice +5 updatedb &` runs the `updatedb` command with a lower priority in the background.
*   **`renice` command**: Use `renice` to change the niceness (priority) of a **running process**.
    *   **Syntax**: `renice -n nice_value PID`.
    *   **Permissions**: Ordinary users can only "make their processes nicer" (increase the positive niceness value, lowering priority). The `root` user, however, can raise or lower the niceness of any process on the system.
    *   **Example**: `pgrep -f backup | xargs renice -n 19` can be used to set the lowest priority for all processes containing "backup" in their name. Similarly, `ionice` can adjust the priority of I/O operations.

**Part 5: Best Practices for Process Termination**

*   **Prioritize Graceful Termination**: Always attempt to terminate processes gracefully using `SIGTERM` (the default for `kill` and `killall`) first. This allows the program to save data and clean up resources, preventing data loss or system instability. Red Hat specifically recommends trying `SIGTERM` first, then `SIGINT`, and only then `SIGKILL`.
*   **Use `SIGKILL` as a Last Resort**: Only resort to `SIGKILL` if a process is unresponsive to `SIGTERM` or other signals. Remember, `SIGKILL` does not allow the process to clean up after itself.
*   **Understand Process Ownership**: Be mindful of permissions. Regular users can only terminate processes they own, while `root` privileges are required to kill processes owned by other users or the system.
*   **Verify Termination**: After sending a kill signal, use commands like `ps` or `jobs` to confirm that the process has indeed terminated.

This comprehensive overview should provide you with the necessary knowledge and tools to effectively identify, manage, and terminate processes on a Linux system.