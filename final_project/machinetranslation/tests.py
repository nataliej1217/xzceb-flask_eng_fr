import unittest
from machinetranslation import translator


class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(translator.english_to_french("Hello"), "Au revoir")


class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.french_to_english("Bonjour"), "Hi")
        self.assertNotEqual(translator.french_to_english("Bonjour"), "Good bye")

unittest.main()