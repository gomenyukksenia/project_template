def print_text_to_console(text):
    print(text)


def write_text_to_file(file_path, text):
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        print("Text was added to:", file_path)
    except Exception as e:
        print("There was some mistake in:", str(e))