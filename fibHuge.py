# Uses Python3
import sys

def get_hugeFib(n,m):
    if n <= 1:
        return n
    
    pisanoArray = [0,1]
    prevModulo = 0
    currentModulo = 1

    for i in range(n-1):
        #placeholder variable to store prevModulo
        placeModulo = prevModulo
        prevModulo = currentModulo % m
        currentModulo = (placeModulo + currentModulo) % m
        pisanoArray.append(currentModulo)
        if currentModulo == 1 and prevModulo == 0:
            pisanoLength = (n%(i+1))
            return pisanoArray[pisanoLength]
        
    return currentModulo

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_hugeFib(n,m))

#so: n divided by the length of the pisano period of m is equivalent to F(n) % m.