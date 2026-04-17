from functools import reduce

data = {
    "user": {
        "profile": {
            "name": "小明",
            "age": 25
        }
    }
}

def safe_get(d, key):
    """安全取键：只在字典上取值，缺失时返回 None"""
    return d.get(key) if isinstance(d, dict) else None

# 按路径取值（存在的路径）
keys1 = ["user", "profile", "name"]
result1 = reduce(safe_get, keys1, data)
print(result1)  # 输出：小明

# 按路径取值（不存在的路径）
keys2 = ["user", "profile", "email"]
result2 = reduce(safe_get, keys2, data)
print(result2)  # 输出：None（不会抛 KeyError）