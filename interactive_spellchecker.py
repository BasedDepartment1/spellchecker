from databases import databases
from databases.table_type import TableType
from levenstein_automata import levenstein_automata


def spell_check(word_to_check: str, table_type: TableType = TableType.BUILTIN)\
        -> list[str]:
    base = databases.get_all_data_from_table(table_type)
    return find_most_fitting_words(word_to_check, base)


def find_most_fitting_words(word_to_check: str, base: list[str]) -> list[str]:
    return levenstein_automata.find_all_matches(word_to_check, base)
