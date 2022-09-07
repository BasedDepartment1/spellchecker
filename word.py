from nltk.stem.snowball import SnowballStemmer


def get_stem(word: str):
    stemmer = SnowballStemmer("russian")
    return stemmer.stem(word)


class Word:
    def __init__(self, word: str):
        stemmer = SnowballStemmer("russian")

        self.stem = stemmer.stem(word)
        self.affix = '' if len(self.stem) == len(word) \
            else word[len(self.stem)::]
