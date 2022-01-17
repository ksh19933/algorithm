import sys
input = sys.stdin.readline

def dfs(idx, tmp):
    if len(tmp) == n//2:
        comb.append(tmp[:])
        return
    
    for i in range(idx, n):
        tmp.append(i)
        dfs(i+1, tmp)
        tmp.pop()

n = int(input())
ans = 100 * n * n
comb_num = [i for i in range(n)]
arr = [list(map(int, input().split())) for _ in range(n)]
comb = []
for i in range(n):
    dfs(i+1, [i])


for i in range(len(comb)//2):
    stat_A = 0
    stat_B = 0
    for x in comb[i]:
        for y in comb[i]:
            stat_A += arr[x][y]
    
    for x in comb[len(comb)-i-1]:
        for y in comb[len(comb)-i-1]:
            stat_B += arr[x][y]

    if ans > abs(stat_A-stat_B):
        ans = abs(stat_A-stat_B)


print(ans)


