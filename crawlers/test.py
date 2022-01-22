import unittest
from scraping import request_content, check_exists, get_threads

class TestCrawlers(unittest.TestCase):
    word = 'askreddit'

    def test_status_code(self):
        """
        Test if status code of request is equal to 200
        """
        
        soup, status_code = request_content(self.word)
        self.assertEqual(status_code, 200)

    def test_check_exists_subreddit(self):
        """
        Test if exists subreddit on reddit
        """

        soup, _ = request_content(self.word)
        result = check_exists(soup)
        self.assertEqual(result, True)

    def test_threads(self):
        """
        Test if return belongs to class <list>
        """

        result = get_threads(self.word)
        self.assertEqual(type(result), list)