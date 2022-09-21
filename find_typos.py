from databases.database import get_data
from spellchecker import spell_check
from coloring.coloring import clear_coloring


def find_typos(data_to_check, custom: bool):
    base = get_data(custom)
    if type(data_to_check) == str:
        spellcheck_file(data_to_check, base)
    else:
        print(spell_check(data_to_check, base))


def spellcheck_file(path, base):
    with open(path, "r") as f:
        text = f.read()
    spellchecked = clear_coloring(spell_check(text, base))
    with open(path, "w") as f:
        f.write(spellchecked)
