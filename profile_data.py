import re
from get_inputs import get_username, get_email, get_phone_number


def is_valid_filepath(filepath: str, regex: re) -> bool:
    if not isinstance(filepath, str):
        return False

    if not re.match(regex, filepath):
        return False

    return True


def get_profile_data() -> dict:
    name = get_username()
    phone = get_phone_number()
    email = get_email()

    return {"name": name, "phone": phone, "email": email}

def save_profile_data(profile: dict, filepath: str) -> None:
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
