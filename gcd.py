# Uses python3

a,b = input().split()
a = int(a)
b = int(b)
c = 0

if a < b:
    c = a
    a = b
    b = c

r = 1
while r != 0:
    r = a % b
    a = b
    b = r
    
print(a)