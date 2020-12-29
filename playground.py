def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(b)
        a, b = b, a + b 
    return b

# print(fib(5))
print(fib(15))