class Student:
    """定义学生类，用于记录学生信息"""
    def __init__(self, name, age, address):
        self.name = name       # 姓名
        self.age = age         # 年龄
        self.address = address # 地址

# 定义需要录入的总人数（题目要求是10位）
total_students = 3

# 使用 for 循环进行录入，range(1, 11) 会产生 1 到 10 的数字
for i in range(1, total_students + 1):
    # 打印当前的头部提示信息
    print(f"当前录入第{i}位学生信息，总共需录入{total_students}位学生信息")
    
    # 配合 input 输入语句获取信息
    input_name = input("请输入学生姓名：")
    input_age = input("请输入学生年龄：")
    input_address = input("请输入学生地址：")
    
    # 使用构造方法创建学生对象 (实例化)
    stu = Student(input_name, input_age, input_address)
    
    # 输入完成后，使用 print 语句输出指定格式的信息
    print(f"学生{i}信息录入完成，信息为：【学生姓名: {stu.name}, 年龄: {stu.age}, 地址: {stu.address}】")
    print("-" * 20) # 打印一条分隔线，让显示更清晰（可选）