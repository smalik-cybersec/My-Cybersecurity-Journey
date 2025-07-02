### Explanation: linux_file_system_permissions

Linux uses a permission model to control who can access files and directories. Each file and directory has a set of permissions that define:

- **Who** can access it:
    - **Owner** (user who owns the file)
    - **Group** (users in the file’s group)
    - **Others** (everyone else)
- **What** they can do:
    - **Read (r):** View the contents of a file or list a directory’s contents.
    - **Write (w):** Modify a file or add/remove files in a directory.
    - **Execute (x):** Run a file as a program or access a directory.

Permissions are displayed as a string of 10 characters (e.g., `-rwxr-xr--`):

- The first character indicates the type (`-` for file, `d` for directory).
- The next three are for the owner, then group, then others.

**Example:**
`-rw-r--r--`

- `-` = regular file
- `rw-` = owner can read/write
- `r--` = group can read
- `r--` = others can read


### Real Linux Commands \& Scenarios

#### 1. Viewing Permissions

```bash
ls -l /path/to/file_or_dir
# Output example:
# -rw-r--r-- 1 alice devs 1234 Jul 2 16:00 report.txt
```

- The leftmost string shows permissions.
- `alice` is the owner, `devs` is the group.


#### 2. Changing Permissions: `chmod`

**Symbolic Mode:**

```bash
chmod u+x script.sh   # Add execute for user (owner)
chmod g-w file.txt    # Remove write from group
chmod o= file.txt     # Remove all permissions from others
```

**Numeric (Octal) Mode:**

- r = 4, w = 2, x = 1
- Add values for each group of three

```bash
chmod 755 script.sh   # rwxr-xr-x (owner: all, group: read/execute, others: read/execute)
chmod 640 file.txt    # rw-r----- (owner: read/write, group: read, others: none)
```


#### 3. Changing Ownership: `chown` and `chgrp`

```bash
sudo chown bob:admins file.txt   # Set owner to bob and group to admins
sudo chgrp devs file.txt         # Change group to devs
```


#### 4. Setting Default Permissions: `umask`

Check current umask:

```bash
umask
# Output example: 0022
```

Set umask for session:

```bash
umask 027
# New files: 640, new directories: 750
```


#### 5. Practical Example: Secure a Log Directory

**Scenario:** Only the `sysadmin` user and `logteam` group should access `/var/logs/secure`.

```bash
sudo mkdir -p /var/logs/secure
sudo chown sysadmin:logteam /var/logs/secure
sudo chmod 770 /var/logs/secure
```

- Only owner and group can read/write/execute; others have no access.

**Effect:**

- `sysadmin` and members of `logteam` can manage logs.
- No one else can even list the directory.


#### 6. Caution

- Removing all permissions from others (`chmod o= file.txt`) is common for sensitive data.
- Changing ownership (`chown`) requires sudo/root.
- Use `chmod` and `chown` carefully, especially on system files.


### Key Takeaways

- Permissions are shown as `rwx` for user, group, others.
- Use `chmod` to set permissions, `chown`/`chgrp` to set ownership.
- `umask` controls default permissions for new files/directories.
- Always verify changes with `ls -l`.


### Try It Yourself

1. **Create a test directory and file, then restrict access to your user only:**

```bash
mkdir ~/private_logs
touch ~/private_logs/secret.log
chmod 700 ~/private_logs
chmod 600 ~/private_logs/secret.log
ls -ld ~/private_logs
ls -l ~/private_logs
```

2. **Experiment with umask:**

```bash
umask 077
touch testfile
ls -l testfile
```


Here’s a practical quiz to help you interpret Linux file system permissions, with explanations and examples you can try in your own lab.

## **Quiz: Interpret Linux File System Permissions**

### **1. Given the following output, what does each part mean?**

```
drwxr-x---
1 alice devs 4096 Jul 2 16:00 project
```

**a.** What does the leading `d` mean?
**b.** What permissions does the owner have?
**c.** What permissions does the group have?
**d.** What permissions do others have?
**e.** Who owns the directory?
**f.** What group is assigned to the directory?

#### **Answers \& Explanations**

- **a.** `d` means this is a **directory**.
- **b.** `rwx` (read, write, execute) — the owner can list, add, and remove files.
- **c.** `r-x` (read, execute) — the group can list and access, but not add/remove files.
- **d.** `---` (no permissions) — others cannot access at all.
- **e.** `alice` is the owner.
- **f.** `devs` is the group.


### **2. What does `chmod 640 file.txt` do?**

- **Owner:** read and write
- **Group:** read only
- **Others:** no access

Try it:

```bash
touch file.txt
chmod 640 file.txt
ls -l file.txt
# Output: -rw-r----- 1 youruser yourgroup ... file.txt
```

*Owner can read/write, group can read, others have no access.*

### **3. What command would you use to give everyone execute permission on `script.sh`, but only the owner can write to it?**

```bash
chmod 755 script.sh
ls -l script.sh
# Output: -rwxr-xr-x
```

*Owner: read/write/execute, group: read/execute, others: read/execute.*

### **4. If a file has permissions `-rw-rw----`, who can read and write it?**

- **Owner and group** can read and write.
- **Others** have no access.


### **5. What does `umask 077` do?**

- **New files:** only owner can read/write.
- **New directories:** only owner can access.
- *Group and others get no permissions by default.*

Try it:

```bash
umask 077
touch testfile
ls -l testfile
# Output: -rw------- (only owner has permissions)
```


### **6. How do you change the group ownership of `data.log` to `admins`?**

```bash
sudo chgrp admins data.log
ls -l data.log
# Output: ... youruser admins ... data.log
```


### **7. What does the following command do?**

```bash
chmod g+w,o-rwx report.txt
```

- **Adds write permission to the group.**
- **Removes all permissions from others.**


### **8. Scenario: You want a directory `secure` where only you (the owner) can access it. What commands do you use?**

```bash
mkdir secure
chmod 700 secure
ls -ld secure
# Output: drwx------ (only owner can list, add, or remove files)
```


## **Key Takeaways**

- **rwx** permissions are for owner, group, and others (in that order).
- Use **chmod** to set permissions, **chown** and **chgrp** for ownership.
- **umask** sets default permissions for new files/directories.
- Always check with `ls -l` or `ls -ld` to verify your changes.


### **Try These Tasks in Your Lab**

1. Create a file only your user can read/write, and no one else can access.
2. Make a directory only accessible to your group, not others.