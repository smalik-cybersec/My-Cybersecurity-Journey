# 🧪 **Lab: Manage Local Users and Groups**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 191*

---

## 🎯 Objective

To practice creating, modifying, and managing **local users and groups** using command-line tools on a Linux system. You'll apply what you’ve learned about user account creation, password policies, group memberships, account locking, and deletions.

> These operations are **essential** for system security, role-based access, and daily Linux system administration.

---

## 🧰 Requirements

* A Linux system with terminal access
* Sudo/root privileges
* Basic familiarity with CLI tools
* Users and groups will be created **temporarily for lab use**

---

## 🧭 Lab Instructions

---

### 🔹 **Step 1: Create Two Local Users**

```bash
sudo useradd -m analyst
sudo useradd -m engineer
```

✅ Each will have a home directory in `/home/`.

Set passwords:

```bash
sudo passwd analyst
sudo passwd engineer
```

---

### 🔹 **Step 2: Force Password Change on First Login**

```bash
sudo chage -d 0 analyst
sudo chage -d 0 engineer
```

✅ This ensures they must update the password upon login.

---

### 🔹 **Step 3: Create a New Group and Add Both Users**

```bash
sudo groupadd devteam
sudo usermod -aG devteam analyst
sudo usermod -aG devteam engineer
```

Verify:

```bash
groups analyst
groups engineer
```

✅ You should see `devteam` included.

---

### 🔹 **Step 4: Create a Shared Folder for the Group**

```bash
sudo mkdir /opt/devteam_share
sudo chown :devteam /opt/devteam_share
sudo chmod 770 /opt/devteam_share
```

✅ Only users in the group `devteam` can access and write to the folder.

---

### 🔹 **Step 5: Set Password Expiry and Policies**

```bash
sudo chage -M 60 -m 7 -W 5 analyst
sudo chage -M 60 -m 7 -W 5 engineer
```

✅ This sets:

* Max age: 60 days
* Min age: 7 days
* Warning: 5 days before expiry

View settings:

```bash
sudo chage -l analyst
sudo chage -l engineer
```

---

### 🔹 **Step 6: Lock and Unlock Accounts**

Lock the `engineer` account:

```bash
sudo usermod -L engineer
```

Try switching:

```bash
su - engineer
```

✅ Should result in **authentication failure**.

Unlock the account:

```bash
sudo usermod -U engineer
```

---

### 🔹 **Step 7: Clean Up – Remove Users and Groups**

```bash
sudo userdel -r analyst
sudo userdel -r engineer
sudo groupdel devteam
```

✅ Confirm removal:

```bash
getent passwd analyst
getent passwd engineer
getent group devteam
```

---

## 📂 Lab File/Directory Structure

```text
/opt/devteam_share/
└── Shared folder owned by group `devteam`

/home/analyst/
└── User home (removed at end)

/home/engineer/
└── User home (removed at end)
```

---

## 🧠 Reflection Questions

1. What’s the difference between `useradd -m` and `useradd` without `-m`?
2. Why is forcing a password reset on first login important?
3. How does group-based sharing help reduce permission complexity?
4. Why is it recommended to expire passwords and set aging policies?
5. What happens to files owned by a user after their account is deleted?

---

## ✅ Completion Checklist

| Task                                    | Done |
| --------------------------------------- | ---- |
| Created two users with passwords        | ✅    |
| Forced password reset                   | ✅    |
| Created group and added users           | ✅    |
| Created shared folder with group access | ✅    |
| Configured password aging               | ✅    |
| Locked and unlocked account             | ✅    |
| Deleted users and group                 | ✅    |

---

## 📎 Summary

This lab gave you real-world experience in:

* Managing local Linux users and groups
* Setting password and account policies
* Enforcing secure, shared resource access
* Cleaning up users and groups responsibly

> These are the **core building blocks** of identity and access management on Linux systems.
