import sqlite3
from databases.table_type import TableType


class DataBaseException(Exception):
    def __init__(self, message: str):
        self.msg = message


class DataBase:
    def __init__(self, name: str):
        self.name = name
        self.__base = sqlite3.connect("words.db")
        self.__cursor = self.__base.cursor()
        self.__try_make_table()

    def get_all_data(self) -> list[str]:
        self.__cursor.execute(f"SELECT * FROM {self.name};")
        data = [stem[0] for stem in self.__cursor.fetchall()]
        return data

    def load_data(self, data: list[str]) -> None:
        for stem in data:
            self.insert_stem(stem)

    def insert_stem(self, stem: str) -> None:
        self.__cursor\
            .execute(f"INSERT OR IGNORE INTO {self.name} VALUES(?);", (stem, ))
        self.__base.commit()

    def is_set_up(self) -> bool:
        content = self.get_all_data()
        return len(content) > 0

    def __try_make_table(self) -> None:
        self.__cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.name}(
            stem TEXT PRIMARY KEY);""")


def add_to_base(word: str, custom: bool):
    table_name = get_table_name(custom)
    db = DataBase(table_name)
    db.insert_stem(word)


def get_data(custom: bool) -> list[str]:
    table_name = get_table_name(custom)
    return DataBase(table_name).get_all_data()


def get_table_name(custom: bool) -> str:
    return TableType.CUSTOM if custom else TableType.BUILTIN
