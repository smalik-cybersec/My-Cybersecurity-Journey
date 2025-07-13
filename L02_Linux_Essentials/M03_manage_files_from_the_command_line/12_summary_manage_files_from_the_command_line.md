# 📎 **Summary: Manage Files from the Command Line**

> *Linux Essentials – Red Hat System Administration*
> *Craw Cyber Security One-Year Diploma – Page 87*

---

## 📖 Summary

In this lesson, you learned how to **create, modify, move, copy, rename, and delete files and directories** using command-line tools in Linux. These operations are essential for **system administration, automation, scripting, forensics**, and **cybersecurity workflows**.

> Mastery of these tools builds your efficiency, safety, and control over any Linux-based environment.

---

## 🔧 Key Commands Covered

| Command       | Purpose                     |
| ------------- | --------------------------- |
| `touch`       | Create an empty file        |
| `mkdir`       | Create a directory          |
| `cp`          | Copy a file or directory    |
| `mv`          | Move or rename a file       |
| `rm`          | Delete files or directories |
| `cat`         | Display file contents       |
| `nano`, `vim` | Edit file contents          |
| `ls`          | List files and directories  |

---

## 🧠 Core Concepts

* **Brace Expansion**: Used to create multiple files or arguments with patterns

  ```bash
  touch report_{jan,feb,mar}.txt
  ```

* **Globbing (Wildcards)**: Used to match file names dynamically

  | Pattern | Meaning                    |
  | ------- | -------------------------- |
  | `*`     | Matches any characters     |
  | `?`     | Matches a single character |
  | `[abc]` | Matches listed characters  |

* **Safe Deletion**: Use `rm -i` to confirm file removal and avoid critical mistakes.

* **Recursive Operations**: Use `-r` to apply actions to entire directories

  ```bash
  cp -r folder1/ folder2/
  rm -r folder/
  ```

---

## 🎯 Practical Cybersecurity Use Cases

| Scenario                        | Command Example                     |        |
| ------------------------------- | ----------------------------------- | ------ |
| Backup a config file            | `cp /etc/ssh/sshd_config ~/backup/` |        |
| Remove malware download folders | `rm -rf ~/Downloads/suspicious/`    |        |
| Organize scanning output        | `mv *.xml ~/pentest/nmap_results/`  |        |
| Investigate tampering           | \`ls -lt /etc                       | head\` |

---

## ✅ What You Should Be Able to Do Now

* Work confidently in any Linux environment without relying on a GUI
* Perform file management tasks using `cp`, `mv`, `rm`, `touch`, and `mkdir`
* Use wildcards and brace expansion to manipulate multiple files efficiently
* Understand file deletion safety and recursion implications
* Begin automating file-based tasks in cybersecurity and DevOps

---

## 📥 Suggested Next Step

> 🔜 Move on to: **Redirect Output and Use Pipes**
> You'll learn how to control where command output goes and chain commands using `>`, `>>`, `|`, and more — powerful for scripting, data analysis, and log management.
