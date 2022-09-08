import word
import re
import databases


def generate_base() -> None:
    databases.try_make_tables()
    if databases.is_set_up():
        raise databases.DataBaseException("Database already has been set up")
    load_info()


def load_info() -> None:
    stems = [word.get_stem(w.lower()) for w in parse_words()]
    load_to_database(stems)


def load_to_database(stems: list) -> None:
    for stem in stems:
        databases.insert_stem(stem)


def parse_words() -> list[str]:
    with open("text_base.txt", encoding="utf8") as f:
        text = f.read()
        return find_words(text)


def find_words(text: str) -> list[str]:
    pattern = re.compile(r'[А-Яа-яёЁ]+')
    return re.findall(pattern, text)
