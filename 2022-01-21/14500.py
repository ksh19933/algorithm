import sys
input = sys.stdin.readline

def polyno(length, sum, x, y):
    global max_sum
    if max_sum >= sum + max_val * (4-length):
        return
    if length == 4:
        max_sum = max(max_sum, sum)
        return
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<= nx < x_ and 0<= ny < y_ and not used[nx][ny]:
            if length == 2:
                used[nx][ny] = True
                polyno(length+1, sum+arr[nx][ny], x, y)
                used[nx][ny] = False
            used[nx][ny] = True
            polyno(length+1, sum+arr[nx][ny], nx, ny)
            used[nx][ny] = False


x_, y_ = list(map(int, input().split()))
arr = []
max_sum = 0
max_val = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
used = [[False] * y_ for _ in range(x_)]

for i in range(x_):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    max_val = max(max_val, max(tmp))

for i in range(x_):
    for j in range(y_):
        used[i][j] = True
        polyno(1, arr[i][j], i, j)
        used[i][j] = False

print(max_sum)


