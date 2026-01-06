# def say_hello():
#     print("Hello")
#     return None
#
#
#
# resulr = say_hello()
# print(f"返回的内容是{resulr}")##返回的内容是None
# print(f"返回的内容的类型是{type(resulr)}")##返回的内容的类型是<class 'NoneType'>

def age_check(age):
    if age >= 18:
        return True
    else:
        return False

result = age_check(16)
if not result:
    print("你的年龄小于18")