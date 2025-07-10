I cannot directly provide the "Custom Guided Exercise: Control System Services" from page 293 of the uploaded `rh124-9.0-student-guide.pdf` because the detailed steps for this specific exercise are not available in the provided document content. The document only lists the title of the exercise on page 293 and then moves to other sections.

However, based on the context of "Control System Services"  and the structure of other guided exercises in the Red Hat System Administration I course, I can provide a custom guided exercise for you to practice controlling system services.

-----

📘 Title: Custom Guided Exercise: Control System Services

🧠 Theory:
This exercise will reinforce your understanding of managing system services using `systemd` and the `systemctl` command in Red Hat Enterprise Linux. You will practice starting, stopping, enabling, and disabling services, which are fundamental tasks for system administrators. System services, often called daemons, are background processes essential for various functionalities like networking, web hosting, or database management. `systemctl` is the primary tool to interact with these services, allowing you to manage their runtime state and their behavior during system boot.

💡 Use Cases:

  * **Application Deployment**: Starting a newly installed application's service.
  * **Troubleshooting**: Stopping a misbehaving service to diagnose issues.
  * **System Hardening**: Disabling unnecessary services to reduce the attack surface.
  * **System Maintenance**: Restarting services after configuration changes or updates.

💻 For Linux Topics:

**Custom Guided Exercise: Control System Services**

**Objectives:**

  * To start and stop a system service.
  * To enable and disable a service for automatic startup at boot.
  * To verify the status of a system service.

**Before You Begin:**
Ensure you have access to a Red Hat Enterprise Linux system, preferably a virtual machine or a lab environment where you have root privileges. This exercise assumes you are operating as the `root` user or using `sudo`.

**Instructions:**

1.  **Log in to your Red Hat Enterprise Linux system and switch to the `root` user.**

    ```bash
    [student@hostname ~]$ sudo -i
    [sudo] password for student: your_password
    [root@hostname ~]#
    ```

      * **Explanation**: This command grants you administrative privileges necessary to control system services.

2.  **Check the status of the `sshd.service` (SSH Daemon).**
    The SSH service (`sshd`) is usually running and enabled by default, as it allows remote access.

    ```bash
    [root@hostname ~]# systemctl status sshd.service
    ```

      * **Explanation**: This command displays detailed information about the `sshd` service, including its current state (active/inactive), whether it's enabled to start on boot, and recent log entries. Look for `Active: active (running)` and `Loaded: loaded (...; enabled; ...)` in the output.

3.  **Attempt to stop the `sshd.service`.**

      * **Important**: If you are connected via SSH, stopping the SSH service will terminate your current session. Ensure you have a console access (e.g., direct VM console) or are comfortable restarting the service immediately after.

    <!-- end list -->

    ```bash
    [root@hostname ~]# systemctl stop sshd.service
    ```

      * **Explanation**: This command sends a stop signal to the `sshd` daemon, attempting to gracefully shut it down.

4.  **Verify that `sshd.service` is inactive.**

    ```bash
    [root@hostname ~]# systemctl status sshd.service
    ```

      * **Explanation**: The output should now show `Active: inactive (dead)`.

5.  **Start the `sshd.service` again.**

    ```bash
    [root@hostname ~]# systemctl start sshd.service
    ```

      * **Explanation**: This command tells `systemd` to initiate the `sshd` service.

6.  **Verify that `sshd.service` is active and running.**

    ```bash
    [root@hostname ~]# systemctl status sshd.service
    ```

      * **Explanation**: You should see `Active: active (running)` once more.

7.  **Disable the `firewalld.service` (Firewall Daemon) to prevent it from starting on boot.**

      * **Caution**: Disabling the firewall can expose your system to network threats. Only do this in a controlled lab environment.

    <!-- end list -->

    ```bash
    [root@hostname ~]# systemctl disable firewalld.service
    ```

      * **Explanation**: This command removes the symbolic link that `systemd` uses to automatically start `firewalld` when the system boots. It does not stop the currently running instance.

8.  **Verify that `firewalld.service` is disabled.**

    ```bash
    [root@hostname ~]# systemctl is-enabled firewalld.service
    ```

      * **Explanation**: This command will simply output `disabled` if successful. You can also use `systemctl status firewalld.service` and look for `Loaded: ...; disabled; ...`.

9.  **Stop the `firewalld.service` in the current session.**

    ```bash
    [root@hostname ~]# systemctl stop firewalld.service
    ```

      * **Explanation**: This terminates the running firewall service.

10. **Verify that `firewalld.service` is inactive.**

    ```bash
    [root@hostname ~]# systemctl status firewalld.service
    ```

      * **Explanation**: The output should show `Active: inactive (dead)`.

11. **Enable and start the `firewalld.service` again using the `--now` option.**

    ```bash
    [root@hostname ~]# systemctl enable --now firewalld.service
    ```

      * **Explanation**: This convenient command combines `enable` (for boot-time startup) and `start` (for immediate activation) into one operation.

12. **Verify that `firewalld.service` is both enabled and running.**

    ```bash
    [root@hostname ~]# systemctl status firewalld.service
    ```

      * **Explanation**: The output should confirm `enabled` and `active (running)`.

13. **Clean up (Optional but recommended for a lab)**: If you were working on a lab system, you might want to return it to its default state. For this exercise, re-enabling `firewalld` is a good practice. Exit the `root` shell.

    ```bash
    [root@hostname ~]# exit
    [student@hostname ~]$
    ```

-----

🧪 Labs / Exercises:

The exercise above provides a hands-on lab experience for controlling system services. Ensure you understand the impact of each command before executing it on a production system.

🧠 Tips & Tricks:

  * **Tab Completion**: Use `systemctl` followed by `Tab` twice to see available subcommands. Use `systemctl status <service_name>.service` and `Tab` twice after `.service` to see available service units.
  * **`systemctl list-unit-files --type=service`**: This command lists all service unit files and their enabled/disabled state, useful for an overview.
  * **`journalctl -u <service_name>`**: If a service fails to start, use `journalctl -u <service_name>` to view its specific log messages for troubleshooting.
  * **`systemctl daemon-reload`**: If you manually modify a service's unit file (e.g., in `/etc/systemd/system/`), you must run `systemctl daemon-reload` for `systemd` to recognize the changes before you try to start/enable the service.

📝 Summary/Recap:

  * `systemctl` is the primary command for managing `systemd` services.
  * `systemctl start`, `stop`, `restart`, `reload` control a service's runtime state.
  * `systemctl enable` and `systemctl disable` configure a service's boot-time behavior.
  * `systemctl status` provides comprehensive information about a service.
  * The `--now` option can be used with `enable` and `disable` to immediately apply the change.

🗂️ Related Topics:

  * **Identify Automatically Started System Processes**: Understanding how to list and check the status of services configured for auto-start.
  * **Analyze and Store Logs**: Essential for debugging service failures.
  * **Process States and Lifecycle**: Understanding what happens when a service starts, stops, or crashes.
  * **Configuring and Securing SSH**: As `sshd` was used as an example, understanding its configuration is a natural next step.