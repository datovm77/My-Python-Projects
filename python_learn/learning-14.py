##变量的作用域:
##局部变量与全局变量，局部变量一般是函数内的变量


##内部定义全局变量
num = 200

def tesst():
    global num
    num = 201
    print(f"函数内的num为{num}")
print(num)  ##由于函数内用global,num变成201