

# jump search 
# tìm vị trí của x trong a 

import math

a = list(map(int, input().split())) 
x = int(input())


def jumpSearch (a, x, n): 
    block = math.sqrt(n)

    tmp = 0
    while a[int(min(block,n) - 1)] < x: 
        tmp = block
        block += math.sqrt(n)
        if tmp >= n: 
            return -1
        
    while a[int(tmp)] < x:
        tmp += 1

        if tmp == min(block,n) : 
            return -1
    
    if a[int(tmp)] == x:
        return int(tmp)

    return -1 # không tìm thấy 



n = len(a)
print(jumpSearch(a,x,n))
