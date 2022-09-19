import re
from levenstein_automata import levenstein_automata


def spell_check(text_to_check: str, base: list[str])\
        -> str:
    pattern = re.compile(r"[А-Яа-яёЁ-]+")
    return re.sub(pattern,
                  lambda m: correct_errors(m.group(), base),
                  text_to_check)


def correct_errors(word, base) -> str:
    possible_words = find_most_fitting_words(word, base)
    if len(possible_words) == 1:
        return possible_words[0]
    return make_suggestion_string(word, possible_words)


def make_suggestion_string(word, possible_words) -> str:
    return word + "{" + ",".join(possible_words) + "}"


def find_most_fitting_words(word_to_check: str, base: list[str]) -> list[str]:
    return levenstein_automata.find_all_matches(word_to_check, base)
