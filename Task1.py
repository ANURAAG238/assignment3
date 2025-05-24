def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=input('enter a number: ')
print("factorial of ",n," is: ",factorial(int(n)))
