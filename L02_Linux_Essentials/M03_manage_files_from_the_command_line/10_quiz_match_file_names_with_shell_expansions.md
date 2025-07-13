# 🧠 **Quiz: Match File Names with Shell Expansions**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 83*

---

## 📋 Instructions

* **Total Questions**: 15
* **Format**: 10 Multiple Choice Questions + 5 Short Answer
* **Passing Score**: 11/15 (73%)
* **Estimated Time**: 15–20 minutes
* **Focus Areas**: Globbing, wildcards, brace expansion, file pattern matching

---

## ✨ Multiple Choice Questions (MCQs)

**1. What does the pattern `*.txt` match?**
A. All files with any extension
B. Only files named `.txt`
C. All files ending with `.txt`
D. Files that start with a dot

---

**2. What is the output of `echo file_{a,b,c}.txt`?**
A. file\_{a,b,c}.txt
B. file\_a.txt file\_b.txt file\_c.txt
C. file1.txt file2.txt file3.txt
D. None of the above

---

**3. What does the wildcard `?` match in file names?**
A. Any number of characters
B. A single character
C. A specific digit only
D. All characters after `?`

---

**4. Which command matches `file1.txt`, `file2.txt`, but not `file12.txt`?**
A. `ls file*.txt`
B. `ls file?.txt`
C. `ls file[1-2].txt`
D. `ls file.txt`

---

**5. Which pattern matches all files starting with `log` and ending with `.sh`?**
A. `log?.sh`
B. `log*.sh`
C. `log[sh]`
D. `log.*.sh`

---

**6. What does the command `touch test_{01..03}.txt` create?**
A. test\_{01..03}.txt
B. test\_1.txt test\_2.txt test\_3.txt
C. test\_01.txt test\_02.txt test\_03.txt
D. test.txt

---

**7. What command would match files named `doc1`, `doc2`, or `doc3`?**
A. `ls doc?.*`
B. `ls doc[1-3]`
C. `ls doc*`
D. `ls doc[1234]`

---

**8. What does `ls file[!a-c].txt` do?**
A. Lists files named filea.txt, fileb.txt, filec.txt
B. Lists all `.txt` files except filea.txt to filec.txt
C. Lists hidden files only
D. Matches no files

---

**9. Which wildcard matches exactly one character?**
A. `*`
B. `?`
C. `[]`
D. `^`

---

**10. What does `ls config[0-9][0-9].yaml` match?**
A. config.yaml
B. config12.yaml, config99.yaml
C. config1.yaml
D. config.yaml12

---

## ✏️ Short Answer Questions

**11. Explain the difference between `*` and `?` in globbing.**
→ *Your Answer:*

---

**12. Write a command to create files named `backup_mon.txt`, `backup_tue.txt`, and `backup_wed.txt`.**
→ *Your Answer:*

---

**13. What does the command `ls report[1-3].csv` match?**
→ *Your Answer:*

---

**14. What command would list files named `test_01.sh` through `test_10.sh`?**
→ *Your Answer:*

---

**15. How is brace expansion different from globbing (wildcard matching)?**
→ *Your Answer:*

---

## ✅ Bonus (Optional)

Create 5 text files named `day1.txt` to `day5.txt` using a single command.
→ *Your Answer:*

```bash
touch day{1..5}.txt
```