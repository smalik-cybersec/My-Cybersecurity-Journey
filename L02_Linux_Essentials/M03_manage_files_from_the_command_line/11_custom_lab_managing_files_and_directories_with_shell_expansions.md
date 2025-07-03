Certainly! Drawing upon the information in the provided sources, here is a custom lab designed to enhance your understanding of **managing files from the command line** using **shell expansions**, similar to the concepts outlined on page 87 of `rh124-9.0-student-guide.pdf`.

---

### Custom Lab: Managing Files and Directories with Shell Expansions

**Goal:** To practice creating, modifying, and deleting files and directories using various shell commands and filename expansion techniques, specifically **shell globbing**.

**Outcomes:** Upon completion of this lab, you will be able to:
*   **Efficiently create new files and directories** using the **`mkdir`** and **`touch`** commands.
*   **Copy and move files** using **`cp`** and **`mv`** with wildcard patterns.
*   **Create and manage links** (both hard and symbolic/soft links) between files.
*   **Utilise shell globbing** features, including **wildcards (`*`, `?`, `[]`)** and **brace expansion (`{}`)**, for pattern matching in commands.
*   **Effectively delete files and directories** using **`rm`** and **`rmdir`** with pattern matching and appropriate options.

**Instructions:** Perform the following tasks. It is recommended to perform these steps within your user's home directory (`~`) or a dedicated practice directory to avoid affecting system files. For example, you can begin by typing `cd ~`.

---

#### **Part 1: Setting up the Environment and Creating Files**

1.  **Create a main workspace directory and subdirectories for organisation.**
    *   Create a new top-level directory named **`dev_projects`** in your current location (e.g., your home directory).
    *   Inside `dev_projects`, create three subdirectories: **`Web_Apps`**, **`Scripts`**, and **`Documents`**.
    *   **Command:** `mkdir -p ~/dev_projects/{Web_Apps,Scripts,Documents}`
        *   **Explanation:** The **`mkdir`** command creates directories. The **`-p`** option ensures that parent directories are created if they don't already exist, and **brace expansion (`{}`)** allows for creating multiple directories with a single command.
    *   **Verification:** Use **`ls -F ~/dev_projects/`** to list the newly created directories. (The **`-F`** option classifies entries, showing a forward slash `/` for directories).

2.  **Create dummy project files using shell expansion.**
    *   Navigate into the `dev_projects` directory: `cd ~/dev_projects`
    *   Inside `~/dev_projects`, create 4 web application files named **`project_alpha_v1.html`** through **`project_alpha_v4.html`**.
    *   Create 3 shell script files named **`backup_tool_vA.sh`**, **`backup_tool_vB.sh`**, and **`backup_tool_vC.sh`**.
    *   Create 2 document files named **`report_final.docx`** and **`report_draft.docx`**.
    *   **Command:**
        ```bash
        touch project_alpha_v{1..4}.html
        touch backup_tool_v{A,B,C}.sh
        touch report_{final,draft}.docx
        ```
        *   **Explanation:** The **`touch`** command creates empty files if they don't exist, or updates their timestamps. **Brace expansion** is again used to efficiently generate sequences (`{1..4}`) and lists (`{A,B,C}`, `{final,draft}`) of file names.
    *   **Verification:** Use **`ls`** to list all files created directly in `~/dev_projects`.

---

#### **Part 2: Listing and Moving Files with Globbing**

1.  **List specific file types using wildcards.**
    *   Display only the files that end with **`.html`**.
    *   Display only files that start with **`backup_tool_v`** followed by any single character and then **`.sh`**.
    *   Display any file name that starts with **`r`** and contains **`_`** followed by any characters, then **`.docx`**.
    *   **Command:**
        ```bash
        ls *.html
        ls backup_tool_v?.sh
        ls r*_*.docx
        ```
        *   **Explanation:** The **asterisk (`*`)** matches any string of zero or more characters, while the **question mark (`?`)** matches exactly one single character.
    *   **Verification:** Observe the outputs, ensuring only the specified files are listed.

2.  **Move files to their respective subdirectories using globbing.**
    *   Move all **`.html`** files into the **`Web_Apps/`** subdirectory.
    *   Move all **`.sh`** files into the **`Scripts/`** subdirectory.
    *   Move all **`.docx`** files into the **`Documents/`** subdirectory.
    *   **Command:**
        ```bash
        mv *.html Web_Apps/
        mv *.sh Scripts/
        mv *.docx Documents/
        ```
        *   **Explanation:** The **`mv`** command moves or renames files. Using **`*`** allows you to move multiple files matching the pattern in one command.
    *   **Verification:** Use **`ls Web_Apps/`**, **`ls Scripts/`**, and **`ls Documents/`** to confirm the files have been moved to their correct locations.

---

#### **Part 3: Copying, Renaming, and Linking Files**

1.  **Create a versioned copy of a web application file.**
    *   Copy `~/dev_projects/Web_Apps/project_alpha_v1.html` to the `Web_Apps` directory, naming the copy `project_alpha_v1_archive.html`.
    *   **Command:** `cp Web_Apps/project_alpha_v1.html Web_Apps/project_alpha_v1_archive.html`

2.  **Create a symbolic link to a script file.**
    *   Create a **symbolic link** (also known as a **soft link**) in the `~/dev_projects` directory itself that points to `~/dev_projects/Scripts/backup_tool_vA.sh`. Name the link **`current_backup_script.sh`**.
    *   **Command:** `ln -s Scripts/backup_tool_vA.sh current_backup_script.sh`
        *   **Explanation:** The **`ln -s`** command creates a symbolic link. Symbolic links are useful for creating shortcuts or referencing files in different locations.
    *   **Verification:** Use **`ls -l current_backup_script.sh`** to view the link details. The output will show `->` pointing to the original file.

3.  **Create a hard link to a document file.**
    *   Create a **hard link** in the `~/dev_projects/Documents` directory that points to `~/dev_projects/Documents/report_final.docx`. Name the hard link **`final_report_copy.docx`**.
    *   **Command:** `ln Documents/report_final.docx Documents/final_report_copy.docx`
        *   **Explanation:** The **`ln`** command (without `-s`) creates a hard link. Hard links create another directory entry for the *same inode*, meaning they are indistinguishable from the original file and share the same data blocks.
    *   **Verification:** Use **`ls -l Documents/report_final.docx Documents/final_report_copy.docx`**. Observe that the link count (the second column in `ls -l` output) for both files is now `2` (or higher if more links exist).

4.  **Rename files using wildcards and character ranges.**
    *   Change the names of all files in the `Web_Apps` directory that start with `project_alpha_v` and end with a digit (1-4) to instead end with `_stable.html`.
    *   **Command:** `mv Web_Apps/project_alpha_v.html Web_Apps/project_alpha_v_stable.html`
        *   **Explanation:** **Square brackets (`[]`)** with a range (`1-4`) match any single character within that range. This renames the files in a batch.
    *   **Verification:** Use **`ls Web_Apps/`** to see the newly renamed files.

---

#### **Part 4: Cleaning Up with Globbing**

1.  **Remove specific archived files.**
    *   Remove all files in the `Web_Apps` directory that contain **`_archive`** in their name.
    *   **Command:** `rm Web_Apps/*_archive.html`
    *   **Verification:** Use **`ls Web_Apps/`** to confirm the files are deleted.

2.  **Remove all `.docx` files (if any were created in previous steps or were left by lab setup)**
    *   Remove all `.docx` files from the `Documents` directory. Use the interactive `-i` option for safety, and confirm each deletion.
    *   **Command:** `rm -i Documents/*.docx`
        *   **Explanation:** The **`-i`** option prompts for confirmation before every deletion, which is useful when using wildcards to prevent accidental removal of unintended files.
    *   **Verification:** Respond `y` to prompts. Then, use **`ls Documents/`** (should ideally show no `.docx` files).

3.  **Delete the entire `dev_projects` directory and its contents.**
    *   Navigate back to your home directory: `cd ~`
    *   Remove the `dev_projects` directory and everything inside it **recursively** and **without prompting**.
    *   **Command:** `rm -rf ~/dev_projects`
        *   **Explanation:** The **`-r`** option (recursive) is essential for deleting directories and their contents, and **`-f`** (force) overrides prompts and error messages, ensuring the command completes without interaction. Use this command with extreme caution, as it permanently deletes files.
    *   **Verification:** Use **`ls -d ~/dev_projects`**. It should return an error indicating the directory does not exist, confirming its deletion.

---