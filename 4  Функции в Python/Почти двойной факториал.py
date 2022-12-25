def almost_double_factorial(n):
    factorial = 1
    if n == 0:
        return 1
    elif n > 0:
        for i in range(1,n+1,2):
            factorial = factorial * i
    return factorial
