import unittest
from formatter import Formatter

class TestFormatter(unittest.TestCase):
    text = 'In the beginning God created the heavens and the earth.'
    size = 20

    def test_split(self):
        """
        Test if text is not equal to result
        """
        
        f = Formatter()
        result = f.split(self.text, self.size)
        self.assertNotEqual(self.text, result)

    def test_fast_split(self):
        """
        Test if text is not equal to result in fast way
        """

        f = Formatter()
        result = f.fast_split(self.text, self.size)
        self.assertNotEqual(self.text, result)

    def test_justify(self):
        """
        Test if text is not equal to justified result
        """

        f = Formatter()
        result = f.justify(self.text, self.size)
        self.assertNotEqual(self.text, result)

    def test_save_file(self):
        """
        Test save file
        """

        f = Formatter()
        self.assertEqual(f.save_file(self.text), True)

if __name__ == '__main__':
    unittest.main()