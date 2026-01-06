#元组
#特点：一旦定义完成，就不可以修改。使用小括号定义，逗号隔开
"""
定义元组字面量
(元素，元素，元素)

定义元组变量
元组变量 = (元素，元素，元素)

定义空元组
变量名 = ()
变量名称 = tuple()

"""
my_tp = (1,'lover',True,'lover')
my_tp1 = ()
my_tp2 = tuple()
print(f"my_tp的类型是{type(my_tp)}")
print(f"my_tp1的类型是{type(my_tp1)}")
print(f"my_tp2的类型是{type(my_tp2)}")

#一.定义一个元素的元组

#如果后面不加括号
my_tp3 = ("love")
print(f"my_tp3的类型是{type(my_tp3)},内容是{my_tp3}")

#正确的定义一个元素的元组的方式
my_tp4 = ("lover",)
print(f"my_tp4的类型是{type(my_tp4)},内容是{my_tp4}")
#二.定义嵌套元组
my_tp5 = ((1,2),(5,6))
print(f"my_tp5的类型是{type(my_tp5)},内容是{my_tp5}")

#用下表索引取出元素
num = my_tp5[1][1]
print(f"从嵌套元组中取出的数据是:{num}")

my_tp6 = ("love","邓紫棋","llloooovvveee")
index = my_tp6.index("邓紫棋")
print(f"在元组my_tp6中查找邓紫棋,的下表是{index}")

my_tp7 = ("love","love","邓紫棋","llloooovvveee")
num = my_tp7.count("love")
print(f"在元组中查找love元素的个数,个数有{num}个")

my_tp8 = ("love","love","邓紫棋","llloooovvveee")
length = len(my_tp8)
print(f"元组中元素的个数,有{length}个")

#元组不可以修改，但是里面嵌套的list可以修改


