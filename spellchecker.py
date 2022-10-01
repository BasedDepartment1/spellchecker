import re
from levenstein_automata.levenstein_automata import find_all_matches
from coloring import coloring, diff_highlighter
from rules.rules import apply_rules


def spell_check(text_to_check: str, base: list[str]) -> str:
    pattern = re.compile(r"[1-9A-Za-zА-Яа-яёЁ-]+")
    return re.sub(pattern,
                  lambda m: correct_errors(m.group(), base),
                  text_to_check)


def correct_errors(word, base) -> str:
    possible_words = find_most_fitting_words(word.replace("-", ""), base)
    if len(possible_words) == 0:
        return coloring.highlight_all(word)
    if len(possible_words) == 1:
        return diff_highlighter.highlight_difference(
            word, apply_rules(possible_words[0])
        )
    return make_suggestion_string(word, possible_words)


def make_suggestion_string(word, possible_words) -> str:
    return format_suggestion_string(word, range_words(word, possible_words))


def format_suggestion_string(word, possible_words):
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


def range_words(word, possible_words: list[str]) -> list[str]:
    ranged_words = add_dashes_and_spaces(possible_words)
    words_count = len(ranged_words)
    for word in possible_words:
        if "-" not in word and " " not in word:
            ranged_words.append(word)
            words_count += 1
        if words_count > 3:
            break

    rule_checked = apply_rules(word)
    if rule_checked != word:
        ranged_words.insert(0, rule_checked)
    return ranged_words


# def check_rules(word):
#     rule_checked = apply_rules(word)
#     if rule_checked != word:
#         return format_suggestion_string(word, rule_checked)
#     return word


def add_dashes_and_spaces(possible_words: list[str]) -> list[str]:
    ranged_words = []
    dash_index = find_index_of_word_with_substring(possible_words, "-")
    space_index = find_index_of_word_with_substring(possible_words, " ")
    if dash_index >= 0:
        ranged_words.append(possible_words[dash_index])
    if space_index >= 0:
        ranged_words.append(possible_words[space_index])
    return ranged_words


def find_space_loss(word_to_check: str, base: list[str]) -> set[str]:
    result = set()
    for i in range(1, len(word_to_check) - 1):
        w1, w2 = word_to_check[:i], word_to_check[i:]
        sug1 = find_all_matches(w1, base)
        sug2 = find_all_matches(w2, base)
        if len(sug1) == 1 and len(sug2) == 1:
            result.add(sug1[0] + " " + sug2[0])
    return result


def find_index_of_word_with_substring(words: list[str], substr: str) -> int:
    for i, word in enumerate(words):
        if substr in word:
            return i
    return -1
