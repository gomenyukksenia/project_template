import pandas as pd


def input_text_from_console():
    text = input("Enter your text: ")
    return text


def read_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print("The file wasn't found")
        return None


def read_text_from_file_with_pandas(file_path):
    try:
        data = pd.read_csv(file_path, sep='\n', header=None)
        text = ' '.join(data[0].tolist())
        return text
    except FileNotFoundError:
        print("The file wasn't found")