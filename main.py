#!/usr/bin/bash
import fnmatch
import os
import re


VALID_EMAIL_PATTERN = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
VALID_PHONE_PATTERN = '^\+?[1-9]\d{0,2}[-\s]?(\d{1,4}[-\s]?){1,4}\d{1,4}$'

def get_username():
    try:
        return os.getlogin()
    except OSError:
        return os.environ.get('USER') or os.environ.get('USERNAME') or 'unknown_user'

def is_valid_cwd(cwd: str, username: str) -> bool:
    # Construct the expected path pattern
    expected_path_pattern = f'/home/{username}/*'
    return fnmatch.fnmatch(cwd, expected_path_pattern)


def get_profile_data() -> dict:
    """returns dict of user's profile data """

    name = input("Enter your name: ")
    phone = input(
        "Please enter your phone number in international format:\n"
        "Examples:\n"
        "- +1 123-456-7890 (USA)\n"
        "- +233 20 1234 5678 (GHANA)\n"
        "- +234 98765 43210 (NIGERIA)\n"
        "Your phone number: "
    )

    email = input("Enter your email address: ")

    return {"name": name, "phone": phone, "email": email}

def is_valid_filepath(filepath: str, regex: re) -> bool:
    if not isinstance(filepath, str):
        return False

    if not re.match(regex, filepath):
        return False

    return True

def save_profile_data(profile: dict, filepath: str) -> None:
    """Save the user's profile information to a file."""

    if not isinstance(profile, dict):
        raise TypeError('Profile has to be of type dict')


    valid_filepath_pattern = '^/home/[a-z0-9_-]{3,16}/.profile.txt$'
    is_path_valid = is_valid_filepath(filepath, valid_filepath_pattern)
    if not is_path_valid:
        raise ValueError("Filepath must match '/home/{username}/.profile.txt' "
                         "format")

    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(f"Name: {profile['name']}\n")
            file.write(f"Phone: {profile['phone']}\n")
            file.write(f"Email: {profile['email']}\n")
    except KeyError as k:
        print(f'Profile dict has some missing keys\n {k}')
    except PermissionError:
        print(f'Permission denied: Cannot write to {filepath}')
    except Exception as e:
        print(f'Failed to write profile data to file at {filepath}:\n{e}')
    return


def load_profile_data(filepath: str) -> list:
    """Load the user's profile information from a file."""

    valid_filepath_pattern = '^/home/[a-z0-9_-]{3,16}/.profile.txt$'
    is_path_valid = is_valid_filepath(filepath, valid_filepath_pattern)
    if not is_path_valid:
        raise ValueError("Filepath must match '/home/{username}/.profile.txt' "
                         "format")

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.readlines()
        profile = [line.strip() for line in content]
        return profile
    except FileNotFoundError:
        return []

def handle_profile_creation(profile_path: str):
    if os.path.isfile(profile_path):
        profile = load_profile_data(profile_path)
        print("Current Profile Information:")
        for line in profile:
            print(line)

        confirmation = input("Is this information up to date? (yes/no): ").strip().lower()
        if confirmation == 'yes':
            print("You can continue using the terminal.")
            return
        else:
            new_profile = get_profile_data()
            save_profile_data(new_profile, profile_path)
            print("Profile updated successfully.")
    else:
        print("Profile file does not exist. Creating a new one.")
        new_profile = get_profile_data()
        save_profile_data(new_profile, profile_path)
        print("Profile created successfully.")

def main():
    username = get_username()
    current_dir = os.getcwd()

    print(current_dir)

    if is_valid_cwd(current_dir, username):
        profile_path = os.path.join('/home',username, '.profile.txt')
        print(profile_path)

        try:
            handle_profile_creation(profile_path)
        except TypeError as te:
            print(te)
        except ValueError as ve:
            print(ve)

    else:
        try:
            new_dir = os.path.expanduser("~")
            os.makedirs(new_dir, exist_ok=True)
            profile_path = os.path.join(new_dir, '.profile.txt')

            print(f"Creating new directory: {new_dir}")
            new_profile = get_profile_data()
            save_profile_data(new_profile, profile_path)
            print("Profile created successfully.")
        except TypeError as te:
            print(te)
        except ValueError as ve:
            print(ve)

if __name__ == "__main__":
    main()
