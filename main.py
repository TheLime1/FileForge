import os
import random

def generate_random_files(extension, num_files):
    # Define size ranges for C/C++ and other code files, including .txt
    code_file_size_range = (280, 850)  # Bytes
    other_file_size_range = (1500000, 3400000)  # Bytes

    if extension in ('c', 'cpp'):
        size_range = code_file_size_range
        if num_files >= 1:
            # For C/C++, ensure at least one of each
            file_names = ["main.c", "header.h", "source.c"]
            for i, file_name in enumerate(file_names):
                file_size = random.randint(*size_range)
                with open(os.path.join("gen", file_name), 'wb') as file:
                    file.write(os.urandom(file_size))
        
        # Create the rest of the C/C++ files
        for i in range(3, num_files):
            file_name = f"file{i - 2}.{extension}"
            file_size = random.randint(*size_range)
            with open(os.path.join("gen", file_name), 'wb') as file:
                file.write(os.urandom(file_size))
    else:
        size_range = other_file_size_range
        # Create a directory named "gen" if it doesn't exist
        os.makedirs("gen", exist_ok=True)

        # Create the rest of the files for other extensions
        for i in range(num_files):
            if extension == 'png':
                file_name = f"file{i + 1}.png"
            else:
                file_name = f"file{i + 1}.{extension}"
            file_size = random.randint(*size_range)
            with open(os.path.join("gen", file_name), 'wb') as file:
                file.write(os.urandom(file_size))

if __name__ == "__main__":
    extension = input("Enter the file extension (e.g., 'c', 'cpp', 'txt', 'png', etc.): ")
    num_files = int(input("Enter the number of files to generate: "))

    generate_random_files(extension, num_files)
    print(f"{num_files} {extension} files have been generated in the 'gen' directory.")
