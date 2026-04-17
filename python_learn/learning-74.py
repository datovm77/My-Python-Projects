import re

def clean_text(raw_text):
    """
    文本清洗函数：
    1. 去除首尾空白
    2. 去除HTML标签
    3. 合并多余空白
    4. 去除特殊符号（保留中英文、数字、空格和常见中英文标点）
    5. 再次清理首尾空白
    """
    text = raw_text
    
    # 第1步：去除首尾空白
    text = text.strip()
    print(f"去除首尾空白：{text!r}")
    
    # 第2步：去除HTML标签
    text = re.sub(r"<[^>]+>", "", text)
    print(f"去除HTML标签：{text!r}")
    
    # 第3步：将多个空白字符替换为单个空格
    text = re.sub(r"\s+", " ", text)
    print(f"合并空白字符：{text!r}")
    
    # 第4步：去除特殊符号（保留常见中英文标点）
    text = re.sub(r"[^\w\s\u4e00-\u9fff,.!?，。！？、；：:;()（）-]", "", text)
    print(f"去除特殊符号：{text!r}")
    
    # 第5步：去除首尾可能多余的空格
    text = text.strip()
    
    return text


# 测试
raw = """
   <p>  Hello,   World!!!  </p>
   <br/>这是一个@#$测试文本~~~  
   <b>包含各种   乱七八糟的   格式</b>   
"""

result = clean_text(raw)
print(f"\n最终结果：{result}")