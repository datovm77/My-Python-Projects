##range(num),获取从0开始，到num结束(不包含num）的数字序列
##range(num1，num2),获取从num1开始，到num2结束(不包含num2）的数字序列
##range(num1，num2,step),获取从num1开始，到num2结束(不包含num2）间隔为2的数字
# range(5,10,2)  ##5，7，9
#
# for x in range(5):
#     print(x,end=' ')
# print(" ")
# for i in range(5,10):
#     print(i,end = ' ')
# print(" ")
# for i in range(5,10,2):  ##数字间隔为2
#     print(i,end = ' ')
count = 0
for x in range(1,100):
    if x % 2 == 0:
        count+=1
print(count)