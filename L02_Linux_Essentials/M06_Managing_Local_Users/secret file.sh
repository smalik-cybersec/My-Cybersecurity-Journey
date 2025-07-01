#!/bin/bash
###############################################################################
# Purpose: Demonstrate complete Linux user, group, and file access management
# Author: Cybersecurity Student
# Date: 2025-07-01
# This script covers:
# - User and group concepts
# - Superuser access
# - User and group account management
# - Password management
# - File and directory permissions
# - Default permissions (umask)
# - Real-world security best practices
###############################################################################

# 1. Describe User and Group Concepts
# -----------------------------------
# Users represent people/services; groups organize users for permission management.
# User info: /etc/passwd | Group info: /etc/group

# 2. Gain Superuser Access
# ------------------------
echo "Switching to superuser for administrative tasks..."
sudo -v  # Validates sudo access (asks for your password if needed)

# 3. Manage Local User Accounts
# -----------------------------
# Create two users: agentA (with home) and agentB (without home)
sudo useradd -m agentA           # -m creates home directory
sudo useradd -M agentB           # -M does NOT create home directory

# 4. Manage Local Group Accounts
# ------------------------------
# Create a group for secret agents
sudo groupadd secret_agents

# 5. Manage User Passwords
# ------------------------
# Set passwords for both users (you'll be prompted to enter them)
echo "Set password for agentA:"
sudo passwd agentA
echo "Set password for agentB:"
sudo passwd agentB

# 6. Add Users to Groups
# ----------------------
# Add both users to the secret_agents group
sudo usermod -aG secret_agents agentA
sudo usermod -aG secret_agents agentB

# 7. Verify User and Group Info
# -----------------------------
echo "User and group info for agentA:"
id agentA
echo "User and group info for agentB:"
id agentB

# 8. Interpret Linux File System Permissions
# ------------------------------------------
# Permissions are shown with ls -l: e.g., -rw-r----- (owner/group/others)
touch secret_file.txt
ls -l secret_file.txt  # Shows current permissions

# 9. Manage File System Permissions from the Command Line
# -------------------------------------------------------
# Only agentA (the owner) can read/write, group can read, others have no access
sudo chown agentA:secret_agents secret_file.txt
sudo chmod 640 secret_file.txt   # rw-r----- (owner: rw, group: r, others: -)

# 10. Manage Default Permissions and File Access (umask)
# ------------------------------------------------------
# Set restrictive umask so new files are private by default
umask 077
# Create a new file to see the effect
touch private_secret.txt
ls -l private_secret.txt  # Should show -rw-------

# 11. Change Ownership and Group of a File
# ----------------------------------------
# Suppose agentB needs to take over secret_file.txt
sudo chown agentB:secret_agents secret_file.txt

# 12. Add/Remove Users from Groups
# --------------------------------
# Remove agentB from secret_agents group
sudo gpasswd -d agentB secret_agents

# 13. Lock and Unlock User Accounts
# ---------------------------------
# Lock agentB's account (cannot log in)
sudo passwd -l agentB
# Unlock agentB's account
sudo passwd -u agentB

# 14. Set Password Expiry for agentA
# ----------------------------------
# Force agentA to change password at next login
sudo passwd --expire agentA

# 15. Create a Shared Directory with Special Permissions
# ------------------------------------------------------
sudo mkdir /srv/secret_shared
sudo chgrp secret_agents /srv/secret_shared
sudo chmod 2770 /srv/secret_shared  # rwxrws--- (setgid: new files inherit group)

# 16. Set Sticky Bit for Shared Directory (if needed)
# ---------------------------------------------------
# Only file owners can delete their files in this directory
sudo chmod +t /srv/secret_shared

# 17. Clean Up (optional)
# -----------------------
# Uncomment these lines if you want to remove test users and files after testing
# sudo userdel -r agentA
# sudo userdel -r agentB
# sudo groupdel secret_agents
# sudo rm secret_file.txt private_secret.txt
# sudo rm -r /srv/secret_shared

echo "Script complete. Review comments and commands for full understanding."
