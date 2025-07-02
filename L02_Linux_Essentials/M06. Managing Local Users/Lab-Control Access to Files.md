Here is a detailed, step-by-step **lab for controlling access to files in Linux**, as outlined in your Red Hat RH124 course materials[^1].

## **Lab: Control Access to Files**

### **Lab Objectives**

- Set file-system permissions on files and directories.
- Interpret the security effects of different permission settings.
- Change permissions and ownership using command-line tools.
- Control default permissions for new files.
- Use special permissions to manage shared directories.


### **Step 1: List and Interpret Permissions**

List files and their permissions:

```bash
ls -l
```

Interpret the output, e.g.:

```
-rw-r--r-- 1 alice staff 4096 Jul 1 12:34 example.txt
```

- `-rw-r--r--`: Owner can read/write, group can read, others can read.


### **Step 2: Change Permissions with `chmod`**

- Make a file readable and writable only by its owner:

```bash
chmod 600 secret.txt
```

- Make a script executable by everyone:

```bash
chmod 755 script.sh
```

- Remove write permission for group and others:

```bash
chmod go-w shared.txt
```


### **Step 3: Change Ownership with `chown` and `chgrp`**

- Change file owner:

```bash
sudo chown bob report.txt
```

- Change group ownership:

```bash
sudo chgrp consultants report.txt
```


### **Step 4: Manage Default Permissions with `umask`**

- Check current umask:

```bash
umask
```

- Set a restrictive umask for the session (owner only):

```bash
umask 077
```

- Create a file and verify its permissions:

```bash
touch private.txt
ls -l private.txt
# Should show -rw-------
```


### **Step 5: Special Permissions for Shared Directories**

- Create a shared directory for a group:

```bash
sudo mkdir /srv/shared
sudo chgrp consultants /srv/shared
sudo chmod 2770 /srv/shared
```

    - The `2` in `2770` sets the **setgid** bit, so new files inherit the group.
- Make the directory "sticky" (only owners can delete their files):

```bash
sudo chmod +t /srv/shared
```


### **Step 6: Real-World Scenario**

**Collaborative Project Folder:**

- Two users, alice and bob, are both members of the `web` group.
- To enable collaboration:

```bash
sudo mkdir /srv/webproject
sudo chgrp web /srv/webproject
sudo chmod 2775 /srv/webproject
```

    - Both users can add/edit files, and new files inherit the `web` group.


### **Step 7: Verify and Test**

- Check permissions and ownership:

```bash
ls -ld /srv/shared /srv/webproject
```

- As alice or bob, create a file and verify group ownership:

```bash
touch /srv/webproject/testfile
ls -l /srv/webproject/testfile
```


### **Summary Table**

| Command | Purpose |
| :-- | :-- |
| chmod | Change file/directory permissions |
| chown | Change file owner |
| chgrp | Change file group |
| umask | Set default permissions for new files |


