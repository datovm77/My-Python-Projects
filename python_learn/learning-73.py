import re

html = "<title>Python教程</title><p>这是一个段落</p><a>链接文字</a>"

# 提取所有标签中的文字
contents = re.findall(r"<\w+>(.*?)</\w+>", html)
print(contents)  # ['Python教程', '这是一个段落', '链接文字']

# 同时提取标签名和内容
pairs = re.findall(r"<(\w+)>(.*?)</\1>", html)
print(pairs)  # [('title', 'Python教程'), ('p', '这是一个段落'), ('a', '链接文字')]
# \1 是反向引用，表示和第1个分组匹配的内容一致