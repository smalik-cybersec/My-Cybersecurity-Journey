# Red Hat System Administration I

## 1. 🧠 What Is It (Definition + Explanation)

* **Definition**: Red Hat System Administration I is a foundational course focusing on essential Linux administration skills using Red Hat Enterprise Linux (RHEL). It covers core tasks such as accessing the command line, managing files, users, groups, permissions, processes, services, and basic networking, as outlined in the provided document (e.g., "RedHatLinux-book.pdf").

* **Explanation**: 
  Red Hat System Administration I introduces learners to the core competencies required to manage RHEL systems effectively. It is part of the Red Hat Certified System Administrator (RHCSA) curriculum, designed for individuals new to Linux or transitioning from other operating systems. The course emphasizes hands-on skills for managing a Linux environment, including navigating the file system, configuring users and groups, controlling services, and securing systems via SSH and file permissions. It aligns with real-world system administration tasks, such as maintaining secure and efficient server environments.

  Think of a Linux system as a city: the kernel is the infrastructure (roads, utilities), and the system administrator is the city manager ensuring everything runs smoothly—traffic (processes), security (permissions), and utilities (services). This course equips you with the tools to manage this "city" effectively, preparing you for real-world scenarios like setting up servers, troubleshooting issues, or securing systems against unauthorized access.

  **Why It Matters**: In cybersecurity, mastering Linux administration is critical because Linux powers most servers, cloud infrastructures, and security tools. Understanding RHEL administration ensures you can maintain secure, reliable systems, which is foundational for roles like system administrator, security analyst, or DevOps engineer.

## 2. 💡 Real-World Use Cases

* **Server Management**: Configuring and maintaining web servers, databases, or application servers running RHEL in enterprise environments.
* **Security Operations**: Setting up secure file permissions and SSH access to protect sensitive data on Linux servers.
* **User Management**: Creating and managing user accounts for employees in an organization, ensuring proper access controls.
* **Troubleshooting**: Using logs and process management tools to diagnose and resolve server issues in a data center.
* **Automation**: Writing shell scripts to automate repetitive administrative tasks, such as backups or user account creation.

## 3. 💻 Examples

Below are examples of common tasks covered in Red Hat System Administration I, using commands from the provided document.

### Example 1: Navigating the File System
```bash
# Display the current working directory
pwd
# Output: /home/user

# List files in long format
ls -l /etc
# Output: Shows files like /etc/passwd, /etc/group

# Change to the /etc directory
cd /etc

# Create an empty file
touch myfile.txt
```

### Example 2: Managing Users
```bash
# Create a new user
sudo useradd -m newuser
# Set a password for the new user
sudo passwd newuser
# Output: Prompts for new password

# Verify user creation
id newuser
# Output: uid=1001(newuser) gid=1001(newuser) groups=1001(newuser)
```

### Example 3: Changing File Permissions
```bash
# Create a file
touch /tmp/example.txt

# Set read/write for owner, read-only for group and others
chmod 644 /tmp/example.txt
# Verify permissions
ls -l /tmp/example.txt
# Output: -rw-r--r-- 1 user user 0 Jul 11 10:20 example.txt
```

### Example 4: Managing Services with systemctl
```bash
# Check the status of the SSH service
systemctl status sshd
# Output: Shows if sshd is active and running

# Start the SSH service
sudo systemctl start sshd

# Enable SSH service to start at boot
sudo systemctl enable sshd
```

## 4. 🧪 Lab Task (Hands-On Practice)

**Objective**: Create a user, assign permissions, and manage a service in a safe, controlled environment (e.g., a virtual machine running RHEL 9).

**Prerequisites**: Use a virtual machine with RHEL 9 installed (e.g., via VMware Workstation, as described in the document). Ensure you have root access.

**Steps**:
1. **Create a User**:
   ```bash
   sudo useradd -m testuser
   sudo passwd testuser
   # Enter a secure password when prompted
   ```
   **Verification**: Run `id testuser` to confirm the user exists.

2. **Create a File and Set Permissions**:
   ```bash
   touch /home/testuser/testfile.txt
   chmod 640 /home/testuser/testfile.txt
   ```
   **Verification**: Run `ls -l /home/testuser/testfile.txt`. Expected output: `-rw-r----- 1 testuser testuser 0 Jul 11 10:20 testfile.txt`.

3. **Manage a Service**:
   ```bash
   sudo systemctl status sshd
   sudo systemctl stop sshd
   sudo systemctl start sshd
   ```
   **Verification**: Run `systemctl is-active sshd`. Expected output: `active`.

**Safety Note**: Perform this lab in a virtual machine to avoid affecting production systems. Use a lab environment like the one provided by CRAW Academy or a local VM setup.

## 5. 📋 Quiz (Knowledge Check)

1. **What command displays the current working directory?**
   A) `ls`
   B) `pwd`
   C) `cd`
   D) `dir`
   **Answer**: B) `pwd`
   **Explanation**: The `pwd` command prints the working directory, showing the full path of the current location in the file system.

2. **Which command creates a new user with a home directory?**
   A) `useradd username`
   B) `useradd -m username`
   C) `adduser -h username`
   D) `newuser username`
   **Answer**: B) `useradd -m username`
   **Explanation**: The `-m` option ensures a home directory is created for the new user.

3. **What does `chmod 644 file.txt` do?**
   A) Sets execute permissions for all
   B) Sets read/write for owner, read-only for group and others
   C) Removes all permissions
   D) Sets read-only for owner
   **Answer**: B) Sets read/write for owner, read-only for group and others
   **Explanation**: In octal notation, 644 translates to `rw-r--r--`, granting read/write to the owner and read-only to group and others.

4. **Which command checks the status of a service?**
   A) `systemctl start service`
   B) `systemctl status service`
   C) `service status`
   D) `chkconfig service`
   **Answer**: B) `systemctl status service`
   **Explanation**: The `systemctl status` command displays the current state of a service, including whether it is active or inactive.

5. **What is the purpose of the `sudo` command?**
   A) Deletes user accounts
   B) Runs commands as another user, typically root
   C) Lists all processes
   D) Changes file ownership
   **Answer**: B) Runs commands as another user, typically root
   **Explanation**: `sudo` allows authorized users to execute commands with superuser privileges, enhancing security by limiting direct root access.

## 6. 🚨 Common Mistakes

* **Not Using `sudo` Correctly**: Beginners often forget to use `sudo` for commands requiring root privileges, resulting in "Permission denied" errors.
  * **Why**: Commands like `useradd` or `systemctl` often require elevated permissions.
  * **Fix**: Always prepend `sudo` when necessary, and ensure the user is in the `wheel` group for sudo access (`usermod -aG wheel username`).

* **Incorrect File Permissions**: Setting overly permissive permissions (e.g., `chmod 777`) can expose files to unauthorized access.
  * **Why**: This undermines security by allowing anyone to read, write, or execute files.
  * **Fix**: Use the principle of least privilege (e.g., `chmod 640` for sensitive files) and verify with `ls -l`.

* **Forgetting to Enable Services at Boot**: Starting a service without enabling it means it won’t persist after a reboot.
  * **Why**: `systemctl start` only affects the current session.
  * **Fix**: Use `systemctl enable` to ensure the service starts at boot.

## 7. ✨ Tips, Tricks, Best Practices

* **Use Tab Completion**: Press the `Tab` key to auto-complete commands or file paths, reducing typos and speeding up navigation.
* **Check Man Pages**: Use `man <command>` (e.g., `man chmod`) for detailed documentation on any command.
* **Backup Before Changes**: Always back up critical files (e.g., `/etc/passwd`) before modifying them, using `cp /etc/passwd /etc/passwd.bak`.
* **Use `systemctl enable --now`**: Combines starting and enabling a service in one command for efficiency.
* **Secure Permissions**: Default to restrictive permissions (e.g., 640 for files, 750 for directories) and adjust only as needed.

## 8. ✅ Summary

* Red Hat System Administration I teaches foundational Linux skills for managing RHEL systems.
* Key tasks include navigating the file system, managing users, setting permissions, and controlling services.
* Commands like `pwd`, `ls`, `useradd`, `chmod`, and `systemctl` are central to administration.
* Always perform labs in a safe, isolated environment like a virtual machine.
* Understanding these skills is critical for cybersecurity roles involving Linux systems.

## 9. 🔗 Related Topics

* **Module 2: Access the Command Line** – Deepens understanding of Bash shell usage.
* **Module 7: Control Access to Files** – Explores file permissions in detail.
* **Module 8: Monitor and Manage Linux Processes** – Covers process management with `ps` and `kill`.
* **Module 9: Control Services and Daemons** – Focuses on `systemd` and service management.
* **Module 10: Configure and Secure SSH** – Details securing remote access with SSH.