import unittest
from translator import english_to_french, french_to_english

class TranslatorTests(unittest.TestCase):
    def test_englishToFrench_translation(self):
        english_text = "Hello"
        expected_french_text = "Bonjour"
        translated_text = english_to_french(english_text)
        self.assertEqual(translated_text, expected_french_text)

    def test_frenchToEnglish_translation(self):
        french_text = "Bonjour"
        expected_english_text = "Hello"
        translated_text = french_to_english(french_text)
        self.assertEqual(translated_text, expected_english_text)

if __name__ == '__main__':
    unittest.main()
