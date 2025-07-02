Embarking on the journey of **getting started with Red Hat Enterprise Linux (RHEL)** involves understanding its fundamental nature, how to acquire and install it, and the initial steps to begin working with the system. This foundational knowledge is crucial, especially for IT professionals aspiring to attain the **Red Hat Certified Systems Administrator (RHCSA)** certification, as the exam is entirely practical and built on real-world experience.

### What is Linux?

At its core, **Linux is a computer operating system (OS)** that manages a computer's hardware and software, allowing applications to run. It is described as a "UNIX-like" operating system, sharing many concepts, features, functionality, and stability with UNIX. The term "Linux" technically refers only to the kernel, which is the OS's core control software.

Key characteristics and benefits of Linux include:
*   **Free and Open-Source Software**: Linux is an **open-source operating system**, meaning its source code is freely available for developers and the public to study, modify, and redistribute. This fosters continuous improvement and innovation.
*   **Multitasking and Multiuser**: It supports multiple programs and users concurrently.
*   **Speed, Efficiency, Scalability, and Flexibility**: Linux is renowned for these qualities, capable of running on a vast range of hardware, from personal devices to supercomputers. Its modular design allows it to be configured as a full graphical desktop or a minimal software appliance.
*   **Powerful Command-Line Interface (CLI)**: Linux features a robust and scriptable command-line interface, which simplifies automation, deployment, and provisioning tasks.
*   **Stability and Robustness**: It is a stable, robust, and feature-rich system, thoroughly tested for smooth operation and high performance across diverse hardware.

Linux's widespread adoption means it's found in countless environments, including smart TVs, in-flight entertainment systems, point-of-sale systems, financial exchanges, and powering cloud technologies and big data solutions.

### Red Hat Enterprise Linux (RHEL)

**Red Hat Enterprise Linux (RHEL) is the most widely used Linux distribution in enterprise environments**. Red Hat, Inc., founded in 1993, takes selected versions of the Linux source code, adds features, improvements, and bug fixes, and then packages them as a commercial Linux distribution. RHEL is a **commercial, stable, and supported** distribution, rigorously tested to ensure smooth and high performance on a wide range of hardware, making it robust for any workload size.

Red Hat's business model is unique: it provides software and services to implement and support professional and commercial Linux systems, generating revenue through professional-level support, consulting, and training services rather than just software sales. Red Hat actively participates in upstream open-source projects and sponsors the community-driven **Fedora distribution**, which serves as a testbed for new features that are eventually stabilised and integrated into RHEL. CentOS Stream now functions as a continuous development environment for preparing the next minor-version RHEL release.

### Obtaining Red Hat Enterprise Linux

To learn, practice, and prepare for certifications like the RHCSA exam, you can **download RHEL ISO images for free**. This is achieved by enrolling in the **Red Hat Developer Program** and creating a user account on the Red Hat Developer's webpage. This no-cost Developer Subscription provides access to RHEL and other related technologies, allowing for a 16-node version of RHEL for personal use, prototyping, or quality assurance.

Alternatively, **third-party rebuilds of RHEL**, such as **AlmaLinux**, can be used for study and practice. These are built from the same open-source code as RHEL, and except for trademarks and direct access to the Red Hat Customer Portal, are functionally identical. However, if your RHCSA exam objectives include installing packages from Red Hat Subscription Management (RHSM), using a rebuild distribution may be a limitation for that specific skill. It is **advised against using Fedora Linux for studying for Red Hat exams**, as configuration settings and commands may differ.

RHEL ISO images can be quite large (e.g., RHEL 9.3 ISO is about 10.43 GB). It is recommended to check the integrity of downloaded ISO files using SHA256 checksums provided by Red Hat.

### Installing Red Hat Enterprise Linux

Installation of RHEL is a necessary first step to begin working with the system. The process is designed to be straightforward for both virtual and physical machine installations.

*   **Virtual Machine (VM) Installation**: This is the recommended method for practicing, as it allows you to emulate a complete computer on your laptop (macOS, Windows, or Linux) using virtualization software like VirtualBox or virt-manager. For RHEL 9, a minimum of 1.5 GB of memory and 1 CPU core is recommended for a VM.
*   **Physical Server Installation**: This involves preparing a bootable USB drive or DVD. The system's BIOS or UEFI settings need to be configured to boot from the selected installation medium.

The installer program is called **Anaconda**. It guides you through a step-by-step process. RHEL can be installed from a DVD, USB drive, or a network source (using NFS, FTP, or HTTP servers). During installation, you select software based on the desired functionality, such as a server, workstation, personal desktop, or virtualization host.

### Initial Setup and Post-Installation

Once the RHEL installation is complete and the system reboots, the **Initial Setup** application runs. This stage is crucial for completing post-installation tasks and involves:
*   **License Agreement**: Accepting the license terms and conditions.
*   **Red Hat Subscription Management (RHSM) Registration**: Registering the system to receive automatic software updates and other management tasks, though this can also be done later.
*   **Firewall Configuration**: Setting up a basic firewall for the computer.
*   **SELinux Activation**: Enabling or disabling Security Enhanced Linux (SELinux).
*   **Date and Time**: Configuring the current date and time, with an option to synchronize with an NTP server.
*   **User Account Creation**: Creating a regular user account.
*   **Hostname and Network Configuration**: Naming the server and configuring network interfaces (IPv4/IPv6, DHCP, DNS).

Upon successful completion, you will be able to log into your new RHEL system, either through a graphical desktop environment (like GNOME 42 in RHEL 9) or a command-line interface.

### Practising with RHEL

Hands-on practice is highly encouraged while reading relevant study materials. Setting up a physical or virtual machine allows you to apply concepts directly. For those studying for RHCSA, various practice exercises are provided throughout study guides to solidify understanding.

A **quiz section** within the "Get Started with Red Hat Enterprise Linux" chapter serves as an initial assessment, testing your understanding of Linux, open source, Linux distributions, and Red Hat Enterprise Linux. It typically covers topics like benefits of open source, Red Hat's product development, and Linux characteristics.