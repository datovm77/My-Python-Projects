import re

text = "我的邮箱是 test@example.com，备用邮箱是 backup@gmail.com"

# findall 返回所有匹配的列表
emails = re.findall(r"\w+@\w+\.\w+", text)
print(emails)  # ['test@example.com', 'backup@gmail.com']

# 有分组时，返回分组内容
pairs = re.findall(r"(\w+)@(\w+\.\w+)", text)
print(pairs)  # [('test', 'example.com'), ('backup', 'gmail.com')]