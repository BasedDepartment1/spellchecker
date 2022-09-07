import re
with open("text_base.txt", encoding="utf8") as f:
    st = f.read()
pattern = re.compile(r'[А-Яа-яёЁ]+')
a = re.findall(pattern, st)
print(a)