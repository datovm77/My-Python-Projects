#异常捕获
# try:
#     可能出现错误的代码
# except:
#     如果出现异常执行的代码
# try:
#     f = open("D:/aaa.txt","r",encoding = "UTF-8")
# except:
#     f = open("D:/aaa.txt","w",encoding = "UTF-8")

# #捕获指定异常
# try:
#     print(name)
# except NameError as e:
#     print("出现变量未定义的异常")
#     print(e)


#捕获多个异常
# try:
#     #1/0
#     print(age)
# except(NameError,ZeroDivisionError) as e:
#     print("有错")
#     print(e)

#没有异常运行else 
# try:
#     #1/0
#     #print(age)
#     print("hello")
# except(NameError,ZeroDivisionError) as e:
#     print("有错")
#     print(e)
# else:
#     print("没有异常")

#无论有没有异常，都要运行
# try:
#     #1/0
#     #print(age)
#     print("hello")
# except(NameError,ZeroDivisionError) as e:
#     print("有错")
#     print(e) 
# else:
#     print("没有异常")
# finally:
#     f.close()#可以用于关闭程序




