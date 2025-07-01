# Manage Local User Accounts
### 1. Core Concept
> Managing local user accounts involves creating, modifying, and deleting user entries on a Linux system to control access and privileges, with user information primarily stored in `/etc/passwd` and `/etc/shadow`.

Linux systems use local user accounts to identify individuals or services that interact with the system. Each user has a unique User ID (UID), a username, a password, and a home directory. Account management ensures proper access control. The `/etc/passwd` file stores basic user details (like username, UID, GID, home directory, and shell), while the `/etc/shadow` file securely stores encrypted passwords and password aging information. These files are critical for system security.

### 2. Why It's Important
* **In Cybersecurity, we use this for:** Implementing robust access control, managing user lifecycles, and revoking access permissions. This prevents unauthorized access to sensitive data and systems, adheres to the principle of least privilege, and is crucial for maintaining a secure and auditable environment.
### 3. Practical Example
```bash
# SCRIPT: Manage Local User Accounts Demo
# AUTHOR: Shahid Ahmad Malik
# DATE: 2025-07-01
# DESCRIPTION: Demonstrates creating, modifying, and deleting a local user account.

echo "--- 1. Creating a new user: cyberuser ---"
# Create a new user 'cyberuser' with a home directory and bash shell
# The -m option creates the home directory if it doesn't exist
# The -s option sets the default shell to /bin/bash
# The -c option adds a comment (full name) for the user
sudo useradd -m -s /bin/bash -c "Cyber Security Student" cyberuser
echo "User 'cyberuser' created."

echo -e "\n--- Verifying user creation (entry in /etc/passwd) ---"
grep cyberuser /etc/passwd

echo -e "\n--- 2. Setting a password for cyberuser ---"
# Set a password for the new user. You will be prompted to enter it.
sudo passwd cyberuser
echo "Password set for 'cyberuser'."

echo -e "\n--- 3. Modifying the user: Adding to a new group (e.g., 'sudo' or 'wheel') ---"
# Add 'cyberuser' to the 'sudo' group to give them sudo privileges (common for admin-like users)
# Use -aG to append to supplementary groups. Replace 'sudo' with 'wheel' on Red Hat based systems if needed.
sudo usermod -aG sudo cyberuser
echo "User 'cyberuser' added to 'sudo' group."

echo -e "\n--- Verifying group membership ---"
# Check the group membership for 'cyberuser'
groups cyberuser

echo -e "\n--- 4. (Optional) Locking and Unlocking a user account ---"
# Lock the user account (prevents login)
# sudo usermod -L cyberuser
# echo "User 'cyberuser' account locked."
# Unlock the user account
# sudo usermod -U cyberuser
# echo "User 'cyberuser' account unlocked."

echo -e "\n--- 5. Deleting the user: cyberuser ---"
# Delete the user 'cyberuser' and remove their home directory (-r)
sudo userdel -r cyberuser
echo "User 'cyberuser' deleted."

echo -e "\n--- Verifying user deletion ---"
# Attempt to find 'cyberuser' in /etc/passwd (should show no output)
grep cyberuser /etc/passwd || echo "User 'cyberuser' no longer exists in /etc/passwd."