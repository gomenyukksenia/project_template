import pandas as pd


def print_text_to_console(text):
    """
        Prints the specified text to the console.

        Args:
            text (str): The text to be printed to the console.

        Returns:
            None
    """
    print(text)


def write_text_to_file(file_path, text):
    """
        Writes the specified text to a file at the given file path.

        Args:
            file_path (str): The path to the file where the text will be written.
            text (str): The text to be written to the file.

        Returns:
            None
    """
    try:
        with open(file_path, 'a') as file:
            file.write(text)
            file.close()
    except Exception as e:
        print("There was some mistake in:", str(e))


def write_text_to_file_with_pandas(file_path, text):
    """
    Writes the specified text to a file using the Pandas.

    Args:
        file_path (str): The path to the file where the text will be written.
        text (str): The text to be written to the file.

    Returns:
        None
    """

    try:
        df = pd.DataFrame({"name": [text]})
        df.to_csv(file_path)
    except Exception as e:
        print("There was an error:", str(e))
