````markdown
# 🧠 Guided Exercise: Control Jobs

## 1. 🧠 What Is It (Definition + Explanation)
* **Control Jobs** refers to the shell feature that allows you to manage multiple processes (jobs) running in the terminal — whether in the foreground, background, or stopped.
* Using **job control**, you can pause (`Ctrl+Z`), resume (`fg` or `bg`), terminate (`kill`), or completely disown a process running from the shell, making terminal-based multitasking efficient and flexible.

---

## 4. 🧪 Lab Task (Hands-On Practice)

> ⚠️ **!! CRITICAL SAFETY WARNING !!:** Tasks **MUST ONLY** be done in safe, controlled environments (VMs, isolated labs), NEVER on real systems without explicit permission.

### 🎯 Objective:
Learn to create, manage, and control foreground and background jobs using `bash` in Linux.

---

## 🧪 Exercise 1: Run a Background Job

### ✅ Step-by-Step:

1. **Start a long-running command in background**
```bash
sleep 1000 &
````

2. **Observe output**

```
[1] 12345
```

* `[1]` → Job ID
* `12345` → PID of the job

3. **Check current jobs**

```bash
jobs
```

Expected Output:

```
[1]+  Running                 sleep 1000 &
```

---

## 🧪 Exercise 2: Stop a Foreground Job and Resume It

1. **Start a command in the foreground**

```bash
cat
```

* Now press `Ctrl+Z` to suspend it.

2. **View stopped job**

```bash
jobs
```

Expected Output:

```
[2]+  Stopped                 cat
```

3. **Resume in background**

```bash
bg %2
```

4. **Bring it back to foreground**

```bash
fg %2
```

(Press `Ctrl+C` to exit `cat`)

---

## 🧪 Exercise 3: Kill Jobs

1. **Start another background job**

```bash
sleep 500 &
```

2. **List jobs**

```bash
jobs
```

3. **Kill it using job ID**

```bash
kill %3
```

4. **Verify**

```bash
jobs
```

---

## 🧪 Exercise 4: Detach Job (Optional)

1. **Start another background job**

```bash
sleep 300 &
```

2. **Disown the job so it won’t terminate if the shell is closed**

```bash
disown %4
```

3. **Check `jobs`**

```bash
jobs
```

(The disowned job no longer appears in the list)

---

## 🧪 Exercise 5: Run and Redirect Output in Background

1. **Create a loop script**

```bash
echo -e '#!/bin/bash\nwhile true; do date; sleep 2; done' > dateloop.sh
chmod +x dateloop.sh
```

2. **Run in background with output redirected**

```bash
./dateloop.sh > output.txt 2>&1 &
```

3. **Watch the output file**

```bash
tail -f output.txt
```

4. **Stop it with `Ctrl+Z`, resume in background with `bg`, or kill it**

---

## 🔍 Post-Exercise Checklist:

✅ Used `&`, `fg`, `bg`, `jobs`, `kill`, and `disown`
✅ Observed behavior of foreground vs background jobs
✅ Managed jobs by Job ID `%n`
✅ Cleaned up and terminated running jobs

---

## ✅ Summary

* Use `sleep`, `cat`, and loops to simulate jobs.
* Use `&` to run jobs in background, `Ctrl+Z` to stop, `bg`/`fg` to resume.
* Use `jobs`, `kill`, and `disown` to control process lifecycle from the shell.
* Always manage jobs carefully to avoid orphaned or zombie processes.

---

## 9. 🔗 Related Topics

* Linux Signals (`kill`, `SIGTSTP`, `SIGINT`)
* Bash Shell Internals
* Daemons vs Jobs
* `nohup` for persistent background execution
* Process Trees and Parent-Child Relationships

---

Would you like a **bonus challenge** to simulate multiple job controls across two terminal sessions or integrate this into a shell script?

```
```
