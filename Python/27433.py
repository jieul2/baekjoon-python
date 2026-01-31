import sys 
sys.setrecursionlimit(100)

#n! = n * (n-1)!
def factorial(number:int):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

number = int(input())
print(factorial(number))

