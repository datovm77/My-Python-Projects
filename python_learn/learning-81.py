class MobilePhone:
    """手机类"""
    def __init__(self, brand, price, battery=100):
        self.brand = brand          # 品牌
        self.price = price          # 价格
        self.battery = battery      # 电量百分比
        self.is_on = False          # 是否开机（默认关机）
    
    def power_on(self):
        if self.is_on:
            print(f"{self.brand}手机已经是开机状态了")
        else:
            self.is_on = True
            print(f"{self.brand}手机已开机 ✓")
    
    def power_off(self):
        if not self.is_on:
            print(f"{self.brand}手机已经是关机状态了")
        else:
            self.is_on = False
            print(f"{self.brand}手机已关机")
    
    def use(self, hours):
        if not self.is_on:
            print("手机未开机，请先开机！")
            return
        cost = hours * 10   # 每小时消耗10%电量
        if cost > self.battery:
            print(f"电量不足！当前电量{self.battery}%，最多还能用{self.battery/10}小时")
        else:
            self.battery -= cost
            print(f"使用了{hours}小时，剩余电量{self.battery}%")
    
    def show_status(self):
        status = "开机" if self.is_on else "关机"
        print(f"【{self.brand}】 价格:{self.price}元 | 电量:{self.battery}% | 状态:{status}")


# ========= 使用 =========
phone = MobilePhone("华为", 4999)
phone.show_status()        # 【华为】 价格:4999元 | 电量:100% | 状态:关机
phone.use(2)               # 手机未开机，请先开机！
phone.power_on()           # 华为手机已开机 ✓
phone.use(3)               # 使用了3小时，剩余电量70%
phone.use(5)               # 使用了5小时，剩余电量20%
phone.use(3)               # 电量不足！当前电量20%，最多还能用2.0小时
phone.show_status()        # 【华为】 价格:4999元 | 电量:20% | 状态:开机