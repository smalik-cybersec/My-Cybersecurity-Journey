Guided Exercise: Manage File System Permissions from the Command Line ..

Here’s a detailed, practical guide to **managing file system permissions from the command line**, based on your Red Hat RH124 course materials.

## **How to Manage File System Permissions from the Command Line**

### **1. Viewing Permissions**

Use the `ls -l` command to display permissions for files and directories:

```bash
ls -l
```

Sample output:

```
-rw-r--r-- 1 alice staff 4096 Jul 1 12:34 example.txt
```

- The first column (`-rw-r--r--`) shows permissions.
- The first character: file type (`-` for file, `d` for directory).
- Next 9 characters: permissions for owner, group, others.


### **2. Changing Permissions with `chmod`**

#### **Symbolic Mode**

- Add execute permission for owner:

```bash
chmod u+x script.sh
```

- Remove write for group:

```bash
chmod g-w file.txt
```

- Add read for others:

```bash
chmod o+r notes.txt
```


#### **Numeric (Octal) Mode**

- `chmod 755 script.sh`
(Owner: rwx, Group: r-x, Others: r-x)
- `chmod 644 document.txt`
(Owner: rw-, Group: r--, Others: r--)


### **3. Changing Ownership with `chown` and `chgrp`**

- Change file owner:

```bash
sudo chown bob report.txt
```

- Change group ownership:

```bash
sudo chgrp staff report.txt
```

- Change both owner and group:

```bash
sudo chown bob:staff report.txt
```


### **4. Guided Exercise: Practice Permissions Management**

**Scenario:**
You want to create a file, restrict access so only you (the owner) can read/write, then share it with a group.

#### **Step-by-Step**

1. **Create a file:**

```bash
touch secret.txt
```

2. **Set permissions so only you can read/write:**

```bash
chmod 600 secret.txt
```

    - Now, only the owner can read and write.
3. **Change the group to 'staff':**

```bash
sudo chgrp staff secret.txt
```

4. **Allow group members to read:**

```bash
chmod 640 secret.txt
```

    - Owner: read/write, group: read, others: none.
5. **Allow group members to write as well:**

```bash
chmod 660 secret.txt
```

    - Owner and group: read/write, others: none.

### **5. Checking Your Work**

- View details:

```bash
ls -l secret.txt
```

- Output example:

```
-rw-rw---- 1 alice staff 0 Jul 1 19:00 secret.txt
```


### **6. Advanced: Set Permissions Recursively**

To set permissions for all files in a directory:

```bash
chmod -R 755 /srv/shared
```

- The `-R` flag applies the change recursively.


### **Summary Table**

| Command | Purpose | Example |
| :-- | :-- | :-- |
| chmod | Change file/directory permissions | `chmod 644 file.txt` |
| chown | Change file owner | `chown alice file.txt` |
| chgrp | Change file group | `chgrp staff file.txt` |
| ls -l | List files with permissions | `ls -l` |

