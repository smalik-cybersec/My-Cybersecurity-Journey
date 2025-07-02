# Can you create a lab session for all the topics which we covered in this module? Everything and every concept you have to separately include every command, every concept from every topic. You have to create that kind of lab session which is very interactive, which is very friendly, which is nice to read, which will demonstrate my expertise, which will upskill me. That kind of lab session you have to create for all the sessions which we discussed. So, actually, no problem. It can be text. I will convert it into markdown later.

Here is a **comprehensive, interactive lab session** that covers every major concept and command from your Red Hat RH124 module on managing users, groups, permissions, and file access. Each section is clearly explained, includes hands-on steps, and is designed to both *teach* and *demonstrate* your expertise. You can copy this text and convert it to markdown as needed.

# Linux User, Group, and File Access Mastery Lab

Welcome! This lab will guide you through every essential skill for managing users, groups, passwords, permissions, and file access on a Linux system. **Read each section, run the commands, and observe the results.** Comments are included for every command to reinforce understanding.

## 1. **User and Group Concepts**

- **Users** are individual identities on the system, each with a UID.
- **Groups** are collections of users, each with a GID, used to manage shared permissions.
- User info: `/etc/passwd`
- Group info: `/etc/group`

**Check your own user and group info:**

```bash
id         # Shows your UID, GID, and group memberships
cat /etc/passwd | grep $USER  # Shows your user record
cat /etc/group | grep $USER   # Shows groups you belong to
```


## 2. **Quiz Yourself: User \& Group Concepts**

- What file stores user info? (`/etc/passwd`)
- What is a GID? (Group ID)
- What is the UID of root? (`0`)
- What is your primary group? (`id -gn`)


## 3. **Gain Superuser Access**

- **Superuser/root** can do anything on the system.
- Use `sudo` for single commands, or `sudo -i` for a root shell.

```bash
sudo whoami        # Should print 'root' if you have sudo access
sudo -i            # Opens a root shell (type 'exit' to leave)
sudo ls /root      # List root's home directory
```

- Use `su -` to switch to root (if you know the root password).


## 4. **Manage Local User Accounts**

- **Create users:**

```bash
sudo useradd -m alice      # Creates 'alice' with a home directory
sudo useradd -M bob        # Creates 'bob' without a home directory
```

- **Set user passwords:**

```bash
sudo passwd alice
sudo passwd bob
```

- **See all users:**

```bash
getent passwd
```

- **Delete a user:**

```bash
sudo userdel -r bob        # Removes bob and his home directory (if any)
```


## 5. **Manage Local Group Accounts**

- **Create groups:**

```bash
sudo groupadd devs
sudo groupadd ops
```

- **Add users to groups:**

```bash
sudo usermod -aG devs alice
sudo usermod -aG ops alice
```

- **Remove user from group:**

```bash
sudo gpasswd -d alice ops
```

- **See all groups:**

```bash
getent group
```

- **Delete a group:**

```bash
sudo groupdel ops
```


## 6. **Manage User Passwords**

- **Change your own password:**

```bash
passwd
```

- **Force user to change password at next login:**

```bash
sudo passwd --expire alice
```

- **Lock and unlock a user account:**

```bash
sudo passwd -l alice   # Lock
sudo passwd -u alice   # Unlock
```

- **Set password expiration policy:**

```bash
sudo chage -M 30 alice   # Password must be changed every 30 days
sudo chage -l alice      # View password aging info
```


## 7. **Interpret Linux File System Permissions**

- **Permissions are shown with `ls -l`:**
    - First char: file type (`-` file, `d` directory)
    - Next 3: owner (rwx)
    - Next 3: group (rwx)
    - Last 3: others (rwx)

```bash
touch secret.txt
ls -l secret.txt
```

- Example: `-rw-r--r--` means owner can read/write, group and others can read.


## 8. **Manage File System Permissions from the Command Line**

- **Change permissions:**

```bash
chmod 600 secret.txt      # Owner can read/write, others none
chmod 644 secret.txt      # Owner read/write, group/others read
chmod 700 secret.txt      # Owner all, others none
chmod +x secret.txt       # Make file executable
```

- **Change ownership:**

```bash
sudo chown alice secret.txt
sudo chgrp devs secret.txt
sudo chown alice:devs secret.txt
```


## 9. **Manage Default Permissions and File Access (umask)**

- **Check current umask:**

```bash
umask
```

- **Set umask for current session:**

```bash
umask 077     # New files: owner only
touch private.txt
ls -l private.txt
```


## 10. **Advanced: Special Permissions**

- **Setgid on directories:**
New files inherit group.

```bash
sudo mkdir /srv/shared
sudo chgrp devs /srv/shared
sudo chmod 2770 /srv/shared
```

- **Sticky bit:**
Only file owner can delete files in shared dir.

```bash
sudo chmod +t /srv/shared
```


## 11. **Lab Challenge: Create a Secure Secret File**

1. **Create a user and group for secret agents:**
```bash
sudo useradd -m agentX
sudo groupadd agents
sudo usermod -aG agents agentX
```

2. **Create a secret file and set ownership:**
```bash
sudo touch /home/agentX/secret_plan.txt
sudo chown agentX:agents /home/agentX/secret_plan.txt
```

3. **Set strict permissions:**
```bash
sudo chmod 640 /home/agentX/secret_plan.txt
```

4. **Set restrictive umask for agentX:**
```bash
sudo -u agentX bash -c "echo 'umask 077' >> ~/.bashrc"
```

5. **Test group access:**
```bash
sudo useradd -m agentY
sudo usermod -aG agents agentY
sudo su - agentY
cat /home/agentX/secret_plan.txt   # Should succeed if group permission is set
exit
```

6. **Remove agentY from group and test again:**
```bash
sudo gpasswd -d agentY agents
sudo su - agentY
cat /home/agentX/secret_plan.txt   # Should fail now
exit
```

7. **Clean up (optional):**
```bash
sudo userdel -r agentX
sudo userdel -r agentY
sudo groupdel agents
sudo rm -rf /srv/shared
```


## 12. **Summary**

- You have practiced every core command and concept for managing users, groups, passwords, permissions, and secure file access in Linux.
- You can now confidently administer local accounts, enforce password policies, set and interpret permissions, and build secure collaboration environments.

**Experiment, break things, and fix them! This is the best way to learn Linux system administration.**

