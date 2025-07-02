To **manage default permissions and file access** in Linux, you need to understand how the system sets permissions for new files and directories, and how these defaults can be controlled and customized for both system-wide and per-user needs.

## **Default Permissions: The Role of `umask`**

When a new file or directory is created, Linux assigns default permissions, then subtracts permissions based on the **umask** value.

- **Default permissions before umask:**
    - Files: `666` (rw-rw-rw-) — no execute by default
    - Directories: `777` (rwxrwxrwx)
- **umask:**
A three-digit octal value that "masks out" permissions you *don’t* want to grant.
For example, a umask of `022` removes write permission for group and others.
- **Resulting permissions:**
New file = default permissions minus umask


### **Check Your Current umask**

```bash
umask
```

- Output example: `0022`


### **Calculate Resulting Permissions**

| umask | New File Permissions | New Directory Permissions |
| :-- | :-- | :-- |
| 022 | 644 (rw-r--r--) | 755 (rwxr-xr-x) |
| 027 | 640 (rw-r-----) | 750 (rwxr-x---) |
| 077 | 600 (rw-------) | 700 (rwx------) |

## **Changing umask**

- **Temporarily (for current shell):**

```bash
umask 027
```

All new files: owner rw, group r, others none.
- **Permanently (for a user):**
Add `umask 027` to your `~/.bashrc`, `~/.profile`, or `~/.bash_profile`.
- **System-wide:**
Set in `/etc/profile`, `/etc/login.defs`, or `/etc/bash.bashrc` (varies by distro)[^1].


## **Guided Exercise: Managing Default Permissions**

### **1. View Current umask and Create a File**

```bash
umask
touch testfile
ls -l testfile
```


### **2. Change umask and Observe Effect**

```bash
umask 077
touch privatefile
ls -l privatefile
```

- `privatefile` should have permissions `-rw-------`


### **3. Set umask Permanently for a User**

Edit `~/.bashrc` or `~/.profile` and add:

```bash
umask 027
```

- Log out and back in, or run `source ~/.bashrc`
- New files will have permissions reflecting the new umask.


## **Environment Files and Permission Defaults**

- **System-wide defaults:** `/etc/profile`, `/etc/login.defs`, `/etc/bash.bashrc`, files in `/etc/profile.d/`[^1].
- **User-specific:** `~/.bash_profile`, `~/.profile`, `~/.bashrc`[^1].
- **Order of execution:**
    - Login shell: `/etc/profile` → user files
    - Interactive shell: user’s `~/.bashrc`
    - Non-interactive shell: depends on `$BASH_ENV`


## **Best Practices**

- Use a restrictive umask (like `077`) for sensitive systems.
- For collaborative directories, use a less restrictive umask (like `002`), and manage group membership carefully.
- Always test by creating a file after changing umask to confirm expected permissions.
