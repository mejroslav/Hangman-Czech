import unittest
import hangman

class WordTest(unittest.TestCase):
    with_diacritics = "příliš žluťoučký kůň úpěl ďábelské ódy".upper()
    without_diacritics = "prilis zlutoucky kun upel dabelske ody".upper()

    def test_remove_diacritics(self):
        """remove_diacritics function should remove hooks and dashes"""
        translated = hangman.remove_diacritics(self.with_diacritics)
        self.assertEqual(translated, self.without_diacritics)

if __name__ == '__main__':
    unittest.main()
