#!/bin/bash
# SCRIPT: Self-Contained Output Script
# AUTHOR: Shahid Ahmad Malik
# DATE: [YYYY-MM-DD]
# DESCRIPTION: A script that forces all its output and created files into a dedicated output directory.

echo "--- Script Initializing ---"

# --- ONE-TIME SETUP: Define and create the output directory ---
# This is the only part you need to configure.
# It creates a unique directory for this specific run using the date and a random number.
OUTPUT_DIR="../../output/run_$(date +%Y%m%d)_$RANDOM"
mkdir -p "$OUTPUT_DIR"
echo "All output for this run will be saved in: $OUTPUT_DIR"
echo "--------------------------------------------------------"


# --- MAIN LOGIC: Wrap everything in parentheses to create a subshell ---
(
    #!/bin/bash
# SCRIPT: manage_users_groups_comprehensive.sh
# AUTHOR: Shahid Ahmad Malik
# DATE: 2025-07-01
# DESCRIPTION: Comprehensive script to demonstrate managing local user accounts, group accounts, and user passwords in Linux.
#             This script requires superuser (sudo) privileges to run.

echo "==================================================="
echo "  Comprehensive User and Group Management Demo"
echo "==================================================="

# --- SECTION 1: User Concepts & Superuser Access ---
echo -e "\n--- SECTION 1: User Concepts & Superuser Access ---"
echo "1.1. Displaying current user and groups:"
whoami
groups
echo "Superuser access is typically gained via 'sudo'."
echo "Example: 'sudo whoami' would show 'root'."
sudo whoami

# --- SECTION 2: Managing Local User Accounts ---
echo -e "\n--- SECTION 2: Managing Local User Accounts ---"

# Create a test user
TEST_USER="demouser"
echo "2.1. Creating a new user: ${TEST_USER}"
sudo useradd -m -s /bin/bash -c "Demonstration User" "${TEST_USER}"
if [ $? -eq 0 ]; then
    echo "User '${TEST_USER}' created successfully."
    grep "${TEST_USER}" /etc/passwd
else
    echo "Failed to create user '${TEST_USER}'. It might already exist."
fi

# Set a password for the test user
echo "2.2. Setting a password for '${TEST_USER}'. You will be prompted."
sudo passwd "${TEST_USER}"
if [ $? -eq 0 ]; then
    echo "Password set for '${TEST_USER}'."
else
    echo "Failed to set password for '${TEST_USER}'."
fi

# Modify user - change shell and add to supplementary group
echo "2.3. Modifying user '${TEST_USER}': adding to 'sudo' group."
# Note: 'sudo' is common on Debian/Ubuntu. Use 'wheel' for RHEL/CentOS.
sudo usermod -aG sudo "${TEST_USER}"
echo "User '${TEST_USER}' modified."
echo "New group memberships for '${TEST_USER}':"
groups "${TEST_USER}"

# Lock/Unlock user account
echo "2.4. Locking user account '${TEST_USER}' (prevents password login)."
sudo passwd -l "${TEST_USER}"
echo "Account status for '${TEST_USER}':"
sudo passwd -S "${TEST_USER}" # -S shows account status (L for locked)

echo "2.5. Unlocking user account '${TEST_USER}'."
sudo passwd -u "${TEST_USER}"
echo "Account status for '${TEST_USER}':"
sudo passwd -S "${TEST_USER}" # -S shows account status (P for password set, U for unlocked)

# --- SECTION 3: Managing Local Group Accounts ---
echo -e "\n--- SECTION 3: Managing Local Group Accounts ---"

# Create a test group
TEST_GROUP="devs"
echo "3.1. Creating a new group: ${TEST_GROUP}"
sudo groupadd "${TEST_GROUP}"
if [ $? -eq 0 ]; then
    echo "Group '${TEST_GROUP}' created successfully."
    grep "${TEST_GROUP}" /etc/group
else
    echo "Failed to create group '${TEST_GROUP}'. It might already exist."
fi

# Add the test user to the test group using gpasswd
echo "3.2. Adding '${TEST_USER}' to group '${TEST_GROUP}' using gpasswd."
sudo gpasswd -a "${TEST_USER}" "${TEST_GROUP}"
echo "Group memberships for '${TEST_USER}':"
groups "${TEST_USER}" # Verify updated group memberships

# Create another user and add to the group
ANOTHER_USER="coder"
echo "3.3. Creating another user '${ANOTHER_USER}' and adding to '${TEST_GROUP}'."
sudo useradd -m "${ANOTHER_USER}"
sudo gpasswd -a "${ANOTHER_USER}" "${TEST_GROUP}"
echo "Group members of '${TEST_GROUP}':"
grep "${TEST_GROUP}" /etc/group

# Remove user from group
echo "3.4. Removing '${ANOTHER_USER}' from group '${TEST_GROUP}'."
sudo gpasswd -d "${ANOTHER_USER}" "${TEST_GROUP}"
echo "Group members of '${TEST_GROUP}' after removal:"
grep "${TEST_GROUP}" /etc/group

# --- SECTION 4: Managing User Passwords & Aging ---
echo -e "\n--- SECTION 4: Managing User Passwords & Aging ---"

# Check password aging
echo "4.1. Viewing password aging info for '${TEST_USER}':"
sudo chage -l "${TEST_USER}"

# Force password change on next login
echo "4.2. Forcing '${TEST_USER}' to change password on next login."
sudo chage -d 0 "${TEST_USER}" # Set last password change date to Jan 1, 1970
echo "Updated password aging info for '${TEST_USER}':"
sudo chage -l "${TEST_USER}"

# --- SECTION 5: Cleanup ---
echo -e "\n--- SECTION 5: Cleanup ---"

echo "5.1. Deleting test users and groups."

# Delete users and their home directories
if id -u "${TEST_USER}" >/dev/null 2>&1; then
    sudo userdel -r "${TEST_USER}"
    echo "User '${TEST_USER}' deleted."
fi

if id -u "${ANOTHER_USER}" >/dev/null 2>&1; then
    sudo userdel -r "${ANOTHER_USER}"
    echo "User '${ANOTHER_USER}' deleted."
fi

# Delete the test group
if grep -q "^${TEST_GROUP}:" /etc/group; then
    sudo groupdel "${TEST_GROUP}"
    echo "Group '${TEST_GROUP}' deleted."
fi

echo -e "\n--- Verification of cleanup ---"
grep "${TEST_USER}" /etc/passwd || echo "User '${TEST_USER}' no longer exists."
grep "${ANOTHER_USER}" /etc/passwd || echo "User '${ANOTHER_USER}' no longer exists."
grep "${TEST_GROUP}" /etc/group || echo "Group '${TEST_GROUP}' no longer exists."

echo -e "\n==================================================="
echo "  Comprehensive User and Group Management Demo COMPLETE"
echo "==================================================="
) > "$OUTPUT_DIR/script_run.log" 2>&1

echo "--- Script Finished. Check the output directory. ---"