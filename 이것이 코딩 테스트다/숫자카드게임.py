n,m = map(int,input().split())


value = 0
for i in range(n):
    arr = list(map(int, input().split()))

    minvalue = min(arr)
    value = max(minvalue, value)

print(value)




