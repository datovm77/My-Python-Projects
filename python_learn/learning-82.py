class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

stu = Student("张三", 20)
print(stu)          # 输出：Student(name=张三, age=20)   ← 清晰多了！
print(str(stu))     # 输出：Student(name=张三, age=20)