# simple_counter.py
# Author: [Your Name]
# Date: [Current Date]
# Description: This script demonstrates a basic while loop by counting from 1 to 5.
# It shows the fundamental structure of a while loop and how to ensure its termination.

# Initialize a counter variable
count = 1

# Loop as long as the 'count' is less than or equal to 5
while count <= 5:
    # Print the current value of the counter
    print(f"Current count: {count}")
    # Increment the counter. This step is crucial to prevent an infinite loop
    # and eventually make the loop condition 'count <= 5' false.
    count += 1

# This message is printed after the loop has finished executing
print("Loop finished!")


# input_validator.py
# Author: [Your Name]
# Date: [Current Date]
# Description: This script demonstrates the use of a while loop for user input validation.
# It continuously prompts the user to enter a password until it meets a minimum length requirement (8 characters).

# Initialize the password variable as an empty string
password = ""

# Loop continues as long as the length of the password is less than 8 characters.
# An empty string initially satisfies this condition, so the loop starts.
while len(password) < 8:
    # Prompt the user to enter a password
    password = input("Please enter a password (minimum 8 characters): ")

    # Check if the entered password is too short
    if len(password) < 8:
        # If it's too short, inform the user and the loop will reiterate
        print("Password is too short. Please try again.")

# Once the loop condition (len(password) < 8) becomes False,
# meaning the password is 8 or more characters long, this message is printed.
print("Password accepted!")