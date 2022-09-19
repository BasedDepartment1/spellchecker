from levenstein_automata.nfa import NFA
from levenstein_automata.matcher import Matcher

ACCURACY = 1


def levenshtein_automata(term, k):
    nfa = NFA((0, 0))
    for i, c in enumerate(term):
        for e in range(k + 1):
            # Correct character
            nfa.add_transition((i, e), c, (i + 1, e))
            if e < k:
                # Deletion
                nfa.add_transition((i, e), NFA.ANY, (i, e + 1))
                # Insertion
                nfa.add_transition((i, e), NFA.EPSILON, (i + 1, e + 1))
                # Substitution
                nfa.add_transition((i, e), NFA.ANY, (i + 1, e + 1))
    for e in range(k + 1):
        if e < k:
            nfa.add_transition((len(term), e), NFA.ANY, (len(term), e + 1))
        nfa.add_final_state((len(term), e))
    return nfa


def get_next_match(word, k, base):
    """
    Uses lookup_func to find all words within levenshtein distance k of word.

    Args:
      word: The word to look up
      k: Maximum edit distance
      base: A database of all alphabet
    Yields:
      Every matching word within levenshtein distance k from the database.
    """
    lev = levenshtein_automata(word, k).to_dfa()
    lookup_func = Matcher(base)
    match = lev.next_valid_string(u'\0')
    while match:
        next_match = lookup_func(match)
        if not next_match:
            return
        if match == next_match:
            yield match
            next_match = next_match + u'\0'
        match = lev.next_valid_string(next_match)


def find_all_matches(word: str, base: list[str]) -> list[str]:
    """
    Uses levenshtein automata to find
    all words within levenshtein distance k of word.

    :param word: The word to look up
    :param base: A database of all words
    :returns:
      Every matching word within predetermined levenshtein
      distance from the database.
    """
    return list(get_next_match(word, ACCURACY, base))
