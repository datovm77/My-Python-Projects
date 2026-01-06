#构造方法
class Student:
    # name = None
    # age = None
    # tel = None    有了下面这个函数，这个可以省略

    def __init__(self,name,age,tel):    #自动运行
        self.name = name
        self.age = age
        self.tel = tel
        print("Student创建了一个对象")

stu1 = Student("邓紫棋",34,1341471)
print(stu1.name)
print(stu1.age)
print(stu1.tel)

print(stu1)