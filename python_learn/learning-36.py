#json：特定格式的字符串
#字典
#嵌套字典的列表
import json
data = [{"name":"邓紫棋","age":18},{"name":"zahngsan","age":28},{"name":"lisi","age":38}]

json_str = json.dumps(data,ensure_ascii=False) #如果有中文，后面这一个要加上
print(type(json_str))
print(json_str)

dict = {"name" : "周杰伦", "addr" : "台北"}
json_str = json.dumps(dict,ensure_ascii=False)
print(type(json_str))
print(json_str)

#字符串重新转换为列表
s = '[{"name": "邓紫棋", "age": 18}, {"name": "zahngsan", "age": 28}, {"name": "lisi", "age": 38}]'
print(type(s))  #<class 'str'>
list = json.loads(s)
print(type(list)) #<class 'list'>

