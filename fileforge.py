import os
import random
import sys

def clear_directory(directory):
    # Clear all files in the specified directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)

def generate_code_files(num_files, size_range, directory):
    # Create the first three code files with specific names
    code_file_names = ["main.c", "header.h", "source.c"]
    for file_name in code_file_names:
        file_size = random.randint(*size_range)
        with open(os.path.join(directory, file_name), 'wb') as file:
            file.write(os.urandom(file_size))

    # Create the rest of the code files
    for i in range(3, num_files):
        file_name = f"file{i - 2}.c"
        file_size = random.randint(*size_range)
        with open(os.path.join(directory, file_name), 'wb') as file:
            file.write(os.urandom(file_size))

def generate_generic_files(extension, num_files, size_range, directory):
    # Create the rest of the files for other extensions
    for i in range(num_files):
        file_name = f"file{i + 1}.{extension}"
        file_size = random.randint(*size_range)
        with open(os.path.join(directory, file_name), 'wb') as file:
            file.write(os.urandom(file_size))

def generate_random_files(extension, num_files):
    # Define size ranges for C/C++ and other code files, including .txt
    code_file_size_range = (280, 850)  # Bytes
    other_file_size_range = (1500000, 3400000)  # Bytes

    # Create a directory named "gen" if it doesn't exist
    os.makedirs("gen", exist_ok=True)

    if extension in ('c', 'cpp'):
        size_range = code_file_size_range
        clear_directory("gen")
        generate_code_files(num_files, size_range, "gen")
    else:
        size_range = other_file_size_range
        generate_generic_files(extension, num_files, size_range, "gen")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python fileforge.py <extension> <num_files>")
    else:
        extension = sys.argv[1]
        num_files = int(sys.argv[2])
        clear_directory("gen")
        generate_random_files(extension, num_files)
        print(f"{num_files} {extension} files have been generated in the 'gen' directory.")
