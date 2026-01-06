money = 500000
## name = None

name = input("请输入您的姓名:")

def query(show_header):
    if show_header:
        print("------------查询余额--------------")
    print(f"{name},您好，你的余额为{money}")

def saving(num):
    global money
    money += num
    print("------------存款--------------")
    print(f"{name}，您好，您存款{num}元成功")

    query(False) ##不显示哪个查询余额

def get_money(num):
    global money
    money -= num
    print("------------取款--------------")

    query(False)  ##不显示哪个查询余额

def main():
    print("------------主菜单--------------")
    print(f"{name},您好，欢迎来到黑心银行ATM，请选择操作")
    print("查询余额[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入你的选择:")

while True:
    kb_input = main()
    if kb_input == "1":
        query(True)
        continue
    elif kb_input == "2":
        num = int(input("您像想要存多少钱？输入："))
        saving(num)
        continue
    elif kb_input == "3":
        num = int(input("您像想要取多少钱？输入："))
        get_money(num)
        continue
    else:
        print("欢迎下次再来！")
        break

