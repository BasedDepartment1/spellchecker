import word
from databases import databases
from databases.table_type import TableType

BUILTIN_PATH = r"C:\Users\bayak\spellchecker\databases\russsian_small.txt"


def generate_base(path: str = None) -> None:
    databases.try_make_tables()
    table_name = TableType.BUILTIN if path is None else TableType.CUSTOM
    if databases.is_set_up(table_name):
        raise databases.DataBaseException("Database already has been set up")
    load_info(path, table_name)


def load_info(path: str | None, table_name: TableType) -> None:
    actual_path = unify_path(path)
    stems = [w.lower() for w in parse_words(actual_path)]
    load_to_database(stems, table_name)


def load_to_database(stems: list, table_name: TableType) -> None:
    for stem in stems:
        databases.insert_stem(stem, table_name)


def parse_words(path: str) -> list[str]:
    with open(path, encoding="cp1251") as f:
        return f.read().split()


def unify_path(path: str | None) -> str:
    return BUILTIN_PATH if path is None else path
