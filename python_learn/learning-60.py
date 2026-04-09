score = 85
result = f"成绩：{score}分，{'及格' if score >= 60 else '不及格'}"
print(result)  # 成绩：85分，及格

s = "分割"
print(f"{s:*^20}")
# 在循环中使用
students = [("小明", 92), ("小红", 55), ("小刚", 78)]
for name, score in students:
    print(f"{name}: {score:3d}分 - {'✓ 及格' if score >= 60 else '✗ 不及格'}")
# 小明:  92分 - ✓ 及格
# 小红:  55分 - ✗ 不及格
# 小刚:  78分 - ✓ 及格