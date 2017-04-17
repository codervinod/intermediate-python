import unittest

import directory

class TestDirectory(unittest.TestCase):

    def setUp(self):
        self.d = directory.Directory()
        self.d.add_number('Rick', '404.452.5202')

    def test_add_number(self):
        self.d.add_number('Frog', '404.452.5112')
        self.assertEqual(self.d.lookup_number('Frog'), '404.452.5112')

    def test_lookup_number(self):
        self.assertEqual(self.d.lookup_number('Rick'), '404.452.5202')

    def test_lookup_number_not_present(self):
        raise AssertionError, 'Not implemented yet'

    def test_remove_number(self):
        raise AssertionError, 'Not implemented yet'

    def test_remove_number_not_present(self):
        raise AssertionError, 'Not implemented yet'

if __name__ == '__main__':
    unittest.main()