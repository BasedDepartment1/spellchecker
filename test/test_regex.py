import unittest
from databases.base_generator import find_words


class RegexTests(unittest.TestCase):
    def test_primitive_case(self):
        word = "слово"
        self.assertListEqual(find_words(word), [word])

    def test_space_delim(self):
        pair = "два слова"
        self.assertListEqual(find_words(pair), ["два", "слова"])

    def test_upper_lower_case(self):
        words = " сЪел ДедА"
        self.assertListEqual(find_words(words), ["сЪел", "ДедА"])

    def test_brackets_and_numbers(self):
        sentence = "(28) Привет мир"
        self.assertListEqual(find_words(sentence), ["Привет", "мир"])

    def test_complex_case(self):
        case = ")(0)(Ilb| (191) \nсложно%(№"
        self.assertListEqual(find_words(case), ["сложно"])


if __name__ == '__main__':
    unittest.main()
