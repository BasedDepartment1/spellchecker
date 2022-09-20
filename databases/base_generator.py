from databases.database import DataBase, DataBaseException
from databases.table_type import TableType

BUILTIN_PATH = r"databases\russsian_small.txt"


def generate_base(path: str = None) -> None:
    table_name = TableType.BUILTIN if path is None else TableType.CUSTOM
    db = DataBase(table_name)
    if db.is_set_up():
        raise DataBaseException("Database has been set up already!")
    load_info(path, db)


def load_info(path: str | None, db: DataBase) -> None:
    actual_path = unify_path(path)
    stems = [w.lower() for w in parse_words(actual_path)]
    db.load_data(stems)


def parse_words(path: str) -> list[str]:
    with open(path, encoding="cp1251") as f:
        return f.read().split()


def unify_path(path: str | None) -> str:
    return BUILTIN_PATH if path is None else path
