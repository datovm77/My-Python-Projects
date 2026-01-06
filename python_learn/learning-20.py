
def list_while_func():
    mylist = [1,'lover',True,'lover']
    index = 0
    while index < len(mylist):
        element = mylist[index]
        print(f"列表的元素:{element}")
        index += 1

def list_for_func():   #更加简单
    mylist = [1,'lover',True,'lover']
    for element in mylist:
        print(f"列表的元素:{element}")



list_while_func()
print("---------------------         ")
list_for_func()