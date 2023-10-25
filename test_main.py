import unittest
import main
import os

class TestGenerateRandomFiles(unittest.TestCase):
    def test_generate_random_files(self):
        # Test that generate_random_files creates the correct number of files
        main.generate_random_files('txt', 5)
        self.assertEqual(len(os.listdir('gen')), 5)

        # Test that generate_random_files renames .txt files to .png files
        main.generate_random_files('png', 1)
        self.assertTrue(os.path.exists('gen/file1.png'))
        self.assertFalse(os.path.exists('gen/file1.txt'))

if __name__ == '__main__':
    unittest.main()