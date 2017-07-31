def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)



def fib_loop(n):
    if n==1 or n==2:
        return 1
    else:
        i=2
        f1=1
        f2=2
        while(i<n):
            f3=f1+f2
            f1=f2
            f2=f3
            i=i+1
        return f3

print(fib_loop(100))