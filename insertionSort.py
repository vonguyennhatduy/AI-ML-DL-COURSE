

a = list(map(int, input().split()))

n = len(a)

for i in range(1,n): 
    pivot = a[i]
    idx = i - 1

    while idx >= 0 and a[idx] > pivot: 
        a[idx + 1] = a[idx]
        idx = idx - 1

    a[idx + 1] = pivot


print(a)


