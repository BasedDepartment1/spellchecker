import argparse
from find_typos import find_typos
from databases.base_generator import generate_base
from databases.database import add_to_base
from rules.rules import clear_rules, set_up_custom_rules


def parse(arguments: list[str]):
    parser = setup_parser()
    args = parser.parse_args(arguments)
    args.function(args)


def setup_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title="commands",
                                       required=True)
    add_database_subparser(subparsers)
    add_spellcheck_subparser(subparsers)
    add_extension_subparser(subparsers)
    add_rule_subparser(subparsers)
    return parser


def add_database_subparser(subparsers):
    db_parser = subparsers.add_parser("setup")
    db_parser.add_argument("-c", "--custom",
                           dest="path",
                           type=str
                           )
    db_parser.set_defaults(function=lambda x: generate_base(x.path))


def add_spellcheck_subparser(subparsers):
    check_parser = subparsers.add_parser("spellcheck")
    check_parser.add_argument("-c", "--custom",
                              action="store_true",
                              dest="custom")

    check_parser.add_argument("-f", "--file",
                              dest="filepath",
                              type=str,
                              nargs=1,
                              )

    check_parser.add_argument("-i", "--interactive",
                              dest="words",
                              nargs="+",
                              )

    check_parser.set_defaults(function=lambda x:
                              find_typos(x.words or x.filepath[0], x.custom))


def add_extension_subparser(subparsers):
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("-c", "--custom",
                            action="store_true",
                            dest="custom")
    add_parser.add_argument("word",
                            type=str)
    add_parser.set_defaults(function=lambda x:
                            validate_insertion(x.word, x.custom))


def add_rule_subparser(subparsers):
    rule_parser = subparsers.add_parser("rules")
    rule_parser.add_argument("-c", "--clear",
                             action="store_true",
                             dest="clear")
    rule_parser.add_argument("-l", "--load",
                             dest="path",
                             type=str)
    rule_parser.set_defaults(function=lambda x:
                             manage_rules(x.clear, x.path))


def manage_rules(clear: bool, path):
    if clear:
        validate_rule_clear()
        return
    if path is not None:
        set_up_custom_rules(path)


def validate_insertion(word_to_add: str, custom: bool):
    table_name = "custom" if custom else "builtin"
    ans = input(f"Are you sure you want to insert word:\n{word_to_add}\ninto "
                f"{table_name} table? (y/n): ")

    if ans == "y":
        add_to_base(word_to_add, custom)


def validate_rule_clear():
    ans = input("Are you sure you want to clear all your rules? (y/n): ")
    if ans == "y":
        clear_rules()
