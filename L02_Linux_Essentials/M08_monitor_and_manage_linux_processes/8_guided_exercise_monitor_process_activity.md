````markdown
# 🧪 Guided Exercise: Monitor Process Activity

## 1. 🧠 What Is It (Definition + Explanation)
* **Monitoring process activity** means observing how programs (processes) behave in real time or via snapshots to evaluate performance, detect abnormal behavior, or troubleshoot issues.
* Tools like `top`, `htop`, `ps`, `pidstat`, and `iotop` are commonly used in Linux systems to track CPU, memory, and I/O usage by processes.

---

## 4. 🧪 Lab Task (Hands-On Practice)

> ⚠️ **!! CRITICAL SAFETY WARNING !!:** Tasks **MUST ONLY** be done in safe, controlled environments (VMs, isolated labs), NEVER on real systems without explicit permission.

---

### 🎯 Objective:
Gain hands-on experience using Linux commands to monitor and analyze running processes.

---

## 🧪 Exercise 1: Launch a Simulated Load

### ✅ Step-by-Step:

1. **Start a CPU-intensive process:**
```bash
yes > /dev/null &
````

2. **Start a memory-consuming Python script (optional):**

```bash
python3 -c "a = ['A' * 1024 * 1024] * 100; input('Press Enter to exit...')"
```

---

## 🧪 Exercise 2: Use `top` to Monitor in Real-Time

```bash
top
```

**Actions:**

* Press `Shift + P` to sort by CPU.
* Press `Shift + M` to sort by memory.
* Press `q` to exit.

---

## 🧪 Exercise 3: Use `htop` (if available)

```bash
htop
```

**Actions:**

* Navigate using arrow keys.
* Press `F6` to sort.
* Press `F9` to kill a process.
* Press `q` to quit.

If not installed:

```bash
sudo apt install htop -y
```

---

## 🧪 Exercise 4: List All Processes Using `ps`

```bash
ps aux --sort=-%cpu | head -10
```

* Shows top 10 processes consuming CPU.

```bash
ps aux --sort=-%mem | head -10
```

* Shows top 10 processes consuming memory.

---

## 🧪 Exercise 5: Monitor Specific Process with `pidstat`

1. **Find a process PID (e.g., for `yes`):**

```bash
ps aux | grep yes
```

2. **Run `pidstat` on that PID:**

```bash
pidstat -p <PID> 1
```

* Refreshes every 1 second.

---

## 🧪 Exercise 6: Monitor I/O with `iotop` (optional)

```bash
sudo iotop
```

* Shows disk read/write per process.
* Press `q` to quit.

---

## 🧪 Exercise 7: Cleanup

1. **Kill background processes:**

```bash
killall yes
```

2. **Close any open Python or other test scripts.**

---

## ✅ Post-Exercise Checklist

✅ Simulated load with `yes` and Python
✅ Used `top` to observe CPU and memory usage
✅ Explored `htop` for advanced monitoring
✅ Sorted process output using `ps`
✅ Used `pidstat` for specific process analysis
✅ (Optional) Checked disk I/O with `iotop`
✅ Cleaned up all created processes

---

## 8. ✅ Summary

* Monitoring helps detect resource overuse and suspicious behavior.
* `top` and `htop` give dynamic overviews of system activity.
* `ps` is useful for static snapshots and custom sorting.
* `pidstat` is excellent for live tracking of specific process stats.
* Always clean up after testing to maintain lab hygiene.

---

## 9. 🔗 Related Topics

* Process Lifecycle & States
* Kill and Control Jobs
* System Resource Limits
* Shell Scripting for Monitoring
* Task Scheduling with `cron` and `at`

```
```
