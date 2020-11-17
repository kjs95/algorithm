n = int(input())

x,y = 1,1

move = input().split()

movetype = ['U','D','L','R']

dx = [0,0,-1,1]
dy = [-1,1,0,0]
nx,ny = 0,0
for i in move:
    for j in range(len(movetype)):
        if i == movetype[j]:
            nx = x + dx[j]
            ny = y + dy[j]

        if nx<1 or ny<1 or nx>n or ny>n:
            continue # 아래 코드 실행하지 않고 넘어감..
        x,y = nx,ny

print(y,x)