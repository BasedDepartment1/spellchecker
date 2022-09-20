import os
import unittest
import tempfile
from spellchecker import spell_check
from find_typos import spellcheck_file
from coloring.coloring import clear_coloring


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.name = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
        self.text = "acc"
        self.base = ["abc"]
        with open(self.name, "w") as f:
            f.write(self.text)

    def tearDown(self) -> None:
        os.remove(self.name)

    def test_file_functions_as_terminal(self):
        expected = clear_coloring(spell_check(self.text, self.base))
        spellcheck_file(self.name, self.base)
        with open(self.name) as f:
            self.assertEqual(expected, f.read())


if __name__ == '__main__':
    unittest.main()
