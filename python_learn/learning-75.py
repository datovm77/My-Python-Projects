import re

def clean_phone_numbers(raw_data):
    """
    从杂乱的文本中提取并标准化手机号
    """
    # 先去除所有的空格、横线、括号
    cleaned = re.sub(r"[\s\-\(\)（）]", "", raw_data)
    
    # 提取11位手机号
    phones = re.findall(r"1[3-9]\d{9}", cleaned)
    
    # 去重并保持顺序
    seen = set()
    unique_phones = []
    for p in phones:
        if p not in seen:
            seen.add(p)
            unique_phones.append(p)
    
    return unique_phones


raw_data = """
联系人列表：
张三: 138-0013-8000
李四: (139) 0013 9000
王五: 138 0013 8000   (和张三相同)
赵六: 15012345678
孙七: 010-88886666 (座机不要)
"""

phones = clean_phone_numbers(raw_data)
for i, phone in enumerate(phones, 1):
    print(f"手机号{i}: {phone}")
# 手机号1: 13800138000
# 手机号2: 13900139000
# 手机号3: 15012345678