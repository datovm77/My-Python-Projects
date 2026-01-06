def my_decorator(func):
    def wrapper(*args, **kwargs):
        # *args, **kwargs 接收任意参数
        print("函数执行前")
        
        # 调用原函数并保存返回值
        result = func(*args, **kwargs)
        
        print("函数执行后")
        return result  # 返回原函数的返回值
    
    return wrapper

@my_decorator
def greet(name):
    print(f"你好, {name}!")
    return "完成"

# 调用
result = greet("小明")
# 输出:
# 函数执行前
# 你好, 小明!
# 函数执行后