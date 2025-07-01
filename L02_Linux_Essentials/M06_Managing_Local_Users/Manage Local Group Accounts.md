Guided Exercise: Manage Local Group Accounts .

Here’s a detailed explanation and practical steps for **managing local group accounts** in Linux, as expected in the Red Hat RH124 curriculum.

## **Manage Local Group Accounts**

### **Key Concepts**

- **Groups** in Linux are collections of users, allowing you to manage permissions for multiple users efficiently.
- Each group has a **group name** and a **Group ID (GID)**.
- Group information is stored in `/etc/group`.


### **Common Group Management Commands**

| Command | Purpose | Example |
| :-- | :-- | :-- |
| `groupadd` | Create a new group | `sudo groupadd developers` |
| `groupdel` | Delete a group | `sudo groupdel developers` |
| `groupmod` | Modify a group’s name or GID | `sudo groupmod -n devops developers` |
| `gpasswd` | Administer group membership | `sudo gpasswd -a alice developers` |
| `id` | Show user and group IDs | `id alice` |
| `getent group` | Show all groups | `getent group` |

## **Guided Exercise: Manage Local Group Accounts**

### **1. Create a New Group**

```bash
sudo groupadd projectx
```

- This creates a group named `projectx`.


### **2. Add a User to the Group**

```bash
sudo gpasswd -a alice projectx
```

- Adds user `alice` to group `projectx`.


### **3. Verify Group Membership**

```bash
groups alice
```

- Output should include `projectx`.


### **4. Remove a User from the Group**

```bash
sudo gpasswd -d alice projectx
```

- Removes `alice` from `projectx`.


### **5. Rename a Group**

```bash
sudo groupmod -n projecty projectx
```

- Renames group `projectx` to `projecty`.


### **6. Delete a Group**

```bash
sudo groupdel projecty
```

- Deletes the group `projecty`.


## **Best Practices**

- Use groups to manage file and directory permissions for teams or projects.
- Remove users from groups when they no longer need access.
- Regularly audit group memberships for security.

