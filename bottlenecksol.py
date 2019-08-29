n = int(input())
radius = input().split() # list(map(int,input().split()))
for i in range(n):
    radius[i] = int(radius[i])

list =[]
for i in range(n):
    a = radius.count(radius[i])
    list.append(a)
print(max(list))


