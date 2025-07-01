Here is a **complete list of Linux commands** we discussed throughout this thread, with detailed explanations and variations. Each command is explained with inline comments to help you understand its purpose, usage, and common options.

# 1. `useradd`

```bash
sudo useradd [options] username
```

- **Purpose:** Create a new user account.
- **Common options:**
    - `-m`: Create the user's home directory.
    - `-M`: Do NOT create the home directory.
    - `-g group`: Set the primary group.
    - `-G group1,group2`: Add supplementary groups.
    - `-s shell`: Specify login shell.

**Examples:**

```bash
sudo useradd -m alice               # Create user alice with home directory
sudo useradd -M bob                 # Create user bob without home directory
sudo useradd -m -g admins charlie  # Create user charlie with primary group admins
sudo useradd -m -G wheel,docker dave  # Create user dave with supplementary groups
```


# 2. `passwd`

```bash
sudo passwd [options] [username]
```

- **Purpose:** Set or change a user's password.
- **Common options:**
    - Without username: changes current user's password.
    - `--expire`: Force password change at next login.
    - `-l`: Lock the user's password (disable login).
    - `-u`: Unlock the user's password.

**Examples:**

```bash
passwd                           # Change your own password
sudo passwd alice                # Set/change password for alice
sudo passwd --expire alice       # Force alice to change password at next login
sudo passwd -l bob               # Lock bob's account
sudo passwd -u bob               # Unlock bob's account
```


# 3. `usermod`

```bash
sudo usermod [options] username
```

- **Purpose:** Modify user account properties.
- **Common options:**
    - `-aG group1,group2`: Append user to supplementary groups.
    - `-g group`: Change primary group.
    - `-l newname`: Change username.
    - `-d /new/home`: Change home directory.
    - `-s /bin/bash`: Change login shell.

**Examples:**

```bash
sudo usermod -aG admins alice    # Add alice to admins group
sudo usermod -g developers bob   # Change bob's primary group to developers
sudo usermod -l robert bob       # Rename user bob to robert
sudo usermod -d /home/robert robert  # Change home directory
```


# 4. `userdel`

```bash
sudo userdel [options] username
```

- **Purpose:** Delete a user account.
- **Common options:**
    - `-r`: Remove user's home directory and mail spool.

**Examples:**

```bash
sudo userdel alice               # Delete user alice (home directory remains)
sudo userdel -r bob              # Delete user bob and remove home directory
```


# 5. `groupadd`

```bash
sudo groupadd [options] groupname
```

- **Purpose:** Create a new group.
- **Common options:**
    - `-g GID`: Specify group ID.

**Examples:**

```bash
sudo groupadd admins             # Create group admins
sudo groupadd -g 1001 developers # Create group developers with GID 1001
```


# 6. `groupdel`

```bash
sudo groupdel groupname
```

- **Purpose:** Delete a group.

**Example:**

```bash
sudo groupdel admins
```


# 7. `groupmod`

```bash
sudo groupmod [options] groupname
```

- **Purpose:** Modify a group.
- **Common options:**
    - `-n newname`: Rename group.
    - `-g GID`: Change group ID.

**Examples:**

```bash
sudo groupmod -n devs developers  # Rename group devs to developers
sudo groupmod -g 2000 admins      # Change GID of admins to 2000
```


# 8. `gpasswd`

```bash
sudo gpasswd [options] groupname
```

- **Purpose:** Administer group membership and passwords.
- **Common options:**
    - `-a user`: Add user to group.
    - `-d user`: Remove user from group.
    - Set group password (rarely used).

**Examples:**

```bash
sudo gpasswd -a alice admins      # Add alice to admins group
sudo gpasswd -d bob admins        # Remove bob from admins group
sudo gpasswd admins               # Set group password for admins
```


# 9. `id`

```bash
id [username]
```

- **Purpose:** Display user and group IDs and group memberships.

**Examples:**

```bash
id                             # Show current user info
id alice                       # Show info for alice
```


# 10. `su`

```bash
su [-] [username]
```

- **Purpose:** Switch user identity.
- `-` starts a login shell (resets environment).

**Examples:**

```bash
su -                          # Switch to root user (prompt for root password)
su - alice                    # Switch to user alice
```


# 11. `ls`

```bash
ls [options] [file/directory]
```

- **Purpose:** List directory contents.
- **Common options:**
    - `-l`: Long listing with permissions.
    - `-a`: Show hidden files.
    - `-ld`: Show directory info instead of contents.

**Examples:**

```bash
ls -l /home/alice              # Show detailed listing of alice's home
ls -la                       # Show all files including hidden
ls -ld /srv/shared           # Show info about directory itself
```


# 12. `chmod`

```bash
chmod [options] mode file
```

- **Purpose:** Change file/directory permissions.
- **Modes:**
    - Numeric (e.g., 644, 755)
    - Symbolic (e.g., u+x, g-w)

**Examples:**

```bash
chmod 600 secret.txt           # Owner read/write only
chmod 755 script.sh            # Owner rwx, group/others r-x
chmod u+x script.sh            # Add execute for owner
chmod g-w file.txt             # Remove write for group
chmod o+r file.txt             # Add read for others
chmod 2770 /srv/shared         # Set setgid bit on directory
chmod +t /tmp                  # Set sticky bit on directory
chmod -R 755 /var/www          # Recursive permission change
```


# 13. `chown`

```bash
sudo chown [options] owner[:group] file
```

- **Purpose:** Change file owner and/or group.

**Examples:**

```bash
sudo chown alice secret.txt           # Change owner to alice
sudo chown alice:admins secret.txt    # Change owner to alice and group to admins
sudo chown :admins secret.txt         # Change group to admins only
```


# 14. `chgrp`

```bash
sudo chgrp group file
```

- **Purpose:** Change group ownership of a file.

**Example:**

```bash
sudo chgrp admins secret.txt
```


# 15. `umask`

```bash
umask [mask]
```

- **Purpose:** Set default file creation permissions mask.
- **Common masks:**
    - `022`: Default (files 644, dirs 755)
    - `077`: Private (files 600, dirs 700)

**Examples:**

```bash
umask                   # Show current mask
umask 077               # Set mask to private
touch testfile
ls -l testfile          # Should show -rw-------
```


# 16. `touch`

```bash
touch filename
```

- **Purpose:** Create an empty file or update timestamp.

**Example:**

```bash
touch secret.txt
```


# 17. `mkdir`

```bash
mkdir [options] directory
```

- **Purpose:** Create directories.
- **Common options:**
    - `-p`: Create parent directories as needed.

**Examples:**

```bash
mkdir /srv/shared
mkdir -p /srv/projects/project1
```


# 18. `getent`

```bash
getent database [key]
```

- **Purpose:** Query system databases like passwd or group.

**Examples:**

```bash
getent passwd alice        # Show user alice info
getent group admins        # Show group admins info
getent passwd              # List all users
getent group               # List all groups
```


# 19. `chage`

```bash
sudo chage [options] username
```

- **Purpose:** Manage password aging and expiry.

**Common options:**

- `-l`: List password expiry info.
- `-M days`: Set max days before password expires.
- `-W days`: Set warning days before expiry.
- `-E date`: Set account expiry date.

**Examples:**

```bash
sudo chage -l alice
sudo chage -M 30 alice
sudo chage -W 7 alice
sudo chage -E 2025-12-31 alice
```


# 20. `echo`

```bash
echo [string]
```

- **Purpose:** Print text to standard output or redirect to files.

**Examples:**

```bash
echo "Hello, world"
echo "------------" >> file.txt    # Append dashed line to file
```


# 21. `cat`

```bash
cat file
```

- **Purpose:** Display file contents.

**Example:**

```bash
cat /etc/passwd
```


# 22. `exit`

```bash
exit
```

- **Purpose:** Exit current shell or logout.


# Summary

| Command | Purpose | Key Variations/Options |
| :-- | :-- | :-- |
| useradd | Create user | `-m`, `-M`, `-g`, `-G` |
| passwd | Set/change password | `--expire`, `-l`, `-u` |
| usermod | Modify user | `-aG`, `-g`, `-l`, `-d` |
| userdel | Delete user | `-r` |
| groupadd | Create group | `-g` |
| groupdel | Delete group |  |
| groupmod | Modify group | `-n`, `-g` |
| gpasswd | Manage group membership | `-a`, `-d` |
| id | Show user/group IDs |  |
| su | Switch user | `-` for login shell |
| ls | List files | `-l`, `-a`, `-d` |
| chmod | Change permissions | Numeric \& symbolic modes, recursive `-R`, special bits |
| chown | Change ownership | Owner and group |
| chgrp | Change group |  |
| umask | Set default file permission |  |
| touch | Create/update file |  |
| mkdir | Create directory | `-p` |
| getent | Query passwd/group |  |
| chage | Password aging | `-l`, `-M`, `-W`, `-E` |
| echo | Print text |  |
| cat | Display file contents |  |
| exit | Exit shell |  |

This list covers all commands you encountered, explained with variations and usage examples. Use this as a reference to deepen your Linux system administration skills. If you want, I can also provide scripts or quizzes based on these commands!
