class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        # 验证逻辑：余额不能为负数
        if balance < 0:
            print("警告：初始余额不能为负数，已自动设为0")
            self.balance = 0
        else:
            self.balance = balance
        # 还可以在构造方法中生成其他属性
        self.account_id = f"ACC-{id(self) % 10000:04d}"
        print(f"账户 {self.account_id} 已创建，户主: {self.owner}")

acc1 = BankAccount("张三", 1000)
# 输出：账户 ACC-XXXX 已创建，户主: 张三

acc2 = BankAccount("李四", -500)
# 输出：警告：初始余额不能为负数，已自动设为0