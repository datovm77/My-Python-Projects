##获取键盘输入
## print("告诉我你是谁！！！")
name = input("告诉我你是谁！！！")
print(f"我知道了你的名字是{name}")

##数据类型转换
num = input("你的银行卡密码是：")   ##input的输出格式都为字符串
num = int(num)
print(f"你银行卡密码的数据类型是{type(num)}")