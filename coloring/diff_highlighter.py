import difflib
from coloring import coloring


def highlight_difference(original: str, actual: str) -> str:
    d = difflib.Differ()
    diff_index = -1
    for i, step in enumerate(d.compare(original, actual)):
        if step[0] in '-+':
            diff_index = i
            break

    return _highlight_diff_index(actual, diff_index)


def _highlight_diff_index(word: str, index: int) -> str:
    if index == -1:
        return word
    if index < len(word):
        return coloring.highlight_symbol_on_position(word, index)
    return _highlight_with_extension(word)


def _highlight_with_extension(word: str) -> str:
    return word + coloring.highlight_all(' ')
