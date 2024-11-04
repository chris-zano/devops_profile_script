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
       Prompts the user to enter a valid phone number in international format.

       Returns:
           str: A valid phone number or None (if
           the maximum number of attempts is reached).
    """
    phone_pattern = r'^\+?[1-9]\d{1, 14}'
    tries_count = 0

    while tries_count < 3:
        phone_number = input(
            "Please enter your phone number in international format:\n"
            "Examples:\n"
            "- +233 123-456-7890 (GHANA)\n"
            "- +234 20 1234 5678 (NIGERIA)\n"
            "- +1 98765 43210 (USA)\n"
            "Your phone number: "
        )

        if re.match(phone_pattern, phone_number):
            print("Phone number accepted.")
            return phone_number
        else:
            print(
                "Invalid format. Please make sure to enter your phone number"
                " in international format (e.g., +1234567890).")
            tries_count += 1

    print("Too many invalid attempts. Please try again later.")
    sys.exit(1)

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

