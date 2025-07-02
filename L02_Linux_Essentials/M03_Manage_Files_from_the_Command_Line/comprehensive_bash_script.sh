#!/bin/bash
# SCRIPT: Full Linux CLI Lab
# AUTHOR: Shahid Ahmad Malik
# DATE: [YYYY-MM-DD]
# DESCRIPTION: A comprehensive lab script that practices core Linux file management commands.
# All output and created files are forced into a single, unique directory inside the project's 'output' folder.

echo "--- Script Initializing ---"

# --- ONE-TIME SETUP: Define and create the unique output directory ---
# This is the only configuration needed. It creates a directory like '.../output/run_20231027_12345'
# The 'pwd' command ensures we are using the full path to the project root, making it more robust.
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUTPUT_DIR="$PROJECT_ROOT/output/lab_run_$(date +%Y%m%d)_$RANDOM"
mkdir -p "$OUTPUT_DIR"
echo "All output for this run will be saved in: $OUTPUT_DIR"
echo "--------------------------------------------------------"


# --- MAIN LOGIC: Wrapped in a subshell to capture all output ---
(
# ===============================
# Linux File Management Lab Script
# All output is redirected to .output/
# ===============================

# Create hidden output directory if it doesn't exist
mkdir -p .output

# 1. Prepare Lab Environment
# --------------------------
# Create a directory structure for the lab
echo "## Creating lab directories" | tee .output/step1.txt
mkdir -p ~/cli_lab/{docs,images,scripts,archive} 2>&1 | tee -a .output/step1.txt
cd ~/cli_lab

# List the created directories
echo "## Listing directories" | tee -a ~/.output/step1.txt
ls -l 2>&1 | tee -a ~/.output/step1.txt
# Expected Output:
# drwxr-xr-x 2 user user 4096 ... archive
# drwxr-xr-x 2 user user 4096 ... docs
# drwxr-xr-x 2 user user 4096 ... images
# drwxr-xr-x 2 user user 4096 ... scripts

# 2. Create Sample Files
# ----------------------
echo "## Creating sample files" | tee .output/step2.txt
touch docs/readme.txt images/logo.png scripts/install.sh 2>&1 | tee -a .output/step2.txt
echo "Welcome to the CLI lab" > docs/readme.txt
echo "echo Hello World" > scripts/install.sh

# List files in each directory
echo "## Listing files in each directory" | tee -a .output/step2.txt
ls -l docs 2>&1 | tee -a .output/step2.txt
ls -l images 2>&1 | tee -a .output/step2.txt
ls -l scripts 2>&1 | tee -a .output/step2.txt

# 3. Listing Files and Directories
# --------------------------------
echo "## Listing all files recursively" | tee .output/step3.txt
ls -lhR 2>&1 | tee -a .output/step3.txt

# 4. Copy, Move, and Rename Files
# -------------------------------
echo "## Copying readme.txt to archive" | tee .output/step4.txt
cp docs/readme.txt archive/ 2>&1 | tee -a .output/step4.txt

echo "## Moving logo.png to docs" | tee -a .output/step4.txt
mv images/logo.png docs/ 2>&1 | tee -a .output/step4.txt

echo "## Renaming install.sh to setup.sh" | tee -a .output/step4.txt
mv scripts/install.sh scripts/setup.sh 2>&1 | tee -a .output/step4.txt

echo "## Listing after copy/move/rename" | tee -a .output/step4.txt
ls -l docs 2>&1 | tee -a .output/step4.txt
ls -l archive 2>&1 | tee -a .output/step4.txt
ls -l scripts 2>&1 | tee -a .output/step4.txt

# 5. Remove Files and Directories
# -------------------------------
# echo "## Removing archive/readme.txt" | tee .output/step5.txt
# rm archive/readme.txt 2>&1 | tee -a .output/step5.txt

# echo "## Removing empty images directory" | tee -a .output/step5.txt
# rmdir images 2>&1 | tee -a .output/step5.txt

# echo "## Listing after removals" | tee -a .output/step5.txt
# ls -l archive 2>&1 | tee -a .output/step5.txt
# ls -l 2>&1 | tee -a .output/step5.txt

# 6. Wildcards and Shell Expansions
# ---------------------------------
echo "## Creating multiple files with brace expansion" | tee .output/step6.txt
touch docs/file{1..3}.txt 2>&1 | tee -a .output/step6.txt

echo "## Listing all .txt files in docs" | tee -a .output/step6.txt
ls docs/*.txt 2>&1 | tee -a .output/step6.txt

echo "## Removing all file*.txt files in docs" | tee -a .output/step6.txt
rm docs/file*.txt 2>&1 | tee -a .output/step6.txt

echo "## Listing docs after removal" | tee -a .output/step6.txt
ls docs 2>&1 | tee -a .output/step6.txt

# 7. Find Files by Name
# ---------------------
echo "## Finding all .sh files in cli_lab" | tee .output/step7.txt
find . -name "*.sh" 2>&1 | tee -a .output/step7.txt

echo "## Finding readme.txt by absolute path" | tee -a .output/step7.txt
find ~/cli_lab -type f -name "readme.txt" 2>&1 | tee -a .output/step7.txt

# 8. Create Links Between Files
# ----------------------------

# Hard link
echo "## Creating a hard link to docs/readme.txt" | tee .output/step8.txt
ln docs/readme.txt docs/readme_hard.txt 2>&1 | tee -a .output/step8.txt

echo "## Listing inodes for hard links" | tee -a .output/step8.txt
ls -li docs/readme.txt docs/readme_hard.txt 2>&1 | tee -a .output/step8.txt
# Expected: Both files share the same inode number

# Symbolic link
echo "## Creating a symbolic link to docs/readme.txt" | tee -a .output/step8.txt
ln -s docs/readme.txt docs/readme_symlink.txt 2>&1 | tee -a .output/step8.txt

echo "## Listing symbolic link" | tee -a .output/step8.txt
ls -l docs/readme_symlink.txt 2>&1 | tee -a .output/step8.txt
# Expected: lrwxrwxrwx ... docs/readme_symlink.txt -> docs/readme.txt

# 9. View and Edit File Contents
# ------------------------------
echo "## Viewing file contents with cat, head, tail, less" | tee .output/step9.txt
cat docs/readme.txt 2>&1 | tee -a .output/step9.txt
head -n 5 docs/readme.txt 2>&1 | tee -a .output/step9.txt
tail -n 5 docs/readme.txt 2>&1 | tee -a .output/step9.txt
# less is interactive; skip in script

# 10. Bash Command Line Shortcuts and History
# -------------------------------------------
echo "## Showing bash history" | tee .output/step10.txt
history 2>&1 | tee -a .output/step10.txt
# Note: In a non-interactive script, history may be limited

# 11. More Shell Expansions (Globbing)
# ------------------------------------
echo "## Globbing examples" | tee .output/step11.txt
touch docs/testA.txt docs/testB.txt docs/testC.txt
ls docs/test?.txt 2>&1 | tee -a .output/step11.txt
ls docs/test[AB].txt 2>&1 | tee -a .output/step11.txt
ls docs/test[!C].txt 2>&1 | tee -a .output/step11.txt

# 12. Advanced: Symbolic Link to Directory and Navigation
# ------------------------------------------------------
echo "## Creating data directory and symlink" | tee .output/step12.txt
mkdir data
touch data/info.txt
ln -s data data_link
ls -l data_link 2>&1 | tee -a .output/step12.txt
ls data_link 2>&1 | tee -a .output/step12.txt

# 13. Clean Up Lab Environment
# ---------------------------
# echo "## Cleaning up lab environment" | tee .output/step13.txt
# cd ~
# rm -rf ~/cli_lab 2>&1 | tee -a .output/step13.txt

# echo "## Lab complete. All outputs are in the .output/ folder." | tee -a .output/step13.txt

) > "$OUTPUT_DIR/lab_run.log" 2>&1  # Redirect all output from the subshell to one log file.

echo "--- Script Finished. Check the output directory for results. ---"