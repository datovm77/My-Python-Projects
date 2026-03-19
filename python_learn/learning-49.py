#此段程序为循环读入测试数据到列表ls中，阅读但不要修改

ls=[ ]                #创建列表ls
item=input()        #读入第一个测试数据
while item!="end":    #判断是否结尾
    ls.append(int(item))    #加入到ls中
    item=input()    #再读一个数据    

####   begin，请在此编程实现功能   ##
ls1 = []
for i in ls:
    flag = 1
    for j in ls1:
        if (i==j):
            flag = 0
            break
    if flag:
        ls1.append(i)


print (ls1,end='')
####  end    #########