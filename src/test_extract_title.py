import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_hello(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_extract_title_ahoj(self):
        self.assertEqual(extract_title("# Ahoj"), "Ahoj")

if __name__ == "__main__":
    unittest.main()