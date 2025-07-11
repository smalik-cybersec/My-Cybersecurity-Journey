# Lab: Configure and Secure SSH

This lab provides a hands-on guide to configuring and securing the SSH (Secure Shell) service on a Red Hat Enterprise Linux (RHEL) system, aligning with topics covered in resources like *RHCSA Red Hat Enterprise Linux 8* or *Red Hat Enterprise Linux 9 Administration*. The goal is to set up a secure SSH environment by configuring key-based authentication, modifying the SSH daemon settings, and ensuring proper firewall and SELinux configurations. This lab follows the structured Markdown format requested, tailored for your One-Year Cybersecurity Diploma Course and suitable for a professional GitHub portfolio.

---

## 1. 🧠 Core Concept

**Definition**: Configuring and securing SSH involves setting up the OpenSSH server (`sshd`) to enable secure remote access while implementing best practices to minimize vulnerabilities, such as using key-based authentication, restricting access, and adjusting network settings.

**Explanation**:
SSH is a critical tool for remote system administration, but its default configuration can be vulnerable to attacks like brute-forcing or unauthorized access. This lab focuses on securing the SSH service by enabling key-based authentication, changing the default port, restricting user access, and ensuring compatibility with firewall and SELinux policies. These steps enhance security while maintaining functionality for legitimate users.

- **Beginner Level**: SSH lets you log in to a remote server securely. Securing it means making sure only the right people can access it, using strong "keys" instead of passwords and locking down settings.
- **Intermediate Level**: The `sshd` daemon is configured via `/etc/ssh/sshd_config`, where you can disable password authentication, change ports, or limit users. Firewall (`firewalld`) and SELinux settings must align with SSH configurations to avoid connectivity issues.
- **Advanced Level**: Advanced SSH security includes using strong ciphers, enabling `Match` blocks for user-specific rules, and monitoring logs (`/var/log/secure`) for unauthorized access attempts. Tools like `fail2ban` or intrusion detection systems can further protect against attacks.

**Analogy**: Securing SSH is like fortifying a castle gate. You replace a weak password lock with a high-security keycard system, limit who can approach the gate, and install cameras (logs) to monitor attempts to break in.

---

## 2. 💻 Use in Real Life

Securing SSH is essential in:

- **System Administration**: Ensuring only authorized administrators can access servers, often in data centers or cloud environments.
- **Security Operations**: Protecting SSH access to prevent unauthorized logins, which could lead to data breaches or system compromise in a SOC environment.
- **Compliance**: Meeting standards like PCI-DSS, HIPAA, or NIST by enforcing strong authentication and access controls.
- **DevOps**: Securing SSH for automated deployments or CI/CD pipelines using tools like Ansible or Jenkins.
- **Penetration Testing**: Ethical hackers test SSH configurations for vulnerabilities, such as weak authentication or exposed root logins.

**Example Use Case**: A system administrator configures SSH on a production web server to allow only key-based logins from specific users, changes the default port to avoid automated attacks, and monitors logs for suspicious activity.

---

## 3. 🐧 For Linux Topics

This lab uses RHEL commands to configure and secure the SSH service. The following commands assume you have two systems: a client (`workstation`) and a server (`server1.example.com`), with the user `student` and `root` access via `sudo`.

### Command: `ssh-keygen`
**Purpose**: Generate a public/private key pair for key-based authentication.
```bash
# On the client (workstation), generate an RSA key pair
ssh-keygen -t rsa -b 4096
# Example output:
# Generating public/private rsa key pair.
# Enter file in which to save the key (/home/student/.ssh/id_rsa): [Press Enter]
# Enter passphrase (empty for no passphrase): [Press Enter]
# Enter same passphrase again: [Press Enter]
# Your identification has been saved in /home/student/.ssh/id_rsa
# Your public key has been saved in /home/student/.ssh/id_rsa.pub
```

### Command: `ssh-copy-id`
**Purpose**: Copy the public key to the remote server.
```bash
# Copy the public key to server1
ssh-copy-id student@server1.example.com
# Example output:
# /usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
# student@server1.example.com's password: [Enter password, e.g., 'student123']
# Number of key(s) added: 1
```

### Command: `vi` or `nano`
**Purpose**: Modify the SSH daemon configuration (`/etc/ssh/sshd_config`).
```bash
# On the server (server1), edit sshd_config
ssh student@server1.example.com 'sudo vi /etc/ssh/sshd_config'
# Add or uncomment the following lines:
# Port 2222
# PermitRootLogin no
# PasswordAuthentication no
# PubkeyAuthentication yes
# AllowUsers student
# Save and exit
```

### Command: `sshd -T`
**Purpose**: Test the SSH configuration for errors.
```bash
# On the server, test the configuration
ssh student@server1.example.com 'sudo sshd -T | grep -E "port|permitrootlogin|passwordauthentication|pubkeyauthentication|allowusers"'
# Example output:
# port 2222
# permitrootlogin no
# passwordauthentication no
# pubkeyauthentication yes
# allowusers student
```

### Command: `systemctl`
**Purpose**: Reload the SSH service to apply changes.
```bash
# On the server, reload sshd
ssh student@server1.example.com 'sudo systemctl reload sshd'
# Verify the service status
ssh student@server1.example.com 'sudo systemctl status sshd'
# Example output:
# ● sshd.service - OpenSSH server daemon
#   Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; vendor preset: enabled)
#   Active: active (running) since Fri 2025-07-11 11:30:00 IST; 5min ago
```

### Command: `firewall-cmd`
**Purpose**: Allow the new SSH port (2222) in the firewall.
```bash
# On the server, update the firewall
ssh student@server1.example.com 'sudo firewall-cmd --permanent --add-port=2222/tcp'
ssh student@server1.example.com 'sudo firewall-cmd --reload'
# Verify the port
ssh student@server1.example.com 'sudo firewall-cmd --list-ports'
# Example output: 2222/tcp
```

### Command: `semanage`
**Purpose**: Update SELinux context for the new SSH port.
```bash
# On the server, install policycoreutils-python-utils if needed
ssh student@server1.example.com 'sudo dnf install -y policycoreutils-python-utils'
# Add SELinux context for port 2222
ssh student@server1.example.com 'sudo semanage port -a -t ssh_port_t -p tcp 2222'
# Verify SELinux port context
ssh student@server1.example.com 'sudo semanage port -l | grep ssh'
# Example output:
# ssh_port_t tcp 22, 2222
```

### Man Pages
- `man sshd_config`: Details directives like `Port`, `PermitRootLogin`, and `AllowUsers`.
- `man sshd`: Explains the SSH daemon and its runtime behavior.
- `man firewall-cmd`: Describes firewall configuration for SSH ports.
- `man semanage`: Covers SELinux port management.

---

## 4. 🐍 For Python Topics

Python’s `paramiko` library can automate SSH configuration tasks, such as editing `sshd_config` or restarting the service.

### Example: Automate SSH Configuration
```python
import paramiko

# Initialize SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the server
    ssh.connect('server1.example.com', username='student', key_filename='/home/student/.ssh/id_rsa')
    
    # Append configuration to sshd_config
    config_lines = [
        "Port 2222\n",
        "PermitRootLogin no\n",
        "PasswordAuthentication no\n",
        "PubkeyAuthentication yes\n",
        "AllowUsers student\n"
    ]
    for line in config_lines:
        ssh.exec_command(f"echo '{line}' | sudo tee -a /etc/ssh/sshd_config")
    
    # Reload the SSH service
    stdin, stdout, stderr = ssh.exec_command('sudo systemctl reload sshd')
    print(stdout.read().decode() or "SSH service reloaded")
    
    # Check for errors
    if stderr.read():
        print(f"Errors: {stderr.read().decode()}")
        
except Exception as e:
    print(f"Operation failed: {e}")
finally:
    ssh.close()
```

**Explanation**:
- `tee -a`: Appends configuration lines to `/etc/ssh/sshd_config` with `sudo` privileges.
- `systemctl reload sshd`: Applies changes without disconnecting sessions.
- **Common Errors**: Insufficient permissions, SELinux denials, or invalid configuration syntax.

**Output**:
```
SSH service reloaded
```

---

## 5. 🧪 Lab / Practice Tasks

### Task 1: Set Up Key-Based Authentication
**Objective**: Configure passwordless SSH access for the `student` user.
```bash
# On the client (workstation)
# Step 1: Generate an RSA key pair
ssh-keygen -t rsa -b 4096
# Press Enter to accept defaults (no passphrase)

# Step 2: Copy the public key to the server
ssh-copy-id student@server1.example.com
# Enter password (e.g., 'student123')

# Step 3: Test passwordless login
ssh student@server1.example.com
# Expected result: Logs in without a password
# [student@server1 ~]$
```

### Task 2: Secure SSH Configuration
**Objective**: Disable password authentication, root login, and change the SSH port to 2222.
```bash
# On the server (server1)
# Step 1: Edit sshd_config
ssh student@server1.example.com 'sudo vi /etc/ssh/sshd_config'
# Add or uncomment:
# Port 2222
# PermitRootLogin no
# PasswordAuthentication no
# PubkeyAuthentication yes
# AllowUsers student
# Save and exit

# Step 2: Test the configuration
ssh student@server1.example.com 'sudo sshd -T | grep -E "port|permitrootlogin|passwordauthentication|pubkeyauthentication|allowusers"'
# Expected output:
# port 2222
# permitrootlogin no
# passwordauthentication no
# pubkeyauthentication yes
# allowusers student

# Step 3: Reload the SSH service
ssh student@server1.example.com 'sudo systemctl reload sshd'
```

### Task 3: Configure Firewall and SELinux
**Objective**: Allow the new SSH port (2222) and update SELinux.
```bash
# On the server
# Step 1: Add port 2222 to the firewall
ssh student@server1.example.com 'sudo firewall-cmd --permanent --add-port=2222/tcp'
ssh student@server1.example.com 'sudo firewall-cmd --reload'

# Step 2: Update SELinux context
ssh student@server1.example.com 'sudo semanage port -a -t ssh_port_t -p tcp 2222'

# Step 3: Verify configurations
ssh student@server1.example.com 'sudo firewall-cmd --list-ports'
# Expected output: 2222/tcp
ssh student@server1.example.com 'sudo semanage port -l | grep ssh'
# Expected output: ssh_port_t tcp 22, 2222

# Step 4: Test the new port
ssh -p 2222 student@server1.example.com
# Expected result: Connects successfully
```

### Task 4: Verify Security Settings
**Objective**: Test restricted access and monitor logs.
```bash
# Step 1: Attempt login as root (should fail)
ssh -p 2222 root@server1.example.com
# Expected output: Permission denied (publickey).

# Step 2: Attempt login with password (should fail)
ssh -p 2222 -o PubkeyAuthentication=no student@server1.example.com
# Expected output: Permission denied (publickey).

# Step 3: Check SSH logs for failed attempts
ssh -p 2222 student@server1.example.com 'sudo tail /var/log/secure'
# Expected output (example):
# Jul 11 11:45:00 server1 sshd[1234]: Failed publickey for root from 192.168.1.100 port 12345 ssh2
```

---

## 6. 🚨 Common Mistakes to Avoid

- **Not Testing Configuration**: Always test with `sshd -T` to catch syntax errors before reloading:
  ```bash
  ssh student@server1.example.com 'sudo sshd -T'
  ```
- **Locking Yourself Out**: Test changes on a second session to avoid losing access if `sshd` fails to start.
- **Incorrect Permissions**: Ensure `/etc/ssh/sshd_config` has `644` permissions and `~/.ssh/authorized_keys` has `600`:
  ```bash
  ssh student@server1.example.com 'sudo chmod 644 /etc/ssh/sshd_config'
  ssh student@server1.example.com 'chmod 600 ~/.ssh/authorized_keys'
  ```
- **Forgetting Firewall/SELinux**: Failing to update `firewalld` or SELinux for a new port blocks connections.
- **Not Backing Up `sshd_config`**: Always create a backup before editing:
  ```bash
  ssh student@server1.example.com 'sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak'
  ```

**Pro Tip**: Use `sudo systemctl reload sshd` instead of `restart` to apply changes without disconnecting active sessions.

---

## 7. ✨ Tips, Tricks & Shortcuts

- **SSH Config File (Client)**: Simplify connections with `~/.ssh/config`:
  ```bash
  Host server1
      HostName server1.example.com
      User student
      Port 2222
      IdentityFile ~/.ssh/id_rsa
  ```
  Then connect with `ssh server1`.
- **Verbose Logging**: Enable debug logging for troubleshooting:
  ```bash
  # Edit /etc/ssh/sshd_config
  LogLevel DEBUG
  ```
  Check logs with:
  ```bash
  ssh student@server1.example.com 'sudo tail /var/log/secure'
  ```
- **Use `fail2ban`**: Install and configure `fail2ban` to block brute-force attacks:
  ```bash
  ssh student@server1.example.com 'sudo dnf install -y fail2ban'
  ssh student@server1.example.com 'sudo systemctl enable --now fail2ban'
  ```
- **Test Locally**: Test configurations on `localhost` before applying to a remote server:
  ```bash
  ssh -p 2222 student@localhost
  ```

---

## 8. ✅ Summary

- Securing SSH involves enabling key-based authentication, changing the default port, disabling root login, and restricting users.
- Key commands include `ssh-keygen`, `ssh-copy-id`, `vi`, `sshd -T`, `systemctl`, `firewall-cmd`, and `semanage`.
- Update firewall and SELinux to support custom ports (e.g., 2222).
- Python’s `paramiko` automates SSH configuration tasks.
- Common errors include syntax mistakes, unupdated firewall/SELinux, or incorrect file permissions.
- Monitor `/var/log/secure` for security events and use tools like `fail2ban` for added protection.

---

## 9. 🔗 Related Topics

- **SSH Key-Based Authentication**: Configure keys before disabling password authentication.
- **Linux File Permissions**: Secure `sshd_config` (`644`) and `authorized_keys` (`600`).
- **Systemd Services**: Manage the `sshd` service for reloads and status checks.
- **Networking and Firewalls**: Configure `firewalld` for SSH ports.
- **Log Analysis**: Analyze `/var/log/secure` for SSH access attempts.

---

## 🧰 Bonus

- **Diagram**: ASCII representation of SSH security workflow:
  ```
  [Client] ----[Key-Based Auth (Port 2222)]----> [Server]
     |                                            |
  (id_rsa)                                 (sshd_config)
     |                                            |
  (Signs challenge) <----> (Verifies key, restricts users)
  ```
- **Cybersecurity Relevance**: SSH is a common target for brute-force attacks. Securing it prevents unauthorized access, data breaches, or lateral movement in a network.
- **Interview Questions** (RHCSA, CEH, CompTIA Security+):
  - How do you secure an SSH server against brute-force attacks?
  - What steps are required to change the SSH port and ensure connectivity?
  - How do you troubleshoot an SSH connection failure after configuration changes?

This lab provides a professional, GitHub-ready guide for configuring and securing SSH, tailored for your cybersecurity diploma. It equips you with practical skills for real-world administration and security tasks. Let me know if you need additional labs or specific configurations!