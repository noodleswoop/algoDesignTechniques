#Uses Python3
import sys

def lastDigit_fibSum(n):
    if n <= 1:
        return n
    
    fibArray = [0 ,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041]
    index = (n+2)%60
    lastDigit = fibArray[index] - 1
    return lastDigit % 10
    
if __name__ == '__main__':
    input = sys.stdin.read();
    n = int(input)
    print(lastDigit_fibSum(n))

#make an array of the first 60 fibonacci numbers
#find n % 60
#and then add 2 to that; that is the index in the array u need to search
#pull that number, subtract 1, find the last digit of that and BOOM
#this is very fast: O(1)
#memory difference of 60 fibs vs 60 last digit fibs is negligible
