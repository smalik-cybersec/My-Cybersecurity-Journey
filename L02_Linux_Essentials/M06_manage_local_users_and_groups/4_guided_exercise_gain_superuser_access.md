The "Guided Exercise: Gain Superuser Access" [495, p. 166] is designed to help you practise **switching to the superuser account** and **running commands as root**, as well as granting other users superuser access through the `sudo` command.

### Objectives and Outcomes
The primary objectives of this exercise are to:
*   Switch to the superuser account to manage a Linux system.
*   Grant other users superuser access through the `sudo` command.

Upon completing the exercise, you should be able to:
*   **Use the `sudo` command to switch to the `root` user** and access an **interactive shell as `root` without knowing the superuser's password**.
*   Understand that the `sudo` command overrides the `PATH` variable from the environment for security reasons, though subsequent commands can still update it.

### Before You Begin
Before starting the exercise, you need to use the `lab` command as the `student` user on the `workstation` machine to prepare your system. This ensures all required resources are available. The command to do this is `lab start users-superuser`.

### Instructions for the Exercise

1.  **Log in and switch to `root`**:
    *   From the `workstation`, open an SSH session to `servera` as the `student` user.
    *   Then, use `sudo -i` to switch to the `root` user on `servera`. You will be prompted for the `student` user's password (`student`). The prompt will change to `[root@servera ~]#`, indicating you are now the `root` user. This command switches to the `root` account and runs the `root` user's default login shell and associated interactive login scripts.

2.  **Explore the `root` environment and `PATH`**:
    *   While in the `root` shell (`sudo -i`), observe the `PATH` variable.
    *   Exit the `root` shell by typing `exit` to return to the `student` user's shell.

3.  **Switch to `root` with `sudo su -`**:
    *   Run the `sudo su -` command from the `student` user's shell to become the `root` user again. You will be prompted for the `student` user's password (`student`).
    *   Note that `sudo su -` behaves differently from `sudo -i` in how it sets the `PATH` variable initially, as `su -` runs the `root` login scripts *after* `sudo` has reset the `PATH`.
    *   Exit the `root` shell by typing `exit` to return to the `student` user's shell.

4.  **Verify `sudo` access for another user**:
    *   Confirm that the `operator1` user has been configured to run any command as any user using `sudo`. This is typically set up by creating a file like `/etc/sudoers.d/operator1` with content such as `operator1 ALL=(ALL) ALL`.

5.  **Perform administrative tasks as the delegated user**:
    *   Switch to the `operator1` user using `su - operator1` and enter their password (`redhat`).
    *   Attempt to view the `/var/log/messages` file *without* using `sudo`; it should fail due to permissions.
    *   Attempt to view the same file *with* `sudo`; it should succeed after you enter the `operator1` user's password (`redhat`). This demonstrates that `sudo` typically requires the user's *own* password for authentication.
    *   Perform other administrative tasks, such as copying `/etc/motd` to `/etc/motdOLD` and then removing `/etc/motdOLD`, using the `sudo` command.

6.  **Return to `workstation`**:
    *   Exit the `operator1` user's shell, then exit the `student` user's shell on `servera` to return to the `workstation`.

### Important Considerations from Sources

*   **`root` Account**: The `root` user is the main administrative account in a Linux system, identified by a **UID of 0**, and has full, unrestricted access and privileges over the entire system.
*   **Security Best Practice**: Red Hat strongly recommends **not logging in directly as the `root` user** for routine tasks. Logging in as `root` means the entire desktop environment runs with administrative privileges, increasing the risk of system compromise if a security vulnerability is exploited. Instead, administrators should log in as a normal, unprivileged user and temporarily gain superuser privileges using mechanisms like `su` or `sudo`.
*   **`su` Command**: The `su` command (Substitute User) allows you to change your identity to another user within the same shell session.
    *   `su` (without a username) defaults to `root` and prompts for the `root` password.
    *   `su -` starts a **login shell** for the target user, meaning their environment variables are loaded, and the working directory changes to their home directory. This is generally preferred for a full impersonation.
    *   `su -c command` executes a single command as a different user without fully switching shells.
    *   When `root` uses `su` to switch to another user, no password is required for the target user.
*   **`sudo` Command**: `sudo` (Super User Do) is the **recommended way to delegate administrative access**.
    *   It allows granular control over which commands a user can execute.
    *   `sudo` typically requires the **user's *own* password** for authentication, not the `root` password. This behaviour can be overridden.
    *   `sudo -i` switches to the `root` account and runs the `root` user's default login shell and associated startup scripts, creating an environment identical to a direct `root` login.
    *   `sudo -s` runs a shell for the `root` user but without loading login scripts.
    *   All `sudo` operations are **logged**, typically in `/var/log/secure`, providing an audit trail.
    *   Configuration for `sudo` is in the `/etc/sudoers` file, which **must be edited using the `visudo` command** to prevent syntax errors and simultaneous edits. Additional `sudo` configurations can be placed in separate files within the `/etc/sudoers.d/` directory for modularity.
    *   The **`wheel` group** is commonly used in RHEL to designate users permitted to use `sudo` for administrative tasks. By default, members of the `wheel` group in RHEL 7 and later can use `sudo` to run commands as any user, including `root`, using their own password.
*   **Auditing**: If users have to log in as a regular user and then switch to the `root` account, you can view a log event to help provide accountability.
*   **Password Complexity**: While the `root` user can assign any password, even weak ones, regular users are typically required to choose a password at least eight characters long that does not contain dictionary words, usernames, or previous passwords.

This guided exercise provides practical experience with the core methods of privilege escalation, which are crucial for system administration in Red Hat Enterprise Linux.