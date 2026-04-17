import re

# match 只从字符串开头匹配
print(re.match(r"\d+", "123abc"))   # <re.Match object; span=(0, 3), match='123'>
print(re.match(r"\d+", "abc123"))   # None （开头不是数字，匹配失败）

# 对比 search（在整个字符串中搜索）
print(re.search(r"\d+", "abc123"))  # <re.Match object; span=(3, 6), match='123'>