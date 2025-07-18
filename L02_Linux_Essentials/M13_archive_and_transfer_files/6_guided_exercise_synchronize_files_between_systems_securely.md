# Guided Exercise: Synchronize Files Between Systems Securely

This exercise will guide you through using `rsync` to securely synchronize files between systems, covering installation verification, basic synchronization, modifying files, using the dry run feature, and handling deletions.

**Prerequisites:**

- Two Linux systems (physical or virtual machines) where you have administrative access (`sudo` privileges).
- SSH access between the two systems, with password-based or key-based authentication set up.
- `rsync` installed on both your local and remote systems.
- **Optional:** A basic understanding of Linux commands and SSH is beneficial.

---

## Exercise Steps:

### 1. Verification and Setup

- **Verify `rsync` installation:**

  - On both your local and remote systems, run the following command to check if `rsync` is installed:
    ```bash
    rsync --version
    ```
  - If `rsync` is not installed, install it using your distribution's package manager:
    - **Debian/Ubuntu:**
      ```bash
      sudo apt update && sudo apt install rsync
      ```
    - **CentOS/RHEL:**
      ```bash
      sudo yum install rsync
      ```

- **Create a test directory and files on the local system:**

  - Open a terminal on your local system and navigate to your home directory:
    ```bash
    cd ~
    ```
  - Create a test directory:
    ```bash
    mkdir ~/mysync_data
    ```
  - Create some test files inside it:
    ```bash
    echo "Hello World" > ~/mysync_data/file1.txt
    echo "Another file to sync" > ~/mysync_data/file2.txt
    ```
  - Create a subdirectory with a file:
    ```bash
    mkdir ~/mysync_data/subdir && echo "Subdir file" > ~/mysync_data/subdir/subfile.txt
    ```

- **Create a destination directory on the remote system:**
  - Establish an SSH connection to your remote system:
    ```bash
    ssh user@remote_ip # Replace 'user' and 'remote_ip'
    ```
  - Create the destination directory:
    ```bash
    mkdir -p /mnt/backup/myfiles
    ```
  - Exit the SSH session:
    ```bash
    exit
    ```

### 2. Basic Synchronization (Local → Remote)

- **Perform a dry run:** First, let's see what `rsync` _would_ do without actually copying anything.

  ```bash
  rsync -avzn ~/mysync_data/ user@remote_ip:/mnt/backup/myfiles/
  ```

  - **Observe the output.** You should see a list of files that would be transferred, along with messages indicating that no actual changes are being made due to the `-n` flag.

- **Execute the actual sync:** Remove the `-n` flag to perform the actual file transfer.

  ```bash
  rsync -avz ~/mysync_data/ user@remote_ip:/mnt/backup/myfiles/
  ```

  - **Observe the output.** You should see the files being transferred.

- **Verify on the remote system:** Log into the remote system (if not already there) and list the contents of the destination directory.
  ```bash
  ssh user@remote_ip 'ls -R /mnt/backup/myfiles'
  ```
  - You should see `file1.txt`, `file2.txt`, and the `subdir` directory containing `subfile.txt`.

### 3. Modifying Files and Resyncing

- **Modify a file on the local system:**
  ```bash
  echo "This is an updated line" >> ~/mysync_data/file1.txt
  ```
- **Perform another dry run:**

  ```bash
  rsync -avzn ~/mysync_data/ user@remote_ip:/mnt/backup/myfiles/
  ```

  - **Observe the output.** You should notice that only `file1.txt` is listed as a change, because `rsync` intelligently detects only the modified file.

- **Execute the resync:**
  ```bash
  rsync -avz ~/mysync_data/ user@remote_ip:/mnt/backup/myfiles/
  ```
- **Verify the content on the remote system:**
  ```bash
  ssh user@remote_ip 'cat /mnt/backup/myfiles/file1.txt'
  ```
  - The output should include the updated line.

### 4. Deleting Files and Using `--delete`

- **Delete a file from the local source:**
  ```bash
  rm ~/mysync_data/file2.txt
  ```
- **Perform a dry run with `--delete`:**

  ```bash
  rsync -avzn --delete ~/mysync_data/ user@remote_ip:/mnt/backup/myfiles/
  ```

  - **Carefully observe the output.** You should see a message indicating that `file2.txt` _would be deleted_ from the remote destination.

- **Execute the sync with `--delete`:**
  ```bash
  rsync -avz --delete ~/mysync_data/ user@remote_ip:/mnt/backup/myfiles/
  ```
- **Verify on the remote system:**
  ```bash
  ssh user@remote_ip 'ls -R /mnt/backup/myfiles'
  ```
  - `file2.txt` should no longer be present in the listing.

### 5. Remote to Local Sync (Pull Operation)

- **Create a new directory locally to pull the data into:**
  ```bash
  mkdir ~/pulled_data
  ```
- **Perform a dry run (Remote → Local):**
  ```bash
  rsync -avzn user@remote_ip:/mnt/backup/myfiles/ ~/pulled_data/
  ```
- **Execute the actual sync:**
  ```bash
  rsync -avz user@remote_ip:/mnt/backup/myfiles/ ~/pulled_data/
  ```
- **Verify locally:**
  ```bash
  ls -R ~/pulled_data
  ```
  - You should see the files and directories (`file1.txt`, `subdir/subfile.txt`) that were on the remote server now copied to your local `~/pulled_data` directory.

---

**Congratulations!** You've successfully completed a guided exercise using `rsync` to securely synchronize files between systems over SSH. This hands-on experience reinforces the core concepts of `rsync` and its secure application in system administration and cybersecurity scenarios. Remember to always use `--dry-run` (`-n`) before executing commands with `--delete` to prevent unintended data loss.
