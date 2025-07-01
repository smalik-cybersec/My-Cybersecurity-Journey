ere is a comprehensive **lab** for "Manage Local Users and Groups," synthesizing the expected learning outcomes and practical tasks from the Red Hat RH124 guide[^1].

## **Lab: Manage Local Users and Groups**

### **Objectives**

- Create, modify, and delete local user accounts.
- Create, modify, and delete local group accounts.
- Manage user-group associations.
- Set and reset user passwords.
- Verify account and group changes.


### **Step 1: Create Local User Accounts**

```bash
sudo useradd -m alice
sudo useradd -m bob
```

- `-m` ensures a home directory is created for each user.


### **Step 2: Set User Passwords**

```bash
sudo passwd alice
sudo passwd bob
```

- Enter and confirm a secure password for each user.


### **Step 3: Create Local Groups**

```bash
sudo groupadd projectA
sudo groupadd projectB
```


### **Step 4: Add Users to Groups**

```bash
sudo usermod -aG projectA alice
sudo usermod -aG projectB bob
sudo usermod -aG projectA,projectB bob
```

- `-aG` appends the user to the group(s) without removing them from other groups.


### **Step 5: Verify Group Membership**

```bash
groups alice
groups bob
```

- Confirm users are in the correct groups.


### **Step 6: Change User Details**

- **Change username:**

```bash
sudo usermod -l alicia alice
```

- **Change user’s primary group:**

```bash
sudo usermod -g projectA bob
```


### **Step 7: Remove Users from Groups**

```bash
sudo gpasswd -d bob projectA
```


### **Step 8: Delete Users and Groups**

- **Delete user (and home directory):**

```bash
sudo userdel -r alicia
```

- **Delete group:**

```bash
sudo groupdel projectB
```


### **Step 9: Review Changes**

- **List all users:**

```bash
getent passwd
```

- **List all groups:**

```bash
getent group
```

- **Check user info:**

```bash
id bob
```


### **Best Practices**

- Always set strong passwords.
- Remove unused accounts and groups promptly.
- Use groups to simplify permission management for shared resources.

**This lab covers all key administrative tasks for managing local users and groups, as outlined in the Red Hat RH124 curriculum.**