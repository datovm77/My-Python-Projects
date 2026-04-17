import re

text = "项目开始日期2026-04-09，截止日期2026/12/31，备注日期20261231"

# 匹配 YYYY-MM-DD 或 YYYY/MM/DD 格式
dates = re.findall(r"\d{4}[-/]\d{2}[-/]\d{2}", text)
print(dates)  # ['2026-04-09', '2026/12/31']

# 提取年月日
for d in dates:
    match = re.search(r"(\d{4})[-/](\d{2})[-/](\d{2})", d)
    print(f"年:{match.group(1)} 月:{match.group(2)} 日:{match.group(3)}")
# 年:2026 月:04 日:09
# 年:2026 月:12 日:31