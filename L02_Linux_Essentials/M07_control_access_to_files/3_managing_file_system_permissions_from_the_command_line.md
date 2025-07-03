Managing file system permissions from the command line is a fundamental skill in Red Hat Enterprise Linux (RHEL), allowing administrators to control who can access, modify, or execute files and directories.

### Understanding Linux File Permissions

Linux file permissions are designed to be flexible and secure, ensuring that users can only perform actions on files and directories for which they have explicit authorisation. Permissions are applied to three distinct **user categories** for each file or directory:
*   The **owner** of the file.
*   The **group** assigned to the file.
*   **Other** users on the system who are neither the owner nor a member of the owning group.

There are three primary **types of permissions** that can be granted or denied for each category:
*   **Read (r)**: Allows viewing the file's contents or, for a directory, listing its contents.
*   **Write (w)**: Allows changing the file's content, or for a directory, creating, erasing, or renaming files and subdirectories within it. It is important to note that the ability to delete or rename files is primarily determined by **write permissions on the containing directory**, not the file itself, unless a special permission (sticky bit) is set.
*   **Execute (x)**: Allows running a file as a program or, for a directory, entering it using the `cd` command. For directories, execute permission is typically needed alongside read permission to list contents.

The absence of a permission is indicated by a hyphen (`-`).

### Viewing File and Directory Permissions

To review file permissions and ownership, the **`ls` command** with the **`-l` (long listing) option** is used.
*   The **first character** of the `ls -l` output indicates the **file type**:
    *   `-` for a regular file.
    *   `d` for a directory.
    *   `l` for a symbolic link.
    *   Other characters exist for special file types like `c` (character device) or `b` (block device).
*   The **next nine characters** are grouped into three sets of three, representing the **read, write, and execute permissions** for the **owner**, **group**, and **others**, respectively.
*   To view information specifically about a directory itself, rather than its contents, the **`-d` option** is used with `ls -l` (e.g., `ls -ld /etc`).
*   A **plus sign (`+`)** immediately following the permission string indicates that **Access Control Lists (ACLs)** or SELinux extended attributes are set on the file. A dot (`.`) after the permissions may also indicate an SELinux security context.

### Changing File and Directory Permissions (`chmod`)

The **`chmod` command** ("change mode") is used to modify file and directory permissions. Only the **file's owner or the root user** can change permissions on a file or directory.

`chmod` supports two main methods for specifying permission changes:

1.  **Symbolic Method:** This method uses letters and symbols to add, remove, or set permissions.
    *   **Who (`u`, `g`, `o`, `a`):**
        *   `u`: The file owner.
        *   `g`: Members of the file's group.
        *   `o`: Other users (public).
        *   `a`: All (owner, group, and others). This is the default if `Who` is not specified.
    *   **What (Operator `+`, `-`, `=`)**:
        *   `+`: Adds the specified permissions.
        *   `-`: Removes the specified permissions.
        *   `=`: Sets permissions exactly as provided, overriding existing ones.
    *   **Which (Mode `r`, `w`, `x`, `X`)**:
        *   `r`: Read permission.
        *   `w`: Write permission.
        *   `x`: Execute permission.
        *   `X`: Conditional execute permission. Applies execute permissions only if the object is a directory or if it already has at least one execute bit set for user, group, or other.
    *   **Examples**:
        *   `chmod go-rw document.pdf`: Removes read and write permission for group and others.
        *   `chmod a+x myscript.sh`: Adds execute permission for everyone.
        *   `chmod -R g+rwx /home/user/myfolder`: Recursively adds read, write, and execute permissions for members of `myfolder`'s group.

2.  **Octal (Numeric) Method:** This method uses a **three-digit (or four-digit for special permissions) octal number** to represent permissions. Each digit corresponds to permissions for the owner, group, and others respectively, from left to right.
    *   Each permission type is assigned a numeric value: **Read (`r`) = 4**, **Write (`w`) = 2**, **Execute (`x`) = 1**. No permission is 0.
    *   To determine the digit for each permission category, **sum the values** for the desired permissions.
        *   `rwx` (read, write, execute) = `4 + 2 + 1 = 7`.
        *   `rw-` (read, write) = `4 + 2 = 6`.
        *   `r-x` (read, execute) = `4 + 1 = 5`.
        *   `r--` (read only) = `4`.
        *   `---` (no permissions) = `0`.
    *   **Examples**:
        *   `chmod 755 file`: Sets read, write, and execute for owner (`7`), and read and execute for group and others (`5`).
        *   `chmod 644 file`: Sets read and write for owner (`6`), and read only for group and others (`4`).

### Changing File and Directory Ownership (`chown` and `chgrp`)

File ownership in Linux consists of a **user owner** and a **group owner**.
*   The **`chown` command** ("change owner") is used to modify the user owner of a file.
    *   Only the **root user** can change the *user* owner of a file.
    *   **Syntax**:
        *   `chown user file`: Changes the user owner.
        *   `chown user:group file`: Changes both the user owner and the group owner simultaneously. Red Hat recommends using a colon (`:`) over a period (`.`) for separation.
        *   `chown :group file`: Changes only the group owner, leaving the user owner unchanged.
*   The **`chgrp` command** ("change group") is specifically used to modify the **group ownership** of a file.
    *   The **file's owner and the root user** can change the group ownership.
    *   **Syntax**: `chgrp group file`.
*   Both `chown` and `chgrp` support the **`-R` option** for recursively changing ownership of an entire directory tree.

### Managing Default Permissions (`umask`)

The **`umask` command** ("user file-creation mask") controls the **default permissions** assigned to new files and directories when they are created.
*   To **view the current `umask` value**, run the `umask` command without any arguments. The output is a four-digit octal number, where the first digit usually relates to special permissions, and the subsequent three digits apply to user, group, and others.
*   To **change the `umask` value** for the current shell session, specify a single octal argument (e.g., `umask 0027`). For persistent changes across sessions, the `umask` command can be added to shell startup scripts like `/etc/profile` or `~/.bashrc`.
*   **Default `umask` values** are typically `0022` for the root user and `0002` for normal users.
*   **Calculating default permissions**: The `umask` value is effectively **subtracted** from a preset initial permission value.
    *   For **files**, the initial value is `666` (`rw-rw-rw-`). For example, `666 - 027 = 640`. Note that newly created regular files do not automatically get execute permissions, even if the `umask` suggests it.
    *   For **directories**, the initial value is `777` (`rwxrwxrwx`). For example, `777 - 027 = 750`.

### Special Permissions

Linux offers **special permission bits** that can be applied to files and directories, extending beyond the basic read, write, and execute permissions. These are represented by an additional leading digit in octal notation.

1.  **Set-UID (SUID) Bit**:
    *   **Numeric value**: **4**.
    *   **On executable files**: When an executable file with the SUID bit set is run, it executes **as if the owner of the file was running it**, applying the owner's permissions. In `ls -l` output, a lowercase `s` appears in the owner's execute position (`-rws`) if execute permission is also present, or an uppercase `S` if it is not.
    *   **On directories**: The SUID bit has **no effect**.

2.  **Set-GID (SGID) Bit**:
    *   **Numeric value**: **2**.
    *   **On executable files**: When an executable file with the SGID bit set is run, it executes **as if the process was a member of the file's owning group**, applying the group's permissions. In `ls -l` output, a lowercase `s` appears in the group's execute position (`drwxrwsr-x`) if execute permission is also present, or an uppercase `S` if it is not.
    *   **On directories**: All new files and subdirectories created within an SGID-enabled directory **inherit the group ownership of that directory**, rather than the primary group of the creating user. This feature is commonly used for **group collaboration**.

3.  **Sticky Bit**:
    *   **Numeric value**: **1**.
    *   **On directories**: When the sticky bit is set on a directory, **only the owner of a file (or the root user) can delete or rename that file** within the directory, even if other users have write permission to the directory. This prevents users from deleting each other's files in shared writable directories. In `ls -l` output, a lowercase `t` appears in the "others" execute position (`drwxrwxrwt`) if execute permission is also present, or an uppercase `T` if it is not.
    *   **On files**: The sticky bit has **no effect**.