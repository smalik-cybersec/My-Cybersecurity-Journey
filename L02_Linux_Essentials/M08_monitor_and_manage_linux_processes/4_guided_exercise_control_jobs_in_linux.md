# 🧪 **Guided Exercise: Control Jobs in Linux**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 242*

---

## 🎯 Objective

This exercise will help you gain practical experience with:

* Running jobs in the **background and foreground**
* **Suspending**, **resuming**, and **terminating** jobs
* Using `jobs`, `fg`, `bg`, `kill`, and `disown` commands to control shell-managed jobs

> Job control is essential for multitasking in terminal sessions, managing long-running tasks, and handling background processes efficiently.

---

## 🧰 Prerequisites

* A Linux system (physical or virtual machine)
* Terminal access as a regular user (e.g., `shahid`)
* Basic command-line knowledge

---

## 🧭 Step-by-Step Instructions

---

### 🔹 **Step 1: Start a Foreground Process and Suspend It**

Run a command that stays active:

```bash
gedit &
```

✅ If GUI apps aren’t available, use a shell command like:

```bash
sleep 300
```

Now **suspend it** by pressing:

```
Ctrl + Z
```

✅ The terminal should output:

```
[1]+  Stopped  sleep 300
```

---

### 🔹 **Step 2: View Active Jobs**

```bash
jobs
```

You will see output like:

```bash
[1]+  Stopped  sleep 300
```

✅ Job ID is shown in brackets (e.g., `%1`)

---

### 🔹 **Step 3: Resume the Job in Background**

```bash
bg %1
```

✅ Output confirms that the job is now running in the background.

---

### 🔹 **Step 4: Bring the Job to Foreground**

```bash
fg %1
```

✅ The process will take control of the terminal again.

---

### 🔹 **Step 5: Start Multiple Jobs in Background**

```bash
sleep 500 &
sleep 600 &
```

✅ You now have multiple background jobs. Run:

```bash
jobs
```

Example output:

```bash
[2]-  Running  sleep 500 &
[3]+  Running  sleep 600 &
```

---

### 🔹 **Step 6: Terminate a Background Job**

Use the job ID with `kill`:

```bash
kill %2
```

✅ This sends SIGTERM. To force it:

```bash
kill -9 %2
```

---

### 🔹 **Step 7: Disown a Background Job**

Start a background job:

```bash
sleep 900 &
```

Find the job ID, then run:

```bash
disown %4
```

✅ Now this job will **not be terminated** even if you close the terminal.

---

## 🧪 Bonus: Check Process Info via `ps`

```bash
ps -u $USER | grep sleep
```

✅ Useful to confirm that the job is still running in the background.

---

## 📂 Final Commands Used

```bash
sleep 300
Ctrl + Z
jobs
bg %1
fg %1
sleep 500 &
sleep 600 &
kill %2
kill -9 %3
disown %4
```

---

## 🧠 Reflection Questions

1. What is the difference between using `&` and `Ctrl + Z`?
2. When might you want to use `disown` before closing a terminal session?
3. How does `fg` differ from `bg` in job control?
4. What happens if you forget to disown a job and close the terminal?
5. Can you view jobs started in a different shell session?

---

## ✅ Completion Checklist

| Task                                     | Done |
| ---------------------------------------- | ---- |
| Ran job in foreground and suspended it   | ✅    |
| Resumed job in background                | ✅    |
| Brought job back to foreground           | ✅    |
| Started multiple background jobs         | ✅    |
| Terminated job using `kill`              | ✅    |
| Disowned a job                           | ✅    |
| Confirmed job state with `jobs` and `ps` | ✅    |

---

## 📎 Summary

You’ve now practiced:

* Suspending and resuming jobs
* Managing multiple foreground/background jobs
* Using `jobs`, `fg`, `bg`, `kill`, and `disown`
* Making processes persistent even after terminal closes

> This skill is essential for **working with long-running tasks**, **multitasking in the shell**, and **session control** as a Linux user or admin.
