import unittest
from spellchecker import spell_check
from coloring.coloring import clear_coloring


class TestSpellChecker(unittest.TestCase):
    def setUp(self) -> None:
        self.base = ["я", "съел", "деда"]

    def assert_contains_all(self, iterable1, iterable2):
        self.assertTrue(all([i in iterable2 for i in iterable1]))
        self.assertTrue(all([i in iterable1 for i in iterable2]))

    def test_do_nothing_on_correct_text(self):
        text = "я съел деда"
        actual = clear_coloring(spell_check(text, self.base))
        self.assertEqual(text, actual)

    def test_do_nothing_with_signs(self):
        text = "я? съел? деда!!!"
        actual = clear_coloring(spell_check(text, self.base))
        self.assertEqual(text, actual)

    def test_replace_if_found_one(self):
        text = "я съел дда"
        expected = "я съел деда"
        actual = clear_coloring(spell_check(text, self.base))
        self.assertEqual(expected, actual)

    def test_writes_all_if_found_multiple(self):
        base = ["я", "съел", "деда", "да"]
        text = "я съел дда"
        expected = ["я съел дда{деда,да}",
                    "я съел дда{да,деда}"]
        actual = clear_coloring(spell_check(text, base))
        self.assertTrue(actual in expected)

    def test_finds_space_loss(self):
        base = ["всем", "привет"]
        text = "всемпривет"
        expected = "всем привет"
        actual = clear_coloring(spell_check(text, base))
        self.assertEqual(expected, actual)

    def test_finds_space_loss_and_typo(self):
        base = ["я", "съел", "деда", "да", "дата"]
        text = "я съел дада"
        expected = ["я съел дада{да да,дата,деда}",
                    "я съел дада{да да,деда,дата}"]
        actual = clear_coloring(spell_check(text, base))
        self.assertTrue(actual in expected)

    def test_finds_double_dash(self):
        base = ["кое-как"]
        text = "кое--как"
        expected = base[0]
        actual = clear_coloring(spell_check(text, base))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
