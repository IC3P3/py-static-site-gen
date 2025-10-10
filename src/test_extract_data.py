import unittest
from extract_data import extract_title


class TestHTMLNode(unittest.TestCase):
    def test_valid_title(self):
        markdown = """# Test this function
This is a test

## Should not take that
"""
        self.assertEqual(
            extract_title(markdown),
            "Test this function"
        )

    def test_not_valid_data(self):
        markdown = """No valid title
### Again not this
"""
        with self.assertRaises(Exception) as assert_error:
            extract_title(markdown)
        self.assertEqual(assert_error.exception.args[0], "No title found!")

    def test_title_mid(self):
        markdown = """## Wrong title
# This is the right test

## Also wrong title
"""
        self.assertEqual(
            extract_title(markdown),
            "This is the right test"
        )


if __name__ == "__main__":
    unittest.main()
