# buble sort
a = [1,7,3,4,5]

for i in range(1,len(a) - 1): 
  for j in range(i + 1,len(a)): 
    if a[i] > a[j]:
      tmp = a[i]
      a[i] = a[j]
      a[j] = tmp


print(a)
# a = [1,3,4,5,7]