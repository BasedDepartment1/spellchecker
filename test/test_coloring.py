import unittest
import coloring
from colorama import Fore, Style


class MyTestCase(unittest.TestCase):
    def test_raises_exception_on_incorrect_indices(self):
        text = "12345 "
        with self.assertRaises(IndexError):
            coloring.highlight_symbol_on_position(text, -1)
            coloring.highlight_symbol_on_position("", 0)
            coloring.highlight_symbol_on_position(text, 6)
            coloring.highlight_symbol_range(text, 4, 2)
            coloring.highlight_all_symbols_before(text, -1)
            coloring.highlight_all_symbols_from(text, 666)

    def test_highlights_symbol(self):
        text = "123"
        colored = coloring.highlight_symbol_on_position(text, 0)
        self.assertEqual(f"{Fore.RED}1{Style.RESET_ALL}23", colored)
        colored = coloring.highlight_symbol_on_position(text, 1)
        self.assertEqual(f"1{Fore.RED}2{Style.RESET_ALL}3", colored)
        colored = coloring.highlight_symbol_on_position(text, 2)
        self.assertEqual(f"12{Fore.RED}3{Style.RESET_ALL}", colored)

    def test_highlights_range(self):
        text = "123"
        colored = coloring.highlight_symbol_range(text, 0, 2)
        self.assertEqual(f"{Fore.RED}12{Style.RESET_ALL}3", colored)
        colored = coloring.highlight_symbol_range(text, 1, 3)
        self.assertEqual(f"1{Fore.RED}23{Style.RESET_ALL}", colored)

    def test_highlights_from(self):
        text = "123"
        colored = coloring.highlight_all_symbols_from(text, 0)
        self.assertEqual(f"{Fore.RED}123{Style.RESET_ALL}", colored)
        colored = coloring.highlight_all_symbols_from(text, 1)
        self.assertEqual(f"1{Fore.RED}23{Style.RESET_ALL}", colored)
        colored = coloring.highlight_all_symbols_from(text, 2)
        self.assertEqual(f"12{Fore.RED}3{Style.RESET_ALL}", colored)

    def test_highlights_to(self):
        text = "123"
        colored = coloring.highlight_all_symbols_before(text, 1)
        self.assertEqual(f"{Fore.RED}1{Style.RESET_ALL}23", colored)
        colored = coloring.highlight_all_symbols_before(text, 2)
        self.assertEqual(f"{Fore.RED}12{Style.RESET_ALL}3", colored)


if __name__ == '__main__':
    unittest.main()
