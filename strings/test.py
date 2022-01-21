import unittest
from formatter import Formatter

class TestFormatter(unittest.TestCase):
    text = 'In the beginning God created the heavens and the earth.'
    size = 20

    def test_split(self):
        f = Formatter()
        result = f.split(self.text, self.size)
        self.assertNotEqual(self.text, result)

    def test_fast_split(self):
        f = Formatter()
        result = f.fast_split(self.text, self.size)
        self.assertNotEqual(self.text, result)

    def test_justify(self):
        f = Formatter()
        result = f.justify(self.text, self.size)
        self.assertNotEqual(self.text, result)

    def test_save_file(self):
        f = Formatter()
        self.assertEqual(f.save_file(self.text), True)

if __name__ == '__main__':
    unittest.main()