""" Helper functions """


def get_name():
    """Prompt user for their name"""

    return input("What is your name my friend?😀 >>> ").strip()


def get_username():
    """Prompt user for their GitHub username name"""

    return input("What is your GitHub username?🐙 >>> ").strip()


def create_txt_file(file_name, content):
    """Create <name>.txt file with <content> written in it"""

    # Format the name with file extension
    name_txt = file_name + ".txt"

    try:
        # Open file (by default creates if doesn't exist), and write content
        f = open(name_txt, "w")
        f.write(content)
        f.close()

        # Print confirmation, on success
        print(f"File '{name_txt}' has been created successfully!🎉 ")

    except Exception as e:
        print(f"Sorry, some error occured >>> {e}")

    # Explicitly return None
    return None
