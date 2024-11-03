#!/usr/bin/bash
import fnmatch
import os

from profile_data import load_profile_data, get_profile_data, save_profile_data

def get_login_username():
    try:
        return os.getlogin()
    except OSError:
        return os.environ.get('USER') or os.environ.get('USERNAME') or 'unknown_user'

def is_valid_cwd(cwd: str, username: str) -> bool:
    expected_path_pattern = f'/home/{username}/*'
    return fnmatch.fnmatch(cwd, expected_path_pattern)

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
    username = get_login_username()
    current_dir = os.getcwd()

    if is_valid_cwd(current_dir, username):
        profile_path = os.path.join('/home',username, '.profile.txt')

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
