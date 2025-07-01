#!/bin/bash
# SCRIPT: Test Output and .gitignore
# AUTHOR: Shahid Ahmad Malik
# DATE: [Enter Today's Date]
# DESCRIPTION: A simple script to test the VMware Shared Folder and .gitignore setup.

echo "--- Starting Test Script ---"

# Define the path to the ignored output directory, relative to the project root.
# Since this script is in .../Scripts/, we go up two levels to get to the root.
OUTPUT_DIR="../../output"

# 1. Create a log file inside the ignored 'output' directory.
echo "This is a log file generated at $(date)." > "$OUTPUT_DIR/test_run.log"
echo "SUCCESS: Created 'test_run.log' in the ignored 'output' directory."

# 2. Create a configuration file in the CURRENT directory (the Scripts folder).
# This file should NOT be ignored.
echo "CONFIG_VERSION=1.0" > "./test_config.txt"
echo "SUCCESS: Created 'test_config.txt' in the current Scripts directory."

echo "--- Test Script Finished ---"