#字符串：字符的容器，不可修改
name = "lovegem"

#通过索引获取字符
value = name[2]
value2 = name[-5]
print(f"获取的元素{value}")
print(f"获取的元素{value2}")

#index的方法
index = name.index("v")
print(f"v在字符串的索引是{index}")

#字符串的替换:replace
new_name = name.replace("love","veryverylove")
print(f"替换后得到的字符串为{new_name}")

#字符串的分割  
name = "gem will forever young"
name_list = name.split(" ")
print(f"字符串{name}切割后得到{name_list}，类型是{type(name_list)}")

#strip方法 ---也可以用来去除\n
name = "   gem will forever young   "
new_name = name.strip()
print(f"strip后的字符串是{new_name}")

name = "012gem will forever young210"
new_name = name.strip("120")
print(f"strip后的字符串是{new_name}")

#统计某个字符的出现次数
name = "12gem will forever young21"
count = name.count('o')
count1 = name.count('forever')
print(f"字母o在字符串出现的次数为{count }")
print(f"字母forever在字符串出现的次数为{count1}")

#统计长度
name = " gem"
length = len(name)
print(f"长度为{length}")

#反转
def reverse_string(s):
    return s[::-1]
