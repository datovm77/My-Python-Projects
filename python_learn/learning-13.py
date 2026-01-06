##函数的嵌套调用
def func_b():
    print("------2------")
def func_c():
    print("------3------")
    func_b()
    print("------4------")
##调用 
func_c()