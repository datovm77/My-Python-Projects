#列表常见的操作方法
mylist = [1,'lover',True,'lover']
#查找元素内的下标索引
index = mylist.index("lover")
print(index)
#插入元素
mylist.insert(1,"get everybody moving")
print(mylist)

#追加元素
mylist.append("llllkkkk")
mylist2 = [1,2,3]

mylist.extend(mylist2)  #追加多个元素
print(mylist)
#删除元素
   #1.通过下标
mylist = [1,'lover',True,'lover']
del  mylist[1]
print(f"列表删除元素后结果是{mylist}")
mylist = [1,'lover',True,'lover']
element = mylist.pop(1)  #可以返回删除后的元素
print(f"列表删除元素后结果是{mylist}")
   #2. 通过元素:只是删除第一个匹配项
mylist = [1,'lover',True,'lover']
mylist.remove('lover')
print(f"列表删除元素后结果是{mylist}")

#清空列表元素
mylist.clear()
print(f"列表被清了后结果是{mylist}")
#修改元素
mylist = [1,'lover',True,'lover']
mylist[1] = 'taylor'  ##修改
print(mylist[1])
#统计某个元素个数
mylist = [1,'lover',True,'lover']
count = mylist.count('lover')
print(f"列表中的‘lover’元素个数为{count}个")

#统计列表总共元素个数
length = len(mylist)
print(f"列表中的所有元素个数为{length}个")
