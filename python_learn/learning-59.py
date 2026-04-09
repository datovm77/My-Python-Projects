name = "Python"
print(f"|{name:<20}|")   # |Python              | 左对齐，宽度20
print(f"|{name:>20}|")   # |              Python| 右对齐
print(f"|{name:^20}|")   # |       Python       | 居中
print(f"|{name:*^20}|")  # |*******Python*******| 居中，用*填充
print(f"|{name:-<20}|")  # |Python--------------| 左对齐，用-填充