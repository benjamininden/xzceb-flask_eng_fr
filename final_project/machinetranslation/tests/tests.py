import unittest
from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test2(self):
        self.assertEqual(french_to_english(" "), " ")

    def test3(self):
        self.assertNotEqual(french_to_english(" "), None)


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test2(self):
        self.assertEqual(english_to_french(" "), " ")

    def test3(self):
        self.assertNotEqual(french_to_english(" "), None)

unittest.main()

