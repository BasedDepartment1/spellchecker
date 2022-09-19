from colorama import Fore, Style


def highlight_symbol_on_position(string: str, index: int) -> str:
    check_single_index(string, index)
    return highlight_symbol_range(string, index, index + 1)


def highlight_all_symbols_from(string: str, start: int) -> str:
    check_single_index(string, start)
    return highlight_symbol_range(string, start, len(string))


def highlight_all_symbols_before(string: str, end: int) -> str:
    check_single_index(string, end)
    return highlight_symbol_range(string, 0, end)


def highlight_symbol_range(string: str, start: int, end: int) -> str:
    check_two_indices(string, start, end)
    return string[:start] + Fore.RED \
        + string[start:end] + Style.RESET_ALL + string[end:]


def check_single_index(word: str, index):
    if is_index_incorrect(index, len(word)):
        raise IndexError("Highlight index was outside of bounds of string!")


def check_two_indices(word, start: int, stop: int) -> None:
    check_single_index(word, start)
    check_single_index(word, stop)
    if start > stop:
        raise IndexError("Start index was greater than end index!")


def is_index_incorrect(index: int, bound: int) -> bool:
    return index < 0 or index > bound
