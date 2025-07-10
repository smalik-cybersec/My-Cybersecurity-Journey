📘 Title: Guided Exercise: Identify Automatically Started System Processes 

🧠 Theory:
This guided exercise focuses on understanding and interacting with system services on Red Hat Enterprise Linux, which are managed by `systemd`. These services are typically "daemons" or background processes that start automatically during system boot or are controlled by the system administrator. The exercise will guide you through using `systemctl` to examine, enable, disable, and manage these services.

💡 Use Cases:

  * **System Initialization**: Understanding which services start at boot and how to control them is fundamental to managing a Linux system's startup behavior.
  * **Resource Management**: Identifying unnecessary running services can help optimize system resources.
  * **Security Posture**: Disabling unneeded services reduces the potential attack surface of a system.
  * **Troubleshooting**: Diagnosing issues related to service startup or operation.

💻 For Linux Topics:

**Guided Exercise: Identify Automatically Started System Processes** 

**Objectives:**

  * Evaluate services and targets on a Red Hat Enterprise Linux system.
  * Control the state of `systemd` units.
  * Control the state of multiple `systemd` units by using targets.

**Before You Begin:**
As the `student` user on the `workstation` machine, use the `lab` command to prepare your system for this exercise. This command prepares your environment and ensures that all required resources are available.

```bash
[student@workstation ~]$ lab start services-status
```

**Instructions:**

1.  **Log in to the `servera` machine as the `student` user and switch to the `root` user.** 

    ```bash
    [student@workstation ~]$ ssh student@servera
    ...output omitted...
    [student@servera ~]$ sudo -i
    [sudo] password for student: student
    [root@servera ~]#
    ```

2.  **Use the `systemctl` command to list the status of all `httpd` service instances.** 
    The `httpd` service, commonly used for the Apache HTTP Server, might have multiple instances or be in various states. 

    ```bash
    [root@servera ~]# systemctl status httpd*
    ```

      * **Explanation**: This command will show the status of any unit file that starts with `httpd`, which is useful if there are multiple versions or related services (e.g., `httpd.service`, `httpd@.service`).

3.  **Ensure that no `httpd` service instances are active.** 
    If any `httpd` services are running, stop them. If the status command from the previous step indicates that any `httpd` service is `active (running)`, stop it using `systemctl stop`. 

    ```bash
    [root@servera ~]# systemctl stop httpd.service
    ```

      * **Explanation**: This command attempts to stop the main `httpd` service. If other `httpd` related services were running, you would stop them individually or consider if a wildcard `httpd*` stop is appropriate (though it's safer to be specific for critical services).

4.  **Confirm that all `httpd` services are inactive by relisting their status.** 

    ```bash
    [root@servera ~]# systemctl status httpd*
    ```

      * **Explanation**: You should see `inactive (dead)` or similar status indicating the service is not running.

5.  **Run the `systemctl status` command on the `mariadb.service` service.** 
    `mariadb.service` is typically the service for the MariaDB database server. 

    ```bash
    [root@servera ~]# systemctl status mariadb.service
    ```

      * **Explanation**: This checks the current state, whether it's enabled to start on boot, and recent logs for the MariaDB service.

6.  **Use the `systemctl` command to make the `mariadb.service` service start automatically at boot time.** 
    This action creates a symbolic link in the appropriate `systemd` directory to ensure the service is enabled. 

    ```bash
    [root@servera ~]# systemctl enable mariadb.service
    ```

      * **Explanation**: This command creates a symlink from `/etc/systemd/system/multi-user.target.wants/mariadb.service` to `/usr/lib/systemd/system/mariadb.service`, indicating that `mariadb` should be started when the `multi-user.target` is reached during boot.

7.  **Ensure that the `mariadb.service` service is running.** 
    If the service is not currently active, start it. 

    ```bash
    [root@servera ~]# systemctl start mariadb.service
    ```

      * **Explanation**: This command immediately starts the MariaDB service in the current session.

8.  **Verify that the `mariadb.service` service is enabled and running.** 

    ```bash
    [root@servera ~]# systemctl status mariadb.service
    ```

      * **Explanation**: The output should now show `Loaded: loaded (...; enabled; ...)` and `Active: active (running)`.

9.  **Disable the `mariadb.service` service.** 
    This removes the symbolic link created earlier, preventing it from starting automatically at future boots. 

    ```bash
    [root@servera ~]# systemctl disable mariadb.service
    ```

      * **Explanation**: This command removes the symlink, so the service will not start automatically on subsequent reboots.

10. **Stop the `mariadb.service` service.** 

    ```bash
    [root@servera ~]# systemctl stop mariadb.service
    ```

      * **Explanation**: This command stops the currently running instance of the MariaDB service.

11. **Verify that the `mariadb.service` service is disabled and inactive.** 

    ```bash
    [root@servera ~]# systemctl status mariadb.service
    ```

      * **Explanation**: The output should now show `Loaded: loaded (...; disabled; ...)` and `Active: inactive (dead)`.

12. **Return to the `workstation` system as the `student` user.** 

    ```bash
    [root@servera ~]# exit
    logout
    [student@servera ~]$ exit
    logout
    Connection to servera closed.
    [student@workstation ~]$
    ```

**Evaluation:**
As the `student` user on the `workstation` machine, use the `lab` command to grade your work. Correct any reported failures and rerun the command until successful. 

```bash
[student@workstation ~]$ lab grade services-status
```

**Finish:**
On the `workstation` machine, change to the `student` user home directory and use the `lab` command to complete this exercise. This step is important to ensure that resources from previous exercises do not impact upcoming exercises. 

```bash
[student@workstation ~]$ lab finish services-status
```

🧪 Labs / Exercises:

The guided exercise above serves as a complete lab for identifying and managing automatically started system processes. Following these steps will provide hands-on experience with `systemctl` commands.

🧠 Tips & Tricks:

  * **`systemctl enable --now <service>`**: This command combines enabling a service to start on boot and immediately starting it in the current session.
  * **`systemctl disable --now <service>`**: Similarly, this command disables a service from starting on boot and immediately stops it.
  * **`systemctl list-unit-files --state=enabled`**: A quick way to see all services that are configured to start automatically.
  * **`systemctl is-enabled <service>`**: Checks if a service is enabled for auto-start.
  * **`systemctl is-active <service>`**: Checks if a service is currently running.
  * **Man pages**: Always consult `man systemctl` for comprehensive details and options.

📝 Summary/Recap:

  * You used `systemctl status` to check the current state and boot-time configuration of services like `httpd` and `mariadb`.
  * You learned to enable services for automatic startup using `systemctl enable` and disable them with `systemctl disable`.
  * You practiced starting and stopping services in the current session using `systemctl start` and `systemctl stop`.
  * This exercise reinforced the use of `systemctl` as the primary tool for `systemd` service management.

🗂️ Related Topics:

  * **Control Services and Daemons**: The broader module covering service management.
  * **Process States and Lifecycle**: Understanding the different states a process can be in.
  * **Monitoring Process Activity**: Using tools like `top` or `ps` to view running processes.
  * **Configuring and Securing SSH**: Often, services are managed on remote systems using SSH.