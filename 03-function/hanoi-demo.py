def hanoi(n,A,B,C):
    if n==1:
        print("移动盘子{0},从{1}到{2}".format(n,A,C))
    else:
        hanoi(n-1,A,C,B)
        print("移动盘子{0},从{1}到{2}".format(n,A,C))
        hanoi(n-1,B,A,C)

n=int(input("请输入一个整数："))
hanoi(n,"左","中","右")