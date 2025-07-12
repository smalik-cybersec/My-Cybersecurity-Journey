Absolutely, Shahid! Here's your complete, professional-grade **Guided Exercise** for:

---

# 🧪 **Guided Exercise: Manage User Passwords**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 187*

---

## 🎯 Objective

To practice secure and effective **password management** for Linux user accounts using command-line tools. You'll learn to:

* Set and reset passwords
* Enforce password changes
* Configure password aging and expiration
* Apply password warning and lockout policies

> These are critical for system hardening, user lifecycle control, and cybersecurity compliance.

---

## 🧰 Prerequisites

* A Linux system (Red Hat-based or similar)
* A user account with `sudo` privileges
* A test user (we’ll use `analyst`)
* Terminal access

---

## 🧭 Step-by-Step Instructions

---

### 🔹 **Step 1: Create a Test User**

```bash
sudo useradd -m analyst
```

Now set the password:

```bash
sudo passwd analyst
```

✅ Set a temporary password (e.g., `Cyber@123`). User should change it later.

---

### 🔹 **Step 2: Force Password Change at Next Login**

```bash
sudo chage -d 0 analyst
```

Check the status:

```bash
sudo chage -l analyst
```

✅ You should see “Password must be changed”.

---

### 🔹 **Step 3: Set Password Expiry Policy**

Set the password to expire every **60 days**:

```bash
sudo chage -M 60 analyst
```

Set a minimum of **7 days** between password changes:

```bash
sudo chage -m 7 analyst
```

Warn the user **5 days** before expiration:

```bash
sudo chage -W 5 analyst
```

Set an account expiration date:

```bash
sudo chage -E 2025-12-31 analyst
```

Verify again:

```bash
sudo chage -l analyst
```

✅ This should now show:

* Max days: 60
* Min days: 7
* Warning: 5
* Expiration: 2025-12-31

---

### 🔹 **Step 4: Test Password Reset**

Try resetting the password for `analyst`:

```bash
sudo passwd analyst
```

✅ This is often needed by sysadmins during account recovery.

---

### 🔹 **Step 5: Lock and Unlock the Account (Bonus)**

Lock the user account:

```bash
sudo usermod -L analyst
```

Try switching:

```bash
su - analyst
```

✅ You should get an authentication failure.

Now unlock:

```bash
sudo usermod -U analyst
```

---

## 🔐 Security Practices During Lab

| Action                       | Security Benefit                          |
| ---------------------------- | ----------------------------------------- |
| Enforced first-login change  | Prevents reuse of default passwords       |
| Password expiration          | Reduces long-term exposure                |
| Minimum days between changes | Stops quick cycling back to old passwords |
| Warning period               | Gives users time to change credentials    |
| Account lock                 | Disables unused or suspicious accounts    |

---

## 📂 Lab Summary

```text
User: analyst
Password: Set and reset
First login change: Enforced
Max days: 60
Min days: 7
Warning: 5 days
Expiry date: 2025-12-31
Account locked and unlocked: Verified
```

---

## 🧠 Reflection Questions

1. Why is it recommended to force a password change on first login?
2. What does `-M` in `chage` stand for?
3. How can setting a minimum change interval prevent abuse?
4. When should you lock vs. expire a user account?
5. Which file stores the password aging and expiry data?

---

## ✅ Completion Checklist

| Task                               | Status |
| ---------------------------------- | ------ |
| Created test user                  | ✅      |
| Set password                       | ✅      |
| Forced password reset              | ✅      |
| Configured password aging policies | ✅      |
| Set account expiry                 | ✅      |
| Locked and unlocked user account   | ✅      |

---

## 📎 Summary

You’ve now practiced:

* Assigning and managing user passwords
* Configuring password expiry, warning, and change intervals
* Locking accounts and enforcing first-time password updates
* Using `passwd`, `chage`, and `usermod` for password lifecycle control

> Password management is a key line of defense in any secure system.

---

✅ Let me know if you’d like:

* 🧠 Quiz based on this lab
* 📥 Markdown or PDF export for GitHub
* ⏭️ Next lesson: *Understand and Modify File Permissions*

You’re hardening your system one password at a time, Shahid 🔐💪 Keep going strong!
