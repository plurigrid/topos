import unittest
import os
import shutil
import hy
from src.core_loop import list_files
from src.utils.file_ops import read_file, write_file, create_directory, copy_file, move_file, delete_file, get_file_metadata

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
        self.assertTrue(os.path.isdir(new_dir))

    def test_copy_file(self):
        src = os.path.join(self.test_dir, 'file1.txt')
        dst = os.path.join(self.test_dir, 'file1_copy.txt')
        copy_file(src, dst)
        self.assertTrue(os.path.exists(dst))
        with open(dst, 'r') as f:
            content = f.read()
        self.assertEqual(content, "This is file1.txt")

    def test_move_file(self):
        src = os.path.join(self.test_dir, 'file2.txt')
        dst = os.path.join(self.test_dir, 'file2_moved.txt')
        move_file(src, dst)
        self.assertFalse(os.path.exists(src))
        self.assertTrue(os.path.exists(dst))
        with open(dst, 'r') as f:
            content = f.read()
        self.assertEqual(content, "This is file2.txt")

    def test_delete_file(self):
        file_to_delete = os.path.join(self.test_dir, 'file3.txt')
        delete_file(file_to_delete)
        self.assertFalse(os.path.exists(file_to_delete))

    def test_get_file_metadata(self):
        file_path = os.path.join(self.test_dir, 'file1.txt')
        metadata = get_file_metadata(file_path)
        self.assertIsInstance(metadata, dict)
        self.assertIn('size', metadata)
        self.assertIn('created', metadata)
        self.assertIn('modified', metadata)

if __name__ == '__main__':
    unittest.main()
