# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

index = 0
for i in range(1, n):
    if a[i] > a[index]:
        index = i
a[index], a[n-1] = a[n-1], a[index]
index = 0
for i in range(1, n-1):
    if a[i] > a[index]:
        index = i
a[index], a[n-2] = a[n-2], a[index]
result = a[n-2] * a[n-1]
print(result)