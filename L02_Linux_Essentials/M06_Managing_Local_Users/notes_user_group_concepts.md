# Describe User and Group Concepts

### 1. Core Concept
> Linux is a multi-user operating system that uses a system of user and group accounts to control who can access files and run programs.

A Linux system is designed to be used by multiple people, sometimes even at the same time. To manage this, it uses two main concepts: users and groups.

* **Users:** Every person who interacts with the Linux system has their own unique user account. This account serves as their identity on the system, dictating what they can do and what files and resources they can access. Think of it like your personal ID card for the system.
* **Groups:** Groups are collections of user accounts. They make it much easier to manage permissions. Instead of setting permissions for each individual user, you can assign permissions to a group, and then all users who are members of that group automatically inherit those permissions. For example, if a team of five users needs to work on a specific project, you can create a group for that project and give the group access to the project files, rather than giving access to each of the five users individually. In Red Hat Enterprise Linux, system groups often have Group IDs (GIDs) from 0-499, with regular user-created groups starting from GID 500.

### 2. Why It's Important
* **In Cybersecurity, we use this for:** Securing files and resources to prevent unauthorized access and maintaining a clear understanding of who has what privileges on a system, which is crucial for auditing and managing system security. By managing users and groups effectively, we ensure that only authorized individuals can perform specific actions or access sensitive data.

### 3. Practical Example
Imagine you have a file named `secret_project.txt`.
* If `userA` creates `secret_project.txt`, `userA` becomes the owner of the file.
* `userA` can then set permissions on `secret_project.txt` so that only they can read and write to it.
* If `userA` wants `userB` and `userC` to also be able to read this file, `userA` could create a group called `project_team`, add `userB` and `userC` to this group, and then change the group ownership of `secret_project.txt` to `project_team` and grant read permissions to the `project_team` group. This way, `userB` and `userC` (as members of `project_team`) can read the file, but anyone else not in the group cannot.