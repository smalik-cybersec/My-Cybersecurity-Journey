The "Guided Exercise: Manage User Passwords" on page 187 of the `rh124-9.0-student-guide.pdf` is designed to provide hands-on experience with configuring password policies for local user accounts in Red Hat Enterprise Linux (RHEL).

This exercise primarily focuses on the use of the `chage` command to manage user password aging and expiration settings, and it also touches upon the `passwd` command for setting user passwords and the `/etc/login.defs` file for defining default password policies for new users.

### Objectives of the Guided Exercise
The exercise aims to teach you how to:
*   **Force a password change** when a user logs in for the first time.
*   **Force a password change every 90 days**.
*   **Set an account to expire 180 days** from the current date.

### Exercise Preparation (`Before You Begin`)
Before starting the guided exercise, you are instructed to use the `lab start users-password` command as the `student` user on the `workstation` machine. This command prepares your environment and ensures that all necessary resources are available for the exercise.

### Detailed Steps of the Guided Exercise (`Instructions`)

The exercise involves the following steps:

1.  **Accessing the Target System**: You begin by opening an SSH session from `workstation` to `servera` as the `student` user, then switching to the `root` user using `sudo -i`. The `sudo -i` command allows you to gain superuser access, and you'll be prompted for the `student` user's password.

2.  **Initial User Setup (Implicit)**: Although not explicitly stated as a goal of *this* exercise, previous guided exercises often involve creating users like `operator1`, `operator2`, and `operator3` and setting their initial passwords (e.g., `redhat`). When the `root` user sets a password for any user using `passwd <username>`, it can assign even a simple password like `redhat`, despite a "BAD PASSWORD" warning, because `root` can override default complexity criteria. In the guided exercise, you're instructed to `su - operator1` and observe that the login fails. This is likely a pre-configured state from the lab setup.

3.  **Forcing Password Change on First Login**:
    *   You are instructed to use `chage -d 0 operator1` as `root` to force `operator1` to change their password upon their next login. The `-d` (or `--lastday`) option sets the date of the last password change. Setting it to `0` days (the UNIX epoch) ensures the user is prompted immediately.
    *   You then attempt to log in as `operator1`. You'll first enter the old password (`redhat`), and then be prompted: "You are required to change your password immediately (administrator enforced)". You then set a new password (e.g., `forsooth123`). After successfully changing it, you log out. This confirms the `-d 0` setting worked.

4.  **Setting Password Maximum Age**:
    *   As `root`, you will set the maximum age of `operator1`'s password to 90 days using `chage -M 90 operator1`. The `-M` (or `--maxdays`) option defines the maximum number of days a password can be used before it must be changed.
    *   You verify this setting using `chage -l operator1`. This command lists all password aging attributes for the specified user, including "Password expires".

5.  **Setting Account Expiration Date**:
    *   Still as `root`, you will determine a date 180 days from the current day using the `date -d "+180 days" +%F` command.
    *   Then, you set `operator1`'s account to expire on that calculated date using `chage -E <YYYY-MM-DD> operator1`. The `-E` (or `--expiredate`) option specifies a date after which the user's account will be locked. This is different from password expiration; an expired account is completely disabled.
    *   You verify the account expiration date using `chage -l operator1`, which will show "Account expires" with the newly set date.

6.  **Setting Default Password Policy for New Users**:
    *   You are instructed to set the `PASS_MAX_DAYS` parameter to `180` in the `/etc/login.defs` file. This file defines default password aging policies for *newly created users*. This means that any user created *after* this change will have a default password maximum age of 180 days. Existing users are *not* affected by changes made in `/etc/login.defs`.
    *   You are advised to use a text editor like `vim /etc/login.defs` for this step, with administrative rights.

7.  **Exiting Sessions**: Finally, you exit from the `root` session on `servera` and return to the `student` session on `workstation`.

### Exercise Conclusion (`Finish`)
To conclude the exercise, you run the `lab finish users-password` command from the `student` user's home directory on `workstation`. This step is crucial for resetting the environment and preventing any impact on subsequent exercises.

### Key Concepts Reinforced by the Exercise

This guided exercise highlights several fundamental aspects of user password management in RHEL:

*   **`chage` Command**: This is the primary tool for managing password aging parameters like minimum/maximum password age, warning period, inactivity period, and account expiration dates on a per-user basis. It directly modifies the `/etc/shadow` file.
*   **`/etc/shadow` File**: This secure file stores hashed passwords and password aging information, including the last change date, minimum/maximum days between changes, warning days, inactivity days, and account expiration dates. It is only readable by the `root` user for security. An exclamation mark `!` at the beginning of the password field indicates a locked account.
*   **`/etc/passwd` File**: This file stores basic user account information but has an 'x' in the password field, indicating the actual password hash is in `/etc/shadow`. It is world-readable.
*   **`/etc/login.defs` File**: This file defines default password aging and other user account settings that apply to *newly created users*. Changes to this file do not affect existing users.
*   **`passwd` Command**: Used by users to change their own passwords and by the `root` user to set or reset any user's password without needing the old one. It checks password strength but `root` can override warnings.
*   **Account Locking/Unlocking**: The `usermod -L` command locks an account by prepending `!` to the password hash in `/etc/shadow`, preventing login. The `usermod -U` command unlocks it by removing the `!`.
*   **Password Hashing**: RHEL stores passwords as hashes (e.g., SHA-512) in `/etc/shadow`, making them irreversible. When a user logs in, the entered password is hashed and compared to the stored hash.
*   **Security Practices**: The exercise implicitly reinforces best practices such as forcing password changes periodically and setting account expirations for temporary users to enhance system security.