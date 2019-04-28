

import time

myFib=[None] * 100
def fib(n):
    if myFib[n] is not None:
        #print(n)
        return myFib[n]
    if n==1 or n==2:
        return 1

    else:
        myFib[n]= fib(n-1) + fib(n-2)
        return (fib(n-1) + fib(n-2))
        
start = time.time()
"the code you want to test stays here"
      
x=fib(20)
end = time.time() 

print(end - start)
print(x)


def fib2(n):
    if n<=1:
        return n
    else:
        return (fib2(n-1) + fib2(n-2))
        
start = time.time()
"the code you want to test stays here"
      
x=fib2(20)
end = time.time() 

print(end - start)
print(x)
