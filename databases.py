import sqlite3


class DataBaseException(Exception):
    def __init__(self, message: str):
        self.msg = message


BUILTIN_TABLE_NAME = 'builtin'
CUSTOM_TABLE_NAME = 'custom'


base = sqlite3.connect("words.db")
cursor = base.cursor()


def try_make_tables() -> None:
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {BUILTIN_TABLE_NAME}(
        stem TEXT PRIMARY KEY);""")

    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {CUSTOM_TABLE_NAME}(
        stem TEXT PRIMARY KEY);""")


def insert_stem(stem: str, custom: bool = False) -> None:
    name = CUSTOM_TABLE_NAME if custom else BUILTIN_TABLE_NAME
    cursor.execute(f"INSERT OR IGNORE INTO {name} VALUES(?);", (stem, ))
    base.commit()


def get_all_data(custom: bool = False) -> list[str]:
    name = CUSTOM_TABLE_NAME if custom else BUILTIN_TABLE_NAME
    cursor.execute(f"SELECT * FROM {name};")
    return [stem[0] for stem in cursor.fetchall()]


def is_set_up() -> bool:
    content = get_all_data()
    return len(content) > 0

