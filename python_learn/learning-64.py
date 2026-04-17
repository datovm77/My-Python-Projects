numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 筛选偶数
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

ls = [x for x in numbers if x % 2 == 0]
print(ls)