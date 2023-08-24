# Uses python3
import sys

def get_change(m):
    numTens = int(m/10)
    newM = m - (numTens*10)
    numFives = int(newM/5)
    numOnes = newM - (numFives*5)
    total = numTens + numFives + numOnes
    return total
    

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))