Let’s go deep into **managing file system permissions from the command line**. This is a foundational skill for any Linux administrator or security professional. You’ll learn the commands, see real examples, and understand the effects of each action.

## **1. Viewing Permissions and Ownership**

### **Check permissions and ownership of files and directories**

```bash
ls -l /path/to/file_or_directory
# Example output:
# -rw-r--r-- 1 alice devs 1234 Jul 2 16:00 report.txt
```

- The first field (`-rw-r--r--`) shows permissions:
    - `-` = regular file, `d` = directory
    - Next three: owner permissions (rwx)
    - Next three: group permissions (rwx)
    - Last three: others permissions (rwx)
- Owner: `alice`, Group: `devs`


## **2. Changing Permissions with `chmod`**

### **Symbolic mode**

```bash
chmod u+x script.sh    # Add execute for owner
chmod g-w file.txt     # Remove write for group
chmod o= file.txt      # Remove all permissions from others
```


### **Numeric (octal) mode**

- r = 4, w = 2, x = 1
- Add values for each set (owner, group, others)

```bash
chmod 755 script.sh    # rwxr-xr-x (owner: all, group: r-x, others: r-x)
chmod 640 file.txt     # rw-r----- (owner: rw, group: r, others: none)
```

**Effect:**

- Controls who can read, write, or execute files and directories.
- Use cases: scripts that only you should run, logs that only admins should read, etc.


## **3. Changing Ownership with `chown` and `chgrp`**

### **Change file owner and group**

```bash
sudo chown bob:admins file.txt   # Set owner to bob, group to admins
sudo chgrp devs file.txt         # Change group to devs only
```

**Effect:**

- Only the owner or root can change file ownership.
- Use case: transferring responsibility for files, setting group-access for teams.


## **4. Setting Default Permissions with `umask`**

### **Check and set umask**

```bash
umask
# Output: 0022

umask 027
# New files: 640, new directories: 750
```

**Effect:**

- `umask` subtracts permissions from the system default (666 for files, 777 for directories).
- Use case: ensuring new files are not world-readable by default.


## **5. Practical Scenario: Secure a Log Directory**

Let’s say you want only your user and your group to access `/var/logs/secure`.

```bash
sudo mkdir -p /var/logs/secure
sudo chown sysadmin:logteam /var/logs/secure
sudo chmod 770 /var/logs/secure
ls -ld /var/logs/secure
# Output: drwxrwx--- 2 sysadmin logteam ... /var/logs/secure
```

- Only `sysadmin` and members of `logteam` can access.


## **6. Cautions and Best Practices**

- **Never** use `chmod 777` on sensitive files/directories; this gives all permissions to everyone.
- Changing ownership (`chown`) requires root privileges.
- Always verify changes with `ls -l` or `ls -ld`.


## **Key Takeaways**

- Use `ls -l` to view permissions and ownership.
- Use `chmod` (symbolic or numeric) to set permissions.
- Use `chown` and `chgrp` to set owner and group.
- Use `umask` to control default permissions for new files.
- Always check your work with `ls -l`.


## **Try These Tasks in Your Lab**

1. **Create a directory only your user can access:**

```bash
mkdir ~/private_dir
chmod 700 ~/private_dir
ls -ld ~/private_dir
```

2. **Set up a shared directory for a group:**

```bash
sudo mkdir /srv/shared
sudo chown :devs /srv/shared
sudo chmod 770 /srv/shared
ls -ld /srv/shared
```



Let's walk through a **guided exercise** for managing file system permissions from the command line, as outlined in the Red Hat RH124 course[^1]. This will give you step-by-step practice with real commands, explanations, and expected results.

## **Guided Exercise: Manage File System Permissions from the Command Line**

### **Objective**

Learn how to:

- View file and directory permissions
- Change permissions using `chmod`
- Change ownership with `chown` and `chgrp`
- Apply both symbolic and numeric permission modes


### **Step 1: Set Up a Practice Environment**

Create a directory and some files to work with:

```bash
mkdir ~/perm-lab
cd ~/perm-lab
touch file1.txt file2.txt
mkdir dir1
```

- `mkdir` creates a new directory.
- `touch` creates empty files.
- `cd` changes into your new directory.


### **Step 2: View Permissions and Ownership**

Check the current permissions:

```bash
ls -l
```

**Expected output:**

```
-rw-rw-r-- 1 youruser yourgroup 0 Jul 2 18:30 file1.txt
-rw-rw-r-- 1 youruser yourgroup 0 Jul 2 18:30 file2.txt
drwxrwxr-x 2 youruser yourgroup 4096 Jul 2 18:30 dir1
```

- First column: file type and permissions
- Third column: owner
- Fourth column: group


### **Step 3: Change Permissions with `chmod`**

#### **A. Symbolic Mode**

```bash
chmod u+x file1.txt       # Add execute permission for the owner
chmod g-w file2.txt       # Remove write permission from group
chmod o-r file1.txt       # Remove read permission from others
```

**Explanation:**

- `u` = user/owner, `g` = group, `o` = others
- `+` adds, `-` removes, `=` sets permissions

Check the result:

```bash
ls -l
```


#### **B. Numeric (Octal) Mode**

```bash
chmod 640 file2.txt       # Owner: rw-, group: r--, others: ---
chmod 755 dir1            # Owner: rwx, group: r-x, others: r-x
```

**Explanation:**

- 6 = 4 (read) + 2 (write)
- 4 = 4 (read)
- 0 = no permissions
- 7 = 4 (read) + 2 (write) + 1 (execute)
- 5 = 4 (read) + 1 (execute)

Check the result:

```bash
ls -l
```


### **Step 4: Change Ownership with `chown` and `chgrp`**

Suppose you have a group called `devs` and a user `alice`.

```bash
sudo chown alice file1.txt        # Change owner to alice
sudo chgrp devs file2.txt         # Change group to devs
sudo chown alice:devs dir1        # Change owner to alice and group to devs
```

Check the result:

```bash
ls -l
```


### **Step 5: Secure a Directory for Logs**

Suppose you want a directory only your user and your group can access:

```bash
mkdir logs
chmod 770 logs
ls -ld logs
```

- `drwxrwx---` means only owner and group can access.


### **Step 6: Experiment and Verify**

Try accessing files as another user (if possible) or simulate with `su`/`sudo` to confirm permissions are enforced.

## **Key Takeaways**

- Use `ls -l` to view permissions and ownership.
- Use `chmod` (symbolic or numeric) to set permissions.
- Use `chown` and `chgrp` to set owner and group.
- Always verify your changes.


## **Lab Tasks to Try**

1. **Create a file only you can read and write:**

```bash
touch private.txt
chmod 600 private.txt
ls -l private.txt
```

2. **Create a shared directory for a group:**

```bash
sudo mkdir /srv/shared
sudo chown :devs /srv/shared
sudo chmod 770 /srv/shared
ls -ld /srv/shared
```


This exercise gives you practical, hands-on experience managing file system permissions from the command line, closely following the Red Hat curriculum[^1].