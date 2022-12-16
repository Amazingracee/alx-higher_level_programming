#!/usr/bin/python3
"""
Module for fetching the status of https://alx-intranet.hbtn.io/status
"""

from urllib.request import urlopen


def get_status():
    """
    Fetches the status of https://alx-intranet.hbtn.io/status
    and returns the body of the response as a bytes object
    """
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        return response.read()


if __name__ == "__main__":
    # Get the status and print the body of the response
    status = get_status()
    print("Body response:")
    print("\t- type:", type(status))
    print("\t- content:", status)
    print("\t- utf8 content:", status.decode('utf-8'))
