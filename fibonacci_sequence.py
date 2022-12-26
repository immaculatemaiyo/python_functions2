def fibonacci(n: int):
    if n < 0:
        print('incorrect input')
    elif n==0:
        return 0
    elif n == 1 or n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(n=-2))
print(fibonacci(n=0))
print(fibonacci(n=1))
print(fibonacci(n=2))
print(fibonacci(n=5))
print(fibonacci(n=9))