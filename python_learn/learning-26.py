def user_info(name,age,gender):
    print(f"姓名是{name},年龄是{age},性别是{gender}")
#位置参数（调用函数）
user_info('小明',20,'男')

#关键字参数（调用函数）
user_info(name = '小明',age = 20,gender = '男')

 