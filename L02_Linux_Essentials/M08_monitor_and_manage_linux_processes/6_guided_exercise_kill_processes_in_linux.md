Absolutely, Shahid! Here's your professional, GitHub-friendly, and hands-on **Guided Exercise** for:

---

# 🧪 **Guided Exercise: Kill Processes in Linux**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 253*

---

## 🎯 Objective

In this exercise, you’ll practice:

* Finding process IDs (PIDs)
* Sending signals to processes (`SIGTERM`, `SIGKILL`)
* Using `kill`, `pkill`, and `killall`
* Gracefully and forcefully terminating running applications

> This is a core skill for any Linux administrator — helping with **system stability**, **troubleshooting**, and **incident response**.

---

## 🧰 Requirements

* A Linux system (VM, WSL, or native)
* Terminal access with sudo rights
* At least one running process (like `sleep`, `nano`, or `firefox`)

---

## 🧭 Step-by-Step Instructions

---

### 🔹 **Step 1: Start a Dummy Process**

Run a test process in the background:

```bash
sleep 300 &
```

✅ Note the job ID and PID. Use:

```bash
jobs
```

To get the PID:

```bash
ps -u $USER | grep sleep
```

---

### 🔹 **Step 2: Kill the Process Gracefully**

First, use the `kill` command to send the default signal (SIGTERM = `-15`):

```bash
kill <PID>
```

✅ Replace `<PID>` with the actual PID of the `sleep` command.

Check again with:

```bash
ps aux | grep sleep
```

✅ The process should now be gone.

---

### 🔹 **Step 3: Kill Another Process Forcefully**

Run another test:

```bash
sleep 600 &
```

Now kill it with `SIGKILL`:

```bash
kill -9 <PID>
```

✅ Use `ps` or `jobs` to verify it's terminated.

---

### 🔹 **Step 4: Use `pkill` to Kill by Name**

Start multiple instances:

```bash
sleep 1000 &
sleep 1000 &
```

Kill all `sleep` processes by name:

```bash
pkill sleep
```

✅ Confirm they are gone:

```bash
pgrep sleep
```

---

### 🔹 **Step 5: Use `killall` to Kill by Exact Name**

Try:

```bash
sleep 500 &
sleep 500 &
```

Then:

```bash
killall sleep
```

✅ `killall` only works on exact name matches, unlike `pkill`.

---

### 🔹 **Step 6: Try Killing a GUI App (If GUI Available)**

If you have a GUI app like `gedit`, launch it:

```bash
gedit &
```

Then:

```bash
xkill
```

✅ Your mouse will turn into a cross — click the window to close it.

---

### 🔹 **Step 7: View Available Signals**

```bash
kill -l
```

✅ This lists all signals like `SIGHUP`, `SIGKILL`, `SIGTERM`, `SIGSTOP`, etc.

---

## 📂 Summary of Commands Practiced

```bash
sleep 300 &
ps -u $USER | grep sleep
kill <PID>
kill -9 <PID>
pkill sleep
killall sleep
xkill
kill -l
```

---

## 🧠 Reflection Questions

1. What’s the difference between `kill -15` and `kill -9`?
2. When would you use `pkill` instead of `kill`?
3. How does `killall` differ from `pkill`?
4. What’s a safer signal to try before using `SIGKILL`?
5. Why should you avoid using `kill -9` unless necessary?

---

## ✅ Completion Checklist

| Task                                        | Status |
| ------------------------------------------- | ------ |
| Launched test processes                     | ✅      |
| Killed process using `kill`                 | ✅      |
| Used `kill -9` for force termination        | ✅      |
| Terminated processes using `pkill`          | ✅      |
| Used `killall` for exact name matches       | ✅      |
| Killed GUI app with `xkill` (if applicable) | ✅      |
| Listed all available signals                | ✅      |

---

## 📎 Summary

You now know how to:

* Find and terminate Linux processes safely
* Use signals effectively (`SIGTERM`, `SIGKILL`, etc.)
* Use `kill`, `pkill`, and `killall` for various use cases
* Apply process control in both terminal and GUI environments

> These tools give you precise control over your Linux system — essential for managing rogue apps, resource issues, and runtime debugging.

---

✅ Let me know if you'd like:

* 🧠 Quiz based on this lab
* 📥 Markdown version for GitHub
* ⏭️ Next topic: *Monitor Processes Using top and ps*

You’re now eliminating rogue processes like a skilled Linux sysadmin, Shahid 💻⚡ Keep dominating the shell!
