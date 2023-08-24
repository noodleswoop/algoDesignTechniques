#Uses Python3
import sys

def lastDigit_fibSum(n):
    if n <= 1:
        return n
    
    sumVar=n+2
    fibArray=[0 for x in range(sumVar)]
    fibArray[0]=1
    fibArray[1]=1
    for i in range(2,sumVar):
        fibArray[i]=(fibArray[i-1] + fibArray[i-2])%10
    if fibArray[sumVar-1] == 0:
        return 9
    return (fibArray[sumVar-1]) - 1
    
if __name__ == '__main__':
    input = sys.stdin.read();
    n = int(input)
    print(lastDigit_fibSum(n))

#n = the nth fibonacci number
#in this case: m = 10; any number mod 10 will get u the last digit of that number
#S(n) = F(n+2) – 1
#which means: the sum of all fibonacci numbers until n is equal to the (n+2)th fib number minus 1
#so basically we need to calculate the last digit of the the (n+2)th fib number and subtract 1 from it
#note: if the last digit of the (n+2)th fib number is 0, the answer isn't negative 1, it's 9, so
#we need to include a provision for that