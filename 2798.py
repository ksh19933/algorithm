import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num_arr = list(map(int, input().split()))
ans = 0

def dfs(idx, sum, depth):
    global ans
    if sum > m or depth > 3:
        return
    elif depth == 3 and sum > ans:
        ans = sum

    for i in range(idx, len(num_arr)):
        dfs(i+1,sum+num_arr[i], depth + 1)

for i in range(len(num_arr)-2):
    dfs(i+1, num_arr[i], 1)

print(ans)