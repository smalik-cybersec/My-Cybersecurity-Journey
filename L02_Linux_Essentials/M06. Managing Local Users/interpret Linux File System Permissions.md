Here is a detailed explanation of how to **interpret Linux file system permissions**, as presented in the Red Hat System Administration I Student Guide (RH124, section 7, page 200)[^1].

## **Understanding Linux File System Permissions**

When you list files with `ls -l`, you see output like:

```
-rw-r--r-- 1 alice staff  4096 Jul  1 12:34 example.txt
```

Let’s break down the permission string: `-rw-r--r--`

### **Permission String Structure**

| Position | Meaning | Example Value |
| :-- | :-- | :-- |
| 1 | File type (`-`=file, `d`=directory, `l`=link) | `-` |
| 2-4 | Owner permissions (user) | `rw-` |
| 5-7 | Group permissions | `r--` |
| 8-10 | Others (world) permissions | `r--` |

### **Permission Types**

- **r** (read): View file contents or list directory.
- **w** (write): Modify file contents or directory (add/remove files).
- **x** (execute): Run the file as a program or enter the directory.


### **Example Breakdown**

`-rw-r--r--`

- **-**: Regular file.
- **rw-**: Owner can read and write.
- **r--**: Group can read only.
- **r--**: Others can read only.


### **Numeric (Octal) Representation**

Permissions can also be represented numerically:

- **r = 4**
- **w = 2**
- **x = 1**

Add the values for each set:

- Owner: `rw-` = 4+2 = **6**
- Group: `r--` = 4 = **4**
- Others: `r--` = 4 = **4**

So, `-rw-r--r--` = **644**

### **Special Permission Bits**

Occasionally, you may see `s`, `t`, or `S` in the permission string:

- **s**: setuid/setgid (run as file owner/group)
- **t**: sticky bit (restricts file deletion in directories like `/tmp`)


## **Quiz: Interpret Linux File System Permissions**

**1. What does `drwxr-x---` mean?**

- d: Directory
- Owner: read, write, execute
- Group: read, execute
- Others: no permissions

**2. What numeric value is `-rwxr-xr-x`?**

- Owner: rwx = 4+2+1 = 7
- Group: r-x = 4+0+1 = 5
- Others: r-x = 4+0+1 = 5
- **Answer:** 755

**3. Who can write to a file with permissions `-rw-r--r--`?**

- Only the owner.

**4. What does the sticky bit do on a directory?**

- Only the file’s owner, the directory’s owner, or root can delete or rename files within the directory.


## **Why Permissions Matter**

- **Security:** Prevent unauthorized access or modification.
- **Collaboration:** Allow group members to work together on shared files/directories.
- **System Integrity:** Protect system files from accidental or malicious changes.
