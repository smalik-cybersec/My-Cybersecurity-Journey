The "Guided Exercise: Manage Local User Accounts" [495, p. 174] is a practical exercise designed to teach you the fundamental administrative tasks of **creating, modifying, and deleting local user accounts** on a Linux system [495, p. 174]. This skill is crucial for any system administrator.

### Objectives and Outcomes
The primary objective of this exercise is to enable you to **configure a Linux system with additional user accounts** [495, p. 174].

### Before You Begin
Before starting the exercise, you need to set up your system using the `lab` command as the `student` user on the `workstation` machine. This ensures all necessary resources are available [495, p. 543]. The command to run is:
*   `[student@workstation ~]$ lab start users-user` [495, p. 543]

### Instructions for the Exercise

The exercise involves performing several user management operations on `servera` [495, p. 543].

1.  **Log in and switch to `root`**:
    *   From your `workstation`, initiate an SSH session to `servera` as the `student` user [495, p. 543].
    *   Once logged in, switch to the `root` user by executing `sudo -i`. You will be prompted for the `student` user's password (`student`) [495, p. 543].

2.  **Create `operator1` user and set password**:
    *   As the `root` user, use the `useradd` command to create a new user named `operator1` [495, p. 543]. The `useradd` command automatically creates the user's home directory (e.g., `/home/operator1`) and a private group with the same name as the user. Default user settings are influenced by `/etc/default/useradd` and `/etc/login.defs`.
    *   Immediately set a password for `operator1` using the `passwd` command, choosing `redhat` [495, p. 544]. Although Red Hat typically enforces password complexity rules (e.g., minimum eight characters, no dictionary words or usernames) for regular users, the `root` user can override these and set simpler passwords.

3.  **Create additional users**:
    *   Repeat the process for `operator2` and `operator3` users, creating them with `useradd` and setting their passwords to `redhat` using `passwd` [495, p. 544, 545].

4.  **Modify user comments**:
    *   Use the `usermod` command to add or change a comment for `operator1` to "Operator One" and for `operator2` to "Operator Two" [495, p. 545]. The `usermod` command is a versatile tool for altering existing user account attributes.
    *   Verify these changes by using `grep` to check the `/etc/passwd` file [495, p. 545].

5.  **Attempt to delete a user's home directory (without `-r`)**:
    *   Try to delete the `operator3` user using `userdel operator3` (without the `-r` option) [495, p. 545]. By default, `userdel` removes the user's entry from the system's authentication files but leaves their home directory intact.

6.  **Verify home directory persistence**:
    *   Confirm that `operator3`'s home directory still exists in `/home` using `ls -l /home` [495, p. 546]. This demonstrates the default behaviour of `userdel`.

7.  **Exit and return to `workstation`**:
    *   Exit the `root` shell, then exit the `student` user's shell on `servera` to return to your `workstation` [495, p. 546].

### Key Concepts in Local User Account Management

Beyond this specific exercise, the sources highlight several important concepts for managing local user accounts:

*   **User Identity**: Linux systems identify users through a **User ID (UID)**. The `root` (superuser) account always has a UID of `0`. System accounts (for services) are typically assigned UIDs from `1` to `999`, while regular user accounts usually start from `1000` onwards.
*   **Core Authentication Files**: Several files are crucial for user authentication and information:
    *   `/etc/passwd`: Contains basic user details like username, UID, primary Group ID (GID), home directory, and default shell. The password field has an 'x' to indicate that the actual encrypted password is stored elsewhere.
    *   `/etc/shadow`: Stores encrypted passwords and password aging information, accessible only by the `root` user for security.
    *   `/etc/group`: Contains local group definitions.
    *   `/etc/gshadow`: Stores encrypted group passwords.
*   **User Creation (`useradd`)**:
    *   The `useradd` command is the standard command-line utility for creating new user accounts.
    *   It typically creates a home directory for the user, populating it with default configuration files from the **`/etc/skel` (skeleton) directory**.
    *   **Administrative privileges (root access)** are mandatory for adding users.
*   **User Modification (`usermod`)**:
    *   The `usermod` command allows administrators to modify various aspects of an existing user account, such as their username (`-l`), home directory (`-d`), default shell (`-s`), and supplementary group memberships (`-aG`).
    *   It can also be used to **lock (`-L`) or unlock (`-U`)** a user account, which prevents or allows login without deleting the account.
*   **User Deletion (`userdel`)**:
    *   The `userdel` command is used to remove user accounts.
    *   To remove the user's home directory and mail spool directory along with the account, the **`-r` option** must be explicitly used (e.g., `userdel -r username`). It is a security best practice to remove unused accounts.
*   **Password Management (`passwd`, `chage`)**:
    *   The `passwd` command is used to set or change user passwords.
    *   **Password aging policies** (e.g., minimum and maximum days between password changes, warning periods, and account expiration) are managed using the `chage` command. These policies are stored in the `/etc/shadow` file.
    *   Accounts can be configured with a **"no-login" shell** (like `/sbin/nologin` or `/bin/false`) to prevent interactive logins, commonly used for service accounts.
*   **Graphical Tools**: Red Hat provides graphical utilities for user management, such as the **Cockpit web console** and the **Red Hat User Manager (`system-config-users`)**. These tools offer a user-friendly interface for creating, modifying, and deleting users and groups.

This exercise, along with the broader context from the sources, equips you with the fundamental skills for effective local user account management in Red Hat Enterprise Linux.