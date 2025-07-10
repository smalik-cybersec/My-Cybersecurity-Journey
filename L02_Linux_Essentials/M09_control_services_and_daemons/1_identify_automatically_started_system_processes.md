📘 Title: Identify Automatically Started System Processes 

🧠 Theory:
In Linux, particularly on modern distributions like Red Hat Enterprise Linux 9, the `systemd` init system is responsible for managing system processes and services. Understanding `systemd` is crucial for identifying and controlling processes that start automatically during system boot or at other specified times. These automatically started processes are often referred to as "services" or "daemons." 

`systemd` provides a comprehensive framework for managing services, including:

  * **Service Units**: Files that define how a service should be started, stopped, and behave. These typically end with `.service` extension and are located in directories like `/etc/systemd/system/` or `/usr/lib/systemd/system/`.
  * **Targets**: Grouping of service units, similar to runlevels in older init systems, which define a state of the system (e.g., `multi-user.target` for a text-based system, `graphical.target` for a desktop environment).
  * **Dependencies**: Services can be configured to start only after other services are running or stop before others.

When the system boots, `systemd` reads the configuration for various services and starts them based on their dependencies and enabled status. 

💡 Use Cases:

  * **System Hardening**: Identifying and disabling unnecessary services reduces the attack surface of a system.
  * **Performance Optimization**: Disabling unneeded services can free up system resources (CPU, RAM).
  * **Troubleshooting**: Investigating why a service failed to start or is misbehaving by examining its status and logs.
  * **Auditing**: Verifying that only authorized services are running on a system.

💻 For Linux Topics:

On Red Hat Enterprise Linux, `systemd` manages how services and other processes are automatically started. The primary command-line tool for interacting with `systemd` is `systemctl`. 

Here's how to identify automatically started system processes:

1.  **List all active services**:
    To see all currently running and loaded `systemd` service units, use the `systemctl` command with the `list-units` and `state=running` options.

    ```bash
    systemctl list-units --type=service --state=running
    ```

      * **`list-units`**: Lists `systemd` units.
      * **`--type=service`**: Filters the list to show only service units.
      * **`--state=running`**: Filters further to show only services that are currently active and running.

    Example Output (simplified):

    ```
    UNIT                         LOAD   ACTIVE SUB     DESCRIPTION
    auditd.service               loaded active running Security Auditing Service
    crond.service                loaded active running Command Scheduler
    dbus.service                 loaded active running D-Bus System Message Bus
    firewalld.service            loaded active running firewalld - dynamic firewall daemon
    nginx.service                loaded active running Nginx Web Server
    sshd.service                 loaded active running OpenSSH server daemon
    systemd-journald.service     loaded active running Journal Service
    ...
    ```

2.  **List all enabled services (configured to start automatically on boot)**:
    To see which services are configured to start automatically when the system boots, use `systemctl list-unit-files`.

    ```bash
    systemctl list-unit-files --type=service
    ```

      * **`list-unit-files`**: Lists all available unit files and their enabled/disabled state.
      * **`--type=service`**: Filters to show only service unit files.

    Look for the `enabled` state in the output:

    ```bash
    UNIT FILE                                 STATE           VENDOR PRESET
    auditd.service                            enabled         enabled
    autovt@.service                           disabled        enabled
    crond.service                             enabled         enabled
    dbus-broker.service                       static          enabled
    dbus.service                              static          enabled
    firewalld.service                         enabled         enabled
    httpd.service                             disabled        disabled
    nginx.service                             enabled         disabled
    sshd.service                              enabled         enabled
    systemd-journald.service                  static          enabled
    ...
    ```

      * **`enabled`**: The service is configured to start automatically at boot.
      * **`disabled`**: The service is not configured to start automatically at boot.
      * **`static`**: The service cannot be enabled or disabled directly; it's typically started as a dependency of another enabled service.
      * **`masked`**: The service is completely disabled and cannot be started manually or by other services.

3.  **Check the status of a specific service**:
    To get detailed information about a specific service, including its current status, whether it's enabled, and recent log entries, use `systemctl status <service_name>`.

    ```bash
    systemctl status sshd.service
    ```

    Example Output:

    ```
    ● sshd.service - OpenSSH server daemon
         Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; vendor preset: enabled)
         Active: active (running) since Thu 2025-07-10 10:00:00 IST; 3h ago
           Docs: man:sshd(8)
                 man:sshd_config(5)
       Main PID: 1234 (sshd)
          Tasks: 1 (limit: 49152)
         Memory: 7.8M
            CPU: 423ms
         CGroup: /system.slice/sshd.service
                 └─1234 /usr/sbin/sshd -D
    ...
    ```

    This output clearly shows if `sshd.service` is `enabled` and `active (running)`.

4.  **Identify services by their target dependencies**:
    Services are often grouped under `targets`. To see which services are part of a specific target (like `multi-user.target`), you can use `systemctl list-dependencies <target_name>`.

    ```bash
    systemctl list-dependencies multi-user.target --type=service
    ```

    This helps understand the boot sequence and what services are brought up with a particular system state.

5.  **Examine system logs for boot-time events**:
    The `journalctl` command can be used to view the `systemd` journal, which contains logs of all system activities, including service startups.

    ```bash
    journalctl -b 0
    ```

      * **`-b 0`**: Shows logs from the current boot. Use `-b -1` for the previous boot, and so on.
        You can then `grep` for specific services or keywords to identify their startup behavior.

    <!-- end list -->

    ```bash
    journalctl -b 0 | grep "Starting"
    ```

🧪 Labs / Exercises:

**Lab: Identify Automatically Started System Processes**

**Goal**: Understand and identify services configured to start automatically on a Red Hat Enterprise Linux system.

**Instructions**:

1.  **Log In**: Log in to your Linux environment as a regular user, and then switch to the `root` user or use `sudo` for commands that require elevated privileges.

2.  **List All Running Services**:

      * Run the command: `systemctl list-units --type=service --state=running`
      * **Observation**: Note down at least 5 services that are currently active and running on your system. What do these services generally do (e.g., networking, logging, security)?

3.  **List All Enabled Services (Auto-start on boot)**:

      * Run the command: `systemctl list-unit-files --type=service`
      * **Observation**: Identify at least 3 services that are `enabled` (meaning they will start automatically on boot) and 3 services that are `disabled`.
      * **Challenge**: Can you find any `static` or `masked` services? What do you think their purpose is based on their names?

4.  **Examine a Specific Enabled Service**:

      * Choose one `enabled` service from your list (e.g., `sshd.service`).
      * Run `systemctl status <service_name.service>` (e.g., `systemctl status sshd.service`).
      * **Observation**: What is the `Loaded` status? Is it `active (running)`? What is its `vendor preset`? What does the `Docs` line tell you?

5.  **Simulate Disabling/Enabling a Service (Do NOT do this on critical services like `sshd` or `network` on a production system)**:

      * Choose a non-critical service like `httpd.service` (if installed) or a newly created dummy service. If you don't have `httpd`, you can create a simple dummy service file for practice:

          * Create `/etc/systemd/system/mytest.service` with content:
            ```
            [Unit]
            Description=My Test Service
            After=network.target

            [Service]
            ExecStart=/usr/bin/bash -c 'echo "My test service started at $(date)" >> /var/log/mytest.log; sleep infinity'
            Type=simple

            [Install]
            WantedBy=multi-user.target
            ```
          * Run `sudo systemctl daemon-reload`
          * Run `sudo systemctl enable mytest.service`
          * Run `sudo systemctl start mytest.service`
          * Check status: `systemctl status mytest.service`
          * View log: `cat /var/log/mytest.log`

      * Now, disable the service: `sudo systemctl disable <service_name.service>`

      * Stop the service: `sudo systemctl stop <service_name.service>`

      * Verify its status: `systemctl status <service_name.service>` (should be `inactive (dead)` and `disabled`).

      * Re-enable and start it: `sudo systemctl enable <service_name.service>` and `sudo systemctl start <service_name.service>`.

      * Clean up (if you created `mytest.service`):

          * `sudo systemctl stop mytest.service`
          * `sudo systemctl disable mytest.service`
          * `sudo rm /etc/systemd/system/mytest.service`
          * `sudo systemctl daemon-reload`

6.  **Analyze Boot Logs for Service Startups**:

      * Run `journalctl -b 0 | grep "Starting"`.
      * **Observation**: Look for messages indicating services starting during the current boot. Can you identify any services you recognized from previous steps?

7.  **Identify Dependencies (Optional)**:

      * Choose a key target like `graphical.target` or `multi-user.target`.
      * Run `systemctl list-dependencies <target_name> --type=service`.
      * **Observation**: See how many services are directly or indirectly started by this target.

🧠 Tips & Tricks:

  * **`systemctl` vs. `service`**: While older systems used the `service` command, `systemctl` is the modern and preferred way to manage services on `systemd`-based Linux distributions.
  * **Tab Completion**: Use tab completion with `systemctl` for service names (e.g., `systemctl status sshd` + Tab will often complete to `sshd.service`).
  * **Reading Service Files**: You can view the content of a service unit file to understand its configuration, dependencies, and how it executes its main command: `cat /usr/lib/systemd/system/<service_name.service>`. Do not modify these files directly; use `systemctl edit` for overrides.
  * **`systemctl daemon-reload`**: After modifying any `systemd` unit file, always run `sudo systemctl daemon-reload` to tell `systemd` to reread its configuration.

📝 Summary/Recap:

  * `systemd` is the init system on modern Red Hat Linux, managing automatically started processes (services/daemons). 
  * The `systemctl` command is used to control and query `systemd`. 
  * `systemctl list-units --type=service --state=running` shows active services. 
  * `systemctl list-unit-files --type=service` shows services configured for auto-start (`enabled`) or not (`disabled`). 
  * `systemctl status <service_name.service>` provides detailed information about a service's current state and configuration. 
  * `journalctl -b 0` can be used to review boot-time logs to see service startup events.

🗂️ Related Topics:

  * **Linux Boot Process**: Understanding the stages of system boot and how `systemd` takes over.
  * **`cron` and `at`**: Other methods for scheduling tasks to run automatically at specific times or intervals.
  * **Networking Services**: Specific configurations for network-related daemons like HTTP, SSH, DNS.
  * **Logging and `journalctl`**: Deeper dive into managing and querying system logs.