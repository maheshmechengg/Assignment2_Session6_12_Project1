# Code for fibonacci
#def fib(n):    # write Fibonacci series up to n
#    n1, n2 = 0, 1
#    while n2 < n:
#        print(n2)
#        n1, n2 = n2, n1+n2

def fib2(n): # return Fibonacci series up to n
    fibseris = []
    n1, n2 = 0, 1
    while n2 < n:
        fibseris.append(n2)
        n1, n2 = n2, n1+n2
    return fibseris