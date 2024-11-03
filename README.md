# User Profile Management Script

### Overview
This script is designed to manage user profile information when a user logs into the terminal. It checks the current working directory and handles profile data accordingly.

### Functionality

1. **Check Current Working Directory**:
   - When a user logs into the terminal, the script will check if the current working directory matches the user's username.

2. **If the Current Directory Matches**:
   - The script will look for a hidden file named `profile.txt` in the user's home directory.
   
   - **If `profile.txt` exists**:
     - Open the file and read its content (name, phone number, email).
     - Display the content to the user.
     - Ask the user to confirm if the information is up to date.
       - **If the user confirms that the information is up to date**: Allow the user to continue using the terminal.
       - **If the user indicates the information is not up to date**:
         - Prompt the user for input to update the data in the `profile.txt` file.

   - **If `profile.txt` does not exist**:
     - Create a new `profile.txt` file.
     - Prompt the user for input (name, phone number, email).
     - Save the entered data in the `profile.txt` file.
     - Allow the user to continue using the terminal.

3. **If the Current Directory Does Not Match**:
   - Create a new directory: `$HOME/username/`.
   - Create the `profile.txt` file in this new directory.
   - Prompt the user for input (name, phone number, email).
   - Save the entered data in the `profile.txt` file.
   - Allow the user to continue with their work.

### Usage
- To execute the script, run it in a terminal environment where Python is installed.

### Example
```bash
$ python3 main.py
