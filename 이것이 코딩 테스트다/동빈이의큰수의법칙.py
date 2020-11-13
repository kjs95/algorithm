n,m,k = map(int,input().split())
num = list(map(int,input().split()))

num.sort()

end = num[-1]
endend = num[-2]

q = m // (k+1)

r = m % (k+1)
result = (end*k + endend) *q + end*r
print(result)

