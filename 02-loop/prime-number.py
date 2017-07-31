import math

num = int(input("输入一个数字："))

for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
        print("该数字不是一个素数")
        break
else:
    print("该数字是一个素数")
