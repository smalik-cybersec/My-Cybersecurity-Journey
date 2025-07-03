The "Lab: Manage Local Users and Groups" on page 191 of the `rh124-9.0-student-guide.pdf` is a practical exercise designed to equip you with essential skills for managing user accounts and group memberships, and configuring password policies in Red Hat Enterprise Linux (RHEL). This lab specifically targets objectives related to adjusting password aging for local user accounts and managing local groups.

### Objectives of the Lab

Upon completing this lab, you should be able to:
*   **Set a default password aging policy** for local user passwords.
*   **Create and use a secondary group** for new users.
*   **Create three new users** with the newly configured secondary group.
*   **Set an initial password** for these newly created users.
*   **Configure administrative rights** for members of the secondary group to execute any command as any user using `sudo`.
*   **Set a user-specific password aging policy** for individual accounts.

### Preparation for the Lab

As the `student` user on the `workstation` machine, you are instructed to use the `lab start users-review` command. This command prepares your environment by ensuring all necessary resources are available for the exercise.

### Detailed Steps and Key Concepts

The lab involves the following sequence of operations, primarily performed as the `root` user on `serverb` after establishing an SSH session from `workstation`:

1.  **Accessing `serverb` as `root`**: You begin by logging into `serverb` as `student` via SSH, then using `sudo -i` to switch to the `root` user. The `sudo -i` command allows a user to gain superuser access, prompting for the `student` user's password.

2.  **Setting a Default Password Aging Policy**:
    *   You are instructed to ensure that newly created users must change their passwords every 30 days. This is typically done by modifying the **`/etc/login.defs`** file, which defines default password aging policies for *newly created users* [conversation history, 76, 151, 683, 685]. Changes here do *not* affect existing users [conversation history].
    *   Specifically, the `PASS_MAX_DAYS` parameter in `/etc/login.defs` would be set to `30`. Other parameters like `PASS_MIN_DAYS` (minimum days between password changes) and `PASS_WARN_AGE` (warning days before expiration) are also found in this file [conversation history, 685].

3.  **Creating a Secondary Group**:
    *   You create a new group named `consultants` with a Group ID (GID) of `35000` using the `groupadd` command. The `groupadd` command is used to create new group accounts. GIDs are unique numerical values assigned to groups.

4.  **Configuring Administrative Rights for the Group**:
    *   You configure administrative rights for all `consultants` group members to execute any command as any user. This is typically achieved by adding an entry to the **`/etc/sudoers.d/`** directory, or directly modifying `/etc/sudoers` (though using `visudo` for direct edits is recommended to prevent syntax errors). A common entry would be `%consultants ALL=(ALL) ALL`, allowing members of the `consultants` group to run any command as any user without a password.

5.  **Creating New Users with Secondary Group Membership**:
    *   You create three new users: `consultant1`, `consultant2`, and `consultant3`. The `useradd` command is used to create user accounts, which also sets up their home directories and private groups by default.
    *   Crucially, these users are added to the `consultants` group as their secondary group. This is done using the `usermod -aG` command, where `-a` appends the user to the specified supplementary groups and `-G` specifies the groups. Secondary groups allow users to share access to files and resources with other group members.

6.  **Setting Initial Passwords**:
    *   The passwords for `consultant1`, `consultant2`, and `consultant3` are set to `redhat`. The `passwd` command is used for this purpose. As `root`, you can set a password for any user.

7.  **Setting Account Expiration Dates**:
    *   The accounts for `consultant1`, `consultant2`, and `consultant3` are set to expire in 90 days from the current day. The **`chage -E`** (or `--expiredate`) command is used for this, specifying a date in `YYYY-MM-DD` format [conversation history]. This sets a specific date after which the account will be locked [conversation history].

8.  **Modifying User-Specific Password Policy**:
    *   The password policy for the `consultant2` account is modified to require a new password every 15 days. This is done using the **`chage -M 15 consultant2`** command, where `-M` (or `--maxdays`) sets the maximum number of days a password remains valid [conversation history]. The `chage` command is the primary tool for managing password aging parameters on a per-user basis, modifying fields in the `/etc/shadow` file [conversation history, 40, 690].
    *   You also force `consultant1`, `consultant2`, and `consultant3` to change their passwords on their first login. This is achieved using **`chage -d 0 <username>`**, where `-d` (or `--lastday`) sets the date of the last password change to the Unix epoch, forcing an immediate change [conversation history].

### Verification and Conclusion

After completing the instructions, you use the `lab grade users-review` command to evaluate your work and correct any reported failures. Finally, `lab finish users-review` is executed to clean up the lab environment, ensuring no impact on subsequent exercises.

This lab provides hands-on experience with fundamental RHEL administration tasks related to user and group management, focusing heavily on the capabilities of the `chage` command for enforcing password policies, and the use of `useradd`, `usermod`, and `groupadd` for account and group creation and modification. It also touches upon the importance of `/etc/shadow` for secure password storage and `/etc/login.defs` for system-wide defaults.