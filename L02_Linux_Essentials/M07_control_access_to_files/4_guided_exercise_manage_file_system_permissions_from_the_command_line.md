# 🧪 **Guided Exercise: Manage File System Permissions from the Command Line**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 212*

---

## 🎯 Objective

This exercise will teach you how to **read**, **interpret**, and **change file and directory permissions** using `chmod`, `chown`, and `chgrp` on the command line.

> These operations are essential for securing files, controlling access, and following the principle of least privilege on Linux systems.

---

## 🧰 Prerequisites

* A Linux terminal with sudo privileges
* Basic understanding of the Linux permission model (`r`, `w`, `x`)
* A test user (e.g., `shahid`) and optional group (`projectx`)

---

## 🧭 Step-by-Step Lab Instructions

---

### 🔹 **Step 1: Create Test Files and Directories**

```bash
mkdir ~/permlab && cd ~/permlab

touch file1.txt file2.sh
mkdir shared_dir private_dir
```

✅ This creates 2 files and 2 directories for testing.

---

### 🔹 **Step 2: Check Current Permissions**

```bash
ls -l
```

Expected output:

```bash
-rw-r--r-- 1 shahid shahid 0 Jul 12  file1.txt
-rw-r--r-- 1 shahid shahid 0 Jul 12  file2.sh
drwxr-xr-x 2 shahid shahid 4096 Jul 12 shared_dir/
drwxr-xr-x 2 shahid shahid 4096 Jul 12 private_dir/
```

---

### 🔹 **Step 3: Modify Permissions Using Symbolic Mode**

```bash
chmod u+x file2.sh       # Make script executable by user
chmod g-w file1.txt       # Remove write access from group
chmod o= file1.txt        # Remove all permissions from others
```

✅ Check result:

```bash
ls -l
```

You should see changes like:

```bash
-rw-r----- 1 shahid shahid 0 file1.txt
-rwxr--r-- 1 shahid shahid 0 file2.sh
```

---

### 🔹 **Step 4: Modify Permissions Using Numeric (Octal) Mode**

```bash
chmod 700 private_dir     # Full access to user only
chmod 775 shared_dir      # Full access to user/group, read-exec for others
```

✅ Check again:

```bash
ls -ld private_dir shared_dir
```

---

### 🔹 **Step 5: Change File Ownership and Group**

Create a new group:

```bash
sudo groupadd projectx
sudo usermod -aG projectx shahid
```

Change group and ownership:

```bash
sudo chown shahid:projectx file1.txt
sudo chgrp projectx shared_dir
```

✅ Check result:

```bash
ls -l
```

---

### 🔹 **Step 6: Recursive Permission Change (Bonus)**

Make everything in the `permlab` directory **owner-only accessible**:

```bash
chmod -R 700 ~/permlab
```

---

## 📂 Final File Structure Snapshot

```text
~/permlab/
├── file1.txt       # rw-r----- (shahid:projectx)
├── file2.sh        # rwxr--r-- (shahid:shahid)
├── private_dir/    # rwx------ (700)
└── shared_dir/     # rwxrwxr-x (775)
```

---

## 🔐 Security Practices Tested

| Action                          | Benefit                               |
| ------------------------------- | ------------------------------------- |
| Removed group/other permissions | Prevented unauthorized access         |
| Made script executable          | Enabled safe execution by owner only  |
| Restricted private directory    | Protected confidential content        |
| Used `-R` flag cautiously       | Enforced consistency across hierarchy |

---

## 🧠 Reflection Questions

1. What does `chmod 700` do to a file or folder?
2. Why is `chmod o=` more secure than `chmod o-rwx`?
3. How do you change a file’s group ownership without affecting its user?
4. When would you use `chmod -R` and what risk does it pose?
5. How does setting executable permissions differ between files and directories?

---

## ✅ Completion Checklist

| Task                                         | Done |
| -------------------------------------------- | ---- |
| Created test files and directories           | ✅    |
| Used `chmod` with symbolic and numeric modes | ✅    |
| Changed ownership with `chown` and `chgrp`   | ✅    |
| Recursively changed permissions              | ✅    |
| Verified each change using `ls -l`           | ✅    |

---

## 📎 Summary

You now know how to:

* Safely modify permissions using `chmod`
* Change file owners and groups with `chown` and `chgrp`
* Interpret symbolic vs numeric permission formats
* Apply recursive permissions in a controlled way
* Set up secure file environments using the command line

> This lab strengthens your ability to **enforce access control** and **lock down sensitive data** — a critical Linux admin and cybersecurity skill.