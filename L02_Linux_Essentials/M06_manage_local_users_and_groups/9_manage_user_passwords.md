To manage user passwords in Red Hat Enterprise Linux (RHEL), administrators employ a combination of command-line tools and secure file configurations to control password storage, complexity, aging, and user access. The process involves understanding where password information is stored and using specific commands to enforce security policies.

### Password Storage
In RHEL, password information is primarily managed through two key files:
*   **`/etc/passwd`**: This is a publicly readable plaintext file. Historically, it stored encrypted passwords, but for enhanced security, it now contains an 'x' in the password field, indicating that the actual hashed password is stored elsewhere. Each line in `/etc/passwd` corresponds to a user and includes fields for username, UID, GID, a comment, the home directory, and the default shell.
*   **`/etc/shadow`**: This file stores user authentication and password aging information, including the hashed password. It is only readable by the root user, making it more secure. The shadow password mechanism first checks `/etc/passwd` for user existence, then `/etc/shadow` for authenticity. The encrypted password string in `/etc/shadow` includes the hashing algorithm (e.g., '$6' for SHA-512 in RHEL 9), the salt, and the encrypted hash.
*   **`/etc/gshadow`**: This file stores hashed group-level passwords and group administrator information. Like `/etc/shadow`, it has no access permissions for non-root users.

### Password Management Tools and Commands

RHEL provides several command-line utilities for managing user passwords and related policies:
*   **`passwd`**: This command is used to **set or change a user's password**.
    *   The **root user can change any user's password** without knowing the previous one, which is useful for password resets.
    *   For regular users, `passwd` enforces "strong" password requirements, such as minimum length (e.g., 8 characters or more for regular users, 6 for root at install) and complexity (mix of letters, numbers, special characters, not based on dictionary words or username). The root user can override these complexity criteria.
    *   Passwords are not displayed on the screen when typed.
    *   The `-e` option can **force a user to change their password upon next login**.
*   **`chage`**: This command (short for "change age") is used to **set or alter password aging parameters** on a user account by modifying fields in `/etc/shadow`.
    *   Options include:
        *   `-d` or `--lastday`: Sets the date of the last password change. Setting it to `0` forces a password change at the next login.
        *   `-m` or `--mindays`: Sets the minimum number of days before a password can be changed again.
        *   `-M` or `--maxdays`: Sets the maximum number of days a password is valid before it must be changed.
        *   `-W` or `--warndays`: Sets the number of days a user will be warned before their password expires.
        *   `-I` or `--inactive`: Sets the number of days of inactivity after password expiry before the account is locked.
        *   `-E` or `--expiredate`: Sets a specific account expiration date.
        *   `-l` or `--list`: Displays the current password aging attributes for a user account.
*   **`usermod`**: While primarily for modifying user account attributes, it can also be used to **lock (`-L`) and unlock (`-U`) user accounts**. Locking an account inserts an exclamation mark `!` at the beginning of the password field in `/etc/shadow`.
*   **`gpasswd`**: This command can be used to set a password for a group, add group administrators, or add/delete group members.
*   **`/etc/login.defs`**: This configuration file defines **default password aging policies** and other user account settings that apply to *newly created users*. Changes made here do not affect existing users. Directives include `PASS_MAX_DAYS`, `PASS_MIN_DAYS`, `PASS_MIN_LEN`, and `PASS_WARN_AGE`.
*   **Cockpit Web Console**: Provides a graphical interface for managing user accounts, including setting and resetting passwords. It allows privileged users to create and manage accounts with administrative rights.

### Security Best Practices for Passwords
*   **Password Hashing**: RHEL uses hashing algorithms (e.g., SHA-512 by default for RHEL 9) to convert cleartext passwords into irreversible, unique strings. When a user attempts to log in, the entered password is hashed, and the result is compared to the stored hash.
*   **Password Complexity**: Passwords should be long (recommended 15-25 characters), include a mix of lowercase and uppercase letters, numbers, and special characters, and avoid dictionary words, usernames, or easily guessable personal information.
*   **Account Locking**: Accounts can be locked to prevent login access, often done for former employees or suspicious activity.
*   **`nologin` Shell**: For accounts not intended for interactive login (e.g., service accounts), the `/sbin/nologin` or `/bin/false` shell can be assigned to prevent shell access while still allowing other service-related access (e.g., file transfers).
*   **`sudo` Access**: Administrative privileges can be delegated using `sudo`, allowing specific users or groups to run commands as root (or another user) using their *own* password, rather than sharing the root password. All `sudo` actions are logged in `/var/log/secure`.
*   **PAM (Pluggable Authentication Modules)**: PAM provides a flexible framework for authentication, allowing administrators to configure complex password policies, account lockout mechanisms, and integrate with various authentication methods beyond local password files. For example, `minlen` in `/etc/security/pwquality.conf` (which PAM utilizes) sets the minimum password length.

### Guided Exercise: Manage User Passwords

This exercise focuses on practical application of these concepts. It typically involves:
1.  **Preparation**: Starting the lab environment using a command such as `lab start users-password`.
2.  **Accessing the server**: Opening an SSH session to the target server (e.g., `servera`) as a `student` user and then switching to the `root` user using `sudo -i`.
3.  **Forcing a password change on first login**: Using `chage -d 0 <username>` to ensure a user (e.g., `operator1`) is prompted to change their password immediately upon their next login. This is verified by attempting to log in as that user.
4.  **Setting password aging policy**:
    *   Changing the maximum password age for a specific user (e.g., `operator1`) to 90 days using `chage -M 90 operator1`.
    *   Setting an account expiration date for a user (e.g., `operator1`) using `chage -E <YYYY-MM-DD> operator1`, which may involve calculating a future date with the `date` command.
    *   Modifying the default maximum password days for *newly created users* by editing the `PASS_MAX_DAYS` parameter in `/etc/login.defs` (e.g., setting it to 180 days).
5.  **Verification**: Using `chage -l <username>` to confirm the applied password aging settings for individual users.
6.  **Cleanup**: Concluding the exercise with a command such as `lab finish users-password` to reset the environment.

These steps provide hands-on experience in implementing password security measures on local RHEL user accounts.




The `chage` command, which stands for "**change age**," is a crucial utility in Red Hat Enterprise Linux (RHEL) for **managing password aging parameters** on user accounts. It directly modifies various fields within the `/etc/shadow` file, which stores user authentication and password aging information. If the `/etc/shadow` file is not used for storing account passwords, the `chage` utility will not function. This command is highly effective for addressing RHCSA objectives related to adjusting password aging for local user accounts.

### Key Options and Their Functions

The `chage` command provides numerous options, available in both short and long formats, to control different password aging attributes:

*   **`-d` (`--lastday`)**: This option specifies **the date when the password was last modified**.
    *   You can set it to an explicit date in `YYYY-MM-DD` format.
    *   Setting it to `0` days (e.g., `chage -d 0 <username>`) **forces the user to change their password upon their next login**.
    *   This corresponds to **field 3** in the `/etc/shadow` file.
    *   For instance, in an exercise, `chage -d 0 operator1` would be used to force `operator1` to change their password.

*   **`-m` (`--mindays`)**: This sets the **minimum number of days that must elapse before a password can be changed again**.
    *   It corresponds to **field 4** in the `/etc/shadow` file.
    *   For example, `chage -m 5 Tim` would set a minimum of 5 days between password changes for the user `Tim`.

*   **`-M` (`--maxdays`)**: This designates the **maximum number of days a password remains valid before the user is required to change it**.
    *   It corresponds to **field 5** in the `/etc/shadow` file.
    *   This value can be set to `99999` to make the password permanent.
    *   For example, `chage -M 30 Tim` would set a maximum of 30 days for `Tim`'s password validity.

*   **`-W` (`--warndays`)**: This sets the **number of days a user will be warned before their password expires**.
    *   It corresponds to **field 6** in the `/etc/shadow` file.
    *   A value of `0` or null in this field disables this warning feature.
    *   For instance, `chage -W 7 Tim` would provide 7 days of warning before `Tim`'s password expires.

*   **`-I` (`--inactive`)**: This specifies the **number of days of inactivity after a password expires before the account becomes locked**.
    *   This period is also known as the inactivity period.
    *   An empty field or setting it to `-1` disables this feature, making the account permanent.
    *   The combination of `-M` and `-I` options with `chage` can be used to effectively **lock an account**.

*   **`-E` (`--expiredate`)**: This sets a **specific account expiration date**.
    *   The date can be specified in `YYYY-MM-DD` format, or `mm/dd/yyyy`.
    *   If left empty, the account will not expire on a specific date.
    *   For example, `chage -E 2030-01-01 usertest` sets the account for `usertest` to expire on January 1, 2030.

*   **`-l` (`--list`)**: This option is used to **display the current password aging attributes** for a user account.
    *   Running `chage -l <username>` will show a summary of all configured aging parameters for that user. For example, `chage -l Tim | grep Account` can extract the account expiration date.

### Relationship with `/etc/shadow` and Date Conversion

The `chage` command directly manipulates the numerical fields in the `/etc/shadow` file, which represent dates as the number of days since January 1, 1970 (UNIX epoch). For example, after running `chage -E 2030-01-01 usertest`, you can `grep usertest /etc/shadow` to see the numerical representation (e.g., `21915` for January 1, 2030). To convert these numerical dates to a human-readable format, you can use the `date` command: `date -d '1970-01-01 UTC + 18650 days'`.

### Practical Applications

`chage` is essential for implementing robust password policies:

*   **Forcing Password Changes**: Setting `-d 0` is a common administrative task to ensure users update their credentials upon next login.
*   **Account Expiration**: It allows administrators to set temporary accounts that automatically expire, which is useful for contractors or temporary access.
*   **Account Locking**: Using `-M` in conjunction with `-I` can enforce a policy where accounts become inactive after a period of password expiry.

While some password aging parameters can also be set using `useradd` and `usermod` commands, `chage` provides dedicated and comprehensive control over these settings.