#单词计数
f = open("D:/test.txt","r",encoding="UTF-8")

# #一次性读取全部内容
# content = f.read()      #得到字符串
# #print(type(content))
# count = content.count("Give")
# print(f"Give一共出现了{count}次")

#一行行读取
count = 0
for line in f:
    line = line.strip()   #变成列表（多个元素
    words = line.split(" ")
    #print(words)
    for word in words:    #遍历列表中的一个个元素
        if word == "Give":
            count += 1

print(f"Give出现的次数是{count}")







f.close()