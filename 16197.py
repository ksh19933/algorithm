import sys
input = sys.stdin.readline

def dfs(depth, arr, coin1, coin2):
    global ans
    if ans != 100:
        if depth > ans:
            return
    if depth > 10:
        return
        
    for k in range(4):
        cnt = 0
        coin1_x = coin1[0] + dx[k]
        coin1_y = coin1[1] + dy[k]
        coin2_x = coin2[0] + dx[k]
        coin2_y = coin2[1] + dy[k]
        if 0 <= coin1_x < r and 0 <= coin1_y < c:
            if arr[coin1_x][coin1_y] == "#":
                coin1_x = coin1[0]
                coin1_y = coin1[1]
        else:
            cnt += 1
        
        if 0 <= coin2_x < r and 0 <= coin2_y < c:
            if arr[coin2_x][coin2_y] == "#":
                coin2_x = coin2[0]
                coin2_y = coin2[1]
        else:
            cnt += 1

        if cnt == 1:
            ans = min(ans, depth)
            return
        elif cnt == 0:
            dfs(depth+1, arr, [coin1_x, coin1_y], [coin2_x, coin2_y])
        
r, c = list(map(int, input().split()))
arr = []
coin = []
ans = 100
for i in range(r):
    tmp = list(input())
    for j in range(c):
        if tmp[j] == "o":
            coin.append([i, j])
    arr.append(tmp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dfs(1, arr, coin[0], coin[1])
if ans == 100:
    print(-1)
else:
    print(ans)
   