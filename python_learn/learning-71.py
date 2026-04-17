import re

text = """
请联系以下邮箱：
张三: zhangsan@company.com
李四: lisi_01@gmail.com
王五: wangwu@pku.edu.cn
客服: support@my-company.org
"""

# 简单版邮箱正则
pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
emails = re.findall(pattern, text)
for email in emails:
    print(email)
# zhangsan@company.com
# lisi_01@gmail.com
# wangwu@pku.edu.cn
# support@my-company.org