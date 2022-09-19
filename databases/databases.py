from databases.__init__ import base, cursor
from databases.table_type import TableType


class DataBaseException(Exception):
    def __init__(self, message: str):
        self.msg = message


def try_make_tables() -> None:
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {TableType.BUILTIN}(
        stem TEXT PRIMARY KEY);""")

    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {TableType.CUSTOM}(
        stem TEXT PRIMARY KEY);""")


def insert_stem(stem: str, name: TableType) -> None:
    cursor.execute(f"INSERT OR IGNORE INTO {name} VALUES(?);", (stem, ))
    base.commit()


def get_all_data_from_table(name: TableType) -> list[str]:
    cursor.execute(f"SELECT * FROM {name};")
    data = [stem[0] for stem in cursor.fetchall()]
    return data


def is_set_up(name: TableType) -> bool:
    content = get_all_data_from_table(name)
    return len(content) > 0
