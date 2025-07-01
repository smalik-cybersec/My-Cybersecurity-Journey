# Lab: Manage Local Users and Groups
### 1. Objective
> The objective of this lab is to gain hands-on experience in creating, modifying, and deleting local user and group accounts, as well as managing user passwords and group memberships on a Linux system.
### 2. Steps & Commands

**Step 1: Create a New User and Group**
* **Description:** Create a new user named `sysadmin_alpha` and a new group named `project_team`.
```bash
sudo useradd -m -s /bin/bash sysadmin_alpha
sudo groupadd project_team

