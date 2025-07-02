The module "3. Manage Files from the Command Line" begins by describing **Linux File System Hierarchy Concepts**. This foundational understanding is crucial for managing files from the command line efficiently.

Here is a comprehensive overview of the Linux File System Hierarchy Concepts:

### 1. The File System Hierarchy: Core Concept and Structure
*   **Unified Inverted Tree**: The Linux operating system organises all files within a **single inverted tree of directories**, known as the **file-system hierarchy**. The "root" of this tree, the **root directory**, is located at the very top and is represented by a **single forward slash (`/`)**.
*   **Directory Separator**: The `/` character is also used as a **directory separator** in file names to delineate between subdirectories in a path, such as `/etc/issue`.
*   **"Everything is a File" Principle**: A fundamental principle in Linux, inherited from UNIX, is that **"everything is a file"**. This means that diverse components, such as disks, processes, and devices, are represented as files within the file system. For example, a disk might be `/dev/sdb`, or a process information under `/proc`. This allows permissions to be consistently applied across various system components. Even directories themselves are considered files with special permissions.

### 2. The Filesystem Hierarchy Standard (FHS)
*   **Standardization**: Linux adheres to a standard, maintained by the Linux Foundation, called the **Filesystem Hierarchy Standard (FHS)**. This standard defines the **names, locations, and permissions** for many file types and directories, promoting consistency across Linux distributions, including Red Hat Enterprise Linux (RHEL).
*   **Purpose of Directories**: The FHS ensures that subdirectories of the root (`/`) are used for **standardized purposes** to organise files by type and purpose. This standard simplifies finding files and understanding the system's organisation.
*   **Static vs. Variable Data**: The FHS distinguishes between **static files** (content remains unchanged unless explicitly modified) and **variable/dynamic files** (content modified and updated by system processes). Static directories contain commands, configuration files, libraries, kernel files, and device files, while dynamic directories contain log files, status files, and temporary files.

### 3. Significant Red Hat Enterprise Linux Directories
The sources highlight several important directories within the Linux file system hierarchy:
*   **`/` (Root)**: The **main storage space** where the system lives, and the top-level directory from which all other directories descend. It contains many higher-level directories that store specific information.
*   **`/boot`**: Contains files necessary to **start the boot process**, including the Linux kernel, GRUB2 configuration, and other boot support files. It's typically a separate partition to ensure accessibility by the BIOS, and usually 500MB is sufficient.
*   **`/dev`**: Stores **special device files** that the system uses to access hardware components (e.g., terminals, hard disks, CD-ROMs, floppy drives). These files represent devices but are not the devices themselves. On RHEL 9, the first SATA, SAS, SCSI, or USB hard drive is named `/dev/sda`.
*   **`/etc`**: The **core system configuration directory** (pronounced "EHT-see"). It contains system-specific configuration files, such as user password files (`/etc/passwd`), boot, device, and networking setup files.
*   **`/home`**: The default location where **regular users store their personal data and configuration files** in their individual home directories.
*   **`/root`**: The **home directory for the administrative superuser**, `root`. For security reasons, it does not reside beneath `/home`.
*   **`/usr`**: Houses **installed software programs, shared libraries, and read-only program data**. It contains a large directory hierarchy, mirroring some root directories (e.g., `/usr/bin`, `/usr/lib`).
    *   `/usr/bin`: User commands and utilities.
    *   `/usr/sbin`: System administration commands.
    *   `/usr/local`: Locally customized software.
    *   `/usr/share/doc`: Linux documentation for applications and packages.
    *   `/usr/share/man`: Manual pages.
*   **`/var`**: Stores **variable data** that changes dynamically, such as log files (`/var/log`), databases, cache directories, printer-spooled documents, and website content.
*   **`/tmp`**: Contains **temporary files** used by applications or users. Its contents are often emptied upon reboot.
*   **`/run`**: Holds **runtime data for processes** that started since the last boot, including process ID files and lock files. It is a `tmpfs` (memory-based) filesystem and does not persist across reboots.
*   **`/proc`**: A **virtual filesystem** that provides information about currently running kernel-related processes, device assignments, and kernel configuration settings. It's primarily memory-based, with files created as needed.
*   **`/sys`**: Similar to `/proc`, this **virtual filesystem** exposes information about devices, drivers, and some kernel features.
*   **`/media`**: A common mount point for **removable media**, such as CD-ROMs, DVDs, and USB flash drives.
*   **`/mnt`**: Another common mount point for **temporarily mounted file systems**, often used for removable media.
*   **`/bin`**, **`/sbin`**, **`/lib`**, **`/lib64`**: In RHEL 7 and later, these directories are **symbolic links** to their counterparts within `/usr` (e.g., `/bin` points to `/usr/bin`), effectively consolidating their contents. Historically, `/bin` contained essential binaries for basic commands (like `ls` and `cp`), `/sbin` for essential superuser binaries (`fsck`, `fdisk`), and `/lib` for essential libraries.

### 4. Specifying and Navigating Files by Name
*   **Pathname**: A **path (or pathname)** indicates the unique file-system location of a file or directory.
*   **Absolute Paths**: An **absolute path** (or fully qualified pathname) pinpoints the precise position of a file from the **root directory (`/`)**. It always begins with a forward slash (`/`).
*   **Relative Paths**: A **relative path** specifies the location of a file or directory **relative to the current working directory**. It does not start with a forward slash (`/`).
*   **Current Working Directory**: This is the directory a user or process is currently "in".
    *   **`pwd` (print working directory)**: Displays the **absolute pathname** of the current working directory.
    *   **`cd` (change directory)**: Used to move between directories.
        *   `cd` or `cd ~`: Returns to the current user's **home directory**.
        *   `cd ..`: Moves up one level to the **parent directory**.
        *   `cd -`: Returns to the **previous working directory**.
*   **`ls` (list)**: Lists files and directories.
    *   **`-l` (long listing)**: Provides detailed information including file type, permissions, owner, group, size, and modification date.
    *   **`-a` (all files)**: Includes **hidden files** (starting with a dot `.`) in the listing.
    *   **`-R` (recursive)**: Lists contents of the specified directory and all its subdirectories.
*   **Wildcards (Shell Expansions)**: The Bash shell offers **pattern matching** features (wildcards) to affect multiple files with a single command.
    *   **`*` (asterisk)**: Matches any sequence of zero or more characters.
    *   **`?` (question mark)**: Matches any single character.
    *   **`[]` (square brackets)**: Matches any single character within a specified set or range (e.g., `[a-z]`).

### 5. File Types and Permissions
*   **File Types**: Linux identifies file types without requiring file name extensions. Common file types include:
    *   `-`: Regular file (text, executable, binary, etc.).
    *   `d`: Directory.
    *   `l`: Symbolic link.
    *   `c`: Character device file.
    *   `b`: Block device file.
    *   `p`: Named pipe file.
    *   `s`: Local socket file.
*   **Permissions**: Every file and directory has **permissions and ownership** associated with it. These control access for the **owning user**, the **owning group**, and **all other users** on the system. Permissions are typically `r` (read), `w` (write), and `x` (execute). These are often represented numerically in octal mode.

### 6. Managing Files and Directories
*   **`touch`**: Creates an **empty file** or updates a file's timestamp.
*   **`mkdir` (make directory)**: Creates new directories.
*   **`cp` (copy)**: Duplicates files or directories. The `-r` or `-R` option is used to recursively copy directories.
*   **`mv` (move)**: Used to **rename files or directories** or to move them to a different location. When moving between filesystems, `mv` copies and then deletes the original.
*   **`rm` (remove)**: Deletes files or directories. Use with caution as deleted files are difficult to recover. The `-r` option is needed to delete non-empty directories.
*   **`rmdir` (remove directory)**: Deletes **empty directories**.
*   **Links**: Allow multiple file names to refer to the same underlying data.
    *   **`ln` (link)**: Command to create links.
    *   **Hard Links**: Are direct pointers to the file's data. Data persists as long as one hard link exists.
    *   **Symbolic Links (Soft Links)**: Act as shortcuts to another file or directory. If the original file is deleted, the symbolic link breaks. Symbolic links can cross file systems, unlike hard links.

This comprehensive overview addresses the core concepts, standardisation, key locations, navigation methods, and basic management operations for files and directories from the command line in Linux.