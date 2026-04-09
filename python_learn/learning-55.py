###begin
num = input()
length = len(num)
print(length)
num_int = int(num)
num_fl = float(num)

print(f"{num_int} {num_int:o} {num_int:x}")
print(f"{num_fl:.6} {num_fl:e}")
print(f"The number {num} in hex is: {num_int:#x}, the number {num} in oct is {num_int:#o}")






###end