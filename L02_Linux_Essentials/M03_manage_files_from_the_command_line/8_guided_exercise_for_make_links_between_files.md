Here is a custom "Guided Exercise" for "Make Links Between Files", designed to help you practice and understand the concepts of hard links and symbolic links in Linux, drawing directly from the information in the sources. This exercise structure is directly inspired by the "Guided Exercise: Make Links Between Files" found on page 533 of `rh124-9.0-student-guide.pdf`.

***

**Guided Exercise: Make Links Between Files**

*   **Purpose**: This exercise will guide you through the process of **creating hard links and symbolic links** between files and directories. You will observe their unique characteristics and understand their advantages and disadvantages. Managing links is a fundamental skill for system administrators in Linux, essential for managing and copying important data.

*   **Outcomes**: Upon successful completion of this exercise, you will be able to:
    *   Create **hard links** using the `ln` command.
    *   Identify hard links by their **link count** and shared inode numbers.
    *   Create **symbolic links** using the `ln -s` command.
    *   Identify symbolic links by the 'l' in their permissions and the **arrow (`->`) pointing to their target**.
    *   Understand the **differences in behavior** between hard and symbolic links, especially concerning filesystem boundaries and deletion of the original file.

*   **Before You Begin**:
    *   As the `student` user on the `workstation` machine, **use the `lab` command to prepare your system for this exercise**. This command prepares your environment and ensures that all required resources are available.
        ```bash
        [student@workstation ~]$ lab start files-make
        ```

*   **Instructions**:

    1.  **Log in to the `servera` machine**:
        *   From your `workstation` terminal, use the `ssh` command to log in to `servera` as the `student` user. The system's configuration supports SSH keys for authentication, so a password is not required.
            ```bash
            [student@workstation ~]$ ssh student@servera
            ```
            *(You will see output similar to "output omitted" as indicated in the source.)*

    2.  **Create a hard link and verify its properties**:
        *   A hard link creates another name that points to the same underlying data as the original file. All hard-linked files are indistinguishable from one another and share the same inode number.
        *   **View the initial link count** for the `/home/student/files/target.file` file. The link count is typically displayed in the third column of the `ls -l` output.
            ```bash
            [student@servera ~]$ ls -l files/target.file
            ```
            *(Expect to see a link count of **1** for this new file.)*
        *   **Create a hard link** called `/home/student/links/file.hardlink` for the `/home/student/files/target.file` file. Use the `ln` command without the `-s` option.
            ```bash
            [student@servera ~]$ ln /home/student/files/target.file \
            /home/student/links/file.hardlink
            ```
        *   **Verify the link count** for both the original file (`/home/student/files/target.file`) and the new hard-linked file (`/home/student/links/file.hardlink`). The link count for **both files should now be 2**.
            ```bash
            [student@servera ~]$ ls -l files/target.file links/file.hardlink
            ```
            *Optional for further exploration (not directly from the source's guided exercise, but supported by the general text):*
            *   **Modify the content** of `files/target.file` (e.g., using `echo "New content" > files/target.file`). Then, display the content of `links/file.hardlink` (e.g., using `cat links/file.hardlink`). You should see the changes reflected, as both names point to the same data.
            *   **Remove the original file**: `rm files/target.file`. Then, verify that `links/file.hardlink` still exists and contains the data. This demonstrates that data is only removed when *all* hard links are gone.

    3.  **Create a symbolic link to a directory and verify its properties**:
        *   A symbolic link (or soft link) is a special file that points to another file or directory by its path. It functions like a shortcut. Symbolic links have a unique inode number and store the pathname to the target. They can cross filesystem boundaries and can link to directories.
        *   **Create a symbolic link** called `/home/student/tempdir` that points to the `/tmp` directory on the `servera` machine. Use the `ln -s` command.
            ```bash
            [student@servera ~]$ ln -s /tmp /home/student/tempdir
            ```
        *   **Verify the newly created symbolic link** using `ls -l`. You should see the letter `l` as the first character in the permissions string, and an arrow (`->`) pointing from the link's name to `/tmp`.
            ```bash
            [student@servera ~]$ ls -l /home/student/tempdir
            ```
            *Optional for further exploration (not directly from the source's guided exercise, but supported by the general text):*
            *   **Create a file through the symbolic link**: `touch ~/tempdir/testfile.txt`. Then, verify the file's existence in the original `/tmp` directory: `ls -l /tmp/testfile.txt`. You should see it there, as the symbolic link transparently redirects operations.
            *   **Understand a broken link**: If you were to delete the *original* `/tmp` directory (which is usually not advisable on a live system, but conceptually important), the `tempdir` symbolic link would remain but would become "broken" or "dangling," pointing to a non-existent target.

    4.  **Return to the `workstation` system**:
        *   Exit the `servera` session to return to your `workstation` terminal.
            ```bash
            [student@servera ~]$ exit
            ```
            *(You will see output similar to "logout Connection to servera closed.".)*

*   **Finish**:
    *   On the `workstation` machine, ensure you are in the `student` user home directory and **use the `lab` command to complete this exercise**. This step is important to ensure that resources from this exercise do not impact subsequent exercises.
        ```bash
        [student@workstation ~]$ lab finish files-make
        ```