# 🧪 **Guided Exercise: Manage Local User Accounts**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 174*

---

## 🎯 Objective

In this guided lab, you’ll learn how to:

* Create and manage local user accounts
* Set and reset user passwords
* Lock, unlock, and expire user accounts
* Modify user account details
* Delete user accounts securely

> These tasks are essential for **user access control**, **privilege separation**, and **compliance enforcement** in real-world Linux systems.

---

## 🧰 Prerequisites

* A Linux system with sudo/root access
* Terminal access (locally or via SSH)
* Basic knowledge of the shell

---

## 🧭 Step-by-Step Instructions

---

### 🔹 **Step 1: Create a New User**

```bash
sudo useradd -m analyst
```

Explanation:

* `-m` creates the user’s home directory (`/home/analyst`)
* The system copies default configs from `/etc/skel`

Check the user:

```bash
cat /etc/passwd | grep analyst
```

---

### 🔹 **Step 2: Set a Password for the New User**

```bash
sudo passwd analyst
```

✅ Set a strong, temporary password.

---

### 🔹 **Step 3: Force Password Change at First Login**

```bash
sudo chage -d 0 analyst
```

Check result:

```bash
sudo chage -l analyst
```

---

### 🔹 **Step 4: Modify the User’s Shell and Comment**

```bash
sudo usermod -s /bin/zsh -c "Cyber Security Analyst" analyst
```

✅ This sets:

* Shell: `/bin/zsh`
* GECOS field: User's full name/comment

Verify:

```bash
grep analyst /etc/passwd
```

---

### 🔹 **Step 5: Lock and Unlock the User Account**

Lock the account:

```bash
sudo usermod -L analyst
```

Try switching to the account:

```bash
su - analyst
```

✅ You should get an authentication failure (account is locked).

Now unlock:

```bash
sudo usermod -U analyst
```

---

### 🔹 **Step 6: Set an Account Expiry Date**

```bash
sudo chage -E 2025-12-31 analyst
```

✅ This will automatically disable the account on Dec 31, 2025.

Verify:

```bash
sudo chage -l analyst
```

---

### 🔹 **Step 7: Delete the User Account Safely**

```bash
sudo userdel -r analyst
```

* `-r` removes the user’s home directory too.
* Always confirm with:

```bash
ls /home/analyst
```

✅ You should see: `No such file or directory`

---

## 🔐 Security Best Practices

| Task                           | Why It's Important                    |
| ------------------------------ | ------------------------------------- |
| Force password change          | Prevents reuse of default credentials |
| Locking unused accounts        | Blocks access without deleting data   |
| Setting expiry for contractors | Enforces time-bound access            |
| Deleting unneeded accounts     | Minimizes attack surface              |

---

## 📂 Final State Summary

```text
Created user: analyst
Set password: Yes
Forced password reset: Yes
Shell changed: /bin/zsh
Account locked/unlocked: Tested
Expiry date: Set to 2025-12-31
Deleted user and home directory: Verified
```

---

## 🧠 Reflection Questions

1. What’s the difference between `usermod -L` and `userdel`?
2. Why is it a good idea to force password changes for new accounts?
3. What happens if you forget the `-r` flag when deleting a user?
4. Which file lists all users on the system?
5. How can you verify that an account is locked or expired?

---

## ✅ Completion Checklist

| Task                              | Done |
| --------------------------------- | ---- |
| Created new user                  | ✅    |
| Set and changed password          | ✅    |
| Modified user comment and shell   | ✅    |
| Locked and unlocked the account   | ✅    |
| Set expiry date                   | ✅    |
| Deleted user and verified cleanup | ✅    |

---

## 📎 Summary

You’ve now learned how to:

* Create and manage Linux user accounts securely
* Control access lifecycles with locks and expirations
* Modify user details using `usermod`, `chage`, `passwd`, and `userdel`
* Protect your system using principle of least privilege and access expiry