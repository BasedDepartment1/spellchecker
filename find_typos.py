from databases.database import get_data
from spellchecker import spell_check
from coloring.coloring import clear_coloring


def find_typos(data_to_check, custom: bool) -> None:
    result = get_spellchecked_result(data_to_check, custom)
    if result:
        print(result)


def get_spellchecked_result(data_to_check, custom: bool) -> str | None:
    base = get_data(custom)
    if type(data_to_check) == str:
        spellcheck_file(data_to_check, base)
        return

    return spell_check(" ".join(data_to_check), base)


def spellcheck_file(path, base):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    spellchecked = clear_coloring(spell_check(text, base))
    with open(path, "w", encoding="utf-8") as f:
        f.write(spellchecked)
