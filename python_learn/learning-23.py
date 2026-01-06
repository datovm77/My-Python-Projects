#列表使用： []————list
#元组使用：()————tuple
#字符串使用：""————str
#集合使用: {} ——————set   empty_set = set()

#字典:通过一个特征找到一个元素
#定义： {key: value,key: value,key: value,key: value}
#空字典：my_dict = {}         my_dict = dict()


my_dict = {"name":"GEM","age":30,"song":"aniy"}
my_dict2 = {}
my_dict3 = dict()
print(f"字典1内容是{my_dict}，类型是：{type(my_dict)}")
print(f"字典2内容是{my_dict2}，类型是：{type(my_dict2)}")
print(f"字典3内容是{my_dict3}，类型是：{type(my_dict3)}")
#用key获取value
my_dict = {"name":"GEM","age":30,"song":"aniy"}
score = my_dict["name"]
print(f"通过name获取的value是{score}")



