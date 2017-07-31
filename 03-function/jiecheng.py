def p(n):
    if n==1 or n==0:
        return 1
    else:
        return n*p(n-1)

n=int(input("请输入一个整数："))

print(n,"!的值为：",p(n))