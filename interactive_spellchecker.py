import databases
import sys
from rapidfuzz.distance import Levenshtein
from word import Word


def spell_check(word_to_check: str) -> list[str]:
    if not databases.is_set_up():
        raise databases.DataBaseException("Database has not been set up")
    return find_most_fitting_words(word_to_check)


def find_most_fitting_words(word_to_check: str) -> list[str]:
    processed_word = Word(word_to_check)
    base = databases.get_all_data()
    stems = find_most_similar_stems(processed_word.stem, base)
    return [stem + processed_word.affix for stem in stems]


def find_most_similar_stems(stem_to_check: str, base: list[str]) -> list[str]:
    min_distance = sys.maxsize
    fitting_stems = []
    for stem in base:
        current_distance = Levenshtein.distance(stem_to_check, stem)
        if current_distance == min_distance:
            fitting_stems.append(stem)
        elif current_distance < min_distance:
            min_distance = current_distance
            fitting_stems = [stem]
    return fitting_stems


