The **Linux File System Hierarchy** is a standardized way of organizing files and directories on a Linux system. It is defined by the Filesystem Hierarchy Standard (FHS), which ensures that system files, user files, applications, and device files are consistently placed across different Linux distributions. This structure is crucial for system administration, automation, security, and troubleshooting.

At the top is the **root directory** (`/`), from which all other directories branch out. Each major directory under `/` has a specific purpose, such as storing user data, system binaries, configuration files, or device information.

#### Key Directories and Their Purposes

| Directory | Purpose |
| :-- | :-- |
| `/` | The root directory; everything starts here |
| `/bin` | Essential user binaries (commands needed for basic system operation) |
| `/sbin` | System binaries (commands for system administration) |
| `/etc` | Configuration files for the system and installed applications |
| `/dev` | Device files (represent hardware devices as files) |
| `/proc` | Virtual filesystem providing process and kernel information |
| `/var` | Variable data (logs, mail, spool files, print queues) |
| `/tmp` | Temporary files (often cleared on reboot) |
| `/usr` | User programs, libraries, documentation, and other non-essential files |
| `/home` | Home directories for regular users |
| `/root` | Home directory for the root (admin) user |
| `/lib`, `/lib64` | Essential shared libraries |
| `/boot` | Boot loader files (kernel, initrd, bootloader config) |
| `/media`, `/mnt` | Mount points for removable or temporary filesystems |
| `/opt` | Optional/add-on application software packages |
| `/srv` | Data for services provided by the system (web, FTP, etc.) |

#### Visualizing the Hierarchy

```
/
├── bin
├── boot
├── dev
├── etc
├── home
│   ├── user1
│   └── user2
├── lib
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin
├── srv
├── tmp
├── usr
│   ├── bin
│   ├── lib
│   └── share
└── var
```


#### Practical Linux Commands and Examples

**1. View the top-level hierarchy:**

```bash
ls /
# Output: bin  boot  dev  etc  home  lib  media  mnt  opt  proc  root  run  sbin  srv  tmp  usr  var
```

- This lists all major directories at the root level.

**2. Explore a specific directory:**

```bash
ls /etc
# Output: passwd  shadow  hosts  network  ... (many config files)
```

- `/etc` contains configuration files.

**3. Check your home directory:**

```bash
echo $HOME
ls $HOME
```

- `$HOME` shows your personal directory, e.g., `/home/user1`.

**4. See mounted filesystems:**

```bash
mount | column -t
# Shows what is mounted and where, e.g., /dev/sda1 on /
```

**5. See process and kernel info:**

```bash
ls /proc
# Output: 1  2  3  ... (process IDs), plus kernel info files
cat /proc/cpuinfo
```

**6. List device files:**

```bash
ls /dev
# Output: sda  sda1  tty  zero  null  ...
```

- These represent hardware devices.


#### Common Errors and What They Mean

- **Permission denied:**
Trying to access or modify files in system directories (`/etc`, `/root`, `/bin`) as a non-root user.
- **No such file or directory:**
Typo or the file doesn’t exist at the specified path.
- **Read-only file system:**
The filesystem is mounted read-only, often in recovery or due to disk errors.


#### Key Takeaways

- The Linux file system is hierarchical, starting from `/`.
- Each directory has a specific, standardized purpose.
- Understanding this structure is essential for navigation, troubleshooting, and system management.


#### Try These in Your Lab

1. **List all top-level directories and check their disk usage:**

```bash
du -sh /*
```

2. **Find out which directory your shell is currently in:**

```bash
pwd
```

Here’s a **quiz** to help you assess your understanding of the **Linux File System Hierarchy Concepts**. These questions are designed in the style of Red Hat’s RH124 course and are suitable for both self-assessment and lab practice.

### Linux File System Hierarchy Concepts — Quiz

**1. What is the root directory in Linux, and what is its symbol?**
a) /root
b) /
c) /home
d) /etc

**2. Which directory contains user home directories?**
a) /usr
b) /home
c) /etc
d) /var

**3. Where are system configuration files typically stored?**
a) /etc
b) /bin
c) /lib
d) /srv

**4. Which directory contains essential command binaries used by all users?**
a) /sbin
b) /usr/bin
c) /bin
d) /opt

**5. What is the purpose of the `/dev` directory?**
a) Contains device files
b) Contains documentation
c) Contains development tools
d) Contains desktop files

**6. Which directory is used for temporary files that may be deleted at reboot?**
a) /var
b) /tmp
c) /opt
d) /srv

**7. What is stored in the `/boot` directory?**
a) User binaries
b) Boot loader files and kernel
c) Backup files
d) Log files

**8. Where are log files typically stored?**
a) /var/log
b) /etc/log
c) /usr/log
d) /tmp/log

**9. What is the function of the `/proc` directory?**
a) Stores process and kernel information as virtual files
b) Stores user processes
c) Stores program binaries
d) Stores printer files

**10. Which directory is the home directory for the root user?**
a) /root
b) /home/root
c) /etc/root
d) /usr/root

### Answer Key

1. b) /
2. b) /home
3. a) /etc
4. c) /bin
5. a) Contains device files
6. b) /tmp
7. b) Boot loader files and kernel
8. a) /var/log
9. a) Stores process and kernel information as virtual files
10. a) /root

#### Try this in your lab:

- Use `ls /` and `ls /var/log` to explore the actual directories and files.
- Use `cat /proc/cpuinfo` to see how `/proc` provides system information.


