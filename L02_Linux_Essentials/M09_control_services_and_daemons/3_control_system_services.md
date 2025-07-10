📘 Title: Control System Services 

🧠 Theory:
In Red Hat Enterprise Linux 9, `systemd` is the init system that manages system services and daemons.  Controlling system services involves managing their lifecycle (starting, stopping, restarting, reloading) and their behavior at boot (enabling, disabling).  `systemd` uses "unit files" (e.g., `.service`, `.target`, `.socket`) to define how these services behave. 

Key concepts for controlling system services include:

  * **Unit States**: Services can be in various states, such as `active (running)`, `inactive (dead)`, `enabled`, `disabled`, `static`, or `masked`. 
  * **Targets**: `systemd` uses targets to group services and other units.  Targets like `multi-user.target` (for command-line systems) and `graphical.target` (for graphical desktops) define a system state, and services are enabled to start with specific targets. 
  * **Dependencies**: Services often have dependencies on other services or system states. `systemd` automatically manages these dependencies when starting or stopping services. 

💡 Use Cases:

  * **Starting a web server**: After installing Apache (`httpd`) or Nginx (`nginx`), you need to explicitly start the service for the web server to become operational. 
  * **Stopping a database**: Before performing maintenance or upgrades on a database like MariaDB, you would stop its service to ensure data integrity. 
  * **Applying configuration changes**: Some services require a "reload" to apply new configuration files without fully restarting, minimizing downtime. 
  * **Enabling services on boot**: If you want a service (e.g., SSH, a custom application) to automatically start every time the system boots, you must enable it. 
  * **Disabling unnecessary services**: For security or performance reasons, you might disable services that are not required on a particular system. 

💻 For Linux Topics:

The primary command for controlling system services in Red Hat Enterprise Linux 9 is `systemctl`. 

Here are the common `systemctl` commands and their usage:

1.  **Starting a service**:
    Use the `start` subcommand to immediately activate and run a service. 

    ```bash
    systemctl start <service_name>.service
    # Example: Start the Apache web server
    systemctl start httpd.service
    ```

2.  **Stopping a service**:
    Use the `stop` subcommand to terminate a running service. 

    ```bash
    systemctl stop <service_name>.service
    # Example: Stop the MariaDB database server
    systemctl stop mariadb.service
    ```

3.  **Restarting a service**:
    Use the `restart` subcommand to stop a service and then start it again. This is useful for applying changes that require a full service reload. 

    ```bash
    systemctl restart <service_name>.service
    # Example: Restart the SSH daemon
    systemctl restart sshd.service
    ```

4.  **Reloading a service**:
    Use the `reload` subcommand to tell a service to reload its configuration files without a full restart. Not all services support this; if a service doesn't, `systemctl` might default to a full restart. 

    ```bash
    systemctl reload <service_name>.service
    # Example: Reload the Nginx web server configuration
    systemctl reload nginx.service
    ```

5.  **Enabling a service (for auto-start on boot)**:
    Use the `enable` subcommand to configure a service to start automatically during system boot. This creates a symbolic link in the appropriate `systemd` target directory. 

    ```bash
    systemctl enable <service_name>.service
    # Example: Enable the firewall service to start on boot
    systemctl enable firewalld.service
    ```

6.  **Disabling a service (prevent auto-start on boot)**:
    Use the `disable` subcommand to prevent a service from starting automatically during system boot. This removes the symbolic link created by `enable`. 

    ```bash
    systemctl disable <service_name>.service
    # Example: Disable a specific HTTPD service instance
    systemctl disable httpd.service
    ```

7.  **Checking the status of a service**:
    Use the `status` subcommand to view the current status of a service, including whether it's active, loaded, enabled for boot, and recent log entries. 

    ```bash
    systemctl status <service_name>.service
    # Example: Check the status of the NetworkManager service
    systemctl status NetworkManager.service
    ```

    Example Output:

    ```
    ● NetworkManager.service - Network Manager
         Loaded: loaded (/usr/lib/systemd/system/NetworkManager.service; enabled; vendor preset: enabled)
         Active: active (running) since Thu 2025-07-10 09:30:00 IST; 5h ago
           Docs: man:NetworkManager(8)
       Main PID: 789 (NetworkManager)
         Status: "NetworkManager is running"
          Tasks: 3 (limit: 49152)
         Memory: 11.2M
            CPU: 200ms
         CGroup: /system.slice/NetworkManager.service
                 └─789 /usr/sbin/NetworkManager --no-daemon
    ...
    ```

8.  **Masking a service**:
    Use the `mask` subcommand to completely disable a service, preventing it from being started manually or by other services. This creates a symlink to `/dev/null`.  This is a strong way to ensure a service stays stopped. 

    ```bash
    systemctl mask <service_name>.service
    ```

9.  **Unmasking a service**:
    Use the `unmask` subcommand to revert the effect of `mask`, allowing the service to be started again. 

    ```bash
    systemctl unmask <service_name>.service
    ```

🧪 Labs / Exercises:

**Lab: Control System Services**

**Goal**: Gain hands-on experience starting, stopping, enabling, and disabling system services on a Red Hat Enterprise Linux system using `systemctl`. 

**Instructions**:

1.  **Prepare your environment**:

      * Log in to your `workstation` machine as the `student` user.
      * Start the lab environment: `lab start services-control`

2.  **Log in to `servera` as `student` and switch to `root`**:

    ```bash
    [student@workstation ~]$ ssh student@servera
    [student@servera ~]$ sudo -i
    ```

3.  **Check the status of `httpd.service`**:

    ```bash
    [root@servera ~]# systemctl status httpd.service
    ```

      * Observe if it's currently running or enabled.

4.  **Stop `httpd.service` if it is active**:

    ```bash
    [root@servera ~]# systemctl stop httpd.service
    ```

      * Verify by checking status again. 

5.  **Disable `httpd.service` to prevent it from starting on boot**:

    ```bash
    [root@servera ~]# systemctl disable httpd.service
    ```

      * Verify the `Loaded` line in `systemctl status httpd.service` now shows `disabled`. 

6.  **Enable `httpd.service`**:

    ```bash
    [root@servera ~]# systemctl enable httpd.service
    ```

      * Verify the `Loaded` line in `systemctl status httpd.service` now shows `enabled`. 

7.  **Start `httpd.service`**:

    ```bash
    [root@servera ~]# systemctl start httpd.service
    ```

      * Verify it is `active (running)`. 

8.  **Restart `httpd.service`**:

    ```bash
    [root@servera ~]# systemctl restart httpd.service
    ```

      * Observe if there are any changes in its uptime or process ID (PID) from `systemctl status`. 

9.  **Mask `httpd.service` (Optional, for advanced understanding)**:

    ```bash
    [root@servera ~]# systemctl mask httpd.service
    ```

      * Try to start it: `systemctl start httpd.service`. You should get an error message.
      * Check status: `systemctl status httpd.service` (should show `masked`).

10. **Unmask `httpd.service`**:

    ```bash
    [root@servera ~]# systemctl unmask httpd.service
    ```

      * Now you should be able to start/stop it normally.

11. **Clean up**: Stop and disable `httpd.service` to return the system to its initial state for this exercise, then exit from `root` and `servera`. 

    ```bash
    [root@servera ~]# systemctl stop httpd.service
    [root@servera ~]# systemctl disable httpd.service
    [root@servera ~]# exit
    [student@servera ~]$ exit
    ```

12. **Grade and finish the lab**:

    ```bash
    [student@workstation ~]$ lab grade services-control
    [student@workstation ~]$ lab finish services-control
    ```

🧠 Tips & Tricks:

  * **Combining commands**: For immediate startup and enabling, use `systemctl enable --now <service>`. For immediate stop and disabling, use `systemctl disable --now <service>`.
  * **Viewing unit files**: You can inspect the content of a service unit file to understand its configuration and dependencies using `cat /usr/lib/systemd/system/<service_name>.service` or `systemctl cat <service_name>.service`.
  * **`systemctl daemon-reload`**: If you manually edit a service unit file, you must run `systemctl daemon-reload` to tell `systemd` to reread its configuration.
  * **Error messages**: If a service fails to start, `systemctl status <service_name>.service` will often provide hints or recent log entries. For more detailed logs, use `journalctl -u <service_name>.service`.

📝 Summary/Recap:

  * `systemctl` is the command-line utility for managing `systemd` services. 
  * `start`, `stop`, `restart`, and `reload` subcommands control the runtime state of a service. 
  * `enable` and `disable` control whether a service starts automatically at boot. 
  * `status` provides detailed information about a service's state. 
  * `mask` and `unmask` provide a way to completely restrict or allow service execution. 

🗂️ Related Topics:

  * **Identify Automatically Started System Processes**: Understanding how to list and check the status of services.
  * **Monitoring and Managing Linux Processes**: General process management tools and concepts.
  * **Analyzing and Storing Logs**: How to effectively use `journalctl` to diagnose service issues.