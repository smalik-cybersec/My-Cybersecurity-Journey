# Manage User Passwords
### 1. Core Concept
> Managing user passwords involves setting, changing, and enforcing policies for user authentication credentials, with hashed passwords securely stored in the `/etc/shadow` file.

User passwords are the primary method of authentication in Linux. They are critical for securing user accounts and, by extension, the entire system. Instead of storing passwords in plain text, Linux stores cryptographic hashes of passwords in the `/etc/shadow` file, which is only readable by the `root` user. The `passwd` command is used by users to change their own password, and by the `root` user (or with `sudo`) to set or reset passwords for other users. Additionally, tools like `chage` allow administrators to implement password aging policies, forcing users to change their passwords regularly to enhance security.

### 2. Why It's Important
* **In Cybersecurity, we use this for:** Establishing robust authentication mechanisms, mitigating brute-force and credential stuffing attacks, and ensuring compliance with security policies. Proper password management, including strength requirements and regular changes, is fundamental to protecting user accounts and preventing unauthorized access to sensitive systems and data.
### 3. Practical Example
```bash
# SCRIPT: Manage User Passwords Demo
# AUTHOR: Shahid Ahmad Malik
# DATE: 2025-07-01
# DESCRIPTION: Demonstrates setting, changing, and checking password aging for a user.

echo "--- 1. Creating a temporary user for password management demo: passwordtestuser ---"
sudo useradd -m passwordtestuser
echo "User 'passwordtestuser' created."
grep passwordtestuser /etc/passwd

echo -e "\n--- 2. Setting a password for 'passwordtestuser' ---"
# You will be prompted to enter a new password for 'passwordtestuser' twice.
echo "Setting password for 'passwordtestuser'. Please enter a strong password when prompted."
sudo passwd passwordtestuser
echo "Password set for 'passwordtestuser'."

echo -e "\n--- 3. Viewing password aging information for 'passwordtestuser' ---"
# This shows details like last password change, min/max days between changes, warning days.
sudo chage -l passwordtestuser

echo -e "\n--- 4. Forcing 'passwordtestuser' to change password on next login ---"
# Set the minimum days between password change to 0, and last password change to 0 (epoch)
# This effectively makes the password expired, forcing a change on next login.
sudo chage -d 0 passwordtestuser
echo "Password for 'passwordtestuser' will expire on next login."

echo -e "\n--- Verifying the change ---"
sudo chage -l passwordtestuser

echo -e "\n--- 5. (Optional) Locking the user's password ---"
# This prevents the user from logging in with their password.
# sudo passwd -l passwordtestuser
# echo "Password for 'passwordtestuser' locked."
# sudo chage -l passwordtestuser

echo -e "\n--- 6. (Optional) Unlocking the user's password ---"
# sudo passwd -u passwordtestuser
# echo "Password for 'passwordtestuser' unlocked."
# sudo chage -l passwordtestuser

echo -e "\n--- 7. Cleaning up the temporary user ---"
sudo userdel -r passwordtestuser
echo "User 'passwordtestuser' deleted and home directory removed."
grep passwordtestuser /etc/passwd || echo "User 'passwordtestuser' no longer exists."