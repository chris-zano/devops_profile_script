"""
This module contains definitions that handle the
reading and writing of user profile data to/from file
"""

from get_inputs import get_username, get_email, get_phone_number

def get_profile_data() -> dict:
    """returns a dictionary of retrieved user data"""
    name = get_username()
    phone = get_phone_number()
    email = get_email()

    return {"name": name, "phone": phone, "email": email}

def save_profile_data(profile: dict, filepath: str) -> None:
    """saves user profile to file"""
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
    """reads user profile data from file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.readlines()
        profile = [line.strip() for line in content]
        return profile
    except FileNotFoundError:
        return []
