num = int(input("请输入一个数字："))
num_temp = num
num_prime = 0

while num_temp != 0:

    num_prime = num_prime * 10 + num_temp % 10
    num_temp //= 10


if num == num_prime:
    print("数字", num, "是一个回文数")
else:
    print("数字", num, "不是一个回文数")
