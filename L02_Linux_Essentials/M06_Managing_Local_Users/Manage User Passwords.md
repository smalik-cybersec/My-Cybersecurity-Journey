Guided Exercise: Manage User Passwords ..

Here’s a comprehensive guide to **managing user passwords** in Linux, along with a step-by-step exercise, as expected in a Red Hat-aligned curriculum and supported by standard Linux administration references.

## **Manage User Passwords**

### **Key Concepts**

- **User passwords** are essential for authentication and system security.
- Password information is securely stored (in hashed form) in `/etc/shadow`.
- Only the root user (or a user with `sudo` privileges) can set or reset other users’ passwords.


## **Essential Commands**

| Command | Purpose | Example |
| :-- | :-- | :-- |
| `passwd` | Change your own or another user’s password | `passwd alice` |
| `chage` | Manage password expiration and aging | `chage -l alice` |
| `sudo` | Run password commands as superuser | `sudo passwd bob` |

## **Guided Exercise: Manage User Passwords**

### **1. Change Your Own Password**

```bash
passwd
```

- You’ll be prompted for your current password, then for the new password (entered twice for confirmation).


### **2. Change Another User’s Password (as root or with sudo)**

```bash
sudo passwd bob
```

- Enter your own password (for sudo), then enter and confirm the new password for `bob`.


### **3. Force a User to Change Password at Next Login**

```bash
sudo passwd --expire bob
```

- The user `bob` will be prompted to set a new password at their next login.


### **4. Lock and Unlock a User Account**

- **Lock:**

```bash
sudo passwd -l bob
```

(Prevents `bob` from logging in.)
- **Unlock:**

```bash
sudo passwd -u bob
```


### **5. Set Password Expiration Policies**

- **View password aging info:**

```bash
sudo chage -l bob
```

- **Set password to expire in 30 days:**

```bash
sudo chage -M 30 bob
```


### **Best Practices**

- Use strong, unique passwords for each account.
- Regularly review and update password expiration policies.
- Lock accounts that are no longer needed or are temporarily inactive.

