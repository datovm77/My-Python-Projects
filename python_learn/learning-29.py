#文件的操作
import time
#打开文件
f = open("D:/test.txt","r",encoding="utf-8")
print(type(f))
#read(num)方法--------num表示要读取字节的长度，如果不填，则读取文件中的所有的数据
#readline方法---------所有元素一次性读取，返回列表，一行一个元素
# print(f"{f.read(12)}")
# print(f"{f.read()}")   #读取位置开始的位置是上一次结束的位置

# line = f.readlines()
# print(f"{line}")
# print(f"{type(line)}")

# line1 = f.readline()  #一次读取一行
# line2 = f.readline()
# line3 = f.readline()
#
# print(f"{line1}")
# print(f"{line2}")
# print(f"{line3}")

for line in f:
    print(f"{line}")

#time.sleep(500000)  括号内为秒
f.close()   #关闭文件

#with open可以在执行完成后自动关闭close文件
# with open("D:/test.txt","r",encoding="utf-8") as f1:
#     for line in f1:
#         print(f"{line}")




