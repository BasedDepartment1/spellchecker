import unittest
from coloring import coloring, diff_highlighter


class DiffHighlighterTest(unittest.TestCase):
    def test_no_highlight_if_equal(self):
        text = checked = "123"
        highlighted = diff_highlighter.highlight_difference(text, checked)
        self.assertEqual(checked, highlighted)

    def test_highlight_one_different_symbol(self):
        text = "123"
        checked = "113"
        expected = coloring.highlight_symbol_on_position(checked, 1)
        actual = diff_highlighter.highlight_difference(text, checked)
        self.assertEqual(expected, actual)

    def test_highlights_whitespace_if_no_last_symbol(self):
        text = "123"
        checked = "12"
        expected = coloring.highlight_symbol_on_position(checked + " ", 2)
        actual = diff_highlighter.highlight_difference(text, checked)
        self.assertEqual(expected, actual)

    def test_highlights_extra_symbols(self):
        text = "123"
        cases = ["o123", "1o23", "12o3", "123o"]

        for i, checked in enumerate(cases):
            expected = coloring.highlight_symbol_on_position(checked, i)
            actual = diff_highlighter.highlight_difference(text, checked)
            self.assertEqual(expected, actual)

    def test_highlights_right_symbol_if_deleted(self):
        text = "12345"
        checked = "1245"
        expected = coloring.highlight_symbol_on_position(checked, 2)
        actual = diff_highlighter.highlight_difference(text, checked)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
