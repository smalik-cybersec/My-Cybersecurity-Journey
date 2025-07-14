# 🧪 **Lab: Control Access to Files**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 224*

---

## 🎯 Objective

This lab will give you hands-on practice with:

* Managing file and directory **access control** using standard Linux permissions
* Setting ownership and group assignments
* Using `chmod`, `chown`, and `umask` to secure file access
* Understanding how to restrict, share, or isolate access effectively

> This lab supports practical enforcement of the **principle of least privilege**, a key concept in cybersecurity and system administration.

---

## 🧰 Requirements

* Linux system with terminal access
* A sudo-enabled user (e.g. `shahid`)
* Basic knowledge of Linux file permissions (`r`, `w`, `x`)

---

## 🧭 Step-by-Step Instructions

---

### 🔹 **Step 1: Prepare Lab Environment**

```bash
mkdir ~/accesslab && cd ~/accesslab
touch confidential.txt teamdoc.txt publicinfo.txt
mkdir project_dir private_dir
```

✅ This creates three files and two directories for permission testing.

---

### 🔹 **Step 2: Assign Ownership and Group**

Create a new group for team access:

```bash
sudo groupadd teamgrp
sudo usermod -aG teamgrp shahid
```

Now change group ownership of the shared file and directory:

```bash
sudo chgrp teamgrp teamdoc.txt
sudo chgrp teamgrp project_dir
```

✅ These are now group-managed resources.

---

### 🔹 **Step 3: Set Permissions**

**1. Confidential file (owner-only access):**

```bash
chmod 600 confidential.txt
```

**2. Team file (read/write for group):**

```bash
chmod 660 teamdoc.txt
```

**3. Public file (read-only for all):**

```bash
chmod 644 publicinfo.txt
```

**4. Private directory (user-only):**

```bash
chmod 700 private_dir
```

**5. Project directory (shared access for group):**

```bash
chmod 770 project_dir
```

✅ Check all with:

```bash
ls -l
```

---

### 🔹 **Step 4: Test Access (Optional Advanced)**

To verify group access:

```bash
sudo su -l shahid
cd ~/accesslab
touch project_dir/test.sh
```

✅ If the directory permissions are set correctly, the user in the `teamgrp` group should be able to create files.

---

### 🔹 **Step 5: Use umask to Prevent Overexposure**

Temporarily restrict new file creation:

```bash
umask 0077
touch secrets.txt
ls -l secrets.txt
```

✅ Should result in:

```bash
-rw------- 1 shahid shahid 0 secrets.txt
```

---

## 🔐 Security Context Recap

| Object             | Permissions | Purpose                           |
| ------------------ | ----------- | --------------------------------- |
| `confidential.txt` | `600`       | Owner-only sensitive data         |
| `teamdoc.txt`      | `660`       | Collaborative edit by team        |
| `publicinfo.txt`   | `644`       | Readable by anyone                |
| `project_dir/`     | `770`       | Group-based shared work           |
| `private_dir/`     | `700`       | Owner-only secured area           |
| `secrets.txt`      | `600`       | Created under restrictive `umask` |

---

## 📂 Final Lab Structure

```text
~/accesslab/
├── confidential.txt   → rw-------
├── teamdoc.txt        → rw-rw----
├── publicinfo.txt     → rw-r--r--
├── secrets.txt        → rw-------
├── private_dir/       → rwx------
└── project_dir/       → rwxrwx---
    └── test.sh        → (created by group user)
```

---

## 🧠 Reflection Questions

1. What permissions would you set to allow only the user and group to read/write a file?
2. Why is `chmod 600` ideal for confidential files?
3. How can a misconfigured `umask` lead to overexposed files?
4. What is the key difference between `chmod 770` and `chmod 777`?
5. How do `chmod`, `chown`, and `chgrp` work together to enforce access?

---

## ✅ Completion Checklist

| Task                                         | Done |
| -------------------------------------------- | ---- |
| Created sample files and directories         | ✅    |
| Assigned group ownership                     | ✅    |
| Set file and folder permissions with `chmod` | ✅    |
| Used `umask` to create secure files          | ✅    |
| Verified correct permission behavior         | ✅    |

---

## 📎 Summary

You now have practical experience with:

* Enforcing secure access with `chmod`
* Controlling ownership with `chown` and `chgrp`
* Using `umask` to control default permissions
* Applying different permission schemes for private, shared, and public content

> This lab teaches you to **proactively control file access**, minimizing security risks and enabling proper collaboration in multi-user environments.
