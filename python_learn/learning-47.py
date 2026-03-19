ls=[ ]				#创建列表ls
item=input()		#读入第一个测试数据
while item!="end":	#判断是否结尾
    ls.append(item)	#加入到ls中
    item=input()	#再读一个数据  

begin = ls[0]
length = len(ls) - 1
end = ls[length]

ls[0] = end
ls[length] = begin

i=len(ls)-1        #获取ls1的最大下标
while i>=0:            #终止下标为0
    print(ls[i])    #逆序打印一个元素
    i=i-1            #下标减1


