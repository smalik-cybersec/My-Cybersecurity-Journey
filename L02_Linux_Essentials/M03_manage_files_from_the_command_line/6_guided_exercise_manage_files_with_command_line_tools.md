Here is a custom "Guided Exercise" designed to help you practice managing files and directories using command-line tools, drawing upon the concepts and commands from the sources.

***

**Guided Exercise: Manage Files with Command-line Tools (Custom)**

*   **Purpose**: This exercise is designed to help you **create, organise, copy, and remove files and directories** using various command-line tools. These are fundamental operations for system administrators in Linux, essential for managing and copying important data.

*   **Outcomes**: Upon successful completion of this exercise, you will be able to:
    *   Create new files and directories using `touch` and `mkdir`.
    *   Copy files and entire directory trees using `cp`.
    *   Move and rename files and directories using `mv`.
    *   Delete files and directories using `rm` and `rmdir`.

*   **Before You Begin**:
    *   As the `student` user on the `workstation` machine, **use the `lab` command to prepare your system for this exercise**.
        ```bash
        [student@workstation ~]$ lab start files-manage
        ```
    *   This command prepares your environment and ensures that all required resources are available.

*   **Instructions**:

    1.  **Create a main project directory**:
        *   **Create a new directory called `my_code_project` in your home directory**.
            ```bash
            mkdir ~/my_code_project
            ```
        *   **Verify its creation** using `ls -d ~/my_code_project`.

    2.  **Populate the project directory with subdirectories**:
        *   **Inside `~/my_code_project`, create subdirectories `documentation`, `scripts`, and `data` in a single command**.
            ```bash
            mkdir ~/my_code_project/{documentation,scripts,data}
            ```
        *   **Verify the structure** using `ls ~/my_code_project`.

    3.  **Create various files within the project structure**:
        *   **Create two empty text files**, `project_plan.txt` and `notes.txt`, inside `~/my_code_project/documentation`.
            ```bash
            touch ~/my_code_project/documentation/project_plan.txt ~/my_code_project/documentation/notes.txt
            ```
        *   **Create an empty shell script**, `setup.sh`, inside `~/my_code_project/scripts`.
            ```bash
            touch ~/my_code_project/scripts/setup.sh
            ```
        *   **Verify file creation** using `ls` for each respective directory (e.g., `ls ~/my_code_project/documentation`).

    4.  **Copy a file to a different location**:
        *   **Create a temporary directory** `~/temp_staging`.
            ```bash
            mkdir ~/temp_staging
            ```
        *   **Copy `~/my_code_project/documentation/project_plan.txt` into `~/temp_staging`**.
            ```bash
            cp ~/my_code_project/documentation/project_plan.txt ~/temp_staging/
            ```
        *   **Verify the copy** using `ls ~/temp_staging`.

    5.  **Rename a file**:
        *   **Rename `~/my_code_project/documentation/notes.txt` to `README.md`**.
            ```bash
            mv ~/my_code_project/documentation/notes.txt ~/my_code_project/documentation/README.md
            ```
        *   **Verify the rename** using `ls ~/my_code_project/documentation`.

    6.  **Move a directory**:
        *   **Move the `~/temp_staging` directory into `~/my_code_project/data`**.
            ```bash
            mv ~/temp_staging ~/my_code_project/data/
            ```
        *   **Verify the move** using `ls ~/my_code_project/data`.

    7.  **Create a backup of the entire project**:
        *   **Create a new directory called `~/project_backups`**.
            ```bash
            mkdir ~/project_backups
            ```
        *   **Recursively copy the entire `~/my_code_project` directory and its contents into `~/project_backups`**.
            ```bash
            cp -r ~/my_code_project ~/project_backups/
            ```
        *   **Verify the recursive copy** using `ls -R ~/project_backups`.

    8.  **Delete an empty directory**:
        *   **Create an empty directory `~/my_code_project/temp_dir_to_delete`**.
            ```bash
            mkdir ~/my_code_project/temp_dir_to_delete
            ```
        *   **Delete this empty directory using `rmdir`**.
            ```bash
            rmdir ~/my_code_project/temp_dir_to_delete
            ```
        *   **Verify its deletion** using `ls ~/my_code_project`.

    9.  **Delete a file permanently**:
        *   **Delete the `~/my_code_project/documentation/project_plan.txt` file**.
            ```bash
            rm ~/my_code_project/documentation/project_plan.txt
            ```
        *   **Verify its deletion** using `ls ~/my_code_project/documentation`.

    10. **Delete a non-empty directory (the main project)**:
        *   **Recursively delete the original `~/my_code_project` directory and all its contents**.
            ```bash
            rm -r ~/my_code_project
            ```
        *   **Verify its deletion** using `ls ~`.

*   **Finish**:
    *   On the `workstation` machine, change to the `student` user home directory and **use the `lab` command to complete this exercise**. This step is important to ensure that resources from this exercise do not impact subsequent exercises.
        ```bash
        [student@workstation ~]$ lab finish files-manage
        ```