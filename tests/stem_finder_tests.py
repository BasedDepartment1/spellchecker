import unittest
from interactive_spellchecker import find_most_similar_stems


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.base = ["кот", "кит", "кошк", "собак",
                     "код"]

    def assert_contains_all(self, iterable1, iterable2):
        self.assertTrue(all([i in iterable2 for i in iterable1]))
        self.assertTrue(all([i in iterable1 for i in iterable2]))

    def test_find_zero_diff_word(self):
        word = "кошк"
        self.assertListEqual(
            find_most_similar_stems(word, self.base), [word]
        )

    def test_slight_error(self):
        word = "сбак"
        self.assertListEqual(
            find_most_similar_stems(word, self.base), ["собак"]
        )

    def test_find_multiple_words(self):
        word = "кид"
        self.assert_contains_all(
            find_most_similar_stems(word, self.base), ["код", "кит"]
        )


if __name__ == '__main__':
    unittest.main()