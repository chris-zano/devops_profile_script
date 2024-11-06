"""
This module contains definitions for retrieving user information
"""

import re
import sys


def get_username():
    """
       Prompts the user to enter their.

       Returns:
           str: user's name
    """
    username = input("Enter your name: ")
    return username


def get_phone_number():
    """
       Prompts the user to enter a valid phone number.

       Returns:
           str: A valid phone number.
    """

    valid_phone_patter = r'^\+?[1-9]\d{0,2}[-\s]?(\d{1,4}[-\s]?){1,4}\d{1,4}$'
    tries_count = 0

    while tries_count < 3:
        phone_number = input("Please enter your phone number in international format:\n"
        "Examples:\n"
        "- +1 123-456-7890 (USA)\n"
        "- +233 20 1234 5678 (GHANA)\n"
        "- +234 98765 43210 (NIGERIA)\n"
        "Your phone number: ")

        if re.fullmatch(valid_phone_patter, phone_number):
            return phone_number

        print("Invalid input")
        print("Please enter your phone number in international format:\n"
        "Examples:\n"
        "- +1 123-456-7890 (USA)\n"
        "- +233 20 1234 5678 (GHANA)\n"
        "- +234 98765 43210 (NIGERIA)\n"
        "Your phone number: ")
        tries_count += 1

def get_email():
    """
        Prompts the user to enter a valid email address.

        Returns:
            str: A valid email or None (if
            the maximum number of attempts is reached).
    """
    email_pattern = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'

    tries_count = 0

    while tries_count < 3:
        email = input("Enter your email address: ")

        if re.fullmatch(email_pattern, email, re.IGNORECASE):
            return email
        else:
            print(f'Email "{email}" is not valid.\n'
                  f'1. Must contain only lowercase letters (a-z), digits (0-9),'
                  f' periods (.), underscores (_), percent signs (%),'
                  f' plus signs (+), and hyphens (-).\n'
                  f'2. Must have an "@" symbol followed by a domain name.\n'
                  f'3. The domain must end with a period followed by a '
                  f' valid TLD (e.g., .com, .org, .net).')
            tries_count += 1

    print("Too many invalid attempts. Please try again later.")
    sys.exit(1)

