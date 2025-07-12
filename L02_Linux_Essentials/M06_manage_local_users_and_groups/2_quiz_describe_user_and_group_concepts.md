Certainly, Shahid! Here is your **complete quiz** for:

---

# 🧠 **Quiz: Describe User and Group Concepts**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 157*

---

## 📋 Instructions

* **Total Questions**: 15
* **Format**: 10 Multiple Choice + 5 Short Answer
* **Passing Score**: 11/15
* **Focus**: Linux user types, UID/GID, group roles, system files, access control

---

## ✨ Multiple Choice Questions (MCQs)

**1. What is the UID of the root user?**
A. 1
B. 999
C. 0
D. 1000

---

**2. Which file contains information about all Linux user accounts?**
A. `/etc/group`
B. `/etc/shadow`
C. `/etc/passwd`
D. `/etc/users`

---

**3. What command will show the current user’s UID and group information?**
A. `whoami`
B. `groups`
C. `id`
D. `echo $USER`

---

**4. What is the purpose of the `/etc/shadow` file?**
A. Stores home directories
B. Lists groups and members
C. Contains hashed user passwords
D. Stores login history

---

**5. A user can belong to how many **primary** groups?**
A. Zero
B. One
C. Unlimited
D. Multiple

---

**6. A user can belong to how many **supplementary** groups?**
A. One
B. None
C. Only 2
D. Multiple

---

**7. Which of the following creates a new group?**
A. `useradd groupname`
B. `groupadd groupname`
C. `addgroup user`
D. `usermod -g groupname`

---

**8. Which of the following files contains the list of all groups?**
A. `/etc/group`
B. `/etc/passwd`
C. `/etc/login.defs`
D. `/etc/sudoers`

---

**9. What does the following command do?
`sudo usermod -aG wheel shahid`**
A. Adds user `shahid` to the `wheel` group
B. Removes user `shahid` from wheel
C. Creates a new user group
D. Changes `shahid`’s UID

---

**10. What type of user is created with UID 1000 or above?**
A. Root user
B. System account
C. Regular login user
D. Administrator account

---

## ✏️ Short Answer Questions

**11. What is the difference between a primary group and a supplementary group?**
→ *Your Answer:*

---

**12. How would you create a new user named `cyberuser` with a home directory?**
→ *Your Answer:*

---

**13. Which command removes a user and their home directory from the system?**
→ *Your Answer:*

---

**14. What are two purposes of groups in Linux access control?**
→ *Your Answer:*

---

**15. How can you view the group memberships of a user named `shahid`?**
→ *Your Answer:*

---

## ✅ Bonus Challenge (Optional)

Write a sequence of commands that:

* Creates a user `analyst`
* Creates a group `cyberops`
* Adds `analyst` to `cyberops` as a secondary group

→ *Your Answer:*

```bash
sudo useradd -m analyst
sudo groupadd cyberops
sudo usermod -aG cyberops analyst
```

---

Let me know if you’d like:

* ✅ Answer key
* 📥 Markdown format for GitHub
* ⏭️ Next topic: *Manage Local User and Group Accounts*

You're learning the **identity and access control engine of Linux**, Shahid 🔐💻 Keep going strong!
