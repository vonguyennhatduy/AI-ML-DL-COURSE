
# tìm vị trí phần tử có giá trị bằng giá trị x cho trước bằng binarysearch
# a = [1,2,3,4,5,6,7,8,9,10]
a = list(map(int, input().split())) 
x = int(input()) #nhập giá trị x cần tìm
l = 0
r = len(a) - 1

def binary_search (a,l,r,x):
    while l <= r: 
        mid = (l + r) // 2
        if a[mid] == x: 
            return mid + 1
        elif a[mid] < x: 
            l = mid + 1
        else: r = mid - 1

    return "khong tim thay"



print(binary_search(a,l,r,x))