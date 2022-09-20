import re
from levenstein_automata.levenstein_automata import find_all_matches
from coloring import coloring, diff_highlighter


def spell_check(text_to_check: str, base: list[str])\
        -> str:
    pattern = re.compile(r"[А-Яа-яёЁ-]+")
    return re.sub(pattern,
                  lambda m: correct_errors(m.group(), base),
                  text_to_check)


def correct_errors(word, base) -> str:
    possible_words = find_most_fitting_words(word, base)
    if len(possible_words) == 0:
        return coloring.highlight_all(word)
    if len(possible_words) == 1:
        return diff_highlighter.highlight_difference(word, possible_words[0])
    return make_suggestion_string(word, possible_words)


def make_suggestion_string(word, possible_words) -> str:
    highlighted_possible_words = [
            diff_highlighter.highlight_difference(word, w)
            for w in possible_words
        ]
    return word + "{" + ",".join(highlighted_possible_words) + "}"


def find_most_fitting_words(word_to_check: str, base: list[str]) -> list[str]:
    possible_words = find_all_matches(word_to_check, base)
    if len(possible_words) == 1:
        return possible_words

    spaced_words = find_space_loss(word_to_check, base)
    return [*list(spaced_words), *possible_words]


def find_space_loss(word_to_check: str, base: list[str]) -> set[str]:
    result = set()
    for i in range(1, len(word_to_check) - 1):
        w1, w2 = word_to_check[:i], word_to_check[i:]
        sug1 = find_all_matches(w1, base)
        sug2 = find_all_matches(w2, base)
        if len(sug1) == 1 and len(sug2) == 1:
            result.add(sug1[0] + " " + sug2[0])
    return result
