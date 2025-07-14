# 🧪 **Guided Exercise: Manage Default Permissions and File Access**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 220*

---

## 🎯 Objective

In this guided lab, you will:

* Understand how **default permissions** are applied via `umask`
* Modify and verify `umask` behavior for both **temporary** and **persistent** sessions
* Apply real-world access control use cases for privacy and group collaboration

> This exercise is essential for system hardening, privacy enforcement, and preventing misconfigured file permissions.

---

## 🧰 Requirements

* Linux system (local or VM)
* A non-root user with sudo rights (e.g., `shahid`)
* Terminal access with basic file permission knowledge

---

## 🧭 Step-by-Step Instructions

---

### 🔹 **Step 1: Check Your Current umask Value**

```bash
umask
```

✅ You might see `0022` or `0002`. This controls the default permission **mask**.

---

### 🔹 **Step 2: Create Test Files and Observe Permissions**

```bash
mkdir ~/umasklab && cd ~/umasklab

touch file1.txt
mkdir dir1

ls -l
```

Check output:

```bash
-rw-r--r-- 1 shahid shahid 0 file1.txt
drwxr-xr-x 2 shahid shahid 4096 dir1
```

> ✅ This shows that umask removed write access from **group and others**.

---

### 🔹 **Step 3: Change umask Temporarily**

Set a stricter umask:

```bash
umask 0077
```

Then create:

```bash
touch file2.txt
mkdir dir2
```

Check again:

```bash
ls -l
```

Expected output:

```bash
-rw------- 1 shahid shahid 0 file2.txt
drwx------ 2 shahid shahid 4096 dir2
```

✅ These are **owner-only access** permissions — suitable for confidential data.

---

### 🔹 **Step 4: Reset umask and Create Group-Shared Resources**

```bash
umask 0002
touch file3.txt
mkdir dir3
```

Check permissions:

```bash
ls -l
```

Expected:

```bash
-rw-rw-r-- 1 shahid shahid 0 file3.txt
drwxrwxr-x 2 shahid shahid 4096 dir3
```

✅ Useful when collaborating with a shared group (e.g., developers or sysadmins).

---

### 🔹 **Step 5: Make umask Permanent for Your User**

Open your shell startup file:

```bash
nano ~/.bashrc
```

Add this line at the end:

```bash
umask 0027
```

Explanation:

* Files will be: `rw-r-----`
* Dirs will be: `rwxr-x---`

Save and apply:

```bash
source ~/.bashrc
```

✅ Now test it:

```bash
touch file4.txt
mkdir dir4
ls -l
```

---

## 🔐 Real-World Use Case Matrix

| Scenario                        | Recommended umask | Purpose                        |
| ------------------------------- | ----------------- | ------------------------------ |
| Private documents               | `0077`            | Restrict all access to owner   |
| Shared project folder           | `0002`            | Allow group collaboration      |
| Secure configuration management | `0027`            | Group read-only, private write |
| Public web directory (rare)     | `0022`            | Allow global read-only         |

---

## 📂 Final Lab Structure

```text
~/umasklab/
├── file1.txt  → rw-r--r--
├── file2.txt  → rw-------
├── file3.txt  → rw-rw-r--
├── file4.txt  → rw-r-----
├── dir1       → rwxr-xr-x
├── dir2       → rwx------
├── dir3       → rwxrwxr-x
└── dir4       → rwxr-x---
```

---

## 🧠 Reflection Questions

1. What is the difference between `umask 0022` and `0077`?
2. Why are newly created **files** never automatically executable?
3. How does `umask` differ from `chmod`?
4. What’s the best `umask` for a personal shell environment with confidential files?
5. How do you make sure your umask changes apply on every login?

---

## ✅ Completion Checklist

| Task                                        | Status |
| ------------------------------------------- | ------ |
| Checked current umask                       | ✅      |
| Created files with default and custom umask | ✅      |
| Changed umask temporarily                   | ✅      |
| Made umask persistent via `.bashrc`         | ✅      |
| Verified permissions for each scenario      | ✅      |

---

## 📎 Summary

You now know how to:

* View and interpret `umask` values
* Use `umask` to enforce secure defaults for file creation
* Apply different access policies for private, group, and shared scenarios
* Persist umask changes for every session

> This is a critical part of **proactive security** — ensuring files and directories start secure by default.
