````markdown
# 🎯 Guided Exercise: Kill Processes

## 1. 🧠 What Is It (Definition + Explanation)
* **Killing processes** is the act of terminating a running or hung process manually using its **PID**, **name**, or **job ID**.
* This is typically done with commands like `kill`, `killall`, or `pkill`, along with signals such as `SIGTERM` or `SIGKILL`, to either gracefully or forcefully shut down the process.
* This skill is essential in system administration, troubleshooting, and cybersecurity operations.

---

## 4. 🧪 Lab Task (Hands-On Practice)

> ⚠️ **!! CRITICAL SAFETY WARNING !!:** Tasks **MUST ONLY** be done in safe, controlled environments (VMs, isolated labs), NEVER on real systems without explicit permission.

---

## 🧪 Exercise 1: Start a Dummy Process

### ✅ Step-by-Step:

1. **Launch a long-running background process:**
```bash
sleep 500 &
````

2. **Check running jobs:**

```bash
jobs
```

3. **Find its Process ID (PID):**

```bash
ps aux | grep sleep
```

---

## 🧪 Exercise 2: Gracefully Kill the Process

1. **Use `kill` with default signal (SIGTERM):**

```bash
kill <PID>
```

2. **Check if it’s still running:**

```bash
ps aux | grep sleep
```

3. **If still running, retry with a forceful signal (SIGKILL):**

```bash
kill -9 <PID>
```

---

## 🧪 Exercise 3: Kill Process by Job ID

1. **Start a foreground job:**

```bash
cat
```

2. **Pause the job with `Ctrl+Z` (puts it in the background in a stopped state).**

3. **View job list:**

```bash
jobs
```

4. **Kill the job using job ID:**

```bash
kill %1
```

---

## 🧪 Exercise 4: Kill by Name Using `pkill` and `killall`

1. **Start multiple processes:**

```bash
sleep 300 &
sleep 400 &
sleep 500 &
```

2. **Use `pkill` to terminate all at once:**

```bash
pkill sleep
```

3. **Or use `killall`:**

```bash
killall sleep
```

4. **Verify all have been terminated:**

```bash
ps aux | grep sleep
```

---

## 🧪 Exercise 5: Review Signals

1. **List available signals:**

```bash
kill -l
```

2. **Try sending a different signal (`SIGHUP`):**

```bash
kill -1 <PID>
```

Observe behavior (some daemons reload, some exit).

---

## 🧪 Exercise 6 (Optional): Interactive Killing with `htop`

1. **Install and run `htop`:**

```bash
sudo apt install htop -y
htop
```

2. **Navigate to a process using arrow keys, press `F9`, select `SIGKILL`, and press Enter.**

---

## 🔍 Post-Exercise Checklist

✅ Used `kill` with and without signals
✅ Used `%` Job ID for job-level termination
✅ Used `pkill` and `killall` for name-based termination
✅ Verified process status with `ps`, `jobs`, or `htop`
✅ Explored different signal types with `kill -l`

---

## ✅ Summary

* You can terminate processes using `kill`, `killall`, `pkill`, or interactively via `htop`.
* Default signal is `SIGTERM` (15), while `SIGKILL` (9) forcefully ends a process.
* You must use caution to avoid killing system-critical or other users’ processes.
* Job control allows killing suspended or background processes by `%job_id`.

---

## 9. 🔗 Related Topics

* Linux Signals (`kill -l`, `SIGTERM`, `SIGKILL`)
* Job Control (`fg`, `bg`, `jobs`)
* Shell Scripting Cleanup (`trap`, `kill`)
* Process Monitoring Tools (`ps`, `top`, `htop`)
* Daemon and Service Control (`systemctl`, `service`)

---

Would you like to try a **real-world challenge** involving automated process monitoring and termination using a bash script?

```
```
