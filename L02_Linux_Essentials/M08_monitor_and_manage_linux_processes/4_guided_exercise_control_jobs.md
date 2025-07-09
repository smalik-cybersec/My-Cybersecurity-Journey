Here is a custom guided exercise on "Control Jobs", drawing upon the information in the provided sources and our conversation history.

---

### Custom Guided Exercise: Control Jobs

**Goal:** To gain practical experience with managing processes within a single shell instance using Linux job control features.

**Objectives:** Upon completing this exercise, you will be able to:
*   Start commands to run in the background.
*   List jobs active in your current shell session.
*   Suspend a foreground job.
*   Move jobs between the foreground and background.
*   Terminate jobs using specific shell commands.

**Before You Begin:**
Ensure you have access to a Linux command-line shell (e.g., Bash).

---

#### Instructions

Follow these steps in your Linux shell. Pay close attention to the output and the behaviour of the shell.

**Step 1: Starting a Job in the Background**
You can run any command or pipeline in the background by appending an **ampersand (`&`)** character to the command. This allows you to immediately regain control of your shell prompt.

1.  Open your terminal.
2.  Execute a simple command in the background. We will use `sleep` as it runs for a specified duration without outputting much.
    ```bash
    sleep 30 &
    ```
    *   Observe the output. You should see a job number in square brackets (e.g., ``) and a Process ID (PID) (e.g., `12345`). The shell returns to the prompt immediately.
3.  Let's start another one:
    ```bash
    ping google.com &
    ```
    *   Notice its job number and PID. This command will keep running and outputting to your terminal in the background.

**Step 2: Listing Current Jobs**
The `jobs` command is a shell built-in utility that lists all jobs currently running or stopped in the shell's session.

1.  Use the `jobs` command to see your active background processes:
    ```bash
    jobs
    ```
    *   You should see both `sleep` and `ping` listed. The `+` sign indicates the current default job (the most recently started or manipulated), and `-` indicates the previous job.
2.  To view the Process IDs (PIDs) alongside the job numbers, use the `-l` (lowercase L) parameter:
    ```bash
    jobs -l
    ```
    *   Compare the PIDs with those displayed when you started the jobs.

**Step 3: Suspending a Foreground Job**
You can temporarily halt a foreground job by pressing **`Ctrl+Z`**. This moves the job to a "Stopped" state and returns the shell prompt.

1.  Start a new foreground job that will run continuously:
    ```bash
    tail -f /var/log/messages
    ```
    *   (Note: If `/var/log/messages` doesn't exist or is empty, try `/var/log/dnf.log` or any other active log file on your system).
    *   This command will continuously display new lines added to the log file. You won't get your prompt back.
2.  While `tail` is running in the foreground, press **`Ctrl+Z`**.
    *   The command should stop, and you will see a message indicating it's "Stopped". Your shell prompt will reappear.
3.  Use `jobs` again to confirm the `tail` process is now in a "Stopped" state:
    ```bash
    jobs
    ```
    *   You should see `Stopped` next to your `tail -f` job.

**Step 4: Moving a Suspended Job to the Background**
A stopped job can be moved to the background using the `bg` (background) command. This allows it to resume execution without occupying your terminal.

1.  Move the `tail -f` job (which you stopped in Step 3) to the background:
    ```bash
    bg
    ```
    *   If you have multiple stopped jobs, you might need to specify the job number (e.g., `bg %2`). The shell will typically select the default job (indicated by `+`) if no argument is given.
    *   You should see the command start running in the background, and its output may begin scrolling in your terminal again.
2.  Verify its status with `jobs`:
    ```bash
    jobs
    ```
    *   The `tail -f` job should now be listed as `Running`.

**Step 5: Bringing a Background Job to the Foreground**
The `fg` (foreground) command brings a suspended or backgrounded job back to the foreground, where it will again occupy your shell prompt.

1.  Bring the `tail -f` job back to the foreground:
    ```bash
    fg
    ```
    *   Similar to `bg`, if you have multiple background jobs, you might need to specify the job number (e.g., `fg %2`).
    *   The `tail` command should now be running in your foreground, and you will not have your shell prompt.
2.  Press **`Ctrl+C`** to terminate the `tail -f` command.
    *   This sends a `SIGINT` (interrupt) signal, which typically terminates the process gracefully. Your shell prompt should return.

**Step 6: Terminating Jobs**
You can use the `kill` command to send signals to processes or jobs, including termination signals.

1.  First, list your remaining jobs to identify their job numbers and PIDs:
    ```bash
    jobs -l
    ```
2.  Terminate one of your `sleep` jobs (or the `ping` job) using its job number. We will use `kill %job_number`. By default, `kill` sends the `SIGTERM` (15) signal, which requests a graceful termination.
    ```bash
    kill %1
    ```
    *   (Replace `%1` with the actual job number of one of your `sleep` jobs).
    *   The job might disappear immediately, or you might see a "Terminated" message.
3.  Sometimes a process doesn't respond to `SIGTERM`. In such cases, `SIGKILL` (9) can be used, which forces immediate termination and cannot be ignored by the process.
    ```bash
    kill -9 %2
    ```
    *   (Replace `%2` with the job number of your other `sleep` or `ping` job).
    *   This job should definitely be terminated immediately.
4.  Verify that all jobs have been terminated:
    ```bash
    jobs
    ```
    *   You should see no output or only the `Done` status for the terminated jobs.

---

#### Outcomes

You have successfully practised the following job control operations within your Linux shell:
*   Initiating commands in the background using `&`.
*   Listing and identifying jobs with `jobs` and `jobs -l`.
*   Suspending foreground processes with `Ctrl+Z`.
*   Moving suspended jobs to the background with `bg`.
*   Bringing background jobs to the foreground with `fg`.
*   Terminating jobs gracefully and forcefully using `kill` with `SIGTERM` and `SIGKILL`.