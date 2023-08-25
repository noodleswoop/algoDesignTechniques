# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    #capacity consists of the max capacity of the knapsack
    #weights is an array of length n
    #values is an array of length n
    
    #FIRST: need to find value[i] / weight [i] to find the price per pound
    perPoundIndex=[] #will also be array of length n
    
    for i in range(len(weights)):
        weight=weights[i]
        val=values[i]
        pricePerPound = val/weight
        index = i
        poundIndex = [pricePerPound, index]
        perPoundIndex.append(poundIndex)

    #SECOND: need to find out which value is the highest in pricePerPound.
    #don't want to rearrange things bc index position matters
    perPoundIndex.sort(reverse=True)
    
    #THIRD: need to find out how many items we can fit in the sack starting w most valuable.
    for i in range(len(perPoundIndex)):
        weightValIndex=perPoundIndex[i][1]
        weightItem=weights[weightValIndex] #pulls the weight of the most valuable item in line from the array
        if weightItem <= capacity:
            capacity = capacity - weightItem
            value+=values[weightValIndex]
        elif weightItem > capacity:
            multiplier=capacity/weightItem
            value+=(multiplier*values[weightValIndex])
            break
    
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
