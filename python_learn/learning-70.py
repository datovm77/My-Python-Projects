import re

text = "Python\npython\nPYTHON"

pattern = re.compile(r"^python$", re.IGNORECASE | re.MULTILINE)
matches = pattern.findall(text)
print(matches)  # ['Python', 'python', 'PYTHON']