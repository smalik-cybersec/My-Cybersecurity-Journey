The "Manage Local User Accounts" section, typically found in Red Hat Enterprise Linux (RHEL) administration guides, focuses on the fundamental tasks associated with **user management** on a Linux system. This includes creating, modifying, and deleting user accounts.

**Objectives and Key Concepts:**

*   **Create, modify, and delete local user accounts**. This is a core administrative task.
*   Understand the purpose of users and groups on a Linux system.
*   Manage local user accounts using various **command-line tools**.

**Methods and Tools for Managing Local User Accounts:**

1.  **Creating User Accounts:**
    *   The `useradd` command is the **primary tool** for creating new users from the command line.
        *   It creates the user's home directory and sets up account information.
        *   It also automatically creates a **private group** for the user, usually with the same name as the username.
        *   Default options for new users are defined in `/etc/default/useradd` or `/etc/login.defs`, and can be viewed using `useradd -D`.
        *   The `useradd` command can take various parameters to override default values, such as specifying a different home directory (`-d`), shell (`-s`), or unique UID (`-u`).
        *   To add users, **administrative privileges (root access)** are required.
    *   **Graphical User Interface (GUI) Tools**:
        *   **Red Hat User Manager** (`system-config-users`) is a GUI utility for user and group configuration. It provides an intuitive interface to create, edit, or delete users and groups.
        *   The **Cockpit web console** also allows privileged users to create and manage user accounts.

2.  **Modifying User Accounts:**
    *   The `usermod` command is used to **change attributes of an existing user account**.
        *   It supports similar options to `useradd` for modifying properties like comments (`-c`), home directory (`-d`), and login shell (`-s`).
        *   It can also **lock (`-L`) or unlock (`-U`)** a user account.
        *   `usermod` is used to add a user to supplementary groups (`-aG`).
    *   **Password Management**:
        *   The `passwd` command is used to **set or change a user's password**.
        *   The `root` user can **reset any user's password without knowing the previous one**.
        *   RHEL enforces **password complexity rules**, typically requiring at least eight characters, and discouraging dictionary words, usernames, or previous passwords.
        *   Password aging policies can be set using `chage`. This includes setting minimum/maximum days between changes, warning periods, and account expiration dates. Password aging information is stored in the `/etc/shadow` file.
        *   The `passwd` command can also be used to force a user to change their password at the next login (`-e`) or to lock/unlock an account (`-l`/`-u`).
    *   **User Account Information Files**:
        *   `/etc/passwd`: Stores basic user account information (username, UID, GID, home directory, shell), with an 'x' placeholder for the password.
        *   `/etc/shadow`: Stores encrypted passwords and password aging information, accessible only by the root user for security.
        *   `/etc/group`: Stores local group information.

3.  **Deleting User Accounts:**
    *   The `userdel` command is used to **remove a user account** from the system.
    *   By default, `userdel` only removes the user's information from authentication files; it **does not delete the user's home directory**.
    *   To remove the user's home directory and mail directory, the `-r` option must be used (`userdel -r username`). This is often recommended for full removal unless files need to be transferred.

**Security Considerations:**

*   Red Hat strongly recommends against logging in directly as the `root` user for routine tasks. Instead, log in as a normal user and use tools like `su` or `sudo` to gain temporary administrative privileges.
*   All `sudo` operations are logged, providing an audit trail.
*   Unused accounts should be routinely deleted, as they can be a security risk if compromised.
*   The `root` user has a UID of 0 and has full, unrestricted access to the system. Normal users typically have UIDs of 1000 and beyond. System accounts use UIDs between 1 and 999.
*   The system creates automatic backups of critical user authentication files like `/etc/passwd` and `/etc/shadow` (e.g., `/etc/passwd-`, `/etc/shadow-`).

This comprehensive approach to managing local user accounts is vital for maintaining security and control over a Linux system.