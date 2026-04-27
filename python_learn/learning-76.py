import sys

for line in sys.stdin:                    # 持续读取每一行，直到 EOF
    chars = line.split()                  # 按空格切分，得到三个字符的列表
    chars.sort()                          # 原地排序（按 ASCII 码值升序）
    print(' '.join(chars)) 