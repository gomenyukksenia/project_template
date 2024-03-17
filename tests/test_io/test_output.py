def input_text_from_console():
    text = input("Enter your text: ")
    return text

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None