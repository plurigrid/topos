import unittest
import os
import shutil
from src.main import list_files
from src.utils.file_ops import read_file, write_file, create_directory

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = os.path.join(os.getcwd(), 'test_directory')
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Create some test files
        self.test_files = ['file1.txt', 'file2.txt', 'file3.txt']
        for file in self.test_files:
            with open(os.path.join(self.test_dir, file), 'w') as f:
                f.write(f"This is {file}")

    def tearDown(self):
        # Remove the temporary directory after tests
        shutil.rmtree(self.test_dir)

    def test_list_files(self):
        os.chdir(self.test_dir)
        files = list_files()
        self.assertEqual(len(files), len(self.test_files))
        for file, metadata in files:
            self.assertIn(file, self.test_files)
            self.assertIsInstance(metadata, dict)
            self.assertIn('size', metadata)
            self.assertIn('created', metadata)
            self.assertIn('modified', metadata)

    def test_list_files_with_subdirs(self):
        subdir = os.path.join(self.test_dir, 'subdir')
        os.makedirs(subdir)
        with open(os.path.join(subdir, 'subfile.txt'), 'w') as f:
            f.write("This is a file in a subdirectory")
        
        os.chdir(self.test_dir)
        files = list_files(include_subdirs=True)
        self.assertEqual(len(files), len(self.test_files) + 1)
        subdir_file = next((f for f, _ in files if f.endswith('subfile.txt')), None)
        self.assertIsNotNone(subdir_file)

    def test_read_file(self):
        content = read_file(os.path.join(self.test_dir, 'file1.txt'))
        self.assertEqual(content, "This is file1.txt")

    def test_write_file(self):
        new_file = os.path.join(self.test_dir, 'new_file.txt')
        write_file(new_file, "This is a new file")
        with open(new_file, 'r') as f:
            content = f.read()
        self.assertEqual(content, "This is a new file")

    def test_create_directory(self):
        new_dir = os.path.join(self.test_dir, 'new_directory')
        create_directory(new_dir)
        self.assertTrue(os.path.exists(new_dir))

class TestToposDirectory(unittest.TestCase):
    def test_list_topos_files(self):
        topos_dir = '/Users/barton/topos'
        if os.path.exists(topos_dir):
            os.chdir(topos_dir)
            files = list_files()
            self.assertIsInstance(files, list)
            self.assertTrue(len(files) > 0)
        else:
            self.skipTest("Topos directory does not exist")

if __name__ == '__main__':
    unittest.main()
