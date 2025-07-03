In Red Hat Enterprise Linux (RHEL), **file system permissions control access to files and directories**. This system, inherited from UNIX, helps **secure files from unauthorized viewing or modification** and protects critical system files. In Linux, the principle that "everything is a file" means that permissions can be assigned not only to traditional files, but also to disks, processes, and other system components.

### Components of Permissions

File permissions are defined for three user categories:
*   **Owner (User)**: The individual who owns the file, typically the creator.
*   **Group**: A predefined collection of users that may have permission to access the file. The file is owned by a single group, usually the primary group of the user who created it, but this can be changed.
*   **Others (World/Public)**: All other users on the system who are not the owner or a member of the owning group.

For each of these categories, three types of permissions can be granted or denied:
*   **Read (r)**: Allows viewing the file's contents.
*   **Write (w)**: Allows changing the file's contents, renaming it, or deleting it.
*   **Execute (x)**: Allows running the file as a command or program.

Permissions can be modified using specific **modes**:
*   **Add (+)**: Adds a permission.
*   **Remove (-)**: Removes a permission.
*   **Set Absolutely (=)**: Sets exactly the provided permissions, replacing any existing ones.

### Displaying Permissions (`ls -l` Output)

The `ls -l` command provides a **detailed, long listing** of files, including their permissions and ownership. When used with the `-d` option (`ls -ld`), it shows information about the directory itself, not its contents.

The permission information is presented as a **10-character string** at the beginning of the `ls -l` output:
1.  **First Character (File Type)**: Indicates the type of file:
    *   `-`: Regular file.
    *   `d`: Directory.
    *   `l`: Symbolic link.
    *   `c`: Character device file.
    *   `b`: Block device file.
    *   `p`: Named pipe file.
    *   `s`: Local socket file.
2.  **Next Nine Characters**: These are grouped into three sets of three characters, representing the **read (r), write (w), and execute (x) permissions** for the owner, group, and others, respectively. A hyphen (`-`) indicates that a permission is denied.
3.  **SELinux/ACL Indicators**:
    *   A **dot (`.`)** after the permission string indicates that an **SELinux security context is applied** to the file. SELinux controls access beyond traditional permissions.
    *   A **plus sign (`+`)** after the permission string indicates that **Access Control Lists (ACLs) are set** on the file. ACLs provide more granular control for specific users or groups.

### Effect of Permissions on Files vs. Directories

The meaning of read, write, and execute permissions **differs depending on whether they apply to a file or a directory**:

**For Regular Files**:
*   **Read (r)**: Allows viewing or copying the file's content.
*   **Write (w)**: Allows changing the file's content.
*   **Execute (x)**: Allows running the file as a program or command. **RHEL by default does not automatically assign executable permissions to newly created regular files**; you must explicitly add them with `chmod` if needed.

**For Directories**:
*   **Read (r)**: Allows listing the contents of the directory (i.e., the filenames).
*   **Write (w)**: Allows creating, erasing, or renaming files and subdirectories *within* that directory.
*   **Execute (x)**: Allows entering the directory (using `cd`), searching through it, or executing programs from it. **To list the contents of a directory (read), you also need execute permission**.

**Important Nuances**:
*   Anyone who has **write permissions to a directory can remove files on it, regardless of the ownership or permissions on the file itself**, unless the "sticky bit" is set on the directory.
*   The `root` user (superuser) has **full access to the system and can override normal permissions** on any file or directory.

### Permission Notation Methods

Permissions can be specified using two main methods:

1.  **Octal Notation (Numeric)**: Each permission type is assigned a power of 2 value, and these values are summed for each user category:
    *   **Read (r) = 4**.
    *   **Write (w) = 2**.
    *   **Execute (x) = 1**.
    *   **Nothing (-) = 0**.
    *   The resulting three-digit octal number (e.g., `755`, `644`, `600`) represents permissions for the owner, group, and others.

2.  **Symbolic Notation**: Uses letters to represent user categories, operators, and permission types:
    *   **Who**: `u` (user/owner), `g` (group), `o` (others), `a` (all).
    *   **Operation**: `+` (add), `-` (remove), `=` (set exactly).
    *   **Permissions**: `r`, `w`, `x`, `X` (conditional execute), `s` (SetUID/SetGID), `t` (sticky bit), `u` (owner's permissions), `g` (group's permissions), `o` (other's permissions).

### Special Permissions

Linux offers three special permission bits that provide additional access-related features beyond basic read/write/execute. They are set using the **first (fourth) octal digit** when using numeric modes, or specific symbolic flags.

1.  **Set User ID (SUID)**:
    *   **On executable files**: When the file is executed, the program runs with the **permissions of the file owner** (e.g., as `root` for `passwd` command), regardless of the user who ran it.
    *   Displayed as `s` in the owner's execute position; `S` if execute bit is not set.
    *   Numeric value: `4` (as the first digit, e.g., `4755`).

2.  **Set Group ID (SGID)**:
    *   **On executable files**: When the file is executed, the program runs with the **permissions of the file's group**.
    *   **On directories**: **New files or subdirectories created within it will inherit the directory's group ownership**. This is beneficial for group collaboration.
    *   Displayed as `s` in the group's execute position; `S` if execute bit is not set.
    *   Numeric value: `2` (as the first digit, e.g., `2775`).

3.  **Sticky Bit**:
    *   **On directories**: Prevents users from deleting or renaming files within that directory unless they are the **owner of the directory, the owner of the file, or the superuser (`root`)**. This is commonly used for shared directories like `/tmp`.
    *   Displayed as `t` in the "others" execute position; `T` if execute bit is not set.
    *   Numeric value: `1` (as the first digit, e.g., `1777`).

### Default Permissions (`umask`)

**Linux assigns default permissions to a file or directory at the time of its creation**. These defaults are determined by the **`umask` (user mask)** value.

*   The `umask` is a **three-digit octal value** (or four digits, with the leftmost `0` currently having no significance for special bits).
*   It operates by **subtracting its value from preset initial permissions**: `0666` (rw-rw-rw-) for files and `0777` (rwxrwxrwx) for directories.
*   The result is the default permission. For example, a `umask` of `0022` results in `644` (`rw-r--r--`) for files and `755` (`rwxr-xr-x`) for directories.
*   You can view the current `umask` with `umask` command and set it temporarily using `umask [octal_value]`.
*   System default `umask` values are usually configured in files like `/etc/profile` and `/etc/bashrc`. Users can override this in their `~/.bashrc` or `~/.bash_profile`.

### Permission Management Tools

*   **`ls -l` and `ls -ld`**: Used to **view** permissions and ownership.
*   **`chmod`**: Used to **change** file and directory permissions. It accepts both symbolic and octal notation.
*   **`chown`**: Used to **change the owner** of files and directories.
*   **`chgrp`**: Used to **change the group ownership** of files and directories.
*   **`umask`**: Used to **set or display the default permissions** for newly created files and directories.
*   **`getfacl` and `setfacl`**: Commands for managing **Access Control Lists (ACLs)**, which provide a more specific way to allocate file permissions beyond traditional `ugo/rwx`.