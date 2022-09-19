import unittest
from levenstein_automata import matcher, levenstein_automata


class AutomataTests(unittest.TestCase):
    def setUp(self) -> None:
        self.base = ["кот", "кит", "кошка", "собака",
                     "код"]
        self.base.sort()

    def assert_contains_all(self, iterable1, iterable2):
        self.assertTrue(all([i in iterable2 for i in iterable1]))
        self.assertTrue(all([i in iterable1 for i in iterable2]))

    def test_find_zero_diff_word(self):
        word = "кошка"
        self.assertListEqual(
            levenstein_automata.find_all_matches(word, self.base), [word]
        )

    def test_slight_error(self):
        word = "сбака"
        self.assertListEqual(
            levenstein_automata.find_all_matches(word, self.base), ["собака"]
        )

    def test_find_multiple_words(self):
        word = "кид"
        self.assert_contains_all(
            levenstein_automata.find_all_matches(word, self.base), ["код", "кит"]
        )


if __name__ == '__main__':
    unittest.main()
