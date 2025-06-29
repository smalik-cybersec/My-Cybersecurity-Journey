# mouse_position.py
# Author: [Your Name]
# Date: [Current Date]
# Description: This script demonstrates basic usage of the pyautogui module.
# It waits for 5 seconds, then reports the current mouse cursor position (X, Y coordinates).
# This can be useful for understanding screen coordinates for GUI automation.

import pyautogui # Import the pyautogui library for GUI automation
import time      # Import the time library for delays

# Inform the user and provide a short delay to allow mouse positioning
print("Preparing to show mouse position. Move your mouse within 5 seconds...")
time.sleep(5) # Pause the script for 5 seconds

try:
    # Get the current X and Y coordinates of the mouse cursor
    # pyautogui.position() returns a tuple (x, y)
    x, y = pyautogui.position()
    print(f"Current mouse position: X={x}, Y={y}")

    # Optional: Uncomment the following lines to test moving the mouse
    # This moves the mouse to the center of a typical Full HD screen (1920x1080)
    # over a duration of 1 second.
    # pyautogui.moveTo(960, 540, duration=1)
    # print("Mouse moved to (960, 540)")

except Exception as e:
    # Catch any exceptions that might occur (e.g., if pyautogui can't find a display)
    print(f"An error occurred: {e}")
    print("Ensure you have a display connected and pyautogui can access it.")

print("Script finished.")