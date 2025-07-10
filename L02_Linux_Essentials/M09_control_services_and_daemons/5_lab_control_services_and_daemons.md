📘 Title: Lab: Control Services and Daemons

🧠 Theory:
This lab provides a practical exercise for mastering the management of system services and daemons on a Red Hat Enterprise Linux system using `systemctl`. Understanding how to effectively control services is crucial for system administration, ensuring system stability, security, and optimal performance. This includes starting, stopping, restarting, reloading configurations, and enabling or disabling services for automatic startup at boot.

💡 Use Cases:

  * **Applying updates:** After installing new software or system updates, services often need to be restarted or reloaded to pick up changes.
  * **Resource optimization:** Disabling unnecessary services can free up system resources, improving performance.
  * **Security hardening:** Disabling unneeded services reduces the system's attack surface, making it more secure.
  * **Troubleshooting service failures:** Stopping and restarting a service is a common first step in diagnosing issues.

💻 For Linux Topics:

**Lab: Control Services and Daemons**

**Objectives:**

  * To practice starting, stopping, and restarting system services.
  * To configure services to automatically start or not start during system boot.
  * To verify the operational status and boot-time configuration of various services.

**Before You Begin:**

  * Ensure you have a Red Hat Enterprise Linux environment (e.g., a virtual machine, cloud instance, or a physical lab server).
  * You must have `root` privileges (or use `sudo`) to perform these operations.
  * This lab will use `httpd.service` (Apache HTTP Server) and `auditd.service` (Audit Daemon) as examples. If these services are not installed on your system, you can install them using `dnf install httpd audit`.

**Instructions:**

1.  **Log in to your Red Hat Enterprise Linux system and switch to the `root` user.**

    ```bash
    [student@hostname ~]$ sudo -i
    [sudo] password for student: your_password
    [root@hostname ~]#
    ```

      * **Explanation**: Root privileges are required to manage system services.

2.  **Check the current status of the `httpd.service`.**

    ```bash
    [root@hostname ~]# systemctl status httpd.service
    ```

      * **Expected Output**: You will likely see `inactive (dead)` unless a web server is already running. The `Loaded` line will show if it's `enabled` or `disabled`.
      * **Explanation**: This command provides comprehensive details about the service, including its active state, whether it's enabled to start on boot, and recent log messages.

3.  **Ensure `httpd.service` is stopped and disabled.**
    If the service is active, stop it. If it's enabled, disable it.

    ```bash
    [root@hostname ~]# systemctl stop httpd.service
    [root@hostname ~]# systemctl disable httpd.service
    ```

      * **Verification**:
        ```bash
        [root@hostname ~]# systemctl status httpd.service
        ```
          * **Expected Output**: `Active: inactive (dead)` and `Loaded: ...; disabled; ...`
      * **Explanation**: It's good practice to ensure a known state before starting a lab exercise. `stop` stops the current running process, and `disable` removes the symlink preventing it from starting on subsequent reboots.

4.  **Start the `httpd.service`.**

    ```bash
    [root@hostname ~]# systemctl start httpd.service
    ```

      * **Explanation**: This command initiates the web server daemon.

5.  **Verify that `httpd.service` is now running.**

    ```bash
    [root@hostname ~]# systemctl status httpd.service
    ```

      * **Expected Output**: `Active: active (running)`
      * **Explanation**: Confirming the service's active state is crucial for ensuring it's operating as expected.

6.  **Enable `httpd.service` to start automatically at boot.**

    ```bash
    [root@hostname ~]# systemctl enable httpd.service
    ```

      * **Explanation**: This creates the necessary symbolic links for `systemd` to start `httpd` during the boot process.

7.  **Verify that `httpd.service` is enabled for boot.**

    ```bash
    [root@hostname ~]# systemctl is-enabled httpd.service
    ```

      * **Expected Output**: `enabled`
      * **Explanation**: This command specifically checks the boot-time configuration of the service.

8.  **Restart the `httpd.service`.**

    ```bash
    [root@hostname ~]# systemctl restart httpd.service
    ```

      * **Explanation**: This is equivalent to `stop` then `start`. It's often used after configuration changes.

9.  **Reload the `httpd.service` configuration (if supported).**
    This applies configuration changes without a full restart. Not all services support `reload`.

    ```bash
    [root@hostname ~]# systemctl reload httpd.service
    ```

      * **Explanation**: If `httpd` configuration files (e.g., `/etc/httpd/conf/httpd.conf`) were modified, `reload` would apply those changes. `systemctl status` will often show if a reload was successful or if a restart was implicitly performed.

10. **Check the status of `auditd.service`.**
    The Audit Daemon records security-related events.

    ```bash
    [root@hostname ~]# systemctl status auditd.service
    ```

      * **Expected Output**: Usually `active (running)` and `enabled`.

11. **Disable `auditd.service` and stop it immediately using a single command.**

    ```bash
    [root@hostname ~]# systemctl disable --now auditd.service
    ```

      * **Explanation**: The `--now` option combines `disable` and `stop`. Use with caution on production systems, as disabling auditing impacts security.

12. **Verify that `auditd.service` is both inactive and disabled.**

    ```bash
    [root@hostname ~]# systemctl status auditd.service
    ```

      * **Expected Output**: `Active: inactive (dead)` and `Loaded: ...; disabled; ...`

13. **Re-enable and start `auditd.service` immediately.**

    ```bash
    [root@hostname ~]# systemctl enable --now auditd.service
    ```

      * **Explanation**: Restoring the audit service is critical for system security and compliance.

14. **Verify that `auditd.service` is active and enabled.**

    ```bash
    [root@hostname ~]# systemctl status auditd.service
    ```

      * **Expected Output**: `Active: active (running)` and `Loaded: ...; enabled; ...`

15. **Clean up and return to `student` user (if applicable).**

      * For this lab, it's generally fine to leave `httpd` stopped and disabled, and `auditd` running and enabled.

    <!-- end list -->

    ```bash
    [root@hostname ~]# exit
    [student@hostname ~]$
    ```

-----

🧠 Tips & Tricks:

  * [cite\_start]**`systemctl list-unit-files --type=service`**: Lists all service unit files and their enabled/disabled state[cite: 1].
  * **`systemctl list-units --type=service --state=running`**: Lists all currently running services.
  * **`systemctl is-active <service>`**: A quick way to check if a service is running. Returns `active`, `inactive`, or `failed`.
  * **`journalctl -xeu <service>`**: For detailed logs of a specific service, especially useful for debugging failures.
  * **Man pages**: Always refer to `man systemctl` for the most comprehensive and up-to-date information on options and subcommands.

📝 Summary/Recap:

  * `systemctl` is the central command for managing `systemd` services.
  * You've gained hands-on experience with `systemctl start`, `stop`, `restart`, `reload`, `enable`, `disable`, and `status`.
  * The `--now` option provides a convenient way to combine `enable`/`disable` with `start`/`stop`.
  * Understanding service states and boot-time configuration is essential for system administration.

🗂️ Related Topics:

  * **Identify Automatically Started System Processes**: How to discover what services are configured to run.
  * **Monitor and Manage Linux Processes**: Broader concepts of process management, including `top` and `ps`.
  * **Analyze and Store Logs**: Essential for debugging and understanding service behavior using `journalctl`.
  * **Configure and Secure SSH**: As you manage services, you'll often do so remotely via SSH.