'''
take the number to get its fib 
'''
def fib(n):
    if n == 1:
        return 0
 

    elif n == 2 or n == 3:
        return 1
 
    else:
        return fib(n-1) + fib(n-2)
 
n = int(input())
print(fib(n))