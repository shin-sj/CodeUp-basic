n = int(input()) 
a = input().split()

for i in range(n) : 
    a[i] = int(a[i])
min = a[0]

for i in range(n-1, -1, -1) :
    if a[i] < min :
        min = a[i]

print(min)