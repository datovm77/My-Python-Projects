# coding=utf-8

##本关的编程任务是补全src/Step1/guests.py文件的代码，实现相应的功能。具体要求如下：

# step 1：将guests列表末尾的元素删除，并将这个被删除的元素值保存到deleted_guest变量；

# step 2：将deleted_guest插入到 step 1 删除后的guests列表索引位置为2的地方；

# step 3：将 step 2 处理后的guests列表索引位置为1的元素删除；

# 打印输出 step 1 的deleted_guest变量；

# 打印输出 step 3 改变后的guests列表。

# 创建并初始化Guests列表
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
# 请在此添加代码，对guests列表进行插入、删除等操作
########## Begin ##########
deleted_guest = guests.pop()

guests.insert(2,deleted_guest)

del guests[1]

print(deleted_guest)
print(guests)
########## End ##########
