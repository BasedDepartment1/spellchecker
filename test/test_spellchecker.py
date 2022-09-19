import unittest
from spellchecker import spell_check


class TestSpellChecker(unittest.TestCase):
    def setUp(self) -> None:
        self.base = ["я", "съел", "деда"]
        self.base.sort()

    def assert_contains_all(self, iterable1, iterable2):
        self.assertTrue(all([i in iterable2 for i in iterable1]))
        self.assertTrue(all([i in iterable1 for i in iterable2]))

    def test_do_nothing_on_correct_text(self):
        text = "я съел деда"
        actual = spell_check(text, self.base)
        self.assertEqual(text, actual)

    def test_do_nothing_with_signs(self):
        text = "я? съел? деда!!!"
        actual = spell_check(text, self.base)
        self.assertEqual(text, actual)

    def test_replace_if_found_one(self):
        text = "я съел дда"
        expected = "я съел деда"
        actual = spell_check(text, self.base)
        self.assertEqual(expected, actual)

    def test_writes_all_if_found_multiple(self):
        base = ["я", "съел", "деда", "да"]
        base.sort()
        text = "я съел дда"
        expected = ["я съел дда{деда,да}",
                    "я съел дда{да,деда}"]
        actual = spell_check(text, base)
        self.assertTrue(actual in expected)


if __name__ == '__main__':
    unittest.main()
