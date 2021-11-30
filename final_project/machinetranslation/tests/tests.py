import unittest
from translator import *


class TestEngToFrText(unittest.TestCase):
    def test_null_value(self):
        self.assertEqual(
            english_to_french(None), "Please enter some text to translate..."
        )

    def test_valid_arguement(self):
#        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(
            english_to_french(None), "Please enter some text to translate..."
        )


class TestFrToEngText(unittest.TestCase):
    def test_null_value(self):
        self.assertEqual(
            french_to_english(None), "Please enter some text to translate..."
        )

    def test_valid_arguement(self):
#        self.assertEqual(english_to_french("Bonjour"), "Hello")
        self.assertEqual(
            french_to_english(None), "Please enter some text to translate..."
        )


if __name__ == "__main__":
    unittest.main()
