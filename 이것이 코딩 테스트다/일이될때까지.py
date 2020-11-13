
n,k = map(int,input().split())
# count = 0
# while n != 1:
#
#
#     if n % k == 0:
#         n = n // k
#     else:
#         n -= 1
#     count += 1
#
# print(count)

count = 0
while n > k:

    r = n%k
    if r == 0:
        n = n // k
        count += 1
    else:
        n -= r
        count += r


if n != 1:
    count += (n-1)
print(count)