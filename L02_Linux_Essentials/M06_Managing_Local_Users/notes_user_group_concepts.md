# User and Group Concepts
### 1. Core Concept
> Users are individual accounts on a Linux system, and groups are collections of users, both used to manage permissions and access control.

In Linux, a "user" represents an individual person or a service that interacts with the system. Each user has a unique identifier (UID), a username, a password, and a home directory. This allows the system to differentiate between who is doing what and to apply specific permissions. "Groups," on the other hand, are organizational units that bundle multiple users together. This is extremely useful for managing permissions efficiently; instead of assigning permissions to many individual users, you assign them once to a group, and all members of that group inherit those permissions.

### 2. Why It's Important
* **In Cybersecurity, we use this for:** Securing systems through precise access control and the implementation of the principle of least privilege, ensuring only authorized entities can interact with specific resources.
### 3. Practical Example
```bash
# To see your current user
whoami

# To see which groups you are a member of
groups

# Example: Listing a file's ownership (user and group)
# The output shows the file owner and its primary group
ls -l /etc/passwd