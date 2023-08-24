# Uses python3
#def calc_fib(n):
    #if (n <= 1):
        #return n

    #return calc_fib(n - 1) + calc_fib(n - 2)

#n = int(input())
#print(calc_fib(n))

n = int(input())
fibArray=[0 for x in range(n)]
if (n <= 1):
    print(n)
else:   
    fibArray[0]=1
    fibArray[1]=1
    for i in range(2,n):
        fibArray[i]=fibArray[i-1] + fibArray[i-2]
    print(fibArray[n-1])