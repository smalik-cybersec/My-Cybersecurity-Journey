# Lab: Manage Local Users and Groups

### 1. Objective
> The objective of this lab is to gain hands-on experience in creating, modifying, and deleting local user and group accounts, as well as managing user passwords and group memberships on a Linux system.

---

### 2. Steps & Commands

---

**Step 1: Create a New User and Group**  
**Description:** Create a new user named `sysadmin_alpha` and a new group named `project_team`.

```bash
sudo useradd -m -s /bin/bash sysadmin_alpha
sudo groupadd project_team
```

---

**Step 2: Set Password for the New User**  
**Description:** Set a secure password for `sysadmin_alpha`. You will be prompted to type the password.

```bash
sudo passwd sysadmin_alpha
```

---

**Step 3: Add the User to the New Group**  
**Description:** Add `sysadmin_alpha` to the `project_team` group as a supplementary group.

```bash
sudo gpasswd -a sysadmin_alpha project_team
```

---

**Step 4: Verify User and Group Creation/Membership**  
**Description:** Check if the user and group were created successfully and verify `sysadmin_alpha`'s group membership.

```bash
grep sysadmin_alpha /etc/passwd
grep project_team /etc/group
groups sysadmin_alpha
```

---

**Step 5: Create Another User and Add to Multiple Groups**  
**Description:** Create a user `developer_beta` and add them to both `project_team` and the `sudo` group (or `wheel` group on RHEL-based systems) if you want them to have administrative capabilities.

```bash
sudo useradd -m -s /bin/bash developer_beta
sudo gpasswd -a developer_beta project_team
sudo gpasswd -a developer_beta sudo   # Use this on Debian/Ubuntu
# sudo gpasswd -a developer_beta wheel   # Use this on RHEL/CentOS
```

---

**Step 6: Change User's Primary Group**  
**Description:** Change `developer_beta`'s primary group to `project_team`.

```bash
sudo usermod -g project_team developer_beta
```

**Verification:**

```bash
id developer_beta
```

---

**Step 7: Implement Password Aging Policy for a User**  
**Description:** Force `sysadmin_alpha` to change their password every 60 days, and give them a 7-day warning.

```bash
sudo chage -M 60 -W 7 sysadmin_alpha
```

**Verification:**

```bash
sudo chage -l sysadmin_alpha
```

---

**Step 8: Lock and Unlock a User Account**  
**Description:** Temporarily lock `developer_beta`'s account to prevent login, then unlock it.

```bash
sudo passwd -l developer_beta
# Attempt to login as developer_beta now (it should fail).

sudo passwd -u developer_beta
# Attempt to login as developer_beta now (it should succeed).
```

---

**Step 9: Delete User and Group Accounts**  
**Description:** Clean up the system by deleting the created users and groups. Ensure home directories are removed.

```bash
sudo userdel -r sysadmin_alpha
sudo userdel -r developer_beta
sudo groupdel project_team
```

**Verification:**

```bash
grep sysadmin_alpha /etc/passwd || echo "sysadmin_alpha deleted."
grep developer_beta /etc/passwd || echo "developer_beta deleted."
grep project_team /etc/group || echo "project_team deleted."
```

---

### 3. Key Takeaway

Successfully performing these lab exercises demonstrates a practical understanding of Linux user and group management. This is foundational for securing systems through proper access control and user lifecycle management.
