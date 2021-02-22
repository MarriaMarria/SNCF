import os
import unittest
from classes2 import TestApi


class Test_read_json(unittest.TestCase):
    def test_read_json(self):
        directory_path = 'stop_areas_maria.json' # somepath
        self.assertTrue(os.path.exists(directory_path))


if __name__ == '__main__':
    unittest.main(verbosity=0)
