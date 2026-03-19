#此段程序为循环读入测试数据到列表ls中，阅读但不要修改

ls=[ ]				#创建列表ls
item=input()		#读入第一个测试数据
while item!="end":	#判断是否结尾
    ls.append(item)	#加入到ls中
    item=input()	#再读一个数据    

####   begin，请在此编程实现功能   ##
ls2 = ['tom','jack','山东','北京']
for i in ls2:
    ls.append(i)

index = 50
while index<=100:
    if index%7==0:
        ls.append(index)
    index = index + 1


print (ls,end='')
####  end    #########