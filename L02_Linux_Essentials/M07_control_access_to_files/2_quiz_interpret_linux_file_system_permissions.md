Absolutely, Shahid! Here's your **professional, structured quiz** for:

---

# 🧠 **Quiz: Interpret Linux File System Permissions**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 204*

---

## 📋 Instructions

* **Total Questions**: 15
* **Format**: 10 Multiple Choice + 5 Short Answer
* **Passing Score**: 11/15
* **Topic**: File system permissions, symbolic and numeric modes, interpreting `ls -l` output

---

## ✨ Multiple Choice Questions (MCQs)

**1. What does the first character in `ls -l` output (e.g., `-rwxr-xr--`) indicate?**
A. File owner
B. Permission type
C. File type
D. Group name

---

**2. Which of the following permissions means the owner can read, write, and execute a file?**
A. `r--`
B. `rw-`
C. `rwx`
D. `r-x`

---

**3. What does `chmod 755 script.sh` do?**
A. Makes file readable only
B. Removes write access from group
C. Grants full access to owner, read-execute to others
D. Locks the file

---

**4. What does the `x` permission allow for a **file**?**
A. Edit contents
B. Run the file as a program
C. Delete the file
D. Change ownership

---

**5. What does the `x` permission allow for a **directory**?**
A. Rename the directory
B. Change permissions
C. Enter/access the directory
D. Read file contents

---

**6. What is the octal (numeric) equivalent of `rw-r--r--`?**
A. 777
B. 600
C. 644
D. 755

---

**7. What is the meaning of permission string `-r--r--r--`?**
A. Only owner can write
B. Only group can execute
C. Everyone can read only
D. File is not accessible

---

**8. Which command removes all permissions from "others"?**
A. `chmod o-w file.txt`
B. `chmod o= file.txt`
C. `chmod 700 file.txt`
D. `chmod u-x file.txt`

---

**9. What is the meaning of `chmod 777 file.txt`?**
A. No access for anyone
B. Read-only for all
C. Full access for all users
D. Owner only can read

---

**10. Which symbolic command grants execute permission to group members?**
A. `chmod g+x file.sh`
B. `chmod u+x file.sh`
C. `chmod o+x file.sh`
D. `chmod g-x file.sh`

---

## ✏️ Short Answer Questions

**11. What does the permission string `drwxr-xr--` indicate?**
→ *Your Answer:*

---

**12. Convert the permission `rwxr--r--` to its numeric (octal) equivalent.**
→ *Your Answer:*

---

**13. How would you give only the owner full access and remove all permissions for group and others?**
→ *Your Answer:*

---

**14. What’s the difference between `chmod 755` and `chmod 700`?**
→ *Your Answer:*

---

**15. Explain what each section of this means: `-rw-rw-r--`**
→ *Your Answer:*

---

## ✅ Bonus Challenge (Optional)

You have a file `secret.sh`. You want to:

* Make it readable and writable **only** by the owner
* Make sure no one else can access it

Write the numeric and symbolic commands:

```bash
chmod 600 secret.sh        # Numeric
chmod u=rw,go= secret.sh   # Symbolic
```

---

Would you like:

* ✅ Answer key
* 📥 Export in Markdown
* 🧪 Practice lab on `chmod`, `ls -l`, and octal modes?
* ⏭️ Next lesson: *Modify File Permissions Using chmod*

You're building a rock-solid foundation in Linux security, Shahid 🔐📁 Keep leveling up!
