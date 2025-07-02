### Special Permissions in Linux

Special permissions in Linux go beyond the basic read (`r`), write (`w`), and execute (`x`) bits. They provide additional control for collaborative environments and specific security needs. The three main special permissions are:

#### 1. **Setuid (Set User ID)**

- When set on an executable file, this permission allows the file to run with the privileges of the file's owner, not the user who launched it.
- **Symbol:** `s` in the user/owner execute position (e.g., `-rwsr-xr-x`)
- **Numeric value:** `4` (used as the first digit in a four-digit `chmod` code)
- **Typical use:** Programs like `/usr/bin/passwd` need to modify system files (like `/etc/shadow`) and thus require root privileges, even when run by normal users.

**Example command:**

```bash
sudo chmod u+s /usr/local/bin/myscript
# Now, myscript runs with its owner's privileges
```


#### 2. **Setgid (Set Group ID)**

- When set on an **executable file**, the process runs with the group privileges of the file’s group.
- When set on a **directory**, all new files and subdirectories created within inherit the directory’s group, regardless of the user’s primary group.
- **Symbol:** `s` in the group execute position (e.g., `drwxr-sr-x` for directories)
- **Numeric value:** `2` (used as the first digit in a four-digit `chmod` code)
- **Typical use:** Shared project directories, so all files stay with the project group.

**Example command:**

```bash
sudo chmod g+s /srv/shared
# All new files in /srv/shared will inherit the group of the directory
```


#### 3. **Sticky Bit**

- When set on a directory, only the file’s owner, the directory’s owner, or root can delete or rename files within that directory, even if others have write access.
- **Symbol:** `t` in the others execute position (e.g., `drwxrwxrwt`)
- **Numeric value:** `1` (used as the first digit in a four-digit `chmod` code)
- **Typical use:** World-writable directories like `/tmp` to prevent users from deleting each other's files.

**Example command:**

```bash
sudo chmod +t /tmp
# /tmp now has the sticky bit set, shown as 't' in the permissions
```


#### **Combining Special Permissions with Numeric Mode**

Special permissions are represented as the first digit in a four-digit `chmod` code:

- Setuid: `4`
- Setgid: `2`
- Sticky: `1`

**Examples:**

- `chmod 4755 file` — setuid + rwxr-xr-x
- `chmod 2770 dir` — setgid + rwxrws---
- `chmod 1777 dir` — sticky + rwxrwxrwt (like /tmp)


### **Summary Table**

| Permission | Symbol | Numeric | Applies to | Effect |
| :-- | :-- | :-- | :-- | :-- |
| setuid | s | 4 | Files | Run as file owner |
| setgid | s | 2 | Files/Dirs | Run as group / Inherit group |
| sticky | t | 1 | Dirs | Only owner/root can delete |

### **Key Takeaways**

- **Setuid**: Use for executables needing owner’s privileges.
- **Setgid**: Use for shared directories to keep group ownership consistent.
- **Sticky bit**: Use for public directories to prevent accidental or malicious file deletion by other users.


### **Lab Tasks to Try**

1. **Set setgid on a shared directory and verify group inheritance:**

```bash
sudo mkdir /srv/shared
sudo chown :projectgroup /srv/shared
sudo chmod 2770 /srv/shared
ls -ld /srv/shared
# Look for 's' in the group execute position: drwxrws---
```

2. **Set the sticky bit on a world-writable directory and test file deletion:**

```bash
sudo chmod 1777 /tmp/testdir
ls -ld /tmp/testdir
# Look for 't' at the end: drwxrwxrwt
```


These special permissions are essential for secure, multi-user environments and collaborative workflows[^1].
