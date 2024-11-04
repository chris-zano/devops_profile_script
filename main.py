#!/usr/bin/bash
import os

from profile_data import load_profile_data, get_profile_data, save_profile_data

def get_login_username():
    try:
        return os.getlogin()
    except OSError:
        return os.environ.get('USER') or os.environ.get('USERNAME') or 'unknown_user'

def has_home_dir(cwd: str, username: str) -> bool:
    return cwd.endswith(username)

def handle_profile_creation(profile_path: str):
    if os.path.isfile(profile_path):
        profile = load_profile_data(profile_path)
        print("Current Profile Information:")
        for line in profile:
            print(line)

        confirmation = input("Is this information up to date? (yes/no): ").strip().lower()
        if confirmation == 'yes' or confirmation == 'y':
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
    home_dir = os.path.expanduser('~')

    if has_home_dir(home_dir, username):
        profile_path = os.path.join(os.path.expanduser('~'), '.profile.txt')

        handle_profile_creation(profile_path)

    else:
        new_dir = os.path.expanduser("~")
        os.makedirs(new_dir, exist_ok=True)
        profile_path = os.path.join(new_dir, '.profile.txt')

        print(f"Creating new directory: {new_dir}")
        new_profile = get_profile_data()
        save_profile_data(new_profile, profile_path)
        print("Profile created successfully.")

if __name__ == "__main__":
    main()
