# 🧠 **Quiz: Specify Files by Name**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 59*

---

## 📋 Instructions

* **Total Questions**: 15
* **Format**: 10 MCQs + 5 Short Answer
* **Goal**: Test your understanding of Linux file pathing, wildcards, and search tools
* **Passing Score**: 11/15 (73%)
* **Time Suggested**: 15–20 minutes

---

## ✨ Multiple Choice Questions (MCQs)

**1. Which of the following is a valid absolute path?**
A. `~/documents/report.txt`
B. `./report.txt`
C. `/etc/passwd`
D. `../report.txt`

---

**2. What does the wildcard `*` mean in Bash?**
A. Matches a specific character
B. Matches only hidden files
C. Matches any number of characters
D. Matches numbers only

---

**3. Which symbol represents the user’s home directory in Linux?**
A. `/`
B. `.`
C. `~`
D. `@`

---

**4. Which of the following lists all files that start with "log" and end with ".txt"?**
A. `ls log.txt`
B. `ls log*.txt`
C. `ls *log.txt`
D. `ls log?.txt`

---

**5. What command will show hidden files in the current directory?**
A. `ls -h`
B. `ls -l`
C. `ls -a`
D. `ls --hidden`

---

**6. Which command is used to search for files by name in a directory tree?**
A. `search`
B. `scan`
C. `find`
D. `locate`

---

**7. What does `ls log?.txt` match?**
A. `log.txt`
B. `log1.txt`, `logA.txt`
C. `logfile.txt`
D. All files starting with log

---

**8. What is the purpose of the `which` command?**
A. Display user’s home directory
B. Find path of a command
C. Show file size
D. List all running processes

---

**9. What does `..` represent in a file path?**
A. Root directory
B. Current directory
C. Parent directory
D. Hidden directory

---

**10. Which of the following commands finds all `.cfg` files inside the `/etc` directory?**
A. `find /etc *.cfg`
B. `find . -type f -name .cfg`
C. `find /etc -name "*.cfg"`
D. `locate /etc/*.cfg`

---

## ✏️ Short Answer Questions

**11. What is the difference between absolute and relative file paths?**
→ *Your Answer:*

---

**12. Write a command to list all `.sh` files in the current directory.**
→ *Your Answer:*

---

**13. How would you display the contents of a file named `report.txt` located in your home directory using an absolute path?**
→ *Your Answer:*

---

**14. Explain the use of the `?` wildcard with an example.**
→ *Your Answer:*

---

**15. What is the difference between the `find` and `locate` commands?**
→ *Your Answer:*

---

## ✅ Bonus Challenge (Optional)

**Write a command to:**

* Find all `.log` files inside `/var/log`
* That were modified in the last 3 days

→ *Your Answer:*

```bash
find /var/log -name "*.log" -mtime -3
```
