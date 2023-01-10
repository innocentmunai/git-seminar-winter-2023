"""
    Python script to get create a .txt file whose name is the user's GitHub
    username, and contains user's full name.
"""

from helpers import get_name, get_username, create_txt_file


def main():

    # Get user's name and GitHub username
    name = get_name()
    username = get_username()

    # Create .txt file and write into it.
    create_txt_file(file_name=username, content=name)

    # That's it!
    return


# Driver code
if __name__ == "__main__":
    main()
