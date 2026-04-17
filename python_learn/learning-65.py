import re

# * : 0次或多次
print(re.findall(r"go*d", "gd god good goood"))
# ['gd', 'god', 'good', 'goood']

# + : 1次或多次
print(re.findall(r"go+d", "gd god good goood"))
# ['god', 'good', 'goood']   （gd 不匹配，因为至少要1个o）

# ? : 0次或1次
print(re.findall(r"colou?r", "color colour"))
# ['color', 'colour']   （u出现0次或1次都行）

# {n} : 恰好n次
print(re.findall(r"\d{3}", "1 12 123 1234"))
# ['123', '123']   （1234中的前3位也匹配）

# {n,m} : n到m次
print(re.findall(r"\d{2,4}", "1 12 123 1234 12345"))
# ['12', '123', '1234', '1234']