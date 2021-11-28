def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(b)
        a, b = b, a + b 
    return b

# print(fib(5))
# print(fib(15))

def factorial(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    return num*factorial(num-1)

print(factorial(3))