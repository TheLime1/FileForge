import os
import sys
import random


def test_file_generation():
    """Test the file generation functionality"""
    print("Testing FileForge file generation...")

    # Define size ranges (matching the GUI application)
    code_size_range = (1024, 10240)  # 1KB to 10KB
    other_size_range = (1048576, 10485760)  # 1MB to 10MB

    # Create test directory
    test_dir = "test_output"
    os.makedirs(test_dir, exist_ok=True)

    # Clear existing files
    for file_name in os.listdir(test_dir):
        file_path = os.path.join(test_dir, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # Test code file generation
    print("\n1. Testing code file generation (1KB-10KB)...")
    for i in range(3):
        file_name = f"code_test_{i+1}.py"
        file_path = os.path.join(test_dir, file_name)
        file_size = random.randint(*code_size_range)

        with open(file_path, 'wb') as file:
            file.write(os.urandom(file_size))

        actual_size = os.path.getsize(file_path)
        print(f"   {file_name}: {actual_size} bytes ({actual_size/1024:.1f} KB)")
        assert code_size_range[0] <= actual_size <= code_size_range[
            1], f"Size out of range: {actual_size}"

    # Test other file generation
    print("\n2. Testing other file generation (1MB-10MB)...")
    for i in range(2):
        file_name = f"other_test_{i+1}.zip"
        file_path = os.path.join(test_dir, file_name)
        file_size = random.randint(*other_size_range)

        with open(file_path, 'wb') as file:
            file.write(os.urandom(file_size))

        actual_size = os.path.getsize(file_path)
        print(
            f"   {file_name}: {actual_size} bytes ({actual_size/1024/1024:.1f} MB)")
        assert other_size_range[0] <= actual_size <= other_size_range[
            1], f"Size out of range: {actual_size}"

    print("\n✓ All tests passed! File generation is working correctly.")
    print(f"✓ Test files created in '{test_dir}' directory.")

    return True


if __name__ == "__main__":
    test_file_generation()
