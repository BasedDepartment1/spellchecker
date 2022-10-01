import json


def apply_rules(word) -> str:
    rules = get_existing_rules()
    if word in rules:
        return rules[word]
    return word


def clear_rules():
    with open("rules.json", "w") as f:
        pass


def set_up_custom_rules(path: str):
    with open(path, encoding="utf-8") as f:
        rules = parse_custom_rules(f.read().split('\n'))
    load_rules_to_json(rules)


def get_existing_rules() -> dict:
    with open("rules.json", "r", encoding="utf-8") as f:
        content = f.read()
        if content == '':
            return dict()
        return json.loads(content)


def parse_custom_rules(lines: list[str]) -> dict:
    rules = dict()
    for line in lines:
        parts = line.split(":")
        value = parts[0]
        keys = parts[1].split(",")
        rules = add_rule_entries(rules, keys, value)
    return rules


def add_rule_entries(rules: dict, keys: list[str], value: str) -> dict:
    for key in keys:
        rules[key] = value
    return rules


def load_rules_to_json(rules: dict):
    existing_rules = get_existing_rules()
    with open("rules.json", "w+", encoding="utf-8") as f:
        all_rules = existing_rules | rules
        json.dump(all_rules, f, ensure_ascii=False, indent=4)
