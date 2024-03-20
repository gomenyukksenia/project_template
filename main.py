from app.io.input import *
from app.io.output import *
from data import *
import pandas as pd


def main():
    # first input function
    console_text = input_text_from_console()
    print("Text from console:", console_text)
    with open("data/input_results.txt", "w") as file:
        file.write(console_text)
        file.close()

    # second input function
    file_text = read_text_from_file("data/read_from.txt")
    if file_text is not None:
        print("Text from file (using built-in functions):", file_text)
        with open("data/input_results.txt", "a") as file:
            file.write(file_text)
            file.close()
    else:
        print("Failed to read text from file")

    # third input function
    file_path = "data/read_from.txt"
    pandas_csv = read_text_from_file_with_pandas(file_path)
    if pandas_csv is not None:
        print("Text from file (using pandas): ", pandas_csv.to_csv())
        with open("data/input_results.txt", "a") as file:
            file.write(pandas_csv.to_csv())
            file.close()
    else:
        print("Failed to read text from file with pandas")

    # first output function
    print_text_to_console("Testing first output function")

    # third output function
    write_text_to_file_with_pandas("data/output_results.txt", "Testing third output function")

    # second output function
    write_text_to_file("data/output_results.txt", "Testing second output function")


if __name__ == "__main__":
    main()
