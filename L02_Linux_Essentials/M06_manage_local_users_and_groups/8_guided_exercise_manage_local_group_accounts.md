The "Guided Exercise: Manage Local Group Accounts" is a specific practical exercise aimed at teaching the fundamental administrative tasks of managing local groups in Red Hat Enterprise Linux (RHEL). Red Hat generally recommends using command-line tools for group management, although graphical utilities are also available.

### Objectives of the Guided Exercise: Manage Local Group Accounts

The primary objectives of this guided exercise are to:
*   **Create groups** and learn how to assign users to these groups as supplementary (secondary) members.
*   **Configure `sudo` access for a specific group**, granting its members administrative privileges.

### Steps Involved in the Guided Exercise

The exercise typically begins by preparing the system environment using a `lab start users-group` command. Once the environment is ready, the following key steps are performed:

1.  **Access the server as a privileged user**: You log in to the target server (e.g., `servera`) as a regular user (e.g., `student`) and then elevate your privileges to `root` using the `sudo -i` command, providing the necessary password.

2.  **Create secondary groups**:
    *   A group named `operators` is created with a specific **Group ID (GID)** of `30000` using the command `groupadd -g 30000 operators`. Groups have a unique GID that the system uses for internal identification.
    *   Another group named `admin` is created without specifying a GID (`groupadd admin`). In this case, the system automatically assigns the next available GID.
    *   The existence of both newly created groups is then **verified** by examining the `/etc/group` file, typically using `tail /etc/group`. The `/etc/group` file contains critical group information, including the group name, GID, and a list of its members.

3.  **Add users to secondary groups**:
    *   Existing users (e.g., `operator1`, `operator2`, and `operator3`) are added as members to the `operators` group. This is achieved using the `usermod -aG operators <username>` command for each user. The `-aG` option is crucial here as it ensures that the user is **appended** to the specified supplementary group without removing their existing group memberships.
    *   Their successful addition is **confirmed** by checking each user's group memberships using the `id <username>` command. This command displays the user's User ID (UID), primary GID, and all groups they belong to.
    *   Similarly, users `sysadmin1`, `sysadmin2`, and `sysadmin3` are added to the `admin` group. Their memberships are then verified by examining the `/etc/group` file again.

4.  **Configure `sudo` access for a group**:
    *   To grant administrative rights to all members of the `admin` group, a configuration file is created within the `/etc/sudoers.d/` directory. This is typically done by redirecting the line `%admin ALL=(ALL) ALL` into a file like `/etc/sudoers.d/admin`. The `%` symbol denotes a group in `sudoers` configuration.
    *   The functionality is **verified** by switching to a user account that is a member of the `admin` group (e.g., `sysadmin1`) and attempting to execute a command with `sudo`. This demonstrates that members of the configured group can now run commands as the superuser.

Finally, the exercise concludes with a `lab finish users-group` command to clean up the environment.

### Core Concepts of Local Group Account Management

This guided exercise, and the broader topic of managing local group accounts, relies on several fundamental Linux concepts and tools:

*   **Group Identity (GID)**: Each group has a unique numeric identifier called a GID. For regular user groups, GIDs typically start at `1000` and above, while values below `1000` are reserved for system groups.
*   **Group Information Files**:
    *   The primary file for local group information is `/etc/group`. It is a plaintext file that defines each group with its name, a placeholder for the password ('x'), its GID, and a comma-separated list of its members (secondary members).
    *   Encrypted group passwords and group administrator information are stored in `/etc/gshadow`, which is only readable by the `root` user for security.
*   **Types of Groups**:
    *   **Primary Group**: Every user has exactly one primary group, which is the default group assigned to files and directories they create. By default, Red Hat Enterprise Linux employs a **User Private Group (UPG)** scheme, where each new user account automatically gets a private group with the same name as the username, and this becomes their primary group. This scheme enhances privacy by default.
    *   **Supplementary (Secondary) Groups**: Users can be members of additional groups beyond their primary group. These supplementary groups allow users to gain specific access permissions to resources shared by that group. The `wheel` group is a common example, often configured to provide `sudo` privileges to its members.
*   **Command-Line Tools for Group Management**:
    *   `groupadd`: Used to **create new group accounts**. It allows specifying a GID with the `-g` option, or it assigns the next available GID.
    *   `groupmod`: Used to **modify properties of an existing group**, such as changing its name with the `-n` option or its GID with the `-g` option.
    *   `groupdel`: Used to **delete a group account**. A group cannot be deleted if it is the primary group of an existing user.
    *   `usermod`: Used to **add users to or remove users from supplementary groups**. The `-aG` option is critical for adding users to supplementary groups without inadvertently removing them from other groups they already belong to.
    *   `newgrp`: Allows a user to **temporarily change their current primary group** within a shell session, which affects the ownership of newly created files. This change is temporary and reverts upon logging out.
    *   `chgrp`: Changes the **group ownership of files or directories**.
*   **Special Permissions for Group Collaboration**:
    *   The **Set Group ID (SGID) bit** (represented by `s` in the group's execute permission field) can be set on a directory. When the SGID bit is set, any new files or subdirectories created within that directory automatically inherit the group ownership of the directory itself, facilitating group collaboration. This can be set using `chmod g+s directory` or by specifying an octal mode such as `2770`.
    *   The **Sticky Bit** (represented by `t` in the 'other' execute permission field) when applied to a directory, prevents users from deleting or renaming files in that directory that they do not own, even if they have write permissions to the directory.
*   **GUI Tools**: The Red Hat User Manager (`system-config-users`) and the Cockpit web console offer graphical interfaces to manage groups, including creating, modifying, and deleting them, and managing group memberships. However, command-line methods are often preferred for efficiency and in certified exams.