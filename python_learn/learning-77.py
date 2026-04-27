class Dog:
    """这是一个狗类"""
    # 属性（描述特征）
    name = ""
    age = 0
    breed = ""     # 品种
    
    # 方法（描述行为）
    def bark(self):
        print(f"{self.name}在叫: 汪汪汪！")
    
    def eat(self, food):
        print(f"{self.name}正在吃{food}")
    
    def show_info(self):
        print(f"名字: {self.name}, 年龄: {self.age}岁, 品种: {self.breed}")


# ============ 第二步：创建对象（实例化） ============
dog1 = Dog()     # 创建第一个对象
dog2 = Dog()     # 创建第二个对象
dog3 = Dog()     # 创建第三个对象


# ============ 第三步：给对象赋予属性值 ============
dog1.name = "旺财"
dog1.age = 3
dog1.breed = "中华田园犬"

dog2.name = "Lucky"
dog2.age = 2
dog2.breed = "金毛"

dog3.name = "豆豆"
dog3.age = 1
dog3.breed = "泰迪"


# ============ 第四步：使用对象 ============
dog1.show_info()      # 名字: 旺财, 年龄: 3岁, 品种: 中华田园犬
dog2.show_info()      # 名字: Lucky, 年龄: 2岁, 品种: 金毛
dog3.bark()           # 豆豆在叫: 汪汪汪！
dog2.eat("骨头")      # Lucky正在吃骨头