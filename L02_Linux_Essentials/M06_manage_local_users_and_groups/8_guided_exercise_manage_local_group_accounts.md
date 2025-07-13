# 🧪 **Guided Exercise: Manage Local Group Accounts**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 180*

---

## 🎯 Objective

This exercise will help you gain hands-on experience with:

* Creating local groups
* Adding and removing users from groups
* Renaming and deleting groups
* Managing shared access using group permissions

> This is essential for **secure multi-user systems**, **file access management**, and **role-based privilege control** in Linux environments.

---

## 🧰 Prerequisites

* A Linux system with root or sudo access
* At least one test user account (e.g., `shahid`)
* A terminal session with basic CLI skills

---

## 🧭 Step-by-Step Instructions

---

### 🔹 **Step 1: Create a New Group**

```bash
sudo groupadd redteam
```

✅ This creates a new group named `redteam`.

Verify:

```bash
getent group redteam
```

---

### 🔹 **Step 2: Add an Existing User to the Group**

```bash
sudo usermod -aG redteam shahid
```

✅ This adds `shahid` to the `redteam` group **without removing existing group memberships**.

Verify:

```bash
groups shahid
```

✅ You should see `redteam` listed among the groups.

---

### 🔹 **Step 3: Create a Shared Directory for the Group**

```bash
sudo mkdir /opt/redteam_share
sudo chown :redteam /opt/redteam_share
sudo chmod 770 /opt/redteam_share
```

Explanation:

* Only members of `redteam` can read/write the directory.
* Others are denied access.

Test with a group member:

```bash
sudo -u shahid touch /opt/redteam_share/test.txt
```

✅ If successful, the group setup is working correctly.

---

### 🔹 **Step 4: Rename the Group**

```bash
sudo groupmod -n cyberops redteam
```

✅ Now `redteam` is called `cyberops`.

Verify:

```bash
getent group cyberops
```

✅ Check that `shahid` is still in the renamed group:

```bash
groups shahid
```

---

### 🔹 **Step 5: Remove the User from the Group (Advanced)**

To remove a user from a group, you can **redefine** their secondary groups:

```bash
sudo gpasswd -d shahid cyberops
```

Verify:

```bash
groups shahid
```

✅ `cyberops` should no longer be listed.

---

### 🔹 **Step 6: Delete the Group**

```bash
sudo groupdel cyberops
```

Verify:

```bash
getent group cyberops
```

✅ It should return nothing (group is deleted).

---

## 🔐 Real-World Use Cases

| Scenario                     | Why Group Control Is Useful             |
| ---------------------------- | --------------------------------------- |
| Team-based file sharing      | Share folders securely with `chmod 770` |
| Controlled admin privileges  | Add users to `sudo`, `docker`, `adm`    |
| Temporary project groups     | Remove group when project ends          |
| Pentesting labs or forensics | Group isolated analysis environments    |

---

## 📂 File System Structure (after setup)

```text
/opt/redteam_share/
└── test.txt      # Created by group member (shahid)
```

---

## 🧠 Reflection Questions

1. What’s the benefit of using groups instead of assigning file access to individual users?
2. Why is the `-aG` option in `usermod` important?
3. How does `chmod 770` protect the group share directory?
4. What happens if you remove a group that users still belong to?
5. How do you check if a user is a member of a group?

---

## ✅ Completion Checklist

| Task                                   | Done |
| -------------------------------------- | ---- |
| Created a new group                    | ✅    |
| Added user to group                    | ✅    |
| Verified membership                    | ✅    |
| Created a group-owned shared directory | ✅    |
| Renamed the group                      | ✅    |
| Removed user from group                | ✅    |
| Deleted the group                      | ✅    |

---

## 📎 Summary

You’ve now learned how to:

* Create and manage Linux groups
* Add and remove users from groups
* Set group ownership on shared directories
* Use groups to **enforce security policies** and **access control**