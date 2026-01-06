#类的定义与使用 
#类的属性：变量（数据）
#类的行为：函数

class Student:
    name = None
    age = None

    def say_hi(self):
        print(f"hi,我是{self.name}")

stu1 = Student()
stu1.name = "周杰伦"
stu1.say_hi()








