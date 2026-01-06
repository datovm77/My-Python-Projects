#其他内置方法  之前学的：  __init__
"""
__init__    构造方法
__str__     字符串方法
__lt__      小于 大于符号比较
__le__      小于等于 大于等于符号比较
__eq__      ==符号比较

"""

#__str__
class Student:
    def __init__(self,name,age,age1):
        self.name = name
        self.age = age
        self.age1 = age1

    #__str__
    def __str__(self):
        return f"Student类对象,name:{self.name}, age:{self.age}"

    # __lt__
    def __lt__(self,other):
        return self.age < other.age  #返回Ture或者False
    # __lt__
    def __lt__(self,other):
        return self.age1 < other.age1  #返回Ture或者False
stu1 = Student("邓紫棋",34,35) 
stu2 = Student("邓紫",35,34)
# print(stu1)
#print(stu1)
# print(stu1.name)
#print(str(stu1))
print(stu1 < stu2)