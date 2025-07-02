To **gain superuser (root) access** in Linux, you use either the `su` or `sudo` commands. Superuser access is necessary for administrative tasks such as installing software, changing system configurations, or managing other users. Here’s a detailed explanation and a guided exercise based on best practices and the referenced Linux Pocket Guide[1].

## **Becoming the Superuser**

### **1. Using `sudo`**

- **Purpose:** Temporarily run a single command with superuser privileges.
- **Syntax:**

```bash
sudo command
```

- **Example:**

```bash
sudo apt update
```

You’ll be prompted for your own password (not root’s password).
- **Why use `sudo`?**
    - Safer: Only the specified command runs as root.
    - Auditable: Actions are logged.
    - Preferred on most modern Linux distributions.


### **2. Using `su`**

- **Purpose:** Switch to the root user or another user.
- **Syntax:**

```bash
su -
```

You’ll be prompted for the root user’s password.
- **Example:**

```bash
su -
```

After entering the root password, your shell prompt will change (often from `$` to `#`), indicating root access. You remain root until you type `exit`.
- **Switch to another user:**

```bash
su - username
```


### **3. Exiting Superuser Mode**

- Simply type:

```bash
exit
```

This returns you to your normal user privileges.


## **Guided Exercise: Gain Superuser Access**

### **Step 1: Run a Command with `sudo`**

```bash
sudo ls /root
```

- You’ll be prompted for your password.
- If successful, you’ll see the contents of the `/root` directory (normally restricted).


### **Step 2: Switch to the Root User with `su`**

```bash
su -
```

- Enter the root password.
- Your prompt should change (e.g., from `$` to `#`).


### **Step 3: Confirm Your Identity**

```bash
whoami
```

- Output should be `root` if you are the superuser.


### **Step 4: Return to Your Normal User**

```bash
exit
```

- This ends the root session and returns you to your regular user prompt.


## **Security Note**

- **Only use superuser privileges when necessary.**
Running commands as root can affect the entire system.
- **Prefer `sudo` over `su`** for better security and auditing.
