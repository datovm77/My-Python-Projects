import re

# 按多种分隔符分割
text = "苹果,香蕉;橘子 西瓜|葡萄"
result = re.split(r"[,;| ]+", text)
print(result)  # ['苹果', '香蕉', '橘子', '西瓜', '葡萄']

# 对比字符串的split：只能按固定字符分割
print(text.split(",;| "))  # ['苹果', '香蕉;橘子 西瓜|葡萄']  只能按逗号