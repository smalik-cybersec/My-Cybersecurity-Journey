Here’s a comprehensive, hands-on lab for **controlling access to files** in Linux, following RH124 Chapter 7 best practices and real-world scenarios[^1].

## **Lab: Control Access to Files**

### **Objectives**

- List and interpret file and directory permissions.
- Change permissions and ownership from the command line.
- Set and verify default permissions.
- Use special permissions (setgid, sticky bit) for group collaboration and security.


### **Step 1: Examine and Interpret Permissions**

#### **A. List Permissions**

```bash
ls -l /tmp
ls -l /etc/passwd
ls -ld /var/log
```

- The first column shows permissions (`drwxr-xr-x`).
- Owner and group are shown in columns 3 and 4.


#### **B. Interpret Permissions**

- `r` (read): View file contents or list directory.
- `w` (write): Modify file or add/remove files in directory.
- `x` (execute): Run file as program or access directory with `cd`.


### **Step 2: Change Permissions and Ownership**

#### **A. Create Test Files and Directories**

```bash
mkdir ~/labfiles
cd ~/labfiles
touch file1.txt
mkdir dir1
```


#### **B. Set Permissions with `chmod`**

```bash
chmod 600 file1.txt   # Owner can read/write, no access for group/others
chmod 755 dir1        # Owner: rwx, group: r-x, others: r-x
ls -l
```

**Explanation:**

- `600`: Only owner can read/write.
- `755`: Owner can do everything; group/others can read and access.


#### **C. Change Ownership with `chown` and `chgrp`**

```bash
sudo chown $USER:labgroup file1.txt   # Change group to 'labgroup'
sudo chown $USER:labgroup dir1
ls -l
```

- Replace `labgroup` with an actual group on your system.


### **Step 3: Set Default Permissions with `umask`**

#### **A. View and Change umask**

```bash
umask
umask 027
touch file2.txt
mkdir dir2
ls -l file2.txt
ls -ld dir2
```

- With `umask 027`, new files: `rw-r-----`, new directories: `rwxr-x---`.


### **Step 4: Use Special Permissions for Collaboration and Security**

#### **A. Setgid for Group Collaboration**

```bash
sudo mkdir /srv/shared
sudo chown :labgroup /srv/shared
sudo chmod 2770 /srv/shared
```

- `2` in `2770` sets the setgid bit: all new files inherit the group.


#### **B. Sticky Bit for Public Directories**

```bash
sudo chmod +t /tmp
ls -ld /tmp
```

- The `t` at the end (`drwxrwxrwt`) means only the file’s owner or root can delete files, even if the directory is world-writable.


### **Step 5: Verify and Test Access**

#### **A. As Another User (if possible)**

```bash
sudo -u anotheruser touch /srv/shared/testfile
ls -l /srv/shared
```

- New files should have group ownership set to `labgroup`.


#### **B. Test Sticky Bit**

```bash
sudo -u anotheruser touch /tmp/otheruserfile
ls -l /tmp/otheruserfile
rm /tmp/otheruserfile   # Should fail unless you are the owner or root
```


## **Key Takeaways**

- Permissions control access for owner, group, and others.
- `chmod` and `chown` are used to set permissions and ownership.
- `umask` defines default permissions for new files/directories.
- Special permissions (setgid, sticky bit) enable safe collaboration and secure public directories.


## **Lab Tasks to Try**

1. **Create a directory only your user can access.**

```bash
mkdir ~/private_dir
chmod 700 ~/private_dir
```

2. **Set up a group-shared directory with setgid and test file creation as another group member.**

**This lab gives you practical, security-focused experience in controlling file access on Linux, directly supporting the objectives outlined in RH124 Chapter 7[^1].**