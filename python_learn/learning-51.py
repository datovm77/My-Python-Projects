list1 = [6,9,12,3,5,8,1,8,131,58,1,581,31,8,46,13,8,4,613,30,546,0,68,4,1,3,16,99,61,-102,-290,116.5,165,-2.3]

list2 = []
for i in list1:
    list2.append(i)

list2.sort(reverse=True)

print(f"原列表为：{list1}")
print(f"复制后的原列表为：{list2}")
