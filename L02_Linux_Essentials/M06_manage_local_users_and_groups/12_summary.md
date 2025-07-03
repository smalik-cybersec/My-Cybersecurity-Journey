The entry "Summary" in your source refers to the **summary section of Chapter 6: Manage Local Users and Groups** in the `rh124-9.0-student-guide.pdf`. This summary follows the "Lab: Manage Local Users and Groups" on page 191 of the same document.

Drawing upon our previous conversation, the lab is a practical exercise designed to teach you how to manage user accounts and group memberships, and how to configure password policies within Red Hat Enterprise Linux (RHEL).

Here is a comprehensive summary of the key concepts and tasks covered in the "Lab: Manage Local Users and Groups":

### Lab Objectives and Preparation
The lab aims to equip you with the skills to:
*   **Set a default password aging policy** for new local user accounts [conversation history].
*   **Create and utilise a secondary group** for new users [conversation history].
*   **Create three new users** and assign them to this secondary group [conversation history].
*   **Set initial passwords** for these new users [conversation history].
*   **Configure `sudo` administrative rights** for members of the secondary group, allowing them to execute any command as any user [conversation history].
*   **Set user-specific password aging policies** for individual accounts [conversation history].

To prepare for the lab, you, as the `student` user on the `workstation` machine, are instructed to use the `lab start users-review` command to set up the environment [conversation history].

### Key Steps and Concepts Covered in the Lab

The lab predominantly involves performing actions as the `root` user on `serverb`, typically accessed via an SSH session from `workstation`, followed by `sudo -i` [conversation history].

1.  **Setting a Default Password Aging Policy**:
    *   You learn to ensure that newly created users must change their passwords every 30 days. This is achieved by modifying the **`/etc/login.defs`** file, specifically the `PASS_MAX_DAYS` parameter [conversation history]. It's crucial to understand that changes in this file affect *new* users, not existing ones [conversation history].

2.  **Creating a Secondary Group**:
    *   A new group, `consultants`, is created with a specified Group ID (GID) of `35000` using the **`groupadd`** command [conversation history]. This command is fundamental for creating new group accounts in Linux.

3.  **Configuring Administrative Rights for the Group**:
    *   Members of the `consultants` group are granted administrative privileges to execute any command as any user, typically without a password prompt. This is usually accomplished by adding an entry like `%consultants ALL=(ALL) ALL` to a file in the **`/etc/sudoers.d/`** directory or by editing `/etc/sudoers` using `visudo` [conversation history].

4.  **Creating New Users and Assigning Secondary Group Membership**:
    *   Three new user accounts (`consultant1`, `consultant2`, `consultant3`) are created using the **`useradd`** command [conversation history].
    *   These users are then added to the `consultants` group as a secondary group using the **`usermod -aG`** command. Secondary groups are vital for users to share access to files and resources [conversation history].

5.  **Setting Initial Passwords**:
    *   Initial passwords (e.g., `redhat`) are set for the newly created users using the **`passwd`** command. As the `root` user, you can set passwords for any account [conversation history].

6.  **Setting Account Expiration Dates**:
    *   The accounts for `consultant1`, `consultant2`, and `consultant3` are configured to expire 90 days from the current date. This is performed using the **`chage -E`** (or `--expiredate`) command, which modifies the user's account expiration date in `YYYY-MM-DD` format [conversation history].

7.  **Modifying User-Specific Password Policy**:
    *   The password policy for `consultant2` is specifically adjusted to require a password change every 15 days using the **`chage -M 15 consultant2`** command, where `-M` (or `--maxdays`) sets the maximum password validity period [conversation history]. The `chage` command is the primary tool for managing per-user password aging parameters, which are stored in the `/etc/shadow` file [conversation history].
    *   Additionally, all three `consultant` accounts are configured to force a password change upon their first login using **`chage -d 0 <username>`**. This sets the last password change date to the Unix epoch, effectively mandating an immediate password update [conversation history].

### Conclusion of the Lab

Upon completing these tasks, you use the `lab grade users-review` command to verify your work and address any issues. Finally, `lab finish users-review` is executed to clean the lab environment for future exercises [conversation history].

This lab provides hands-on experience with critical administrative commands (`groupadd`, `useradd`, `usermod`, `passwd`, `chage`) and important configuration files (`/etc/login.defs`, `/etc/shadow`, `/etc/sudoers`, and files within `/etc/sudoers.d/`) relevant to user and group management and security in RHEL [conversation history].