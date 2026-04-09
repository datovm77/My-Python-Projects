# coding=utf-8

# 存放姓氏和名字的变量
first_name = input()
last_name = input()

# 请在下面添加字符串拼接的代码，完成相应功能
########## Begin ##########
##ls = [first_name,last_name]

ls = []
ls.append(first_name)
ls.append(last_name)
print(*ls,sep=' ')


########## End ##########