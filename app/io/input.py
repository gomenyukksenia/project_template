import pandas as pd


def input_text_from_console():
    """
        Entering text from the console.

        Returns:
            str: The text inputted by the user.
    """
    text = input("Enter your text: ")
    return text


def read_text_from_file(file_path):
    """
        Reads text from a file using Python's built-in capabilities.

        Args:
            file_path (str): The path to the file from which text will be read.

        Returns:
            str: The text read from the file.
            None: If the file is not found.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            file.close()
            return text
    except FileNotFoundError:
        print("The file wasn't found")
        return None


def read_text_from_file_with_pandas(file_path):
    """
        Reads text from a file using the "pandas" library.

        Args:
            file_path (str): The path to the file from which text will be read.

        Returns:
            str: The text read from the file.
            None: If the file is not found.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("The file wasn't found")
