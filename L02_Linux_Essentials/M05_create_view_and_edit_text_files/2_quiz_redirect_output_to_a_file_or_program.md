# 🧠 **Quiz: Redirect Output to a File or Program**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 124*

---

## 📋 Instructions

* **Total Questions**: 15
* **Format**: 10 Multiple Choice + 5 Short Answer
* **Time**: \~15–20 minutes
* **Passing Score**: 11/15
* **Goal**: Test your knowledge of I/O redirection in Linux

---

## ✨ Multiple Choice Questions (MCQs)

**1. What does the `>` operator do in Bash?**
A. Appends output to a file
B. Displays output on screen
C. Overwrites file with command output
D. Reads input from a file

---

**2. What does `>>` do?**
A. Appends output to a file
B. Overwrites output to a file
C. Redirects errors
D. Pipes data to another command

---

**3. What is the purpose of `2>` in Bash?**
A. Redirect standard input
B. Redirect both stdout and stderr
C. Redirect standard error
D. Append to log files

---

**4. Which of the following redirects both stdout and stderr to the same file?**
A. `command > output.txt`
B. `command >> output.txt`
C. `command > output.txt 2>&1`
D. `command 2> output.txt > output.txt`

---

**5. What is the file descriptor number for standard error (stderr)?**
A. 0
B. 1
C. 2
D. 3

---

**6. Which operator is used to read input from a file?**
A. `>`
B. `<`
C. `2>`
D. `|`

---

**7. What happens if the file already exists and `>` is used?**
A. Appends to the file
B. Nothing
C. Prompts for confirmation
D. Overwrites the file

---

**8. Which of the following correctly appends standard error to a file?**
A. `command >> error.txt`
B. `command 2>> error.txt`
C. `command >>2 error.txt`
D. `command 2> error.txt`

---

**9. What does this command do: `sort < names.txt > sorted.txt`?**
A. Edits `names.txt` directly
B. Sorts and displays on screen
C. Sorts input file and saves result in `sorted.txt`
D. Invalid syntax

---

**10. Which command sends both standard output and standard error to `/dev/null` (discarded)?**
A. `command > /dev/null`
B. `command 2> /dev/null`
C. `command &> /dev/null`
D. `command >> /dev/null`

---

## ✏️ Short Answer Questions

**11. What is the difference between `>` and `>>`?**
→ *Your Answer:*

---

**12. Write a command that redirects only the standard error output to a file called `error.log`.**
→ *Your Answer:*

---

**13. How do you combine stdout and stderr into a single file using redirection?**
→ *Your Answer:*

---

**14. What does the following command do?
`grep "root" /etc/passwd > rootusers.txt 2> grep_errors.txt`**
→ *Your Answer:*

---

**15. Which operator would you use to feed a file’s contents into a program like `sort` or `awk`?**
→ *Your Answer:*

---

## ✅ Bonus Challenge (Optional)

Write a one-liner command that:

* Sorts a file named `users.txt`
* Redirects the result to `sorted.txt`
* Logs any errors into `error.log`

→ *Your Answer:*

```bash
sort < users.txt > sorted.txt 2> error.log
```
