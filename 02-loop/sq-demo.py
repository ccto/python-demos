x = float(input('请输入数字'))
low = 0
hight = x
guess = (low + hight) / 2

while abs(guess**2 - x) > 1e-5:
    if guess**2 < x:
        low = guess
    else:
        hight = guess
    guess = (low + hight) / 2

print("平方根是：", guess)
